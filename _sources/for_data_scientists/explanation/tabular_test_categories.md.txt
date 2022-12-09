# Summary Tests
## Drift
Test for differences in the distribution of the reference dataset versus the         evaluation dataset. If predictions and labels are provided, measure the         performance degradation caused by shifting data as well as drift in         predictions and labels themselves.        <br>        <br>        Labels and predictions are not required but they improve results.
## Abnormal Inputs
Check the evaluation dataset for abnormal values commonly encountered in         production. If model predictions are provided, test if the observed abnormal          values cause a degradation in your model’s performance.        <br>        <br>        Labels and predictions are not required but they improve results.
## Subset Performance
Test that your model performs equally well across different subsets of the         evaluation dataset.        <br>        <br>        Predictions are required. Labels are required for most tests.
## Bias And Fairness
Test that your model does not discriminate based on protected features.        <br>        <br>        For some tests predictions, labels, and/or model are required.
## Transformations
Augment your evaluation dataset with synthetic abnormal values to proactively         test your pipeline’s error-handling behavior and measure the performance         degradation caused by different types of abnormal values.        <br>        <br>        Model is required. Labels are not required but they improve results.
## Model Performance
Test that your model performs well on the evaluation dataset and         is not degrading in performance.        <br>        <br>        Predictions are required. Labels are required for exact performance metrics,        otherwise approximate performance metrics will be used.
## Data Cleanliness
Test for data reliability by checking that your data is consistent and complete.
## Attacks
Test the robustness of your model by measuring the maximum         difference in model predictions that can be caused by small perturbations to         data points.        <br>        <br>        Model is required.
## Finance Compliance
Test that your model aligns with financial regulatory standards. This test suite    consists of a selection of bias and fairness, abnormal input, and attack tests.    <br>    <br>    For some tests predictions, labels, and/or model are required.
## Hiring Compliance
Test that your model aligns with hiring regulatory standards. This test suite    consists of a selection of bias and fairness tests.    <br>    <br>    For some tests predictions, labels, and/or model are required.
## Healthcare Compliance
Test that your model aligns with healthcare regulatory standards. This test suite    consists of a selection of bias and fairness, data cleanliness, and data leakage tests.    <br>    <br>    For some tests predictions, labels, and/or model are required.
## Subset Performance Degradation
Test that your model's performance on different subsets of the data has not         degraded.        <br>        <br>        Predictions are required. Labels are required for most tests.
