Specify a Computer Vision Model
==========================

Similar to the tabular use case, RIME expects CV models to be specified as Python files that expose the following function:

- `predict_dict(x: dict) -> dict`: the input `x` is a single data point in dictionary form (e.g. `{'image_path': 'data/moo.png', ...}`). The output of the function should be a python dictionary whose format depends on the CV Task. The following key-value pairs are expected within the output dictionary for each task:

    - Image Classification: the 'probabilities' key specifies the probability distribution over the label classes, e.g., `{'probabilities': [0.11, 0.84, 0.05, ...]}`
    - Object Detection: the 'predicted_bounding_boxes' key specifies the bounding boxes predicted to be in the image. This value should be a list of dictionaries, with each dictionary corresponding to a predicted bounding box. Each predicted bounding box dictionary should have a 'probabilities' key (specifying a list of predicted probabilities for each class) and the following keys to specify the box location: 'x_min', 'x_max', 'y_min', 'y_max' (where the value for each key is a numeric). An example of this is: `{
    "predicted_bounding_boxes": [
      {
        "x_min": 0.3051212430000305,
        "x_max": 0.5722537040710449,
        "y_min": 0.07785701006650925,
        "y_max": 0.5583255887031555,
        "probabilities": [
          0.38,
          0,
          0.62,
          0
        ]
  }`

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

### Step 4: Implement a predict function
Implement the `predict_dict` function. This should look something like:

```
# Image Classification Example
def predict_dict(x: dict) -> dict:
    """Return the predicted class probabilities."""
    # the image to predict on will always be in "__image__" key
    image = x["__image__"]
    # preprocess image as necessary
    image = transform(image)
    image = torch.unsqueeze(image, 0)
    output = model.forward(image)
    probs = torch.squeeze(torch.softmax(output, dim=1))
    return {"probabilities": probabilities}
```
