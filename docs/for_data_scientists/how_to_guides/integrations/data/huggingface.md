# Hugging Face Datasets

RIME now offers a data provider that natively integrates with Hugging Face's [`load_dataset`](https://huggingface.co/docs/datasets/v2.3.2/en/package_reference/loading_methods#datasets.load_dataset) API. To use this functionality, specify `"type": "huggingface"` in the `data_info` configuration arg and provide the target dataset tag.

### Data Info Configuration

```python
{
    "data_info": {
        "type": "huggingface",                      (REQUIRED)
        "dataset_uri": "path",                      (REQUIRED)
        "ref_split": "train",
        "eval_split": "test",
        "text_key": "text",
        "label_key":  "label",
        "eval_label_key": "label",
        "loading_params": {}
    },
    ...
}
```

### Arguments

- **`dataset_uri`**: string, ***required***
    
    The path or name of the dataset.

- **`ref_split`**: string,  *default* = `"train"`

    The name of the split to use for the reference set.

- **`eval_split`**: string,  *default* = `"test"`

    The name of the split to use for the evaluation set.

- **`text_key`**: string, *default* = `"text"`

    The name of the feature holding the input text.

- **`label_key`**: string, *default* = `"label"`

    The name of the feature holding the classification label in the reference set. 
    If `null`, assume labels are not provided for this dataset.

- **`label_key`**: string or null, *default* = `"label"`

    The name of the feature holding the classification label in the evaluation set.
    If `null`, assume labels are not provided for this dataset.

- **`loading_params`**: string or null, *default* = `null`

    Additional kwargs passed to `load_dataset`. This can help e.g., specify a dataset configuration name (if multiple are available.)