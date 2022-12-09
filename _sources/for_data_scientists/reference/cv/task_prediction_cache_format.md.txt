Prediction Cache Data Format
==================

### Supported File Formats

RIME CV supports the same file formats for the prediction cache as it does for the [input data](task_data_format), namely [JSON](https://www.json.org/json-en.html) (`.json`) and [JSON lines](https://jsonlines.org/) (`.jsonl`) formats. Each prediction should be stored in its own dictionary in the json list or as a dictionary on its own line for JSONL files.

To use a prediction cache for a given test run, it is currently required that a prediction be present for every data point in the corresponding input data. For example, if a dataset is of size `N`, line `i` in the prediction cache should contain the model output for input example `i` in the dataset for every `0 <= i < N`.

The data format for each prediction is similar to that for the [input data](task_data_format), the only difference being the "image identifier" and ground truth label keys for the CV task are removed.


#### Image Classification

For the Image Classification task, each prediction is represented by a dictionary containing the following key-value pair:

```python
[
    {
      "probabilities": [0.02, 0.94, 0.04]                 (REQUIRED)
    },
    ...
]
```

- **`probabilities`**: List[float],  ***required***

    The model prediction for this data point. This should be a normalized vector of class probabilities, with a probability for each possible class.

#### Object Detection

For the Object Detection task, each prediction is represented by a dictionary of the following form:
```python
[
    {
        "predicted_bounding_boxes": [
            {
                "x_min": 0.3051212430000305,
                "x_max": 0.5722537040710449,
                "y_min": 0.07785701006650925,
                "y_max": 0.5583255887031555,
                "probabilities": [
                    0.38,
                    0,
                    0,
                    0.62,
                    0
                ]
            }
        ]
        ...
    }
    ...
]
```

- **`predicted_bounding_boxes`**: List[dict]

    The model prediction for this data point. It should be a list of predicted bounding boxes where each element is a dictionary. Each predicted box dictionary contains a “probabilities” key which represents the confidence for each class and four coordinates indicating the location of the box.
