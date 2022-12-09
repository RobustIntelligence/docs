# Validating Your Model with AI Stress Testing

This tutorial will guide you through validating a Binary Classification model with AI Stress Testing.

This model was trained on a slightly modified version of the <a target="_blank" rel="noopener" href="https://www.kaggle.com/uciml/adult-census-income">Adult Census Income</a> dataset and is available in the `rime_trial/` bundle provided during installation.

{{ stress_test_bio }}

## Running Stress Testing on the Income Example

### Stress Testing with a Model and Datasets

In this example, we will be providing the model directly to RI, which enables the most thorough possible analysis. However, RI can be run with prediction logs alone (or even just datasets), which we will illustrate below as well.

To start a run of AI Stress Testing using a model and datasets:
```bash
rime-engine run-stress-tests --config-path examples/income/stress_tests_model.json
```
{{ tabular_ui_redirect }}

{{ cli_note }}

### Stress Testing with Prediction Logs

To start a run of AI Stress Testing using prediction logs (no model) and datasets:
```bash
rime-engine run-stress-tests --config-path examples/income/stress_tests_prediction_logs.json
```

Note that the command is exactly the same EXCEPT for the `--config-path` provided.

### Stress Testing with Bias And Fairness Tests

To start a specific suite of tests geared towards bias and fairness:

```bash
rime-engine run-stress-tests --config-path examples/income/stress_tests_bias_and_fairness.json
```

The command is exactly the same as the others; however, in the configuration file we have specified `Bias And Fairness` under `categories` as well as a list of `protected_features` in our `data_info`:
```python
{
  "run_name": "Income - Bias And Fairness",
  "data_info": {
    "protected_features": ["sex", "race", "education", "age", "native.country"]
    ...
  },
  "test_config": {
    "categories": ["Bias And Fairness"],
    "run_default": false
  },
  "model_info": { ... }
}
```
---

## Running Stress Testing on Your Own Model and Datasets

This guide will cover how to run AI Stress Testing on your own model and datasets.

### Define a Python Model File

A model is not required for AI Stress Testing, but providing one will produce better results.

For step-by-step instructions, please see [How to Create a Python Model File](../../../for_data_scientists/reference/tabular/specify_model.md).

### Gather Datasets

For a detailed specification of data formatting, see [Input Data Format](../../../for_data_scientists/reference/tabular/task_data_format.md).

#### 1. Split the Data

For AI Stress Testing, RI requires two datasets: a reference dataset (typically the training data) and an evaluation dataset (typically the validation, testing, or other data).
Currently RI expects each dataset to be passed in as a `.csv` or `.parquet` file where each column is a separate feature.

#### 2. Specify Labels (Recommended)

Providing labels allows RI to surface model performance metrics across our tests. These should be passed in as a column in both datasets.

NOTE: For Multi-Class Classification models, each label should be a nonnegative integer `i` where the corresponding prediction for label `i` should be found in the `ith` dimenson of the prediction vector.

#### 3. Specify Predictions (Recommended)

If a model has not already been specified, providing predictions will produce better results. These should be passed in as a column in both datasets.

NOTE: For Multi-Class Classification models, predictions must be specified in a separate csv or parquet file as a dataframe where the `ith` column represents the predicted probabilities for the `ith` class/label.

### Create Configuration

With your data and model ready, you can now create a configuration file. Examples of these can be found in the `rime_trial/` bundle (the ones used for this example are under `examples/income/`).

For a detailed reference on what the configuration should look like, see [AI Stress Testing Configuration Reference](../../../for_data_scientists/reference/tabular/stress_testing.md).

### Run the CLI

To start a run of AI Stress Testing using your configuration file, simply replace the `--config-path` argument below:
```bash
rime-engine run-stress-tests --config-path <PATH-TO-CONFIGURATION>
```
{{ tabular_ui_redirect }}

---

### Troubleshooting
{{ troubleshooting_python_package_redirect }}
