# Data and Model Setup
For readability, we recommend running these guides in a Jupyter notebook.

Begin by setting the `RIME_PATH` variable to your local path to the trial bundle you downloaded as part of installation, e.g., `RIME_PATH = '/home/ec2-user/rime_trial'`

```python
import pandas as pd
RIME_PATH = 'SET THIS!'
train_df = pd.read_csv(RIME_PATH + 'examples/fraud/train.csv')
test_df = pd.read_csv(RIME_PATH + 'examples/fraud/val.csv')
label_col = "isFraud"
```

Make sure to split the train label data out for RIME:
```python
def split_df(df: pd.DataFrame, label_col: str):
    labels = df[label_col]
    df = df.drop(columns=[label_col])
    return df, labels

train_df, train_labels = split_df(train_df, label_col)
test_df, test_labels = split_df(test_df, label_col)
```

We then load the model as well as the preprocessing helper from their corresponding pickle files:
```python
import catboost as catb
import pickle

model = catb.CatBoostClassifier()
model.load_model(str(RIME_PATH + "examples/fraud/fraud.catb"))
with open(RIME_PATH + "examples/fraud/null_impute.pkl", "rb") as f:
    null_impute = pickle.load(f)

def preprocess(x: dict):
    """Null impute categoricals."""
    for col_name in x.keys():
        if pd.isnull(x[col_name]) and col_name in null_impute.keys():
            x[col_name] = null_impute[col_name]
    return x

def preprocess_df(df: pd.DataFrame):
    """Null impute categoricals."""
    new_df = df.copy()
    for col_name in df.columns:
        if col_name in null_impute.keys():
            new_df.loc[new_df[col_name].isnull(), col_name] = null_impute[col_name]
    return new_df
```

We now define the inference function we want to use. We can either define a `predict_dict` or `predict_df` function.

NOTE: We recommend using `predict_df` to speed up profiling and testing.
```python
# We now define our interface.
def predict_dict(x: dict):
    """Predict dict function."""
    new_x = preprocess(x)
    new_x = pd.DataFrame(new_x, index=[0])
    return model.predict_proba(new_x)[0][1]
```

With this, we can directly start using the tests for the RIME Python Library! We first instantiate the data containers:

```python
from rime.tabular import DataContainer, TabularRunContainer, ModelTask

data_container = DataContainer.from_df(train_df, model_task=ModelTask.BINARY_CLASSIFICATION, labels=train_labels)
test_data_container = DataContainer.from_df(test_df, labels=test_labels, model_task=ModelTask.BINARY_CLASSIFICATION, ref_data=data_container)
container = TabularRunContainer.from_predict_dict_function(data_container, test_data_container, predict_dict, ModelTask.BINARY_CLASSIFICATION)
```

Once you have done that, we can access the components we need from the `container` as follows:
```python
model_wrapper = container.model.base_model
df = container.eval_data.df
labels = container.eval_data.labels
```

This allows us to do initial profiling on the dataset and model. Now you're all set to run tests.
