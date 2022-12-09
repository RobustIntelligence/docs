Model Configuration
===================

Configuring a CV model source can be done by specifying a mapping in the RIME JSON
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
    model file, please reference the [Specify a Model section](specify_model_cv.md).
    <!-- TODO point to images-specific doc -->
