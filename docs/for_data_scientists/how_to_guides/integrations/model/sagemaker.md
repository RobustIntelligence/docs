# SageMaker

### Model Providers

In order to connect RIME to a deployed SageMaker model, you can copy the below Python snippet into a Python model. Then go through that snippet and replace all the TODOs with necessary credentials/endpoints.

Once that is done, you can specify that model file when [configuring your model source](/for_data_scientists/reference/tabular/model_source.md).

```python
"""This is a template for how you can use RIME for a model hosted on AWS SageMaker.

We expect this file to contain a `predict_dict` function that takes in a mapping from
feature name to feature value. This corresponds to one row in the dataset. This
method should return a score between 0 and 1.

This specific file implements this assuming that 1) your SageMaker model is hosted
on an AWS endpoint, and 2) that you have AWS credentials stored on your given
machine through the AWS CLI, and 3) that you have the requisite Python packages -
boto3, SageMaker - installed.

"""
import json
import boto3
import sagemaker
import pandas as pd


# Step 1: Initialize the Boto3 session.
# Note: By default we assume that your AWS credentials
# (aws_access_key_id, aws_secret_access_key) are stored in `~/.aws/credentials`.
# These can be generated through the AWS CLI through the `aws configure` command,
# and will be fetched through the default session initialization.
# If you would like to generate a temporary session id, please use the commented
# code instead of the default code instead.
sagemaker_session = sagemaker.Session()

# NOTE: uncomment below (and comment above) for using a temp session token.
# sts_client = boto3.client('sts')
# DURATION_SECONDS = 3600
# session_token_response = sts_client.get_session_token(
#     DurationSeconds=DURATION_SECONDS,
# )
# TEMP_ACCESS_KEY = session_token_response["Credentials"]["AccessKeyId"]
# TEMP_SECRET_ACCESS_KEY = session_token_response["Credentials"]["SecretAccessKey"]
# TEMP_SESSION_TOKEN = session_token_response["Credentials"]["SessionToken"]
# boto_session = boto3.Session(
#     aws_access_key_id=TEMP_ACCESS_KEY,
#     aws_secret_access_key=TEMP_SECRET_ACCESS_KEY,
#     aws_session_token=TEMP_SESSION_TOKEN,
#     region_name="us-east-1"
# )
# sagemaker_session = sagemaker.Session(boto_session=boto_session)

# Step 2: Specify endpoint and setup SageMaker predictor.
# The endpoint name can be found on your AWS SageMaker console, under 'Endpoints'.
# The API reference for the Predictor class can be found here:
# https://sagemaker.readthedocs.io/en/stable/api/inference/predictors.html
# You must also specify the serializer for the data - see
# https://sagemaker.readthedocs.io/en/stable/api/inference/serializers.html
# for more details.
serializer = sagemaker.serializers.CSVSerializer()
endpoint_name = 'TODO: put your endpoint here'
predictor = sagemaker.predictor.Predictor(
    endpoint_name,
    sagemaker_session=sagemaker_session,
    serializer=serializer
)

# Step 3: Implement the below function that should be applied to a row of data
# (in dictionary form), including any requisite preprocessing logic.
# By default, we assume that after preprocessing, the input is then sent to the
# model endpoint through `predictor.predict`, but feel free to edit/add/remove
# functions as you wish.

def custom_preprocessing(x: dict):
    # TODO: fill out with column order (assuming CSV input format)
    feature_columns = [
        "col1",
        "col2",
        "..."
    ]
    features = [x[f] for f in feature_columns]
    return features


def predict_dict(x: dict) -> float:
    d = custom_preprocessing(x)
    response = float(predictor.predict(d))
    return response

```