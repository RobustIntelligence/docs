# Protecting Your Model with AI Firewall

{{ fw_how_to_intro }}

In this walkthrough, we will be using the <a target="_blank" rel="noopener" href="https://www.kaggle.com/c/ieee-fraud-detection">IEEE-CIS Fraud Detection</a> dataset, which is available in the `rime_trial/` bundle provided during installation.

## Overview

Instantiate an AI Realtime Firewall from an existing AI Stress Testing run. You can also view a simulation of real-time events by running [AI Continuous Tests](rime_ai_firewall_continuous_tests.md).

{{ fw_realtime_overview }}

## 1. Run AI Stress Testing

The first step in setting up AI Realtime Firewall is running AI Stress Testing and configuring an AI Firewall for a given project. These steps are very similar to steps 1-3 of [AI Continuous Tests](rime_ai_firewall_continuous_tests.md).

```
rime-engine run-stress-tests --config-path examples/fraud/stress_tests_with_model.json
```

<img src="../../../_static/ui/FirewallConfig0.png" />

{{ fw_how_to_deploy_step }}

<img src="../../../_static/ui/FirewallConfig.png" />

## 2. Set up a Firewall client in a Jupyter notebook

{{ fw_notebook_setup }}

### Load Example Dataset and Model

Let's add some helper preprocessing code to the notebook. Remember to make sure that you create the notebook in your `rime_trial` folder!

```python
import catboost as catb
import pickle
import pandas as pd
import os

RIME_PATH = os.path.abspath('.')

model = catb.CatBoostClassifier()
model.load_model(str(RIME_PATH + "/examples/fraud/fraud.catb"))
with open(RIME_PATH + "/examples/fraud/null_impute.pkl", "rb") as f:
    null_impute = pickle.load(f)


def preprocess(x: dict):
    """Null impute categoricals."""
    for col_name in x.keys():
        if pd.isnull(x[col_name]) and col_name in null_impute.keys():
            x[col_name] = null_impute[col_name]
    return x
```

We now define the inference function (`predict_dict`):

```python
# We now define our interface.
def predict_dict(x: dict):
    """Predict dict function."""
    new_x = preprocess(x)
    new_x = pd.DataFrame(new_x, index=[0])
    return model.predict_proba(new_x)[0][1]
```

Now we are ready to run the Firewall in a real-time setting!

### Running the AI Realtime Firewall with Sample Datapoints

Let's first import the Firewall Realtime package:

```python
from rime.tabular.firewall.base import TabularFirewall
from rime.tabular.firewall.uploader import FirewallUploader
from rime.core.client.firewall_client import FirewallClient
from rime.tabular import ModelTask
```

Let's then instantiate a firewall object:

```python
firewall_id = "$YOUR_FIREWALL_ID"
firewall_url = "localhost:5002"
upload_client = FirewallUploader.from_url(
    firewall_id,
    firewall_url,
)
fw_client = FirewallClient.from_cli_args(firewall_url)
firewall = TabularFirewall.from_components(
    firewall_id=firewall_id,
    predict_dict=predict_dict,
    model_task=ModelTask.BINARY_CLASSIFICATION,
    upload_client=upload_client,
    firewall_client=fw_client
)
```

Your Firewall ID can be found by clicking the Settings toggle in the right-hand side of the Firewall homepage.

## 3. Monitor Events

Finally, let's try to pass in a sample datapoint!
```python
test_df = pd.read_csv('examples/fraud/val.csv')
label_col = "isFraud"
test_df = test_df.drop(label_col, axis=1)
datapoint = test_df.iloc[0].to_dict()
```

The firewall surfaces a graph of "flagged" events. Datapoints that do not raise errors will not be logged in the UI.
For this specific datapoint, let's introduce a data corruption:
```python
datapoint['Count_1'] = 100000
```
Now let's run the firewall over this datapoint.
```python
firewall_response = firewall.validate_single_and_upload(datapoint)
```

If you take a look at `firewall_response.summary.action` you'll find that the Firewall has `flagged` the datapoint.

Once you have deployed your firewall, and input data are starting to roll in, the AI Firewall will evaluate each and every data point, and output a decision: `flag`, `pass`, `impute`, or `block` based on the rules criteria.

NOTE: Only non-passing datapoints will be shown in the UI. That way, you are only alerted on problematic datapoints.

### Configuring Firewall Behavior

By default, the AI Firewall will "flag" a problematic datapoint, unless it is determined that the datapoint could raise errors (in which case it will "block"). This behavior is configurable.

Below, we will use the `rime` Python Library to enable "block" behavior for the "Numeric Outliers" rule.
```python
from rime.tabular.schema import FirewallAction
from rime.tabular.data_tests.schema.type import DataTestType
firewall.set_flagged_action_for_rule(DataTestType.NUM_OUTLIER, FirewallAction.BLOCK)
```

We can then test this with the current datapoint.

```python
datapoint = datapoint.copy()
del datapoint["addr1"]
firewall.validate_single_and_upload(datapoint)
```

If you navigate back to the "Realtime Events" tab on AI Firewall, you will see a new datapoint that has been blocked by the Firewall.

For more information on configuring the Firewall, check out the [AI Firewall Reference](/local_trial/reference/firewall.md).

### Troubleshooting
{{ troubleshooting_python_package_redirect }}
