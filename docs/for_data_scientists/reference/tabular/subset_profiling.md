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
    "num_subsets": 5,
    "min_frq": 0.01,
    "confidence_level": 0.95
  }
}
```


### Arguments

- `num_subsets`: int, *default* = `5`

  The number of subsets to partition each feature into. A higher number will lead to smaller subsets.

- `min_frq`: float, *default* = `0.01`
 
  The minimum relative size of subsets to evaluate. A `min_frq = 0.01` indicates that only
  subsets that contain >= 1% of the data should be evaluated.

- `confidence_level`: float, *default* = `0.95`

  For certain model performance metrics, confidence intervals are computed for the performance over each subset. This parameter allows you to set the confidence level used to determine the confidence interval.
