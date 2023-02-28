Input Data Format
========================

### Supported File Formats

RIME CV currently supports both [JSON](https://www.json.org/json-en.html) (`.json`) and JSON lines (`.jsonl`) formats, optionally compressed using [gzip](https://www.gnu.org/software/gzip/) (`.json.gz` or `.jsonl.gz`). For JSON lines files, RIME expects each line to be a dictionary representing a single data point. For standard JSON files, RIME expects the content to be a list of dictionaries. The structure of each dictionary is task-specific. See below for a detailed description of the expected data format for supported tasks.

> Note: The Robust Intelligence computer vision test suite supports only RGB images as defined by Python, which is 3x8-bit pixels in true color.

### Expected Keys by Task

#### Image Classification

For the Image Classification task, each data point is represented by a dictionary. This dictionary must allow RIME to load the image that the data point represents. For example, it may contain an `image_path` key. However, RIME supports arbitrary image loading procedures which means that we do not require any fixed keys in advance. Besides simply loading the image itself, you may also provide supplementary information that can make RIME faster/smarter:

```python
[
    {
    "some_key_which_helps_load_image": "value",    (REQUIRED but name/value of key decided by user)
    "label": 1,                                    (OPTIONAL)
    "probabilities": [0.02, 0.94, 0.04],           (OPTIONAL)
    "timestamp": "2022-06-30 10:03:34"             (OPTIONAL)
    },
    ...
]
```

- **`some_key_which_helps_load_image`**: string, ***required, name and value of this key is your choice***

    As described in the [image loading section](specify_image_loading.md), RIME applies an image loading function which the user defines to load images into memory. This image loading function takes in a single datapoint dictionary and outputs a `PIL Image` object. The purpose of this key is to provide the necessary information for the `load_image` function you define. For example, if your definition of `load_image` loads an image from a file path then providing an `image_path` key may be a good idea.

- `label`: int,

    The ground truth class label. This should be an integer in `[0, num_classes)`, where `num_classes` is the length of the probability vector output by the model. The label for a class should correspond to the index of that class in the model output.

- `probabilities`: List[float]

    The model prediction for this data point. This should be a normalized vector of class probabilities, with a probability for each possible class. NOTE: predictions also can be provided in a separate file. See the [CV Prediction Configuration](../cv/prediction_info) reference for more on how to provide cached predictions.

- `timestamp`: string

    Required for AI Firewall and Continuous Testing only. The time associated with the given data point. Timestamps should
    be specified as "YYYY-MM-DD" if a date or ""YYYY-MM-DD HH:TT:SS"
    if a date and time, where YYYY is the year as a four digit number, MM
    is the month as a two digit number, DD is the day as a two digit number, HH
    is the hour as a two digit number, TT is the minute as a two digit number
    and SS is the second as a two digit number.


#### Object Detection

For the Object Detection task, each data point is represented by a dictionary. This dictionary must allow RIME to load the image that the data point represents. For example, it may contain an `image_path` key. However, RIME supports arbitrary image loading procedures which means that we do not require any fixed keys in advance. Besides simply loading the image itself, you may also provide supplementary information that can make RIME faster/smarter:

```python
[
    {
        "some_key_which_helps_load_image": "value",    (REQUIRED but name/value of key decided by user)
        "label": [                                     (OPTIONAL)
            {
                "class_id": 12,
                "x_min": 0.106,
                "x_max": 0.942,
                "y_min": 0.19683257918552036,
                "y_max": 0.9502262443438914
            }
        ],
        "predicted_bounding_boxes": [                  (OPTIONAL)
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
        ],
        "timestamp": "2022-06-30 10:03:34"             (OPTIONAL)
    }
    ...
]
```

- **`some_key_which_helps_load_image`**: string, ***required, name and value of this key is your choice***

    As described in the [image loading section](specify_image_loading.md), RIME applies an image loading function which the user defines to load images into memory. This image loading function takes in a single datapoint dictionary and outputs a `PIL Image` object. The purpose of this key is to provide the necessary information for the `load_image` function you define. For example, if your definition of `load_image` loads an image from a file path then providing an `image_path` key may be a good idea.

- `label`: List[dict],

    The ground truth class label. This should be a list of label bounding boxes where each label bounding box is a dictionary. Each bounding box contains a “class_id” and four coordinates representing the location of the box.

- `predicted_bounding_boxes`: List[dict]

    The model prediction for this data point. It should be a list of predicted bounding boxes where each element is a dictionary. Each predicted box dictionary contains a “probabilities” key which represents the confidence for each class and four coordinates indicating the location of the box. NOTE: predictions also can be provided in a separate file. See the [CV Prediction Configuration](../cv/prediction_info) reference for more on how to provide cached predictions.

- `timestamp`: string

    Required for AI Firewall and Continuous Testing only. The time associated with the given data point. Timestamps should
    be specified as "YYYY-MM-DD" if a date or ""YYYY-MM-DD HH:TT:SS"
    if a date and time, where YYYY is the year as a four digit number, MM
    is the month as a two digit number, DD is the day as a two digit number, HH
    is the hour as a two digit number, TT is the minute as a two digit number
    and SS is the second as a two digit number.

