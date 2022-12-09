Data Configuration
==================

Configuring a data source can be done by specifying a mapping in the main RIME JSON configuration file, under the
`data_info` argument. By default, RIME can load any dataset from disk or cloud storage so long as the files are correctly formatted. RIME additionally supports user-defined dataloaders contained in a configured python file as well as a native integration with the [Hugging Face datasets hub](https://huggingface.co/datasets).

The `data_info` configuration communicates how RIME should should ingest data and has expects different arguments depending on its `type`. 
The `data_info` type can direct the RI platform to load both the reference and evaluation datasets from the same source type, such as files, a user-defined dataloader, or a Huggingface dataset.

Alternatively, to load reference and evaluation sets from different data sources, you can specify the "split" type. 
In the split approach, you may specify a separate "single" data info struct for each of the reference and evaluation datasets: `ref_data_info` and `eval_data_info`.
Each of the reference and evaluation single data structs can take on a different configuration type, similar to the types listed above.
The full list of single data info configuration templates is given below.

### Default Data Info Template
```python
{
    "data_info": {
        "ref_path": "path/to/ref.jsonl.gz",        (REQUIRED)
        "eval_path": "path/to/eval.jsonl.gz",      (REQUIRED)
        "embeddings": null
    },
    ...
}
```

### Arguments

- **`ref_path`**: string, ***required***

    Path to reference data file. Please reference the [NLP file guide](task_data_format) for a description of supported file formats.

- **`eval_path`**: string, ***required***
    
    Path to evaluation data file. Please reference the [NLP file guide](task_data_format) for a description of supported file formats.

- `embeddings`: list or `null`, *default* = `null`

    A list of dictionaries corresponding to information for each embedding. The arguments for each dictionary are described below.

    - `key`: string

        Name of the key in the data dictionary corresponding to the specified embedding. For example, if each data point is represented by `{"text": "", "label": 1, "probabilitiies": [...], "context_vec": [...]}`, specifying `embeddings: [{"key": "context_vec"}]` in the `data_info` would direct the RI Platform to treat this value as a dense vector-valued embedding feature.

### Custom Dataloader Template
```python
{
    "data_info": {
        "type": "custom",                           (REQUIRED)
        "load_path": "path/to/dataloader.py",       (REQUIRED)
        "embeddings": null
    },
    ...
}
```

### Arguments

- **`type`**: string, ***required***

    Must be set to "custom".

- **`load_path`**: string, ***required***

    Path to the custom dataloader file. Please reference the [NLP Dataloader](specify_custom_dataloader) documentation instructions on how to create a compatible file.

- `embeddings`: list or `null`, *default* = `null`

    A list of dictionaries corresponding to information for each embedding. The arguments for each dictionary are described below.

    - `key`: string

        Name of the key in the data dictionary corresponding to the specified embedding. For example, if each data point is represented by `{"text": "", "label": 1, "probabilitiies": [...], "context_vec": [...]}`, specifying `embeddings: [{"key": "context_vec"}]` in the `data_info` would direct the RI Platform to treat this value as a dense vector-valued embedding feature.

### Hugging Face Dataset Template

```python
{
    "data_info": {
        "type": "huggingface",                      (REQUIRED)
        "dataset_uri": "path",                      (REQUIRED)
        "ref_split": "train",
        "eval_split": "test",
        "text_key": "text",
        "text_pair_key": "text_pair",
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

- `ref_split`: string, *default* = "train"

    The key used to access the reference split from the downloaded ['DatasetDict'](https://huggingface.co/docs/datasets/v2.3.2/en/package_reference/main_classes#datasets.DatasetDict).

- `eval_split`: string, *default* = "test"

    The key used to access the evaluation split from the downloaded ['DatasetDict'](https://huggingface.co/docs/datasets/v2.3.2/en/package_reference/main_classes#datasets.DatasetDict).

- `text_key`: string, *default* = "text"

    The feature name for the NLP input text attribute.

- `text_pair_key`: string, *default* = "text_pair"

    The feature name for the NLP second input text attribute (for NLI model task).

- `label_key`: string or null, *default* = "label"

    The feature name for the label class ID. If `null`, don't load labels.

- `eval_label_key`: string or null, *default* = "label"

    The feature name for the label class ID in the evaluation split. If `null`, don't load labels.

- `loading_params`: dict or null, *default* = `null`

    Additional kwargs to pass to ['load_dataset'](https://huggingface.co/docs/datasets/v2.3.2/en/package_reference/loading_methods#datasets.load_dataset). 

### Split Data Info Template

```python
{
    "data_info": {
        "ref_data_info": ...,              (REQUIRED)
        "eval_data_info": ...,            (REQUIRED)
    },
    ...
}
```

### Arguments

- **`ref_data_info`**: SingleDataInfo, ***required***

    Path to single data info struct (see below).
- **`eval_data_info`**: SingleDataInfo, ***required***

    Path to single data info struct (see below).


### Single Data Info Templates

Note that these single data info structs can be used to specify both the `ref_data_info` as well as `eval_data_info`
in the split data into template above.

Note that *all* single data info structs also take in a set of NLP parameters which allow the user to additionally
specify properties of their data, such as predictions in `prediction_info` and embeddings in `embeddings`.
The full list is detailed below.

#### General NLP Parameters for Single Data Info

```python
{
    "prediction_info": null,
    "embeddings": null
}
```

#### Arguments

- `prediction_info`: mapping, *default* = `null`

    Arguments to specify prediction info. Very similar to the `prediction_info` struct in the [Prediction Configuration](prediction_info.md) page. 
    Note that only one of these two structs can be specified. If `prediction_info` is specified in reference and evaluation single data info structs,
    then it cannot also be specified as a separate top-level struct in the JSON configuration.

    - `path`: string or `null`, *default* = `null`

        Path to prediction cache corresponding to the data file. Please see the [NLP Prediction Cache Data Format](task_prediction_cache_format) reference for a description of supported file format.

    - `n_samples`: int or `null`, *default* = `null`

        Number of samples from each dataset to score. If both `ref_path` and `eval_path` are specified, this must be set to null. If either prediction cache is not specified and `n_samples` is set to `null`, the default is to score the entire dataset. If model throughput is low, it is recommended to use a prediction cache or specify a smaller value for `n_samples`.

- `embeddings`: list or `null`, *default* = `null`

    A list of dictionaries corresponding to information for each embedding. The arguments for each dictionary are described below.

    - `key`: string

        Name of the key in the data dictionary corresponding to the specified embedding. For example, if each data point is represented by `{"text": "", "label": 1, "probabilitiies": [...], "context_vec": [...]}`, specifying `embeddings: [{"key": "context_vec"}]` in the `data_info` would direct the RI Platform to treat this value as a dense vector-valued embedding feature.

#### File-based Single Data Info Template

```python
{
    "file_name": "path/to/file.csv",
    **nlp_params
}
```

#### Arguments

- **`file_name`**: string, ***required***

    Path to data file.

- `**nlp_params`: Dict

    See NLP Parameters above.


#### Custom Dataloader Single Data Info Template

```python
{
    "load_path": "path/to/custom_loader.py",
    "load_func_name": "load_fn_name",
    "loader_kwargs": null,
    "loader_kwargs_json": null,
    **nlp_params
}
```

#### Arguments

- **`load_path`**: string, ***required***

    Path to custom loader Python file.

- **`load_func_name`**: string, ***required***

    Name of the loader function. Must be defined within the Python file.

- `loader_kwargs`: Dict, *default* = `null`
    
    Arguments to pass in to the loader function, in dictionary form. We pass these arguments in as **kwargs.
    Only one of `loader_kwargs` and `loader_kwargs_json` can be specified.

- `loader_kwargs_json`: Dict

    Arguments to pass in to the loader function, in JSON-serialized string form.
    We pass these arguments in as **kwargs.
    Only one of `loader_kwargs` and `loader_kwargs_json` can be specified.

- `**nlp_params`: Dict

    See NLP Parameters above.


#### Data Collector Single Data Info Template

NOTE: this can only be specified as part of a Continuous Testing config, not offline testing config. See the 
[Continuous Tests Configuration](firewall_continuous_tests.md) for more details.

```python
{
    "start_time": start_time,
    "end_time": end_time,
    **nlp_params
}
```

#### Arguments

- **`start_time`**: int, ***required***

    Start time of the data collector to fetch data from. Format is UNIX epoch time in seconds.

- **`end_time`**: int, ***required***

    End time of the data collector to fetch data from. Format is UNIX epoch time in seconds.

- `**nlp_params`: Dict

    See NLP Parameters above.

#### Hugging Face Single Data Info Template

```python
{
    "data_info": {
        "type": "huggingface",                      (REQUIRED)
        "dataset_uri": "path",                      (REQUIRED)
        "split_name": "train",
        "text_key": "text",
        "text_pair_key": "text_pair",
        "label_key": "label",
        "loading_params": null
    },
    ...
}
```

#### Arguments

- **`type`**: string, ***required***

    Must be set to "huggingface".

- **`dataset_uri`**: string, ***required***

    The path or tag passed to ['load_dataset'](https://huggingface.co/docs/datasets/v2.3.2/en/package_reference/loading_methods#datasets.load_dataset). 

- `split_name`: string, *default* = "train"

    The key used to access the split from the downloaded ['DatasetDict'](https://huggingface.co/docs/datasets/v2.3.2/en/package_reference/main_classes#datasets.DatasetDict).

- `text_key`: string, *default* = "text"

    The feature name for the NLP input text attribute.

- `text_pair_key`: string, *default* = "text_pair"

    The feature name for the NLP second input text attribute (for NLI model task).

- `label_key`: string or null, *default* = "label"

    The feature name for the label class ID. If `null`, don't load labels.

- `loading_params`: dict or null, *default* = `null`

    Additional kwargs to pass to ['load_dataset'](https://huggingface.co/docs/datasets/v2.3.2/en/package_reference/loading_methods#datasets.load_dataset).
