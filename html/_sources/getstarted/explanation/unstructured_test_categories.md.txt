# Test Categories

## Drift

Tests for differences in the distribution of the reference dataset versus the evaluation dataset. When predictions and labels are provided, measures the         performance degradation caused by shifting data as well as drift in predictions and labels themselves.

Labels and predictions are not required but improve results.

## Abnormal Inputs

Check the evaluation dataset for abnormal values commonly encountered in production. If model predictions are provided, test if the observed abnormal values cause a degradation in your model’s performance.

Labels and predictions are not required but improve results.

## Subset Performance

Test that your model performs equally well across different subsets of the evaluation dataset.

Predictions are required. Labels are required for most tests.

## Transformations

Test your model's invariance to different types of data transformations.

Model is required. Labels are not required but improve results.

## Model Performance

Test that your model performs well on the evaluation dataset and is not degrading in performance.

Predictions are required. Labels are required for exact performance metrics, otherwise approximate performance metrics will be used.

## Adversarial

Test the robustness of your model by measuring the maximumdifference in model predictions that can be caused by small perturbations to the input.

Model is required.

## Data Cleanliness

Test for data reliability by checking that your data is consistent and complete.

## Subset Performance Degradation

Test that your model's performance on different subsets of the data has not degraded.

Predictions are required. Labels are required for most tests.

## Data Poisoning Detection

Test for the presence of potentially corrupted samples in your data.

Labels are required.

Note that the default behavior of this test in Continuous Testing depends on the quality of data used for the initial stress test.

If corrupted samples were detected in the stress test, the continuous test is more permissive.
