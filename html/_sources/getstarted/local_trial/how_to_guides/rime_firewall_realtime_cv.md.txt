# Protecting Your Model with AI Firewall

{{ fw_how_to_intro }}

This walkthrough uses the Image Classification dataset.

## Overview

Instantiate an AI Realtime Firewall from an existing AI Stress Testing run. You can also view a simulation of real-time events by running [AI Continuous Tests](rime_ai_firewall_continuous_tests.md).

{{ fw_realtime_overview }}

## 1. Run AI Stress Testing

The first step in setting up AI Realtime Firewall is running AI Stress Testing and configuring an AI Firewall for a given project. These steps are very similar to steps 1-3 of [AI Firewall Continuous Tests](rime_ai_firewall_continuous_tests_cv.md).
```
rime-engine run-images --config-path images_examples/classification/awa2/stress_test_config.json
```

<img src="../../../_static/ui/FirewallConfig0_image.png" />

{{ fw_how_to_deploy_step }}

<img src="../../../_static/ui/FirewallConfig_image.png" />

## 2. Set up a Firewall client in a Jupyter notebook

{{ fw_notebook_setup }}

### Load Example Dataset and Model

Let's import some code to the notebook. Remember to make sure that you create the notebook in your `rime_trial` folder!
```python
import numpy as np
import os
import json

RIME_PATH = os.path.abspath('.')
```

Now we are ready to run the Firewall in a real-time setting!

### Running the AI Realtime Firewall with Sample Datapoints

Let's first import the Firewall Realtime package:
```python
from rime.images.firewall.base import ImageFirewall
from rime.tabular.firewall.uploader import FirewallUploader
from rime.core.client.firewall_client import FirewallClient
from rime.images.schema.task import Task
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
firewall = ImageFirewall.from_components(
    firewall_id=firewall_id,
    task=Task.CLASSIFICATION,
    upload_client=upload_client,
    firewall_client=fw_client
)
```

Your Firewall ID can be found by clicking the Settings toggle in the right-hand side of the Firewall homepage.

## 3. Monitor Events

Finally, let's try to pass in a sample datapoint!
```python
test_data_path = 'images_examples/classification/awa2/data/test_inputs_trial.json'
test_data = json.load(open(test_data_path, 'r'))
test_datapoint = test_data[127].copy()
```

The firewall surfaces a graph of "flagged" events. Datapoints that do not raise errors will not be logged in the UI.
This specific datapoint contains an image example that is unusually bright.

Now let's run the firewall over this datapoint.
```python
probs = np.array(test_datapoint["probabilities"])
firewall_response = firewall.validate_single_and_upload(test_datapoint, pred=probs)
```

If you take a look at `firewall_response.summary.action` you'll find that the Firewall has `flagged` the datapoint.

Once you have deployed your firewall, and input data are starting to roll in, the AI Firewall will evaluate each and every data point, and output a decision: `flag`, `pass`, `impute`, or `block` based on the rules criteria.

NOTE: Only non-passing datapoints will be shown in the UI. That way, you are only alerted on problematic datapoints.

### Troubleshooting
{{ troubleshooting_python_package_redirect }}
