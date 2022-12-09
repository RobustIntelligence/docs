# Debugging the Python SDK

## Troubleshooting RIME Stress Tests

When running a suite of stress tests on arbitrary models and datasets on a custom image, things can go wrong.
The RIME SDK has tools available to help you debug your stress test jobs.
This document includes a few common failure scenarios and recommended debugging techniques.

### Lost Job Object

If you close your Python notebook or scripting session, you will lose access to the ephemeral in-memory objects such as `Job`.
To recover these objects, connect the client to the same backend service.
```Python
rime_client = Client("my_vpc.rime.com", api_key="api-key")
```
Then, use `rime_client.list_stress_test_jobs()` to query the server for a list of jobs from the past two days.
You can filter by status and project ID to reduce the volume of jobs returned.
Then, you can call `get_status()` on each job to find which job is yours.
The return value from `get_status()` includes the start time and status of the job which should help you identify which job you started.
```Python
jobs = rime_client.list_stress_test_jobs(status_filters= ['succeeded', 'failed'], project_id="bar")
# Print out the metadata for each job to see which one you started most recently.
for job in jobs:
    print(job.get_status())
```

### Test Run Results Don't Show Up in UI

This indicates that the `Job` executing the suite of stress tests failed along the way.
There are a number of reasons why this would happen.
Here are a few:
* Misspecified `test_run_config`, dataset, or model.
* Resource limits exceeded.
* Managed image doesn't include the model's required dependencies.
* SDK version doesn't match the version of the cluster.
The best place to start is the `get_status()` of the `Job` object.
If the job status is `'FAILING'` and the `verbose` flag is set to `True`, `get_status()` will dump the logs to `stdout`.
For configuration issues, this can be very helpful.
```Python
# Assume the job is 'FAILING'
status = job.get_status(verbose=True, wait_until_finish=True)
# This will dump the logs if there are any to stdout.
```
Looking at the logs can help solve a lot of problems.

If you have trouble making additional progress with debugging, please contact RI support.
