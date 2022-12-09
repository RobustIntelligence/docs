# Using the REST API

This walkthrough will cover how to create a project, run a basic stress test, and get test case results using the REST API instead of the SDK. This walkthrough will cover using the REST API via Curl or Python, but you can use the API in any language.

## REST API Walkthrough(Python)

```python
import json
import time
import requests

# TODOS FOR YOUR STRESS TEST
# Set equal to your reference, evaluation and model data paths.
REFERENCE_DATA_PATH = ""  # TODO: Specify
EVALUATION_DATA_PATH = ""  # TODO: Specify
MODEL_PATH = ""  # TODO: OPTIONAL
# Set equal to your cluster url. e.g. "https://rime.YOUR_CLUSTER.dev"
CLUSTER_URL = ""  # TODO: Specify
# Set equal to an authorized api key for your cluster.
API_TOKEN = ""  # TODO: Specify

API_URL = f"{CLUSTER_URL}/v1"
# Used to authenticate REST requests to your cluster.
headers = {"rime-api-key": API_TOKEN}

# CREATE A PROJECT
PROJECT_NAME = ""  # TODO: Specify
PROJECT_DESCRIPTION = ""  # TODO: Specify
project_body = {
    "name": PROJECT_NAME,
    "description": PROJECT_DESCRIPTION
}
# Note: projects must have unique names otherwise this request will return an error.
res = requests.post(f"{API_URL}/projects", json=project_body, headers=headers)
if res.status_code != 200 :
    raise ValueError(res)
projectId = res.json()["project"]["id"]

# CONFIGURING YOUR STRESS TEST:
stress_test_config = {
    "run_name": "REST API example 1",
    "data_info": {
        "pred_col": "preds",
        "label_col": "label",
        "ref_path": REFERENCE_DATA_PATH,
        "eval_path": EVALUATION_DATA_PATH
    },
    "model_info": {
        "path": MODEL_PATH
    },
}

body = {
    "testRunConfig": json.dumps(stress_test_config),
    "projectId": projectId
}

# CREATING YOUR STRESS TEST
res = requests.post(f"{API_URL}/stress-tests", json=body, headers=headers)
if res.status_code != 200:
    raise ValueError(res)

# QUERYING RESULTS:
# Get the job id from the previous response and wait for it to finish.
job_id = res.json()['job']['jobId']
# Get a job object with job metadata from the job id.
job_response = requests.get(f"{API_URL}/jobs/{job_id}", headers=headers)
while True:
    job_response = requests.get(f"{API_URL}/jobs/{job_id}", headers=headers)
    if job_response.status_code != 200 :
        raise ValueError(res)
    job_response_json = job_response.json()
    print(job_response_json)
    # Check status of whether job succeeded, failed, or is still running.
    job_status = job_response_json['job']['status']
    if job_status == "JOB_STATUS_SUCCEEDED":
        # Get the test run id associated with the job.
        test_run_id_json = requests.get(f"{API_URL}/jobs/{job_id}/test-run-id", headers=headers).json()
        test_run_id = test_run_id_json["testRunId"]
        break
    elif job_status == "JOB_STATUS_FAILED":
        # Get logs of job failure.
        logs = requests.get(f"{API_URL}/logs/{job_id}", headers=headers, stream=True)
        for line in logs.iter_lines():
            if line:
                print(line)
        raise ValueError(line)
    else:
        # If job is not done, then try again after ten seconds.
        time.sleep(10)

# LISTING TESTS RESULTS
all_test_cases = []
# Due to pagination, the initial query should use the test_run_id, all subsequent ones 
# should use page_token.
page_token = ""
payload = {"listTestCasesQuery.testRunId": test_run_id}
while True:
    # Make multiple calls, iterating through pages until all test cases are returned.
    if page_token != "":
        payload = {"page_token": page_token}
    res = requests.get(f"{API_URL}/test-cases", params=payload, headers=headers)
    if res.status_code != 200 :
        raise ValueError(res)
    res_json = res.json()
    all_test_cases.extend(res_json['testCases'])
    page_token = res_json['nextPageToken']
    # If the previous response specifies that hasMore is false, we have gotten all the test cases.
    if not res_json["hasMore"]:
        break
# All the test cases. You can load this into a dataframe to better view or analyze the results on the UI.
print(all_test_cases)
```
