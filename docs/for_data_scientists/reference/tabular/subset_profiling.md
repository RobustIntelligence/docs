# Subset Profiling Configuration

RIME automatically slices and profiles subsets of the provided datasets.
The configuration of this slicing and profiling affects the runtime of RIME and the ways in which the data and model
are evaluated. We expose this configuration for those users that would like finer-grained control over this process.
Each parameter has a default value, so you only need to specify
those parameters for which you disagree with the default.

### Template
This configuration should be specified within the [AI Stress Testing Configuration](stress_testing.md) JSON file, under the `subset_profiling_config` parameter.
```python
{
  ...,
  "subset_profiling_config": {
    "num_subsets": 10,
    "min_frq": 0.01,
    "confidence_level": 0.95,
    "subset_summary_metric": "accuracy",
    "num_feats_for_subset_summary": 3
  }
}
```


### Arguments

- `num_subsets`: int, *default* = `10`

  The number of subsets to partition each feature into. A higher number will lead to smaller subsets.

- `min_frq`: float, *default* = `0.01`
 
  The minimum relative size of subsets to evaluate. A `min_frq = 0.01` indicates that only
  subsets that contain >= 1% of the data should be evaluated.

- `confidence_level`: float, *default* = `0.95`

  For certain model performance metrics, confidence intervals are computed for the performance over each subset. This parameter allows you to set the confidence level used to determine the confidence interval.

- `subset_summary_metric`: Optional[str], *default* = `null`

  The subset performance degradation summary metric is calculated by taking the difference between the worst subset degradation and the overall degradation of the configured metric. 

- `num_feats_for_subset_summary`: int, *default* = `3`

  The number of features over which the subset performance degradation summary metric is aggregated. Features with higher importance are selected first. 
