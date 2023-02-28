# Summary Tests

Individual tests measure a single, specific aspect. Drift, for example, is tracked by over 10
different tests. A summary test answers the higher-level question "is there problematic drift present in my data?"

By default, test run results presents these summary tests first. This sample test results page 
includes five summary tests in the first view.

<img src="../_static/summary_test_overview_page.png">

Click a test to see the specific page for that summary test.

<img src="../_static/summary_test_page.png">

Summary tests provide the following information:

## Test result metrics

These metrics are the outcome of data analysis and do not expose the underlying raw data, which cannot be recreated based on these results. Test results are encrypted.

**Performance impact** describes the model's baseline performance and changes to that performance.

**Drift impact** estimates the effect on performance caused by statistically significant drift in a given feature.

**Severity scores** are aggregate scores that describe the resilience of an ML deployment. Severity scores vary depending on the vulnerability of the model and dataset to the changes introduced by a given test.

**Thresholds** are values that the tests consider to be significant indicators of test failure. When a metric exceeds a specified threshold, the test associated with that metric fails, either as a warning or as an alert.

## Model features

Information in this section provides a summary of the data. The underlying data cannot be recreated from this information.

**Feature names** in the dataset.

**Feature distributions** in the dataset, including ranges and common categories.

**The values of individual features or groups of features**. Categorical features list the different possible categories. Numerical features list the possible ranges.

## Failing rows

Lists the rows that fail abnormal inputs tests. Abnormal inputs testing can be [disabled](../../for_data_scientists/reference/nlp/test_suite.rst).

## Original data points

NLP and Image tests include a sample of data points when the Transformation or Attacks tests are run. Transformation or Attacks testing can be [disabled](../../for_data_scientists/reference/nlp/test_suite.rst).

Realtime Events tests include every individual data point in the underlying dataset. Realtime Events testing can be disabled by using feature or license flags.

## Software monitoring logs

All confidential data in software monitoring logs is masked or filtered.
