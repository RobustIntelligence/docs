# MLflow

Copy the code snippet below and follow the commented steps, replacing all the TODOs with necessary credentials/endpoints, to connect RIME to a locally stored MLflow model.

Once that is done, you can specify that model file when [configuring your model source](/for_data_scientists/reference/tabular/model_source.md).


```python
"""Template for connecting an MLflow model to RIME.

We expect this file to contain a `predict_df` function that takes in a Pandas
DataFrame corresponding to one or more rows in the dataset. This method should
return a NumPy array containing scores between 0 and 1 for each row in the dataset.
The DataFrame will be loaded from the data sources you configure.

This specific file implements this assuming that 1) your MLflow model is
logged locally in the default 'mlruns' directory within the 'model' directory
and 2) you have the mlflow library installed.

"""

from pathlib import Path

import numpy as np
import pandas as pd
import mlflow.sklearn

# Step 1: Load the model.

RUN_ID = 'TODO: Run ID'
model_dir = Path(__file__).parent
model = mlflow.sklearn.load_model(model_dir / f"mlruns/0/{RUN_ID}/artifacts/model")
    
# Step 2: If the model requires additional preprocessing to the input data, 
# include the logic in the below 'preprocess_df' function or 'predict_df'
# function. By default, RIME passes rows from the dataset defined in the config
# to 'predict_df' with the label and prediction columns omitted.

def preprocess_df(df: pd.DataFrame) -> pd.DataFrame:
    """Apply preprocessing to rows of the dataframe."""
    
    return df

# Step 3: Implement the below function that returns a prediction per row in
# the dataset, with any additional preprocessing if necessary.

def predict_df(df: pd.DataFrame) -> np.ndarray:
    """Return array of probabilities assigned to the positive class."""
    
    # Apply custom preprocessing to the row.
    df = preprocess_df(df)
    
    return model.predict_proba(df)[:,1]
```
