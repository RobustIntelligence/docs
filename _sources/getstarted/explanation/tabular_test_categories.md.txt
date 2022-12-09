# Summary Tests
## Drift
Test for differences in the distribution of the reference dataset versus the         evaluation dataset. If predictions and labels are provided, measure the         performance degradation caused by shifting data as well as drift in         predictions and labels themselves.        <br>        <br>        Labels and predictions are not required but they improve results.
## Abnormal Inputs
Check the evaluation dataset for abnormal values commonly encountered in         production. If model predictions are provided, test if the observed abnormal          values cause a degradation in your model’s performance.        <br>        <br>        Labels and predictions are not required but they improve results.
## Subset Performance

Test that your model performs equally well across different subsets of the evaluation dataset. 

Predictions are required. Labels are required for most tests.

## Bias and Fairness

Test that your model does not discriminate based on protected features. You must specify these protected features as an array value for the `protected_features` key in the `data_info` object.

For some tests predictions, labels, and/or model are required.

## Transformations
Augment your evaluation dataset with synthetic abnormal values to proactively         test your pipeline’s error-handling behavior and measure the performance         degradation caused by different types of abnormal values.        <br>        <br>        Model is required. Labels are not required but they improve results.
## Model Performance
Test that your model performs well on the evaluation dataset and         is not degrading in performance.        <br>        <br>        Predictions are required. Labels are required for exact performance metrics,        otherwise approximate performance metrics will be used.
## Data Cleanliness
Test for data reliability by checking that your data is consistent and complete.
## Attacks

Test the robustness of your model by measuring the maximum difference in model predictions that can be caused by small perturbations to data points.

Model is required.

## Subset Performance Degradation
Test that your model's performance on different subsets of the data has not         degraded.        <br>        <br>        Predictions are required. Labels are required for most tests.
## Data Poisoning Detection

Test for the presence of potentially corrupted samples in your data.

Labels are required.

Note that the default behavior of this test in Continuous Testing depends on the quality of data used for the initial stress test. If corrupted samples were detected in the stress test, then the continuous test will be more permissive.
