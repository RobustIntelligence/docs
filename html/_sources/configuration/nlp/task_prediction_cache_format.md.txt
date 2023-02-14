Prediction Cache Data Format
==================

### Supported File Formats

RIME NLP supports the same file formats for the prediction cache as it does for the [input data](task_data_format), namely [JSON](https://www.json.org/json-en.html) (`.json`) and [JSON lines](https://jsonlines.org/) (`.jsonl`) formats. Each prediction should be stored in its own dictionary in the json list or as a dictionary on its own line for JSONL files.

To use a prediction cache for a given test run, it is currently required that a prediction be present for every data point in the corresponding input data. For example, if a dataset is of size `N`, line `i` in the prediction cache should contain the model output for input example `i` in the dataset for every `0 <= i < N`.

The data format for each prediction is similar to that for the [input data](task_data_format), the only difference being the "text" and ground truth label keys for the NLP task are removed.


#### Text Classification

For the Text Classification task, each prediction is represented by a dictionary containing the following key-value pair:

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


#### Named Entity Recognition

For the Named Entity Recognition task, each prediction is represented by a dictionary containing the following key-value pair:

```python
[
    {
      "predicted_entities": [                         (REQUIRED)                 
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


- **`predicted_entities`**: List[dict],  ***required***
    
    The model predictions for this data point. This should be a list of dictionaries, with each dictionary corresponding to an entity. Each entity dictionary should have a 'type' key (specifying the type the entity is predicted to be) as well as a 'mentions' key which contains all the mentions predicted to refer to this entity. Each mention itself a dictionary with two keys: a 'start_offset' key and a 'end offset' key, which are both integers referring to the start and end of the mention in question. See the [NLP Prediction Configuration](prediction_info) reference for more on how to provide cached predictions.
