Manual Continuous Tests Configuration
=============================

Configuration of manual RIME AI Firewall Continuous Tests is done through a JSON configuration file that you pass as an argument to the RIME CLI.


The configuration can take on different forms, offering a tradeoff between simplicity and flexibility. In the **file path**-based approach,
you may choose to specify a small number of file paths referencing the data and predictions file. This option works well for manual
CT runs. Alternatively in the **data info**-based approach, you can choose to specify `eval_data_info` directly and specify one of 
many [data sources](data_source.md). This allows you to specify `eval_data_info` from scratch - allowing you to modify all arguments,
including `pred_col`, `label_col`, `timestamp_col`, and more. 


### File Path-based Continuous Test Template
```python
{
  "eval_path": ...,                       (REQUIRED)
  "timestamp_col": ...,                   (REQUIRED)
  "eval_pred_path" ...,
}
```

### Arguments

- **`eval_path`**: string, ***required***

    Path to evaluation data file.

- **`timestamp_col`**: string, ***required***

  Name of column in data that corresponds to timestamps. The timestamp should
  be specified as "YYYY-MM-DD" if it is a date or ""YYYY-MM-DD HH:TT:SS"
  if it is a date and time where YYYY is the year as a four digit number, MM
  is the month as a two digit number, DD is the day as a two digit number, HH
  is the hour as a two digit number, TT is the minute as a two digit number
  and SS is the second as a two digit number.

  The time period for each continuous testing run. Current accepted
  values are `"day"` and `"hour"`.

- `eval_pred_path`: string or null, *default* = `null`

  Path to a csv or parquet file containing the predictions on the evaluation dataset.
  This is how predictions are specified for multi-class models. If you specified this 
  argument when running stress testing, you should also specify this when running 
  continuous testing. Otherwise predictions are assumed to be stored under the same
  `pred_col` specified when running stress testing.


### Data Info-based Continuous Test Template
```python
{
  "eval_data_info": {           (REQUIRED)
    "type": ...,
    ...
  },
}
```

### Arguments

- **`eval_data_info`**: SingleDataInfo, ***required***

    Configuration for the datasources to use for the evaluation set. 
    For a reference on how to configure a datasource, see the [Single Data Info section of Data Configuration](data_source.md#single-data-info-templates).
    
