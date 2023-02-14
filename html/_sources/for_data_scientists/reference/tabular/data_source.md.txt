Data Configuration
==================

Configuring a data source can be done by specifying a mapping in the main RIME JSON configuration file, under the
`data_info` argument.

The `data_info` configuration can take on different forms, offering a tradeoff between simplicity and flexibility. In the **default** approach,
you may choose to specify the file paths to both the reference and evaluation datasets, along with supporting arguments such as `pred_col`, 
`label_col`, and more. This is the easiest configuration to get started with.
In the **split** approach, you may choose to specify a separate "single" data info struct for both the reference and evaluation datasets:
`ref_data_info` and `eval_data_info`. Both the reference and evaluation single data info structs can take on different configuration types, 
from a file-path based approach, to a custom data loader, to a Delta Lake table, to our data collector (for Continuous Testing only). This allows
you to specify different data loaders for the reference and evaluation datasets. The configuration
templates for all of these data infos are also detailed below.

NOTE: for AI Continuous Testing, predictions are required. Either `pred_col` must be specified or `ref_pred_path` and `eval_pred_path` must be specified.

### Default Data Info Template
```python
{
    "data_info": {
        "ref_path": "path/to/ref.csv",              (REQUIRED)
        "eval_path": "path/to/eval.csv",            (REQUIRED)
        "label_col": "Label",
        "pred_col": "Prediction",                   (WORKS FOR ALL TASKS EXCEPT MULTI-CLASS, REQUIRED FOR CONTINUOUS TESTING)
        "ref_pred_path": "path/to/ref/preds.csv",   (ONLY SPECIFY FOR MULTI-CLASS, REQUIRED FOR CONTINUOUS TESTING)
        "eval_pred_path": "path/to/eval/preds.csv", (ONLY SPECIFY FOR MULTI-CLASS, REQUIRED FOR CONTINUOUS TESTING)
        "nrows": null,
        "categorical_features": null,
        "protected_features": null,
        "features_not_in_model": null,
        "feature_type_path": null,
        "ranking_info": null,                        (REQUIRED FOR RANKING)
        "loading_kwargs": null,
        "embeddings": null
    },
    ...
}
```

### Arguments

- **`ref_path`**: string, ***required***

    Path to reference data file.
- **`eval_path`**: string, ***required***

    Path to evaluation data file.
- `label_col`: string or null, *default* = `null`

    Name of column in data that corresponds to the labels.
- `pred_col`: string or null, *default* = `null`

    Name of column in data that corresponds to the predictions.
- `ref_pred_path`: string or null, *default* = `null`

    Path to a CSV or Parquet file containing the predictions on the reference dataset. This is how
    predictions are specified for multi-class models.
- `eval_pred_path`: string or null, *default* = `null`

    Path to a CSV or Parquet file containing the predictions on the evaluation dataset. This is how
    predictions are specified for multi-class models.
- `nrows`: int or null, *default* = `null`

    Number of rows of data to load and test. If `null`, will load all rows. By default it is `null`.
- `categorical_features`: list or null, *default* = `null`

    List of categorical features in data. If provided, these should be ALL the categorical features. If `null`, RIME will automatically determine whether a column is categorical or not. By default it is `null`.
- `protected_features`: list or null, *default* = `null`

    List of protected features in data. If the `Bias and Fairness` category is added to `categories` in the test config (see [TestSuiteConfig()](tests.md), and `protected_features` are included, a set of bias and fairness tests will be run over the protected features.
- `features_not_in_model`: list or null, *default* = `null`

    List of features in the dataset that are not used by the model. Specifying this will ensure that only relevant tests are run on these features.
- `feature_type_path`: string, *default* = `null`

    Path to a CSV file that specifies the data type of each feature. The file should have two columns: `FeatureName` and `FeatureType`. The possible values for `FeatureType` are `BoolCategoricalColumn`, `DomainColumn`, `EmailColumn`, `NumericCategoricalColumn`, `StringCategoricalColumn`, `UrlColumn`, `FloatColumn`, `IntegerColumn`.
- `ranking_info`: mapping, *default* = `null`

    Arguments to be used for Ranking tasks. If you are not running RIME on a Ranking task this value should be null. If you are running on a Ranking task, the following keys should be provided:
    - `query_col`: string, *required*

        Name of column in dataset that contains the query ids.
    - `nqueries`: int or null, *default* = `null`

        Number of queries to consider when running RIME. If `null`, will use all queries.
    - `nrows_per_query`: int or null, *default* = `null`

        Number of rows to use per query when running RIME. If `null`, will use all rows.
    - `drop_query_id`: bool, *default* = True

        Whether to drop the query ID column from the dataset to avoid passing as a feature to the model.
- `loading_kwargs`: mapping, *default* = `null`

    Keyword arguments to be passed to the `pandas` loading function (either `pd.read_CSV` or `pd.read_Parquet`, depending on your data format). NOTE: if you wish to specify `nrows`, this should NOT be done with these kwargs but rather with the `nrows` parameter above.

- `embeddings`: list or `null`, *default* = `null`

    A list of dictionaries corresponding to information for each embedding. The arguments for each dictionary are described below.

    - `name`: string

        Name of the embedding to be shown in the test run results.

    - `cols`: list
  
        List of column names corresponding to the embedding. For example, suppose each data row is represented by columns `age`, `is_member`, `query_0`, `query_1`, `query_2`, etc., where each column "`query_\d`" is a dimension of a sentence embedding extracted from a user query. Specifying `"embeddings": [{"name": "user_query", "cols": ["query_0", "query_1", "query_2", ...]}]`  (i.e., specifying each column contained by the embedding) would direct the RI Platform to treat these columns as a single dense vector-valued embedding feature.


### Split Data Info Template
```python
{
    "data_info": {
        "ref_data_info": ...,              (REQUIRED)
        "eval_data_info": ...,            (REQUIRED)
    },
    ...
}
```

### Arguments

- **`ref_data_info`**: SingleDataInfo, ***required***

    Path to single data info struct (see below).
- **`eval_data_info`**: SingleDataInfo, ***required***

    Path to single data info struct (see below).

### Single Data Info Templates

Note that these single data info structs can be used to specify both the `ref_data_info` as well as `eval_data_info`
in the split data into template above.

Note that *all* single data info structs also take in a set of tabular parameters which allow the user to additionally
specify properties of their data. These parameters include fields such as `label_col`, `pred_col`, `nrows`, `protected_features`,
and more. The full list is detailed below. Note that for AI Continuous Testing, predictions are required. 
Either `pred_col` must be specified or `pred_path` must be specified.

#### General Tabular Parameters for Single Data Info
```python
{
    "label_col": "Label",
    "pred_col": "Prediction",                   (WORKS FOR ALL TASKS EXCEPT MULTI-CLASS, REQUIRED FOR CONTINUOUS TESTING)
    "pred_path": "path/to/preds.csv",           (ONLY SPECIFY FOR MULTI-CLASS, REQUIRED FOR CONTINUOUS TESTING)
    "nrows": null,
    "nrows_per_time_bin": null,
    "categorical_features": null,
    "protected_features": null,
    "features_not_in_model": null,
    "feature_type_path": null,
    "ranking_info": null,                       (REQUIRED FOR RANKING)
    "loading_kwargs": null,
    "embeddings": null
}
```

#### Arguments
- `label_col`: string or null, *default* = `null`

    Name of column in data that corresponds to the labels.
- `pred_col`: string or null, *default* = `null`

    Name of column in data that corresponds to the predictions.
- `pred_path`: string or null, *default* = `null`

    Path to a CSV or Parquet file containing the predictions on the evaluation dataset. This is how
    predictions are specified for multi-class models.
- `nrows`: int or null, *default* = `null`

    Number of rows of data to load and test. If `null`, will load all rows. By default it is `null`.
- `nrows_per_time_bin`: int or null, *default* = `null`

    Number of rows of data per time bin to load and test in continuous testing (does not affect stress testing results). If `null`, will load all rows. By default it is `null`.
- `categorical_features`: list or null, *default* = `null`

    List of categorical features in data. If provided, these should be ALL the categorical features. If `null`, RIME will automatically determine whether a column is categorical or not. By default it is `null`.
- `protected_features`: list or null, *default* = `null`

    List of protected features in data. If the `Bias And Fairness` category is added to `categories` in the test config (see [TestSuiteConfig()](tests.md), and `protected_features` are included - a set of bias and fairness tests will be run over the protected features.
- `features_not_in_model`: list or null, *default* = `null`

    List of features in the dataset that are not used by the model. Specifying this will ensure that only relevant tests are run on these features.
- `feature_type_path`: string, *default* = `null`

    Path to a CSV file that specifies the data type of each feature. The file should have two columns: `FeatureName` and `FeatureType`. The possible values for `FeatureType` are `BoolCategoricalColumn`, `DomainColumn`, `EmailColumn`, `NumericCategoricalColumn`, `StringCategoricalColumn`, `UrlColumn`, `FloatColumn`, `IntegerColumn`.
- `ranking_info`: mapping, *default* = `null`

    Arguments to be used for Ranking tasks. If you are not running RIME on a Ranking task this value should be null. If you are running on a Ranking task, the following keys should be provided:
    - `query_col`: string, *required*

        Name of column in dataset that contains the query ids.
    - `nqueries`: int or null, *default* = `null`

        Number of queries to consider when running RIME. If `null`, will use all queries.
    - `nrows_per_query`: int or null, *default* = `null`

        Number of rows to use per query when running RIME. If `null`, will use all rows.
    - `drop_query_id`: bool, *default* = True

        Whether to drop the query ID column from the dataset to avoid passing as a feature to the model.
- `loading_kwargs`: mapping, *default* = `null`

  Keyword arguments to be passed to the `pandas` loading function (either `pd.read_CSV` or `pd.read_Parquet`, depending on your data format). NOTE: if you wish to specify `nrows`, this should NOT be done with these kwargs but rather with the `nrows` parameter above.

- `embeddings`: list or `null`, *default* = `null`

    A list of dictionaries corresponding to information for each embedding. The arguments for each dictionary are described below.

    - `name`: string

        Name of the embedding to be shown in the test run results.

    - `cols`: list
  
        List of column names corresponding to the embedding. For example, suppose each data row is represented by columns `age`, `is_member`, `query_0`, `query_1`, `query_2`, etc., where each column "`query_\d`" is a dimension of a sentence embedding extracted from a user query. Specifying `"embeddings": [{"name": "user_query", "cols": ["query_0", "query_1", "query_2", ...]}]`  (i.e., specifying each column contained by the embedding) would direct the RI Platform to treat these columns as a single dense vector-valued embedding feature.

#### File-based Single Data Info Template

```python
{
    "file_name": "path/to/file.csv",
    **tabular_params
}
```

#### Arguments

- **`file_name`**: string, ***required***

    Path to data file.

- **`**tabular_params`**: Dict

    See Tabular Parameters above.


#### Custom Dataloader Single Data Info Template

```python
{
    "load_path": "path/to/custom_loader.py",
    "load_func_name": "load_fn_name",
    "loader_kwargs": null,
    "loader_kwargs_json": null
    **tabular_params
}
```

#### Arguments

- **`load_path`**: string, ***required***

    Path to custom loader Python file.

- **`load_func_name`**: string, ***required***

    Name of the loader function. Must be defined within the Python file.

- **`loader_kwargs`**: Dict, *default* = `null`
    
    Arguments to pass in to the loader function, in dictionary form. We pass these arguments in as **kwargs.
    Only one of `loader_kwargs` and `loader_kwargs_json` can be specified.

- **`**loader_kwargs_json`**: Dict

    Arguments to pass in to the loader function, in JSON-serialized string form.
    We pass these arguments in as **kwargs.
    Only one of `loader_kwargs` and `loader_kwargs_json` can be specified.

- **`**tabular_params`**: Dict

    See Tabular Parameters above.


#### Data Collector Single Data Info Template

NOTE: this can only be specified as part of a Continuous Testing config, not offline testing config. See the 
[Continuous Tests Configuration](firewall_continuous_tests.md) for more details.

```python
{
    "start_time": start_time,
    "end_time": end_time,
    **tabular_params
}
```

#### Arguments

- **`start_time`**: int, ***required***

    Start time of the data collector to fetch data from. Format is UNIX epoch time in seconds.

- **`end_time`**: int, ***required***

    End time of the data collector to fetch data from. Format is UNIX epoch time in seconds.

- **`**tabular_params`**: Dict

    See Tabular Parameters above.

#### Intersections Template

Specifies a custom group based on a specified intersection of features. Subset performance tests run over the specified intersection.

```python
{
    {
    "data_info": {
        "ref_path": "path",
        "eval_path": "path",
        "ref_pred_path": "path",
        "eval_pred_path": "path",
        "label_col": "Column label",
        "protected_features": ["feature1", "feature2", "feature3"],
	        "intersections": [{"features": ["feature1", "feature2", "feature3"]}, {"features": ["feature3", "feature4"]}]
}
```

#### Arguments

- **`ref_path`**: string, ***required***

    Path to reference data file.

- **`eval_path`**: string, ***required***

    Path to evaluation data file.

- **`ref_pred_path`**: string, ***required***

    Path to a CSV or Parquet file containing the predictions on the reference dataset. This is how
    predictions are specified for multi-class models.

- **`eval_pred_path`**: string, ***required***

    Path to a CSV or Parquet file containing the predictions on the evaluation dataset. This is how
    predictions are specified for multi-class models.

- **`label_col`**: string, ***required***

    Name of column in data that corresponds to the labels.

- **`protected_features`**: array, ***required***

    List of protected features in data. If the `Bias And Fairness` category is added to `categories` in the test config (see [TestSuiteConfig()](tests.md), and `protected_features` are included, a set of bias and fairness tests will be run over the protected features.

- **`intersections`**: array, ***required***

    A list of arrays of features. The intersection of the sets of features specifies a custom group on which the performance tests are run.

#### Delta Lake Single Data Info Template

NOTE: the Databricks secret access token (along with the "server_hostname" and "http_path")
are specified as part of [Data Sources Configuration](/for_admins/data-sources.md).
If you are launching a manual Stress Test run or Continuous Test run,
do not fill in the server_hostname or http_path fields; those fields + the secret token
will automatically be inserted if you specify the corresponding data source name when 
kicking off the run.

```python
{
    "server_hostname": "<workspace-id>.cloud.databricks.com",
    "http_path": "http/path",
    "table_name": "table_name",
    "start_time": start_time,
    "end_time": end_time,
    "time_col": "Timestamp column",
    **tabular_params
}
```

#### Arguments

- **`server_hostname`**: string, ***required***

    Server hostname of the Databricks cluster. This should be specified as part of a Data Source.
    See [Databricks docs](https://docs.databricks.com/dev-tools/python-sql-connector.html) for more details.

- **`http_path`**: string, ***required***

    HTTP Path of the Databricks cluster. This should be specified as part of a Data Source.
    See [Databricks docs](https://docs.databricks.com/dev-tools/python-sql-connector.html) for more details.

- **`table_name`**: string, ***required***

    Name of the Delta Lake table. 

- **`start_time`**: int, ***required***

    Start time of the Delta Lake table to fetch data from. Format is UNIX epoch time in seconds.

- **`end_time`**: int, ***required***

    End time of the Delta Lake table to fetch data from. Format is UNIX epoch time in seconds.

- **`time_col`**: string, ***required***
    
    Name of the timestamp column. This is a required field in order to determine the range of 
    data which satisfies the `start_time` and `end_time` params.

- **`**tabular_params`**: Dict

    See Tabular Parameters above.
