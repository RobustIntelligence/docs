Data Configuration
==================

Configuring a data source can be done by specifying a mapping in the main RIME JSON configuration file, under the
`data_info` argument. By default, RIME can load any dataset from disk or cloud storage so long as the files are correctly formatted. RIME additionally supports user-defined dataloaders contained in a configured python file as well as a native integration with the [Hugging Face datasets hub](https://huggingface.co/datasets).


## Stress Testing
### Default Template
```python
{
    "data_info": {
        "ref_path": "path/to/ref.jsonl.gz",        (REQUIRED)
        "eval_path": "path/to/eval.jsonl.gz",      (REQUIRED)
    },
    ...
}
```

### Arguments

- **`ref_path`**: string, ***required***

    Path to reference data file. Please reference the [NLP file guide](task_data_format) for a description of supported file formats.

- **`eval_path`**: string, ***required***
    
    Path to evaluation data file. Please reference the [NLP file guide](task_data_format) for a description of supported file formats.


### Custom Dataloader
```python
{
    "data_info": {
        "type": "custom",                           (REQUIRED)
        "load_path": "path/to/dataloader.py",       (REQUIRED)
    },
    ...
}
```

### Arguments

- **`type`**: string, ***required***

    Must be set to "custom".

- **`load_path`**: string, ***required***
    
    Path to the custom dataloader file. Please reference the [NLP Dataloader](specify_custom_dataloader) documentation instructions on how to create a compatible file.


### Hugging Face Dataset

```python
{
    "data_info": {
        "type": "huggingface",                      (REQUIRED)
        "dataset_uri": "path",                      (REQUIRED)
        "ref_split": "train",
        "eval_split": "test",
        "label_key": "label",
        "eval_label_key": "label"
        "loading_params": null

    },
    ...
}
```
### Arguments

- **`type`**: string, ***required***

    Must be set to "huggingface".

- **`dataset_uri`**: string, ***required***
    
    The path or tag passed to ['load_dataset'](https://huggingface.co/docs/datasets/v2.3.2/en/package_reference/loading_methods#datasets.load_dataset). 

- `ref_split`: string, *default* = `train`

    The key used to access the reference split from the downloaded ['DatasetDict'](https://huggingface.co/docs/datasets/v2.3.2/en/package_reference/main_classes#datasets.DatasetDict).

- `eval_split`: string, *default* = `test`

    The key used to access the evaluation split from the downloaded ['DatasetDict'](https://huggingface.co/docs/datasets/v2.3.2/en/package_reference/main_classes#datasets.DatasetDict).


- `text_key`: string, *default* = "text"

    The feature name for the NLP input text attribute.

- `label_key`: string or null, *default* = "label"

    The feature name for the label class ID. If 'None', don't load labels.

- `eval_label_key`: string or null, *default* = "label"

    The feature name for the label class ID in the evaluation split. If 'None', don't load labels.

- `loading_params`: dict or null, *default* = `null`

    Additional kwargs to pass to ['load_dataset'](https://huggingface.co/docs/datasets/v2.3.2/en/package_reference/loading_methods#datasets.load_dataset). 