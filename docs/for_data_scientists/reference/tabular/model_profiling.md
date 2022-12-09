# Model Profiling Configuration

RIME performs some profiling of the model in order to inform which tests to run.  
This can take some time, depending on the size of the dataset, so we provide some options to control this.  
By default, RIME will attempt to infer an optimal value for all of these options, so only use these parameters if you think RIME is not selecting appropriate values.  

### Template
This configuration should be specified within the [AI Stress Testing Configuration](stress_testing.md) JSON file, under the `model_profiling_info` parameter.
```python
{
  ...,
  "model_profiling_info": {
    "nrows_for_summary": null,
    "nrows_for_feature_importance": null,
    "feature_importance_config": {
       "path": "path/to/feature/importance.csv",
       "feature_imp_column": "featureImportance",
       "feature_name_column": "featureName"
    },
    "num_calib_bins": 10,
    "impact_metric": null,
    "drift_impact_metric": null,
    "metric_configs": {...}
  }
}
```


### Arguments

- `nrows_for_summary`: int or `null`, *default* = `null`

  The number of rows to use for calculating summary metrics of model. You may want to specify a smaller amount if making calls to your model takes a while.
- `nrows_for_feature_importance`: int or `null`, *default* = `null`

  The number of rows to use when calculating feature importance of the model. You may want to specify a smaller amount if making calls to your model takes a while. If a feature importance config is provided, this will be ignored.
- `feature_importance_config`: mapping or `null`, *default* = `null`

  If you want to provide information about feature importance, you should specify that here. The value of this key should be another dictionary with the following key value pairs:
  - `path`: str
    
    Path to csv or parquet file containing feature importance information, should be relative to `mount_dirs/data` subdirectory.
  - `feature_imp_column`: str
    
    Name of the column in this csv that corresponds to feature importance values.
  - `feature_name_column`: str
    
    Name of the column in this csv that corresponds to the feature name.
- `num_calib_bins`: int, *default* = 10

  The number of bins to use when computing the calibration curve for a binary classification model.
- `impact_metric`: `MetricName` or `null`, *default* = `null`

  The metric to use when computing model impact for abnormal input and transformation tests.
- `drift_impact_metric`: `MetricName` or `null`, *default* = `null`

  The metric to use when computing model impact for drift tests.
- `metric_configs`: mapping or `null`, *default* = `null`

  The parameters to configure each metric used during testing. For instance, to configure NDCG to accumulate only to a specific rank `k=50`, specify `{"normalized_discounted_cumulative_gain": {"k": 50}}`.
