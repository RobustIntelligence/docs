# Test Run Progress

After kicking off a stress test or continuous testing job, it is natural to want to monitor the progress
of that job. Currently, RIME only shows test run progress and status in the UI for stress
test jobs. However, it exposes a way to programmatically monitor the progress of both 
stress testing and continuous testing jobs.

When kicking off a stress test with the Python SDK (`job = rime_client.start_stress_test`) the object returned is
a `Job` which can be used to monitor progress. `job.get_status()` will return the current progress of the job,
and `job.get_status(wait_until_finish=True, verbose=True)` will continue outputting the progress of the job every 5 seconds
until the job completes.

To get the current progress of a job:

```python
job.get_status()
```

To continuously get the progress of a job:

```python
job.get_status(wait_until_finish=True, verbose=True)
```

You can do the same for a continuous test that you have just kicked off.

For full documentation on what a `Job` is and how else it can be used, please see [the reference documentation](/for_data_scientists/reference/python-sdk.rst).
