# Using the REST API

This walkthrough will cover how to run a basic stress test using the REST API instead of the SDK. This walkthrough will cover using the REST API via Curl or Python, but you can use the API in any language.

## REST API Walkthrough(Python)

```python
import json
import time
import requests

#CREATING YOUR STRESS TEST:
stress_test_config = {
    "run_name": "REST API example 1",
    "data_info": {
        "pred_col": "preds",
        "label_col": "label",
        "ref_path": "<ref data path>",
        "eval_path": "<eval data path>"
    },
    "model_info": {
        "path": "<model path>"
    },
}
body = {
    "test_run_config": json.dumps(stress_test_config),
}
# You will need to set this equal to your cluster url
RIME_CLUSTER_URL= "" #TODO: Specify
API_URL = f"{RIME_CLUSTER_URL}/v1"
# You will need to set api key equal to an api key for your cluster.
headers = {"rime-api-key": "*****"}
res = requests.post(API_URL + '/stress-tests', json=body, headers=headers)
if res.status_code != 200 :
    raise ValueError(res)
# QUERYING RESULTS:
# Get the job id from the previous response and wait for it to finish.
job_id = res.json()['job']['jobId']
job_response = requests.get(API_URL + "/jobs/" + job_id, headers=headers)
while True:
    job_response = requests.get(API_URL + "/jobs/" + job_id, headers=headers)
    if job_response.status_code != 200 :
        raise ValueError(res)
    # Check if job succeeded or failed
    job_response_json = job_response.json()
    print(job_response_json)
    job_status = job_response_json['job']['status']
    if job_status == "JOB_STATUS_SUCCEEDED":
        # Get the test run id associated with the job
        test_run_id = job_response_json['job']['jobData']['stress']['testRunId']
        break
    elif job_status == "JOB_STATUS_FAILED":
        raise ValueError(job_response_json)
    else:
        # If job is not done, then try again after ten seconds
        time.sleep(10)

all_test_cases = []
# The initial query should use the test_run_id, all subsequent ones should use page_token.
page_token = ''
body = {"list_test_cases_query":{"test_run_id": test_run_id}}
while True:
    # Make multiple calls, iterating through pages until all test cases are returned
    if page_token:
        data = {"page_token": page_token}
    res = requests.post(API_URL + '/test-cases', json=body, headers=headers)
    if res.status_code != 200 :
        raise ValueError(res)
    res_json = res.json()
    all_test_cases.extend(res['testCases'])
    page_token = res['nextPageToken']
    # If the page token is an empty string, we have gotten all the test cases.
    if not res["hasMore"]:
        break
# All the test cases. You can load this into a dataframe to better view or analyze the results on the UI.
print(all_test_cases)
```
