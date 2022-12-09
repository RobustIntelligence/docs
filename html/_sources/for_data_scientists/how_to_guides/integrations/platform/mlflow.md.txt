# RIME 🤝 MLflow

RIME integrates with MLflow Tracking. This integration unlocks the true power of 
AI Stress Testing when experimenting with many models. 

With the RIME SDK you are able to query for RIME metrics and include them in your 
MLflow experiments. You can see in the below code snippet. To get a better understanding
of the integration, take a look at the 
<a href="https://www.loom.com/share/0b265c7e30604bd696063b215514d3e7" target="_blank">MLflow Demo Video.</a>


```python
import mlflow
from rime_sdk import Client

# Set these before beginning!
BACKEND_URL = "rime-backend.<YOUR_ORG_NAME>.rime.dev"
API_KEY = "<YOUR_API_KEY>"

# Connect to your cluster.
rime_client = Client(BACKEND_URL, api_key=API_KEY)
project = rime_client.create_project(
    name="Example Project", description="Example logging RIME artifacts to MLflow.",
)
config = {...}

# Run the test!
job = rime_client.start_stress_test(
    test_run_config=config, project_id=project.project_id
)

# Query the results.
test_run = job.get_test_run()
test_run_result = test_run.get_result_df()
test_cases_result = job.get_test_cases_df(show_test_case_metrics=True)

# Preparing the test cases results to log.
test_cases_result.to_csv("test_cases_results.csv")

# Log experiment results to MLflow.
with mlflow.start_run():
    cols = test_run_result.columns
    col_is_metric = test_run_result.dtypes != object
    for index, is_metric in enumerate(col_is_metric):
        col = cols[index]
        if is_metric:
            mlflow.log_metric("rime_" + col, test_run_result[col][0])
        else:
            mlflow.log_param("rime_" + col, test_run_result[col][0])
    mlflow.log_artifact("test_cases_results.csv")
    mlflow.set_tag("RIME Stress Test Link", test_run.get_link())
    mlflow.set_tag("RIME Test Run ID", test_run.test_run_id)
    mlflow.set_tag("RIME Project ID", project.project_id)
mlflow.end_run()

```
