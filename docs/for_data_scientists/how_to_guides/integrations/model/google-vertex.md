# Google Vertex AI

Copy the code snippet below and follow the commented steps, replacing all the TODOs with necessary credentials/endpoints, to connect RIME to a deployed Google Vertex AI model.

Once that is done, you can specify that model file when [configuring your model source](/for_data_scientists/reference/tabular/model_source.md).

```python
"""Template for connecting a model hosted on Google Vertex AI to RIME.

We expect this file to contain a `predict_df` function that takes in a Pandas
DataFrame corresponding to one or more rows in the dataset. This method should
return a NumPy array containing scores between 0 and 1 for each row in the dataset.

This specific file implements this assuming that 1) your Vertex AI model is
hosted on a Google Cloud endpoint, 2) the machine where this is being run 
has the proper permissions to query that endpoint, and 3) that you have the
requests library installed.

"""

import json
import os

import numpy as np
import pandas as pd
import requests

# Step 1: Define endpoint variables.
AUTH_TOKEN = "TODO: Add real Google Cloud authorization token."
ENDPOINT_ID = "TODO: Add real endpoint ID."
PROJECT_ID = "TODO: Add real project ID."
REGION = "TODO: Add real project region."
ENDPOINT = (
    f"https://{REGION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}"
    f"/locations/{REGION}/endpoints/{ENDPOINT_ID}:predict"
)
HEADERS = {"Authorization": f"Bearer {AUTH_TOKEN}", "Content-Type": "application/json"}

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
    """Return a NumPy array of model scores for each row in the DataFrame."""

    df = preprocess_df(df)

    # Vertex AI endpoint expects all values to be cast to string.
    data = {"instances": df.astype(str).to_dict(orient="records")}
    response = requests.post(
        ENDPOINT,
        headers=HEADERS,
        data=json.dumps(data),
    )
    response_json = response.json()
    if "error" in response_json:
        raise ValueError(response_json["error"])

    # Example successful response
    # {
    #   "predictions": [
    #       {"scores": [0.2, 0.8], "classes": ["0", "1"]},
    #   ],
    #   ...
    # }

    preds = response_json["predictions"]
    scores = [x["scores"][1] for x in preds]
    return np.array(scores)
```
