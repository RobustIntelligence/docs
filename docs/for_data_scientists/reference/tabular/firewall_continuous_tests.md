AI Firewall Continuous Tests
=============================

Configuration of RIME AI Firewall Continuous Tests is done through a JSON configuration file that you pass as an argument to the RIME CLI.

Note: This is for the production version of Firewall Continuous Tests, where it is assumed you have already created a
Firewall and are uploading the latest production data to it. 

### Template
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
