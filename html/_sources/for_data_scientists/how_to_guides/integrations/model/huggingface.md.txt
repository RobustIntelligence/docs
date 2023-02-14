# Hugging Face

RIME now supports an API that downloads Hugging Face models by providing the 
Hugging Face Model's URI. Currently, RIME supports Hugging Face NLP Classification Models. 

### Hugging Face Classification Model

```python
{
    "model_info": {
        # In order to specify a Hugging Face classification model you need to specify a `model_info` with `"type": "huggingface_classification"`
        "type": "huggingface_classification",      (REQUIRED)
        # Specify the Hugging Face Model's URI.
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


