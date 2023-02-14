Model Configuration
===================

Configuring an NLP model source can be done by specifying a mapping in the RIME JSON
configuration file, under the `model_info` argument. Models can be defined via a custom 
`model.py` file or through a native integration with [Hugging Face](https://huggingface.co/models).


### Template
```python
{
    "model_info": {
        "path": "/path/to/model.py"        (REQUIRED)
    }
    ...
}
```

### Arguments

- **`path`**: string, ***required***

    Path to Python model file. For instructions on how to create this Python
    model file, please see [Specify a Model](specify_model_nlp.md).
    <!-- TODO add an NLP-specific doc -->


### Hugging Face Classification Model

```python
{
    "model_info": {
        "type": "huggingface_classification",      (REQUIRED)
        "model_uri": "path",                      (REQUIRED)
        "tokenizer_uri": null,
        "model_max_length": null,

    },
    ...
}
```

### Arguments

- **`model_uri`**: string, ***required***

    The pretrained model name or path used to load a pretrained Hugging Face model from disk or from the model hub.

- **`tokenizer_uri`**: string or null, *default* = `null`

    The pretrained tokenizer name or path used to load the tokenizer from disk or from the model hub. If `null`, RIME defaults to loading from the provided `model_uri`.

- **`model_max_length`**: int or null, *default* = `null`

    The maximum sequence length (in tokens) supported by the model. If `null`, RIME infers the maximum length from the pretrained model and tokenizer.