# Monitoring Your Model with AI Firewall

This guide will cover how to configure the AI Firewall to continuously monitor your model in production.

We will be using an image classification model trained on the <a target="_blank" rel="noopener" href="https://cvml.ist.ac.at/AwA2/">Animals with Attributes 2 Dataset</a>.

## CV Setup

{{ cv_setup_extra_note }}

---

## Running AI Firewall Continuous Tests

### 1. Run AI Stress Testing

Kick off a Stress Testing run (the reference dataset and model from this run will be used for firewall continuous tests).
```bash
rime-engine run-images --config-path images_examples/classification/awa2/stress_test_config.json
```

### 2. Configure a Firewall in the Web Client

In the RI web client, click on the "Default Project" and navigate to the "AI Firewall" tab on the left <img src="../../_static/ui/AIFirewallShield.svg" />. You should see the following page.

<img src="../../_static/ui/Firewall_Page.png" />

Click on "Configure AI Firewall" and fill out the details. The "Name" field can be a name of your choice. The "AI Stress Test" field should be "Image Classification" (this refers to the AI Stress Testing run that we just ran). Finally, the "Bin Size" field should be "1 Day". Once you've filled everything out, **copy the "Firewall ID"** (you will need this later to upload data and predictions to monitor) and click "Done".

<img src="../../_static/nlp_ui/Firewall_Deploy.png" />

### 3. Run Continuous Tests on Incremental Data

We can now upload data and predictions and run AI Firewall Continuous Tests. The following command uses data from March 1, 2022 to March 13, 2022.

NOTE: If you forgot to record the firewall ID in the previous step, you can find it by clicking the <img src="../../_static/ui/GearIcon.svg" /> on the right.
```bash
rime-engine run-firewall-images --config-path images_examples/classification/awa2/firewall_config.json --firewall-id $FIREWALL_ID
```

{{ tabular_ui_redirect }}

{{ cli_note }}

---

## Using Your Own Model and Datasets

This guide will cover how to run AI Firewall Continuous Tests on your own model and datasets.

### Collect Data in the Correct Format

Data formatting requirements are very similar to those for AI Stress Tests (see [Input Data Format](/for_data_scientists/reference/cv/task_data_format.md)); however, **for continuous tests, timestamp information is also needed.**

For AI Firewall Continuous Tests, RI requires two datasets: a reference dataset and an (incremental) evaluation dataset. The latter must supply timestamps with each data point, using the key `"timestamp"`. This allows the data to be sliced into batches appropriately, each of which will be compared to the reference dataset during continuous testing.

Datasets must be passed in as `.json` or `.jsonl` files, optionally compressed via `gzip` (creating `json.gz` or `jsonl.gz`).

### Create Configuration

With your data ready, you can now create a configuration file.

For a detailed reference on what the configuration should look like, see [Continuous Tests Configuration](/for_data_scientists/reference/cv/firewall_continuous_tests.md).

### Run the CLI

#### AI Firewall Continuous Tests

You will need to have configured a firewall in the web client beforehand to get a Firewall ID. Please refer to the sections above for instructions.

Once complete, you can run the CLI like so:
```bash
rime-engine run-firewall-images --firewall-id $FIREWALL_ID --config-path <PATH-TO-CONFIGURATION>
```

{{ tabular_ui_redirect }}

{{ cli_note }}


### Troubleshooting

{{ troubleshooting_python_package_redirect }}
