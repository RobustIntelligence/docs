# Data Profiling Configuration

RIME performs profiling of data in order to inform how its tests run. This involves inferring feature types, 
computing feature relationships, and restricting feature counts. RIME uses safe default values and flags exceptions for each parameter,
so all these parameters are optional.

### Template
This configuration should be specified within the [AI Stress Testing Configuration](stress_testing.md) JSON file, under the `data_profiling_info` parameter.
```python
{
    ...,
    "data_profiling_info": {
        "min_nunique_for_numeric": 10,
        "numeric_violation_threshold": 0.01,
        "categorical_violation_threshold": 0.05, 
        "min_unique_prop": 0.99,
        "allow_float_unique": false,
        "num_quantiles": 1001,
        "num_feats_to_profile": null,
        "compute_feature_relationships": true,
        "compute_numeric_feature_relationships": false,
        "ignore_nan_for_feature_relationships": true,
        "class_names": null
    }
}
```

### Arguments
- `min_nunique_for_numeric`: int, *default* = 10 

    Minimum number of unique values in column for it to be considered a numeric column, otherwise its considered categorical.
- `numeric_violation_threshold`: float, *default* = 0.01,

    Maximum fraction of violations when assigning numeric columns (not including missing values).
- `categorical_violation_threshold`: float, *default* = 0.05,

    Maximum fraction of violations when assigning categorical subtypes (not including missing values).
- `min_unique_prop`: float, *default* = 0.99 

    If data has at least min_unique_prop proportion of unique values then classify as a column that must have unique values.
- `allow_float_unique`: bool, *default* = False

    Allow float columns to be inferred as unique.
- `num_quantiles`: int, *default* = 1001

    The number of quantiles to store for numerical columns.
- `num_feats_to_profile`: int or `null`, *default* = `null` 

    Number of features to profile for smart feature sampling.
- `compute_feature_relationships`: bool, *default* = True

    Whether to compute feature relationships.
- `compute_numeric_feature_relationships`: bool, *default* = False 

    Whether to compute feature relationships for discretized numeric columns.
- `ignore_nan_for_feature_relationships`: bool, *default* = True 

    Whether to ignore nan when computing feature relationships.
- `class_name`: List[str] or `null`, *default* = `null`

    Optional list of label class names (in label order). For classification tasks only.
