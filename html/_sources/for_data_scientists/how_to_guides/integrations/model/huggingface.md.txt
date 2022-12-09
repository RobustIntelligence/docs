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
        "class_map": null,
        "ignore_class_names": False
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

- **`class_map`**: List[int] or null, *default* = `null`

    If provided, RIME reorders the model's predicted class probabilities. For example, suppose your dataseet has labels [0, 1] meaning ["Negative", "Positive"] respectively, but the model outputs probabilities for classes ["Positive", "Negative"]. Providing`"class_map": [1, 0]` would make the model compatible with the dataset. Default to the natural order of model logits.

- **`ignore_class_names`**

    If `True`, ignore the label names provided in the Huggingface model's `label2id` configuration. Otherwise, use the configured label names as the `class_names` within RIME and verify they match any provided manually or through the provided dataset.