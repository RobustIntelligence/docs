# Data Profiling Configuration

RIME performs profiling of data in order to inform how its tests run. This involves computing and
aggregating various image features. RIME uses safe default values and flags exceptions for each parameter,
so all these parameters are optional.

### Template

```python
{
  "class_names": ...,
}
```

### Arguments

- `class_names`: List[str] or `null`, *default* = `null`

    For the `"Image Classification"` model task only. Specify a list of class names corresponding to each integer class label for readability. The index of each name in the provided list should correspond with the class's index in the model's output 'probabilities' vector as well as the integer label in the data.
