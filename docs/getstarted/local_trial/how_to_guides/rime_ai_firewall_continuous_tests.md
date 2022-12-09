# Monitoring Your Model with AI Firewall Continuous Tests

This guide will cover how to configure the AI Firewall to continuously monitor your model in production.

We will be using the <a target="_blank" rel="noopener" href="https://www.kaggle.com/c/ieee-fraud-detection">IEEE-CIS Fraud Detection</a> dataset, which is available in the `rime_trial/` bundle provided during installation.

---

## Running AI Firewall Continuous Tests

### 1. Run AI Stress Testing

Kick off a run of AI Stress Testing (the reference dataset and model from this run will be used for the firewall).
```bash
rime-engine run-stress-tests --config-path examples/fraud_firewall/stress_testing_config.json
```

### 2. Configure a Firewall in the Web Client

{{ ct_open_firewall_page }}

<img src="../../../_static/ui/Firewall_Page.png" />

{{ ct_configure_steps_local_trial }}

<img src="../../../_static/ui/Firewall_Deploy.png" />

### 3. Run Continuous Tests on Incremental Data

We can now upload data and predictions and run AI Firewall Continuous Tests. The following command runs firewall continuous tests on data and predictions from April 29th, 2021.

NOTE: If you forgot to record the firewall ID in the previous step, you can find it by clicking the <img src="../../../_static/ui/GearIcon.svg" /> on the right.
```bash
rime-engine run-firewall --config-path examples/fraud_firewall/firewall_2021_04_29_to_2021_04_30_config.json --firewall-id $FIREWALL_ID
```

{{ tabular_ui_redirect }}

To simulate an incremental data load from the next day, you can run the same command with a different config.
```bash
rime-engine run-firewall --config-path examples/fraud_firewall/firewall_2021_04_30_to_2021_05_01_config.json --firewall-id $FIREWALL_ID
```

However, splitting the datasets into bin-sized batches is unnecessary --- multiple bins (days in this case) can be uploaded together. They will be split automatically and firewall continuous tests will be run on each time period. For example, the following uploads data and predictions from April 1st, 2021 until April 29th, 2021.
```bash
rime-engine run-firewall --config-path examples/fraud_firewall/firewall_2021_04_01_to_2021_04_29_config.json --firewall-id $FIREWALL_ID
```

{{ cli_note }}

---

## Using Your Own Model and Datasets

This guide will cover how to run AI Firewall Continuous Tests on your own model and datasets.

### Collect Data in the Correct Format

Data formatting requirements are very similar to those for AI Stress Tests (see [Input Data Format](../../../for_data_scientists/reference/tabular/task_data_format.md)); however, **for continuous tests, timestamp information is also needed.**

For AI Firewall Continuous Tests, RI requires two datasets: a reference dataset and an (incremental) evaluation dataset. The latter must supply a datetime column so that it can be sliced into batches appropriately. Bin-sized slices of the evaluation dataset will be compared to the reference dataset during continuous testing.

Datasets must be passed in as a `.csv` or `.parquet` file, where each column is a separate feature, and predictions must be present in both datasets.

### Create Configuration

With your data ready, you can now create a configuration file.

For a detailed reference on what the configuration should look like, see [Continuous Tests Configuration](../../../for_data_scientists/reference/tabular/firewall_continuous_tests.md).

### Run the CLI

#### AI Firewall Continuous Tests

You will need to have configured a firewall in the web client beforehand to get a Firewall ID. Please refer to the sections above for instructions.

Once complete, you can run the CLI like so:
```bash
rime-engine run-firewall --firewall-id <FIREWALL-ID> --config-path <PATH-TO-CONFIGURATION>
```

{{ tabular_ui_redirect }}

{{ cli_note }}


### Troubleshooting

{{ troubleshooting_python_package_redirect }}
