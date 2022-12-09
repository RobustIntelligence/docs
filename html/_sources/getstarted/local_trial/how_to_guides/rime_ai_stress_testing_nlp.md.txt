# Validating Your Model with AI Stress Testing

This tutorial will guide you through validating NLP models with AI Stress Testing.

All examples are available in the `rime_trial/` bundle provided during installation.

{{ stress_test_bio }}

## NLP Setup

{{ nlp_setup_extra_note }}

## Running Stress Testing on a Text Classification Example

This example uses a DistilBERT emotion recognition model trained on a slightly modified version of the <a target="_blank" rel="noopener" href="https://github.com/dair-ai/emotion_dataset">CARER Emotion Recognition Dataset</a>, which relies on a couple of additional dependencies.

To install, please run the following command:
```bash
pip install -r nlp_examples/trial_model_requirements.txt
```

To start a run of AI Stress Testing using a model and datasets:
```bash
rime-engine run-nlp --config-path nlp_examples/classification/emotion_recognition/stress_tests_config.json
```

**NOTE:** if the above command throws a `ModuleNotFoundError`, it is likely that you forgot to install the NLP Extras ([see setup above](#nlp-setup)).

{{ nlp_ui_redirect }}

If you explore the test config in `nlp_examples/classification/emotion_recognition/stress_tests_config.json` you'll see that we've configured a few parameters to specify the data, model, and other task-specific information.

{{ nlp_config_note }}

## Running Stress Testing on a Text Classification Example with Metadata

In this tutorial, we will cover adding custom metadata to your test run.

This example uses a RoBERTa based model trained on tweets and finetuned for sentiment analysis. The dataset used in this example is data scraped from Twitter to analyze how travelers expressed feelings about airlines.

The data includes several attributes alongside `text` and `label` that RI will also run automated tests on:
- Custom numeric metadata: `Retweet_count`
- Custom categorical metadata: `Reason`, `Airline`, `Location`

These attributes exist for each datapoint in the `meta` dict, as key-value pairs. For example:
```
{"text": "@USAirways You have no idea how upset and frustrated I am right now. I'll be sure to follow through with never flying with you again.", "label": 0, "meta": {"Reason": "Can't Tell", "Airline": "US Airways", "Location": "Saratoga Springs", "Retweet_count": 0}}
```

To start a run of AI Stress Testing using a model, datasets, and custom metadata:
```bash
rime-engine run-nlp --config-path nlp_examples/classification/sentiment_analysis/stress_tests_config_with_metadata.json
```

If you poke around in `stress_tests_config_with_metadata.json` you'll see that we've added `custom_numeric_metadata` and `custom_categorical_metadata` to `data_profiling_info`:
```python
{
    "run_name": "Sentiment Analysis (Twitter Airline)",
    "model_task": "Text Classification",
    "data_info": { ... },
    "model_info": { ... },
    "prediction_info": { ... },
    "data_profiling_info": {
        "class_names": [
            "negative",
            "neutral",
            "positive"
        ],
        "custom_numeric_metadata": [
            "Retweet_count"
        ],
        "custom_categorical_metadata": [
            "Reason",
            "Airline",
            "Location"
        ]
    },
    "random_seed": 42
}
```

For a full reference on the data profile file see the [Data Profiling Configuration](/for_data_scientists/reference/nlp/data_profiling.md).

## Running Stress Testing on a Named Entity Recognition Example

This examples uses the <a target="_blank" rel="noopener" href="https://huggingface.co/dslim/bert-base-NER">bert-base-NER</a> model from Hugging Face.

To start a run of AI Stress Testing using the `bert-base-NER` model:
```bash
rime-engine run-nlp --config-path nlp_examples/ner/conll/stress_tests_config.json
```

If you poke around in `nlp_examples/ner/conll/stress_tests_config.json` you'll see that we've changed the `model_task` to `Named Entity Recognition`, along with a couple of other parameters.

{{ nlp_config_note }}

---

## Running Stress Testing on Your Own Model and Datasets

### Define a Python Model File

Please refer to [How to Create an NLP Model FIle](/for_data_scientists/reference/nlp/specify_model_nlp.md) for step-by-step instructions on creating a model interface for RI.

### Gather Datasets

#### 1. Prepare Input Data

For a detailed specification of data formatting, see [Input Data Format](/for_data_scientists/reference/nlp/task_data_format.md)

#### 2. Specify Prediction Logs (Recommended)

Because model inference is usually the most time-consuming part of the testing framework, we recommend specifying cached prediction logs using the [prediction_info](/for_data_scientists/reference/nlp/prediction_info) argument of the runtime config.

In the classification example above, we specified model predictions separately in the files `nlp_examples/classification/emotion_recognition/data/{train|val}_preds.json`.

An example prediction can be viewed from this file by running the following command from your terminal:
```
cat nlp_examples/classification/emotion_recognition/data/test_preds.json | jq '.[0]'
```

RI supports predictions stored in compressed `.json` or `.jsonl` format and accepts predictions added within the datafile itself (by adding the "probabilities" key to each data sample).

However, if you do not wish to create a prediction log beforehand, RI can call your model during a test run and infer its performance using a subsample of the provided datasets. See `nlp_examples/classification/emotion_recognition/stress_tests_config_no_preds.json` for an example.

### Create Configuration

With your data and model ready, you can now create a configuration file. Examples of these can be found in the `rime_trial/` bundle (the ones used for these examples are under `nlp_examples/`).

For a detailed reference on what the configuration should look like, see [AI Stress Testing Configuration Reference](/for_data_scientists/reference/nlp/stress_testing.md).

### Run the CLI

To start a run of AI Stress Testing using your configuration file, simply replace the `--config-path` argument below:
```bash
rime-engine run-nlp --config-path <PATH-TO-CONFIGURATION>
```

## Conclusion

Congratulations! You've successfully used RI to test out the various NLP models.

Once again, we strongly recommended that you run RI using a cached predictions file, similar to the one provided in the first part of this tutorial. This will greatly improve both the RI runtime and the test suite result quality.

Model inference tends to be the most computationally expensive part of each RI run, especially for large transformer models. While access to the model is still required for some tests due to design constraints (e.g., the use of randomness, iterative attacks, etc.), providing a prediction file can help RI avoid redundant computation so each run is fast and focused.

## Troubleshooting
{{ troubleshooting_python_package_redirect }}
