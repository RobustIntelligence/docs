# Prediction Configuration

RIME performs some model profiling in order to measure its overall performance. Depending on the dataset size and model throughput, profiling can be time-consuming. We provide some options to speed this process up.

### Template
```python
{
    "prediction_info": {
        "ref_path": null,
        "eval_path": null,
        "n_samples": null
    },
    ...
}
```

### Arguments

- `ref_path`: string or `null`, *default* = `null`

    Path to prediction cache corresponding to the reference data file. Please see the [NLP Prediction Cache Data Format](task_prediction_cache_format) reference for a description of supported file format.

- `eval_path`: string or `null`, *default* = `null`
    
    Path to prediction cache corresponding to the evaluation data file. Please see the [NLP Prediction Cache Data Format](task_prediction_cache_format) reference for a description of supported file format.

- `n_samples`: int or `null`, *default* = `null`

    Number of samples from each dataset to score. If both `ref_path` and `eval_path` are specified, this must be set to null. If either prediction cache is not specified and `n_samples` is set to `null`, the default is to score the entire dataset. If model throughput is low, it is recommended to use a prediction cache or specify a smaller value for `n_samples`.