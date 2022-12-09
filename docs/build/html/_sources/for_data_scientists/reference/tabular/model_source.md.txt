Model Configuration
===================

Configuring a model source can be done by specifying a mapping in the RIME JSON
configuration file, under the `model_info` argument.


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
    model file, please see [Specify a Model](specify_model.md).
