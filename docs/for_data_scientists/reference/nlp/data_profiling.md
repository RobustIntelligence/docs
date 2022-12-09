# Data Profiling Configuration

RIME performs profiling of data in order to inform how its tests run. This involves computing and
aggregating various text features. RIME uses safe default values and flags exceptions for each parameter,
so all these parameters are optional.

### Template

```python
{
  "class_names": ...,
  "ngram_filter_stop_words": false,
  "ngram_filter_punctuation": false,
  "custom_numeric_metadata": ...,
  "custom_categorical_metadata": ...,
}
```

### Arguments

- `class_names`: List[str] or `null`, *default* = `null`

    For the `"Text Classification"` and `"Natural Language Inference"` model tasks only. Specify a list of class names corresponding to each integer class label for readability. The index of each name in the provided list should correspond with the class's index in the model's output 'probabilities' vector as well as the integer label in the data.


- `ngram_filter_stop_words`: bool, *default* = `False`

    Whether to filter stop words for N-Gram drift and abnormal inputs tests.

- `ngram_filter_punctuation`: bool, *default* = `False`

    Whether to filter all unicode punctuation for N-Gram drift and abnormal inputs tests.

- `custom_numeric_metadata`: List[str] or `null`, *default* = `null`

    Specify a list of numeric features that exist in your data, that RIME will run tests on (ex: Age). These should have a corresponding key-value pair within the 'meta' dict for each datapoint.

- `custom_categorical_metadata`: List[str] or `null`, *default* = `null`

    Specify a list of categorical features that exist in your data, that RIME will run tests on (ex: Author). These should have a corresponding key-value pair within the 'meta' dict for each datapoint.