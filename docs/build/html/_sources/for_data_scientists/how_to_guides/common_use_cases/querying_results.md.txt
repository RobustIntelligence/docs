# Querying RIME Results

Besides viewing RIME results in the web application, you may use the Python SDK to retrieve data that can be programmatically parsed. This functionality is very helpful for incorporating RIME into your production model/data pipelines. For instance, if you are interested in the results of a specific feature, test, or statistic, you can fetch stress testing results from the RIME backend and write code to make decisions (e.g. whether to deploy the model) based on the results.

To begin, initialize the `Client` and point it to the location of your RIME backend.

```python
from rime_sdk import Client

client = Client("rime.<YOUR_ORG_NAME>.rime.dev", "<YOUR_API_TOKEN>")
```

## Get the Results

To retrieve information about the test run results, first retrieve the desired test run object:

```python
test_run = client.get_test_run("your_desired_test_run_id_here")
```

If the user is running Continuous Testing and wants to retrieve a test run corresponding to a specific time bin, this appoach can be deployed:

```python
test_runs = firewall.get_test_runs()
from datetime import datetime
desired_start = datetime(2018, 8, 18, 0, 0)
test_run = next(test_run for test_run in test_runs if test_run.start_time == desired_start)
```


Now the user can analyze the results of the test run at varying levels of granularity! We can begin by retrieving a high-level summary of the test run as a Pandas DataFrame:

```python
high_level_results = test_run.get_result_df()
```

<img src="../../../_static/queryability_high_level_results.png">

If we want to dig into a specific test batch (i.e. look at the `unseen categorical` test specifically), we can do the following to get a results overview as a Pandas Series:

```python
test_batch = test_run.get_test_batch("unseen_categorical")
high_level_test_batch_results = test_batch.summary()
```

<img src="../../../_static/queryability_high_level_batch_results.png">

If we want more granularity, we can retrieve all the individual test cases for the given test batch (e.g. the results of `unseen categorical` over each feature) as a Pandas DataFrame:

```python
granular_test_batch_results = test_batch.get_test_cases_df()
```

<img src="../../../_static/queryability_granular_test_batch_results.png">

In general, we can retrieve this granular information for all tests at once as a Pandas DataFrame:

```python
all_granular_test_batch_results = test_run.get_test_cases_df(show_test_case_metrics=True)
```

<img src="../../../_static/queryability_all_granular_test_batch_results.png">

At the test-case level, RIME returns information that can be test-specific. If we are placing the test cases for all tests into the same table, this could result in a sparse table with columns that are empty for most rows. If the user wants to avoid this sparsity and only retrieve common columns across all tests the user can simply leave the `show_test_case_metrics` flag unspecified as follows:

```python
limited_all_granular_test_batch_results = test_run.get_test_cases_df()
```

<img src="../../../_static/queryability_limited_all_granular_test_batch_results.png">

The user can also get an iterator representing all of the test batches. This can be useful if the user does not know the name of the test batch they want to query or if the user has a custom use case which involves iterating over all test batch objects:

```python
iterator_over_all_test_batches = test_run.get_test_batches()
````
