"""Airflow + MLFlow demo."""
import json
import logging
import os
import pickle
from datetime import datetime, timedelta
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, List, Tuple, Union, cast

import joblib
import mlflow
import numpy as np
import pandas as pd
from catboost import CatBoostClassifier
from dateutil.parser import parse as parse_date
from mlflow import ActiveRun
from mlflow.entities.experiment import Experiment
from mlflow.entities.run import Run
from mlflow.models.model import Model
from mlflow.tracking.client import MlflowClient
from mlflow.utils.file_utils import TempDir
from rime_sdk import Client
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from airflow import DAG
from airflow.models.taskinstance import TaskInstance
from airflow.operators.python import PythonOperator, ShortCircuitOperator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set Constants
RIME_BACKEND_URL = os.environ["RIME_UPLOAD_URL"]  # Can update to different cluster
RIME_API_KEY = os.environ["RIME_API_KEY"]
LABEL_COL = "label"
PRED_COL = "pred"
TIMESTAMP_COL = "timestamp"
UI_LINK_COL = "UI Link"
RIME_DATE_FORMAT = "%Y-%m-%d"
AIRFLOW_HOME = Path(__file__).parent.parent
TEST_RESULTS_OUT_DIR = AIRFLOW_HOME / "rime_run_results"
TEST_RESULTS_OUT_DIR.mkdir(exist_ok=True)
REF_PATH = AIRFLOW_HOME / "fraud_data" / "data" / "fraud_ref.csv"
EVAL_PATH = AIRFLOW_HOME / "fraud_data" / "data" / "fraud_eval.csv"
INCREMENTAL_PATH = AIRFLOW_HOME / "fraud_data" / "data" / "fraud_incremental.csv"
RIME_PROJECT_NAME = f"Airflow Demo {datetime.now().strftime('%Y-%m-%d %H:%M')}"
MLFLOW_EXPERIMENT_NAME = "airflow_demo"
MLFLOW_CLIENT = MlflowClient()
DEPLOYMENT_DATE = datetime(2018, 7, 31)
PRODUCTION_END_DATE = datetime(2018, 8, 30)


def fetch_fraud_data(split: str) -> pd.DataFrame:
    """Fetch fraud data (X and Y) for the specified split."""
    if split == "train":
        path = REF_PATH
    elif split == "test":
        path = EVAL_PATH
    elif split == "incremental":
        path = INCREMENTAL_PATH
    else:
        raise ValueError("Invalid split.")
    return pd.read_csv(path).drop(["preds"], axis=1)


def _get_mlflow_experiment() -> Experiment:
    """Retrieve the MLFlow experiment for this run."""
    experiment = MLFLOW_CLIENT.get_experiment_by_name(MLFLOW_EXPERIMENT_NAME)
    if experiment is None:
        MLFLOW_CLIENT.create_experiment(MLFLOW_EXPERIMENT_NAME)
        experiment = MLFLOW_CLIENT.get_experiment_by_name(MLFLOW_EXPERIMENT_NAME)
        if experiment is None:
            raise ValueError("Could not create experiment.")
    return experiment


def _extract_feature_types(
    df: pd.DataFrame, exclude_cols: List[str]
) -> Tuple[List[str], List[str]]:
    """Extract categorical and continuous features (if not provided)."""
    dtypes = df.dtypes
    dtypes = dtypes[~dtypes.index.isin(exclude_cols)]
    cat_features = list(dtypes[dtypes == object].index)
    cont_features = list(dtypes[dtypes != object].index)
    return cat_features, cont_features


def _get_x_and_y(df: pd.DataFrame, label_col: str) -> Tuple[pd.DataFrame, pd.Series]:
    """Get X and Y."""
    Y = df[label_col]
    X = df.drop([label_col], axis=1)
    return X, Y


def _log_mlflow_sklearn_model(
    run_id: str, sk_model: Pipeline, artifact_path: str, registered_model_name: str
):
    """Log an mlflow model with the provided run_id."""
    with TempDir() as tmp:
        local_path = tmp.path("model")
        mlflow_model = Model(artifact_path=artifact_path, run_id=run_id)
        mlflow.sklearn.save_model(
            sk_model=sk_model, path=local_path, mlflow_model=mlflow_model
        )
        # pylint: disable=protected-access
        MLFLOW_CLIENT._record_logged_model(run_id, mlflow_model)
        MLFLOW_CLIENT.log_artifacts(run_id, local_path, artifact_path=artifact_path)
        mlflow.register_model(
            "runs:/%s/%s" % (run_id, artifact_path), registered_model_name
        )
    return mlflow_model.get_model_info()


def _preprocess_df(
    df: pd.DataFrame, cat_features: List[str], cont_features: List[str]
) -> pd.DataFrame:
    """Apply string preprocessing to categorical features."""
    cat_df = df[cat_features].astype(str)
    cont_df = df[cont_features]
    return pd.concat([cat_df, cont_df], axis=1)


def _eval_metrics(actual: np.ndarray, pred: np.ndarray) -> dict:
    """Metrics to for train and test to report in our training loop."""
    acc = accuracy_score(actual, pred)
    f1 = f1_score(actual, pred)
    prec = precision_score(actual, pred)
    recall = recall_score(actual, pred)
    auc = roc_auc_score(actual, pred)
    return {"accuracy": acc, "f1": f1, "precision": prec, "recall": recall, "auc": auc}


def _evaluate_model_and_log_metrics(
    pipeline: Pipeline,
    preprocessed_x: pd.DataFrame,
    y: pd.Series,
    run_id: str,
    split: str,
):
    """Evaluate the model and log metrics."""
    predicted_qualities = pipeline.predict(preprocessed_x)
    eval_metrics = _eval_metrics(y, predicted_qualities)
    for metric_name, score in eval_metrics.items():
        MLFLOW_CLIENT.log_metric(run_id, f"{split}_{metric_name}", score)


def _get_pipeline(model_type: str, cat_features: List[str]) -> Pipeline:
    """Get the pipeline for the model type."""
    if model_type == "catboost-classifier":
        pipeline = Pipeline(
            [("clf", CatBoostClassifier(cat_features=cat_features, verbose=False))]
        )
    elif model_type == "sgd-classifier":
        pipeline = Pipeline(
            [
                ("impute", SimpleImputer(strategy="most_frequent")),
                ("ohe", OneHotEncoder(sparse=False, handle_unknown="ignore")),
                ("normalizer", StandardScaler()),
                ("clf", SGDClassifier(loss="modified_huber")),
            ]
        )
    elif model_type == "logistic-regression-classifier":
        pipeline = Pipeline(
            [
                ("impute", SimpleImputer(strategy="most_frequent")),
                ("ohe", OneHotEncoder(sparse=False, handle_unknown="ignore")),
                ("normalizer", StandardScaler()),
                ("clf", LogisticRegression()),
            ]
        )
    else:
        raise ValueError(f"Unsupported model_type {model_type}")
    return pipeline


def train_model(
    ti: TaskInstance, model_type: str, **kwargs: Any,
) -> Tuple[ActiveRun, Pipeline]:
    """Train specified pipeline and log to MLFlow."""
    mlflow_experiment = _get_mlflow_experiment()
    train_x, train_y = _get_x_and_y(
        ti.xcom_pull(task_ids="fetch_train_data"), LABEL_COL
    )
    test_x, test_y = _get_x_and_y(ti.xcom_pull(task_ids="fetch_test_data"), LABEL_COL)
    mlflow_run = MLFLOW_CLIENT.create_run(
        experiment_id=mlflow_experiment.experiment_id, tags={"model_type": model_type}
    )
    run_id = mlflow_run.info.run_id
    cat_features, cont_features = _extract_feature_types(train_x, [LABEL_COL])
    pipeline = _get_pipeline(model_type, cat_features)
    for k, v in kwargs.items():
        MLFLOW_CLIENT.log_param(run_id, k, v)
    train_x = _preprocess_df(train_x, cat_features, cont_features)
    test_x = _preprocess_df(test_x, cat_features, cont_features)
    pipeline.fit(train_x, train_y.values.flatten())
    _log_mlflow_sklearn_model(
        run_id, pipeline, f"{model_type}-model", registered_model_name=model_type,
    )
    _evaluate_model_and_log_metrics(pipeline, train_x, train_y, run_id, "train")
    _evaluate_model_and_log_metrics(pipeline, test_x, test_y, run_id, "test")
    return mlflow_run, pipeline


def get_model_file_contents() -> str:
    """Get the example `model.py` contents."""
    file_str = """
import joblib
import pickle
from pathlib import Path

import numpy as np
import pandas as pd

model_dir = Path(__file__).parent / "model_extras"
if model_dir.exists():
    cat_features = pickle.load(open(model_dir / "cat_features.pkl", "rb"))
    cont_features = pickle.load(open(model_dir / "cont_features.pkl", "rb"))
    pipeline = joblib.load(model_dir / "pipeline.joblib")
else:
    raise ValueError("model files do not exist in desired format")


def preprocess_df(df: pd.DataFrame) -> pd.DataFrame:
    \"\"\"Apply string preprocessing to categorical features.\"\"\"
    cat_df = df[cat_features].astype(str)
    cont_df = df[cont_features]
    return pd.concat([cat_df, cont_df], axis=1)


def predict_df(df: pd.DataFrame) -> np.ndarray:
    \"\"\"Return predicted probabilities.\"\"\"
    df = preprocess_df(df)
    # Index for binary classification
    return pipeline.predict_proba(df)[:, 1]
    """
    return file_str


def upload_model(ti: TaskInstance, model_val: str) -> str:
    """Upload trained model to RIME cluster and return the resultant model directory path."""
    upload_path = "rime_airflow_walkthrough"
    client = Client(RIME_BACKEND_URL, api_key=RIME_API_KEY)
    df = ti.xcom_pull(task_ids="fetch_train_data")
    _, net = ti.xcom_pull(task_ids=f"train_model_{model_val}")
    cat_features, cont_features = _extract_feature_types(df, [LABEL_COL])
    with TemporaryDirectory() as temp_dir:
        _dir = Path(temp_dir) / model_val
        d = str(_dir)
        extras_dir = _dir / "model_extras"
        extras_dir.mkdir(parents=True)
        with open(_dir / "model.py", "w") as f:
            f.write(get_model_file_contents())
        joblib.dump(net, extras_dir / "pipeline.joblib")
        with open(extras_dir / "cat_features.pkl", "wb") as f:
            pickle.dump(cat_features, f)
        with open(extras_dir / "cont_features.pkl", "wb") as f:
            pickle.dump(cont_features, f)
        uploaded_path = client.upload_model_directory(d, upload_path=upload_path)
    return uploaded_path + "/model.py"


def upload_dataset_file(client: Client, df: pd.DataFrame, file_tag: str) -> str:
    """Upload dataframe to RIME cluster."""
    upload_path = "rime_airflow_walkthrough"
    with TemporaryDirectory() as d:
        f = Path(d) / f"{file_tag}_data.csv"
        df.to_csv(f, index=False)
        uploaded_name = client.upload_file(f.resolve(), upload_path=upload_path)
    return uploaded_name


def _add_preds_and_upload_dataset_file(
    net: Union[Pipeline, Any], df: pd.DataFrame, file_tag: str
):
    """Make predictions and upload."""
    client = Client(RIME_BACKEND_URL, api_key=RIME_API_KEY)
    df = df.copy()
    to_drop = [col for col in (LABEL_COL, TIMESTAMP_COL) if col in df.columns]
    cat_features, cont_features = _extract_feature_types(df, to_drop)
    df[PRED_COL] = net.predict_proba(
        _preprocess_df(df.drop(to_drop, axis=1), cat_features, cont_features)
    )[:, -1]
    return upload_dataset_file(client, df, file_tag)


def add_preds_and_upload_dataset_file(ti: TaskInstance, model_val: str, split: str):
    """Make predictions and upload."""
    df = ti.xcom_pull(task_ids=f"fetch_{split}_data")
    _, net = ti.xcom_pull(task_ids=f"train_model_{model_val}")
    model_split_tag = f"{model_val}-{split}"
    return _add_preds_and_upload_dataset_file(net, df, model_split_tag)


def create_rime_project() -> str:
    """Create a RIME project."""
    rime_client = Client(RIME_BACKEND_URL, api_key=RIME_API_KEY)
    project = rime_client.create_project(
        name=RIME_PROJECT_NAME, description="This is an Airflow Demo"
    )
    return project.project_id


def run_stress_test(ti: TaskInstance, model_val: str) -> Tuple[Path, Path, str]:
    """Run a stress test on the model."""
    rime_project_id: str = ti.xcom_pull(task_ids="create_rime_project")
    ref_path = ti.xcom_pull(
        task_ids=f"add_preds_and_upload_ref_dataset_file_{model_val}"
    )
    eval_path = ti.xcom_pull(
        task_ids=f"add_preds_and_upload_eval_dataset_file_{model_val}"
    )
    model_path = ti.xcom_pull(task_ids=f"upload_model_{model_val}")
    rime_client = Client(RIME_BACKEND_URL, api_key=RIME_API_KEY)
    model_test_config = {
        "run_name": f"Airflow Tutorial: Model {model_val}",
        "data_info": {
            "label_col": LABEL_COL,
            "pred_col": PRED_COL,
            "ref_path": ref_path,
            "eval_path": eval_path,
        },
        "model_info": {"path": model_path},
        "model_task": "Binary Classification",
    }
    stress_job = rime_client.start_stress_test(
        model_test_config, project_id=rime_project_id
    )
    # Block until the stress test is complete
    stress_job.get_status(verbose=True, wait_until_finish=True)
    # Save test results (high-level)
    test_run = stress_job.get_test_run()
    test_run_results = test_run.get_result_df()
    test_run_results[UI_LINK_COL] = test_run.get_link()
    test_run_results_save_path = (
        TEST_RESULTS_OUT_DIR / f"test_run_results_{model_val}.csv"
    )
    test_run_results.to_csv(test_run_results_save_path, index=False)
    # Save test case results (low-level)
    test_cases_results = stress_job.get_test_cases_result()
    test_case_results_save_path = (
        TEST_RESULTS_OUT_DIR / f"test_cases_results_{model_val}.csv"
    )
    test_cases_results.to_csv(test_case_results_save_path, index=False)
    return (
        test_run_results_save_path,
        test_case_results_save_path,
        test_run.test_run_id,
    )


def log_results_to_mlflow(ti: TaskInstance, model_val: str) -> float:
    """Log test results to MLFlow and return pass rate."""
    test_run_results_save_path, test_case_results_save_path, test_run_id = ti.xcom_pull(
        task_ids=f"run_stress_test_{model_val}"
    )
    rime_project_id: str = ti.xcom_pull(task_ids="create_rime_project")
    _mlflow_run, _ = ti.xcom_pull(task_ids=f"train_model_{model_val}")
    mlflow_run = cast(Run, _mlflow_run)
    run_id = mlflow_run.info.run_id
    test_run_results = pd.read_csv(test_run_results_save_path)
    col_is_metric = test_run_results.dtypes != object
    for index, is_metric in enumerate(col_is_metric):
        col = test_run_results.columns[index]
        if is_metric:
            MLFLOW_CLIENT.log_metric(run_id, "rime_" + col, test_run_results[col][0])
        else:
            MLFLOW_CLIENT.log_param(run_id, "rime_" + col, test_run_results[col][0])
    MLFLOW_CLIENT.log_artifact(
        run_id, test_case_results_save_path, "test_cases_results"
    )
    # Update tags to include RIME info
    MLFLOW_CLIENT.set_tag(
        run_id, "RIME Stress Test Link", test_run_results[UI_LINK_COL][0]
    )
    MLFLOW_CLIENT.set_tag(run_id, "RIME Stress Test Run ID", test_run_id)
    MLFLOW_CLIENT.set_tag(run_id, "RIME Project ID", rime_project_id)
    num_passed: int = test_run_results["metrics.summary_counts.pass"][0]
    num_total: int = test_run_results["metrics.summary_counts.total"][0]
    test_pass_rate = num_passed / num_total
    MLFLOW_CLIENT.log_metric(run_id, "rime_pass_rate", test_pass_rate)
    return test_pass_rate


def choose_best_model(ti: TaskInstance, model_types: List[str]) -> str:
    """Select the best model from the MLFLow experiments."""
    num_models = len(model_types)
    task_ids = [f"log_results_to_mlflow_{i}" for i in range(num_models)]
    pass_rates = ti.xcom_pull(task_ids=task_ids)
    best_model_index = np.argmax(pass_rates)
    return model_types[best_model_index]


def transition_best_model_to_production(ti: TaskInstance) -> str:
    """Transition the best model to production and return endpoint uri."""
    mlflow_experiment = _get_mlflow_experiment()
    production_model_name = ti.xcom_pull("choose_best_model")
    latest_versions = MLFLOW_CLIENT.get_latest_versions(production_model_name)
    latest_version = latest_versions[0]
    version_number = int(latest_version.version)
    if latest_version.current_stage != "Production":
        logger.info(f"Transitioning model version {version_number} to production.")
        MLFLOW_CLIENT.transition_model_version_stage(
            name=production_model_name, version=version_number, stage="Production"
        )
    else:
        logger.info("Model already in production.")
    model_uri = f"models:/{production_model_name}/Production"
    # Terminate non-production runs
    for run in MLFLOW_CLIENT.list_run_infos(
        experiment_id=mlflow_experiment.experiment_id
    ):
        if run.run_id != latest_version.run_id:
            logger.info(f"Terminating run {run.run_id}.")
            MLFLOW_CLIENT.set_terminated(run.run_id)
    return model_uri


def create_firewall() -> str:
    """Create a firewall for the deployed model"""
    fraud_project_id, stress_test_run_id = get_project_and_stress_test_ids_from_mlflow()
    client = Client(RIME_BACKEND_URL, api_key=RIME_API_KEY)
    project = client.get_project(fraud_project_id)
    try:
        logger.info(
            f"Creating firewall for run {stress_test_run_id}"
            f" and project {fraud_project_id}."
        )
        project.create_firewall(
            name="Airflow Firewall", bin_size="day", test_run_id=stress_test_run_id,
        )
    except ValueError as err:
        logger.warning(f"Firewall already exists: {err}")
        logger.info(f"Updating to target model from stress test {stress_test_run_id}")
        firewall = project.get_firewall()
        firewall.update_firewall_stress_test_run(stress_test_run_id)


default_args = {
    "owner": "airflow",
    "start_date": DEPLOYMENT_DATE,
    "depends_on_past": False,
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
    "provide_context": True,  # Whether to pass variables to subsequent tasks
}

with DAG(
    dag_id="RIME_Stress_Testing",
    default_args=default_args,
    schedule_interval="@once",  # set interval
    start_date=DEPLOYMENT_DATE,
    # indicate whether or not Airflow should do any runs for
    # intervals between the start_date and the current date that haven't been run thus far
    catchup=False,
) as preprod_dag:
    # Create a RIME project
    create_project_task = PythonOperator(
        task_id="create_rime_project", python_callable=create_rime_project,
    )
    fetch_train_data_task = PythonOperator(
        task_id="fetch_train_data",
        python_callable=fetch_fraud_data,
        op_kwargs={"split": "train"},
    )
    fetch_test_data_task = PythonOperator(
        task_id="fetch_test_data",
        python_callable=fetch_fraud_data,
        op_kwargs={"split": "test"},
    )
    root = [fetch_train_data_task, fetch_test_data_task]
    log_results_to_mlflow_tasks = []
    model_types = [
        "catboost-classifier",
        "sgd-classifier",
        "logistic-regression-classifier",
    ]
    for i, (model_type) in enumerate(model_types):
        train_task = PythonOperator(
            task_id=f"train_model_{i}",
            python_callable=train_model,
            op_kwargs={"model_type": model_type,},
            show_return_value_in_logs=False,
        )
        model_val_kwargs = {"model_val": str(i)}
        model_upload_task = PythonOperator(
            task_id=f"upload_model_{i}",
            python_callable=upload_model,
            op_kwargs=model_val_kwargs,
        )
        ref_upload_task = PythonOperator(
            task_id=f"add_preds_and_upload_ref_dataset_file_{i}",
            python_callable=add_preds_and_upload_dataset_file,
            op_kwargs={"split": "train", **model_val_kwargs},
        )
        eval_upload_task = PythonOperator(
            task_id=f"add_preds_and_upload_eval_dataset_file_{i}",
            python_callable=add_preds_and_upload_dataset_file,
            op_kwargs={"split": "test", **model_val_kwargs},
        )
        stress_tests_task = PythonOperator(
            task_id=f"run_stress_test_{i}",
            python_callable=run_stress_test,
            op_kwargs=model_val_kwargs,
        )
        mlflow_task = PythonOperator(
            task_id=f"log_results_to_mlflow_{i}",
            python_callable=log_results_to_mlflow,
            op_kwargs=model_val_kwargs,
        )
        upload_tasks = [model_upload_task, ref_upload_task, eval_upload_task]
        # pylint: disable=pointless-statement
        root >> train_task >> upload_tasks >> stress_tests_task >> mlflow_task
        create_project_task >> stress_tests_task
        log_results_to_mlflow_tasks.append(mlflow_task)

    selection_task = PythonOperator(
        task_id="choose_best_model",
        python_callable=choose_best_model,
        op_kwargs={"model_types": model_types},
    )
    deploy_task = PythonOperator(
        task_id="transition_best_model_to_production",
        python_callable=transition_best_model_to_production,
    )
    create_firewall_task = PythonOperator(
        task_id="create_firewall", python_callable=create_firewall,
    )
    # pylint: disable=pointless-statement
    log_results_to_mlflow_tasks >> selection_task >> deploy_task >> create_firewall_task

### Below are the functions for the production firewall DAG ###
def _parse_interval_bound(interval_time: str) -> str:
    """Get the start date for the catchup interval in RIME format."""
    return parse_date(interval_time).strftime(RIME_DATE_FORMAT)


def fetch_production_data(interval_start: str) -> Tuple[pd.DataFrame, str]:
    """Fetch the production data for the given interval."""
    incremental = fetch_fraud_data("incremental")
    interval_start = _parse_interval_bound(interval_start)
    included = incremental[incremental[TIMESTAMP_COL] == interval_start]
    return (included, interval_start)


def get_rime_project_id() -> str:
    """Get the project ID for the deployed firewall."""
    project_id, _ = get_project_and_stress_test_ids_from_mlflow()
    return project_id


def get_production_model_name() -> str:
    """Get the name of the (first) production model."""
    for model in MLFLOW_CLIENT.list_registered_models():
        latest_versions = MLFLOW_CLIENT.get_latest_versions(
            model.name, stages=["Production"]
        )
        if len(latest_versions) > 0:
            return model.name
    raise ValueError("No production model found.")


def get_production_model_run_id() -> str:
    """Get the mlflow run ID of the model in production."""
    production_model_name = get_production_model_name()
    latest_versions = MLFLOW_CLIENT.get_latest_versions(
        production_model_name, stages=["Production"]
    )
    run_id = latest_versions[0].run_id
    return run_id


def get_project_and_stress_test_ids_from_mlflow() -> Tuple[str, str]:
    """Get the project and run ID from MLflow."""
    run_id = get_production_model_run_id()
    run = mlflow.get_run(run_id)
    stress_test_run_id = run.data.params["rime_test_run_id"]
    project_id = run.data.params["rime_project_id"]
    return project_id, stress_test_run_id


def add_prod_preds_and_upload_dataset_file(ti: TaskInstance) -> str:
    """Add production predictions and upload data."""
    df, interval_start = ti.xcom_pull(task_ids="fetch_production_data")
    production_model_name = get_production_model_name()
    production_model = mlflow.sklearn.load_model(
        model_uri=f"models:/{production_model_name}/Production"
    )
    split = interval_start.split(" ")[0].replace("-", "")
    model_split_tag = f"production-{split}"
    return _add_preds_and_upload_dataset_file(production_model, df, model_split_tag)


def continue_if_data_available(ti: TaskInstance) -> bool:
    """Continue if data is available."""
    df, _ = ti.xcom_pull(task_ids="fetch_production_data")
    return df.shape[0] > 0


def start_firewall_continuous_test(ti: TaskInstance, interval_start: str) -> dict:
    """Run firewall over a batch of data."""
    project_id: str = ti.xcom_pull(task_ids="get_rime_project_id")
    prod_data_path: str = ti.xcom_pull(task_ids="add_prod_preds")
    incremental_config = {
        "eval_path": prod_data_path,
        "timestamp_col": TIMESTAMP_COL,
    }
    client = Client(RIME_BACKEND_URL, api_key=RIME_API_KEY)
    firewall = client.get_firewall_for_project(project_id)
    ct_job = firewall.start_continuous_test(
        test_run_config=incremental_config, disable_firewall_events=False
    )
    status = ct_job.get_status(
        verbose=True, wait_until_finish=True, poll_rate_sec=15.0
    )
    with TemporaryDirectory() as _dir:
        local_path = Path(_dir) / "incremental_firewall_status.json"
        with open(local_path, "w") as f:
            json.dump(status, f)
        run_id = get_production_model_run_id()
        interval_start = _parse_interval_bound(interval_start)
        MLFLOW_CLIENT.log_artifact(
            run_id, local_path, f"incremental_firewall_status_{interval_start}"
        )
    return status


with DAG(
    dag_id="RIME_Firewall",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=DEPLOYMENT_DATE,
    end_date=PRODUCTION_END_DATE,
    catchup=True,
) as prod_dag:
    interval_start = "{{ data_interval_start }}"
    interval_end = "{{ data_interval_end }}"
    fetch_prod_data_task = PythonOperator(
        task_id="fetch_production_data",
        python_callable=fetch_production_data,
        op_kwargs={"interval_start": interval_start, "interval_end": interval_end},
    )
    # Only run the firewall if the DF from fetch_production_data is not empty
    short_circuit_task = ShortCircuitOperator(
        task_id="continue_if_data_available",
        python_callable=continue_if_data_available,
    )
    get_project_task = PythonOperator(
        task_id="get_rime_project_id", python_callable=get_rime_project_id,
    )
    add_prod_preds_task = PythonOperator(
        task_id="add_prod_preds",
        python_callable=add_prod_preds_and_upload_dataset_file,
    )
    run_firewall_task = PythonOperator(
        task_id="run_firewall",
        python_callable=start_firewall_continuous_test,
        op_kwargs={"interval_start": interval_start},
    )
    # pylint: disable=pointless-statement,line-too-long
    fetch_prod_data_task >> short_circuit_task >> add_prod_preds_task >> run_firewall_task
    get_project_task >> run_firewall_task
