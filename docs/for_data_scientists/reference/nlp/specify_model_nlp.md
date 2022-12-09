Specify an NLP Model
==========================

Similar to the tabular use case, RIME expects NLP models to be specified as Python files that expose the following function:

- `predict_dict(x: dict) -> dict`: the input `x` is a single example or data point in dictionary form (e.g. `{'text': 'Hello, world!', ...}`). The output of the function should be a python dictionary whose format depends on the NLP Task. The following key-value pairs are expected within the output dictionary for each task:

    - Text Classification and Natural Language Inference: the 'probabilities' key specifies the probability distribution over the label classes, e.g., `{'probabilities': [0.11, 0.84, 0.05, ...]}`
    - Named Entity Recognition: the 'predicted_entities' keys specify the entities predicted to be in the string. This value should be a list of dictionaries, with each dictionary corresponding to an entity. Each entity dictionary should have a 'type' key (specifying the type the entity is predicted to be) as well as a 'mentions' key which contains all the mentions predicted to refer to this entity. Each mention itself a dictionary with two keys: a 'start_offset' key and a 'end offset' key, which are both integers referring to the start and end of the mention in question. An example of this is: 
    ```python
      {
        "predicted_entities": [
          {
            "type": "LOC",
            "mentions": [
              {
                "start_offset": 0,
                "end_offset": 6
              }
            ]
          }
        ]
      }
  ```

The following steps outline how to implement the Python interface expected by RIME. This is done by loading a model binary from disk.

### Step 1: Specify model path

Create an empty folder. From inside this folder, create a new python file. This will contain the `predict_dict()` function that will serve as the interface between RIME and your model. Place the saved model weights and any other requisite model artifacts in the same folder as the file.

In the new python file, create a constant for the path to this binary storying the model weights:

```
from pathlib import Path

cur_dir = Path(__file__).absolute().parent

MODEL_NAME = 'TODO: change this to the model file name'
MODEL_PATH = cur_dir / MODEL_NAME
```

### Step 2: Retrieve custom code
If custom code is needed to perform data preprocessing (or to call your API), we need to make sure it is loaded into the runtime environment. If this code is already available as a Python package, see the `Custom Requirements` section.

If your code is NOT a Python package (and is instead a Python file or folder) then please put all relevant files in the same directory you created in [Step 1](#step-1-specify-model-path), and add the following snippet to the Python file:

```
import sys
sys.path.append(str(cur_dir))
```

### Step 3: Access the model

As an example, if you used pytorch to save your model parameters, you might load the model as follows:

```
import torch
model = torch.load(MODEL_PATH)
```

### Step 4: Import / implement preprocessing function

If the model you are using expects inputs other than a raw string, you will need to load/define all custom tokenization or preprocessing functions. Getting the preprocessing functionality could look like:
```
from custom_package import preprocess, tokenize
```
or
```
def preprocess(txt: str) -> str:
    clean_txt = txt.strip()
    return clean_txt

def tokenize(txt: str) -> list:
    tokens = txt.split()
    return tokens

```

### Step 5: Implement a predict function
Implement the `predict_dict` function. This should look something like:

```
# Text Classification Example
def predict_dict(x: dict) -> dict:
    """Return the predicted class probabilities."""
    txt = x['text']
    preprocessed = preprocess(txt)
    tokens = tokenize(preprocessed)
    probabilities: List[float] = model.predict(tokens)
    return {"probabilities": probabilities}

# Natural Language Inference Example
def predict_dict(x: dict) -> dict:
    """Return the predicted class probabilities."""
    preprocessed_text = preprocess(x['text'])
    preprocessed_text_pair = preprocess(x['text_pair'])
    tokens = tokenize(preprocessed_text, preprocessed_text_pair)
    probabilities: List[float] = model.predict(tokens)
    return {"probabilities": probabilities}
    
# Named Entity Recognition Example
def predict_dict(x: dict) -> dict:
    """Return the predicted entities."""
    txt = x['text']
    preprocessed = preprocess(txt)
    results = ner(preprocessed)
    for res in ner_results:
        results.append(
            {
                'type': res['entity_group'],
                'mentions': [
                    {'start_offset': res['start'], 'end_offset': res['end'], }
                ],
            }
        )
    return {'predicted_entities': results}
```
