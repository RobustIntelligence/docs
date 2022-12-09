Input Data Format
========================

## Automated Validation
{{ rime_data_format_check_redirect }}

---

## Supported File Formats

RIME NLP currently supports both [JSON](https://www.json.org/json-en.html) (`.json`) and [JSON lines](https://jsonlines.org/) (`.jsonl`) formats, optionally compressed using [gzip](https://www.gnu.org/software/gzip/) (`.json.gz` or `.jsonl.gz`). For JSON lines files, RIME expects each line to be a dictionary representing a single data point. For standard JSON files, RIME expects the content to be a list of dictionaries. The structure of each dictionary is task-specific. See below for a detailed description of the expected data format for supported tasks.

## Requirements By Task

### Text Classification

For the Text Classification task, each data point is represented by a dictionary containing the following keys:

```python
[
  {
    "text": "Hello, world!",               (REQUIRED)
    "label": 1,
    "probabilities": [0.02, 0.94, 0.04]
  },
  ...
]
```

- **`text`**: string, ***required***

    The input string for this data point.

- `label`: int

    The ground truth class label. This should be an integer in `[0, num_classes)`, where `num_classes` is the length of the probability vector output by the model. The label for a class should correspond to the index of that class in the model output.

- `probabilities`: List[float]

    The model prediction for this data point. This should be a normalized vector of class probabilities, with a probability for each possible class. NOTE: predictions also can be provided in a separate file. See the [NLP Prediction Configuration](prediction_info) reference for more on how to provide cached predictions.

### Natural Language Inference

For the Natural Language Inference task, each data point is represented by a dictionary containing the following keys:

```python
[
  {
    "text": "Hello, world!",               (REQUIRED)
    "text_pair": "Greetings, Earth!",      (REQUIRED)
    "label": 0,
    "probabilities": [0.96, 0.03, 0.01]
  },
  ...
]
```

- **`text`**: string, ***required***

    The first input string (premise) for this data point.

- **`text_pair`**: string, ***required***

    The second input string (hypothesis) for this data point.

- `label`: int

    The ground truth class label. This should be an integer in `[0, num_classes)`, where `num_classes` is the length of the probability vector output by the model. The label for a class should correspond to the index of that class in the model output.

- `probabilities`: List[float]

    The model prediction for this data point. This should be a normalized vector of class probabilities, with a probability for each possible class. NOTE: predictions also can be provided in a separate file. See the [NLP Prediction Configuration](prediction_info) reference for more on how to provide cached predictions.


### Named Entity Recognition

For the Named Entity Recognition task, each data point is represented by a dictionary containing the following keys:

```python
[
  {
  "text": "Hello, world!",               (REQUIRED)
  "entities": [
    {
      "mentions": [
        {
          "start_offset": 7,
          "end_offset": 11
        }
      ],
      "type": "LOC"
    }
  ],
  "predicted_entities": [
    {
      "mentions": [
        {
          "start_offset": 7,
          "end_offset": 11
        }
      ],
      "type": "ORG"
    }
  ]
  },
  ...
]
```

- **`text`**: string, ***required***

    The input string for this data point.

- `entities`: List[dict]

    The ground truth annotations. This should be a list of dictionaries, with each dictionary corresponding to an entity. Each entity dictionary should have a 'type' key (specifying the type the entity is predicted to be) as well as a 'mentions' key which contains all the mentions predicted to refer to this entity. Each mention itself a dictionary with two keys: a 'start_offset' key and a 'end offset' key, which are both integers referring to the start and end of the mention in question.

- `predicted_entities`: List[dict]

    The model predictions for this data point. This should be a list of dictionaries, with each dictionary corresponding to an entity. Each entity dictionary should have a 'type' key (specifying the type the entity is predicted to be) as well as a 'mentions' key which contains all the mentions predicted to refer to this entity. Each mention itself a dictionary with two keys: a 'start_offset' key and a 'end offset' key, which are both integers referring to the start and end of the mention in question. See the [NLP Prediction Configuration](prediction_info) reference for more on how to provide cached predictions.
