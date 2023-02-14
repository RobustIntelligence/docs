# Protecting Your Model with AI Firewall

{{ fw_how_to_intro }}

In this walkthrough, we will be using the <a target="_blank" rel="noopener" href="https://www.kaggle.com/datasets/Cornell-University/arxiv?select=arxiv-metadata-oai-snapshot.json">ArXiv Topic Classification</a> dataset.

## Overview

AI Firewall Realtime can be easily instantiated from an existing AI Stress Testing Run. You can also view a simulation of real-time events by running [AI Firewall Continuous Tests](rime_ai_firewall_continuous_tests_nlp.md).

{{ fw_realtime_overview }}

## 1. Run AI Stress Testing

The first step in setting up AI Firewall Realtime is running AI Stress Testing and configuring an AI Firewall for a given project. These steps are very similar to steps 1-3 of [AI Firewall Continuous Tests](rime_ai_firewall_continuous_tests_nlp.md).

```
rime-engine run-nlp --config-path nlp_examples/classification/arxiv/stress_tests_config_no_model.json
```

<img src="../../_static/ui/FirewallConfig0_nlp.png" />

{{ fw_how_to_deploy_step }}

<img src="../../_static/ui/FirewallConfig_nlp.png" />

## 2. Review and Download Auto-Configured AI Firewall Rules

{{ fw_rules_review }}

<img src="../../_static/ui/FirewallConfig_Rules_nlp.png" />

## 3. Setup a Firewall Client in a Jupyter Notebook

{{ fw_notebook_setup }}

### Load Example Dataset and Model

Let's import some code to the notebook. Remember to make sure that you create the notebook in your `rime_trial` folder!
```python
import catboost as catb
import pickle
import pandas as pd
import os
import json
import gzip

RIME_PATH = os.path.abspath('.')
```

Now we are ready to run the Firewall in a real-time setting!

### Running the AI Firewall Realtime with Sample Datapoints

Let's first import the Firewall Realtime package:
```python
from rime.nlp.firewall.base import NLPFirewall
from rime.tabular.firewall.uploader import FirewallUploader
from rime.core.client.firewall_client import FirewallClient
from rime.nlp.schema.task import Task
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
firewall = NLPFirewall.from_components(
    firewall_id=firewall_id,
    json_file="rules.json",
    task=Task.CLASSIFICATION,
    upload_client=upload_client,
    firewall_client=fw_client
)
```

Your Firewall ID can be found by clicking the Settings toggle in the right-hand side of the Firewall homepage.

## 4. Monitor Events

Finally, let's try to pass in a sample datapoint!
```python
test_data_path = 'nlp_examples/classification/arxiv/data/val_0_with_label.json.gz'
with gzip.open(test_data_path, "rb") as f:
    test_data = json.loads(f.read(), encoding="utf-8")
test_datapoint = test_data[0].copy()
```

The firewall surfaces a graph of "flagged" events. Datapoints that do not raise errors will not be logged in the UI.
For this specific datapoint, let's introduce a data corruption (making the text an empty string):
```python
test_datapoint["text"] = ""
```

Now let's run the firewall over this datapoint.
```python
firewall_response = firewall.validate_single_and_upload(test_datapoint)
```

If you take a look at `firewall_response.summary.action` you'll find that the Firewall has `flagged` the datapoint.

Once you have deployed your firewall, and input data are starting to roll in, the AI Firewall will evaluate each and every data point, and output a decision: `flag`, `pass`, `impute`, or `block` based on the rules criteria.

NOTE: Only non-passing datapoints will be shown in the UI. That way, you are only alerted on problematic datapoints.

### Troubleshooting
{{ troubleshooting_python_package_redirect }}
