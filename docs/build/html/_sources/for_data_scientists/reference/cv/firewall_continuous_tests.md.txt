AI Firewall Continuous Tests
=============================

Configuration of RIME AI Firewall Continuous Tests is done through a JSON configuration file that you pass as an argument to the RIME CLI.

Note: This is for the production version of Firewall Continuous Tests, where it is assumed you have already created a
Firewall and are uploading the latest production data to it.

### Template
```python
{
  "eval_path": ...,                       (REQUIRED)
  "eval_pred_path" ...,
}
```

### Arguments

- **`eval_path`**: string, ***required***

    Path to evaluation data file.

- `eval_pred_path`: string or null, *default* = `null`

  Path to a file containing the predictions on the evaluation dataset. A prediction file is required IF predictions are not included in the data file.
