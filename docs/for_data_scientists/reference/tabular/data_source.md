Data Configuration
==================

Configuring a data source can be done by specifying a mapping in the main RIME JSON configuration file, under the
`data_info` argument.

NOTE: for AI Continuous Testing, predictions are required. Either `pred_col` must be specified or `ref_pred_path` and `eval_pred_path` must be specified.

### Template
```python
{
    "data_info": {
        "ref_path": "path/to/ref.csv",        (REQUIRED)
        "eval_path": "path/to/eval.csv",      (REQUIRED)
        "label_col": "Label",
        "pred_col": "Prediction",             (WORKS FOR ALL TASKS EXCEPT MULTI-CLASS, REQUIRED FOR CONTINUOUS TESTING)
        "ref_pred_path": "path/to/ref/preds.csv",  (ONLY SPECIFY FOR MULTI-CLASS, REQUIRED FOR CONTINUOUS TESTING)
        "eval_pred_path": "path/to/eval/preds.csv",  (ONLY SPECIFY FOR MULTI-CLASS, REQUIRED FOR CONTINUOUS TESTING)
        "nrows": null,
        "categorical_features": null,
        "loading_kwargs": null,
        "ranking_info": null,
        "protected_features": null
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

  Path to a csv or parquet file containing the predictions on the reference dataset. This is how
  predictions
  are specified for multi-class models.
- `eval_pred_path`: string or null, *default* = `null`

  Path to a csv or parquet file containing the predictions on the evaluation dataset. This is how
  predictions
  are specified for multi-class models.
- `nrows`: int or null, *default* = `null`

    Number of rows of data to load and test. If `null`, will load all rows. By default it is `null`.
- `categorical_features`: list or null, *default* = `null`

    List of categorical features in data. If provided, these should be ALL the categorical features. If `null`, RIME will automatically determine whether a column is categorical or not. By default it is `null`.
- `loading_kwargs`: mapping, *default* = `null`

    Keyword arguments to be passed to the `pandas` loading function (either `pd.read_csv` or `pd.read_parquet`, depending on your data format). NOTE: if you wish to specify `nrows`, this should NOT be done with these kwargs but rather with the `nrows` parameter above.
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
- `protected_features`: list or null, *default* = `null`

    List of protected features in data. If the `Bias And Fairness` category is added to `categories` in the test config (see [TestSuiteConfig()](tests.md), and `protected_features` are included - a set of bias and fairness tests will be run over the protected features.
