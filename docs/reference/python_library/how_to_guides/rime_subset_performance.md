# Analyzing Subset Performance

{{ rime_library_setup_note }}

## Overview

The RIME Python Library offers detailed insights into the performance of different feature subsets in your data --- excellent for detecting potential bias.

In this walkthrough, we will use AI Stress Tests to discover performance variation across feature subsets and then refine our model accordingly.

For more information, see the Subset Performance Jupyter notebook included in the trial bundle.

## Using RIME Library to Analyze Model Performance

### Running Feature Subset AI Stress Tests

In the example below, we illustrate how model accuracy varies across different subsets of the `DeviceType` categorical feature.

```python
from rime.tabular.tests import FeatureSubsetTest
from rime.tabular.metric import AccuracyMetric
test = FeatureSubsetTest("DeviceType", AccuracyMetric, (0.001, 0.02, 0.1))
test.run_notebook(container)
```

In the `subsets_info` dictionary, each key is a subset of the feature tested on: `desktop`, `mobile`, and `None`.

It contains information about the metric performance (`perf`), confidence intervals (`margin_error`), performance difference from the entire feature (`diff`), positivity rate (`pos_rate`), and other information regarding the indices and size of the subset in the feature.

**By inspecting the `worst_subset` key, we can see that the model underperforms with respect to accuracy for inputs in the `mobile` category!**

**Output**
```
{'status': 'FAIL',
 'severity': 'Medium',
 'params': {'_id': '4cb6fd45-83c0-fdd3-b393-974ef3736ead',
  'metric_name': <MetricName.ACCURACY: 'accuracy'>,
  'metric_cls': rime.tabular.metric.shared_metrics.AccuracyMetric,
  'min_sample_size': 20,
  'perf_change_thresholds': (0.001, 0.02, 0.1),
  'perf_change_threshold': 0.001,
  'col_name': 'DeviceType'},
 'columns': ['DeviceType'],
 'num_failing': 2,
 'overall_perf': 0.9692,
 'sample_size': 10000,
 'subsets_metric_dict': {'overall_perf': 0.9692,
  'subsets_info': {'desktop': {'name': 'desktop',
    'size': 1504,
    'criterion': 'desktop',
    'perf': 0.9461436170212766,
    'margin_error': 0.011408309534789187,
    'diff': 0.023056382978723367,
    'pos_rate': 0.06648936170212766,
    'sample_size_info': {<SampleSizeType.POS_LABEL: 'Positive Label'>: 100,
     <SampleSizeType.NEG_LABEL: 'Negative Label'>: 1404,
     <SampleSizeType.POS_PRED: 'Positive Prediction'>: 33,
     <SampleSizeType.NEG_PRED: 'Negative Prediction'>: 1471}},
   'mobile': {'name': 'mobile',
    'size': 947,
    'criterion': 'mobile',
    'perf': 0.9292502639915523,
    'margin_error': 0.016330589417348093,
    'diff': 0.039949736008447645,
    'pos_rate': 0.11298838437170011,
    'sample_size_info': {<SampleSizeType.POS_LABEL: 'Positive Label'>: 107,
     <SampleSizeType.NEG_LABEL: 'Negative Label'>: 840,
     <SampleSizeType.POS_PRED: 'Positive Prediction'>: 50,
     <SampleSizeType.NEG_PRED: 'Negative Prediction'>: 897}},
   'None': {'name': 'None',
    'size': 7549,
    'criterion': 'None',
    'perf': 0.9788051397536097,
    'margin_error': 0.003249127676628865,
    'diff': -0.00960513975360977,
    'pos_rate': 0.021592263876010067,
    'sample_size_info': {<SampleSizeType.POS_LABEL: 'Positive Label'>: 163,
     <SampleSizeType.NEG_LABEL: 'Negative Label'>: 7386,
     <SampleSizeType.POS_PRED: 'Positive Prediction'>: 3,
     <SampleSizeType.NEG_PRED: 'Negative Prediction'>: 7546}}}},
 'worst_subset': {'name': 'mobile',
  'size': 947,
  'criterion': 'mobile',
  'perf': 0.9292502639915523,
  'margin_error': 0.016330589417348093,
  'diff': 0.039949736008447645,
  'pos_rate': 0.11298838437170011,
  'sample_size_info': {<SampleSizeType.POS_LABEL: 'Positive Label'>: 107,
   <SampleSizeType.NEG_LABEL: 'Negative Label'>: 840,
   <SampleSizeType.POS_PRED: 'Positive Prediction'>: 50,
   <SampleSizeType.NEG_PRED: 'Negative Prediction'>: 897}}}
```

### Analyzing Model Performance

#### Overall Analysis
When RunContainers are created, RIME profiles the model's performance with respect to its feature subsets. We can obtain all that information very easily through built-in functions.

To obtain the overall performance metrics for the model, we can use `get_overall_metrics`:
```python
from rime.tabular.performance.error_analysis import get_overall_metrics

get_overall_metrics(test_data_container)
```
The output of the function, below, summarizes the performance of the model.

**Output**
```
{'AUC': 0.8373003844966462,
 'Accuracy': 0.9693,
 'F1': 0.33693304535637153,
 'Positive Prediction Rate': 0.0093,
 'Average Prediction': 0.03285634791790353,
 'Precision': 0.8387096774193549,
 'False Positive Rate': 0.001557632398753894,
 'False Negative Rate': 0.7891891891891891,
 'Recall': 0.21081081081081082,
 'Prediction Variance': 0.0066419034307548305,
 'Prediction Variance (Negative Labels)': 0.0018745259970643715,
 'Prediction Variance (Positive Labels)': 0.08604940885317178}
```

Another tool in error analysis lets us see the model's biggest misses.
Let's inspect the model's worst false positives and false negatives:
```python
from rime.tabular.performance import get_biggest_errors
fp, fn = get_biggest_errors(df, model_wrapper, labels)
```

Here is the model's worst **false positive**:
```python
worst_fp_idx = fp.idxmax()
worst_fp_example = df.iloc[worst_fp_idx,:]
worst_fp_pred = model_wrapper.predict(worst_fp_example)
worst_fp_label = labels[worst_fp_idx]

print("WORST FALSE POSITIVE:\n{}\n\nLabel: {}, Predicted Value: {}".format(worst_fp_example, worst_fp_label, worst_fp_pred))
```

**Output**
```
WORST FALSE POSITIVE:
Timestamp                    3036316.0
Product_type                         C
Card_company                      visa
Card_type                       credit
Purchaser_email_domain       gmail.com
Recipient_email_domain       gmail.com
Device_operating_system            NaN
Browser_version            chrome 63.0
Resolution                         NaN
DeviceInfo                     Windows
DeviceType                     desktop
TransactionAmt                  81.037
TransactionID                3135204.0
addr1                              NaN
addr2                              NaN
card1                           2256.0
card2                            545.0
card3                            185.0
card5                            226.0
dist1                              NaN
dist2                             17.0
Count_1                           37.0
Count_2                           47.0
Count_3                            0.0
Count_4                           13.0
Count_5                            0.0
Count_6                           13.0
Count_7                           13.0
Count_8                           28.0
Count_9                            0.0
Name: 6466, dtype: object

Label: 0, Predicted Value: 0.8809023171385614
```

Here is the model's worst **false negative**:
```python
worst_fn_idx = fn.idxmin()
worst_fn_example = df.iloc[worst_fn_idx,:]
worst_fn_pred = model_wrapper.predict(worst_fn_example)
worst_fn_label = labels[worst_fn_idx]

print("WORST FALSE NEGATIVE:\n{}\n\nLabel: {}, Predicted Value: {}".format(worst_fn_example, worst_fn_label, worst_fn_pred))
```

**Output**
```
WORST FALSE NEGATIVE:
Timestamp                     12761407.0
Product_type                           W
Card_company                        visa
Card_type                          debit
Purchaser_email_domain     anonymous.com
Recipient_email_domain               NaN
Device_operating_system              NaN
Browser_version                      NaN
Resolution                           NaN
DeviceInfo                           NaN
DeviceType                           NaN
TransactionAmt                    1795.8
TransactionID                  3476245.0
addr1                              184.0
addr2                               87.0
card1                             4436.0
card2                              174.0
card3                              150.0
card5                              226.0
dist1                                NaN
dist2                                NaN
Count_1                              1.0
Count_2                              1.0
Count_3                              0.0
Count_4                              0.0
Count_5                              1.0
Count_6                              1.0
Count_7                              0.0
Count_8                              0.0
Count_9                              1.0
Name: 9385, dtype: object

Label: 1, Predicted Value: 0.00330668052035523
```

#### Granular Analysis
For more subset specific analysis, we can run the `get_worst_overall_subset` function
which returns a dictionary of the worst performing subsets for each feature.

```python
from rime.tabular.performance.error_analysis import get_worst_overall_subset

worst_subsets = get_worst_overall_subset(test_data_container)
worst_subsets
```

**Output**
```
{'Timestamp': '[88174.0, 1208944.3]',
 'Product_type': 'S',
 'Card_company': 'discover',
 'Card_type': 'debit',
 'Purchaser_email_domain': 'yahoo.com',
 'Recipient_email_domain': 'None',
 'Device_operating_system': 'Windows 7',
 'Browser_version': 'None',
 'Resolution': '1334x750',
 'DeviceInfo': 'Trident/7.0',
 'DeviceType': 'None',
 'TransactionAmt': '(100.0, 117.0]',
 'TransactionID': '[2987101.0, 3038557.2]',
 'addr1': '(325.0, 330.0]',
 'addr2': '(87.0, 96.0]',
 'card1': '(16573.5, 18375.0]',
 'card2': 'None',
 'card3': '[100.0, 150.0]',
 'card5': '(226.0, 237.0]',
 'dist1': '(1.0, 2.0]',
 'dist2': '(74.222, 150.0]',
 'Count_1': '(2.0, 3.0]',
 'Count_2': '[0, 1.0]',
 'Count_3': '0',
 'Count_4': '[0, 1.0]',
 'Count_5': '(1.0, 3.0]',
 'Count_6': '[0, 1.0]',
 'Count_7': '(1.0, 2252.0]',
 'Count_8': '[0, 1.0]',
 'Count_9': '(1.0, 2.0]'}
```

Finally, if more granular analysis is desired, you can pass in the metrics to analyze and determine the worst subsets for only those metrics.

```python
from rime.tabular.performance.error_analysis import get_worst_subsets_for_metrics
from rime.tabular.metric import AccuracyMetric

worst_subsets_for_metrics = get_worst_subsets_for_metrics(test_data_container,
                                                          [AccuracyMetric])
worst_subsets_for_metrics
```

**Output**
```
{'Timestamp': {'Accuracy': ('(4613225.0, 6027819.5]', 0.9575098814229249)},
 'Product_type': {'Accuracy': ('C', 0.9137055837563451)},
 'Card_company': {'Accuracy': ('discover', 0.9351851851851852)},
 'Card_type': {'Accuracy': ('credit', 0.9375244045294807)},
 'Purchaser_email_domain': {'Accuracy': ('hotmail.com', 0.9470443349753694)},
 'Recipient_email_domain': {'Accuracy': ('hotmail.com', 0.9246861924686193)},
 'Device_operating_system': {'Accuracy': ('Windows 7', 0.9646017699115044)},
 'Browser_version': {'Accuracy': ('chrome 64.0', 0.9241379310344827)},
 'Resolution': {'Accuracy': ('1366x768', 0.9291338582677166)},
 'DeviceInfo': {'Accuracy': ('Windows', 0.9427570093457944)},
 'DeviceType': {'Accuracy': ('mobile', 0.9260823653643083)},
 'TransactionAmt': {'Accuracy': ('(280.0, 3967.81]', 0.9436619718309859)},
 'TransactionID': {'Accuracy': ('(3188929.0, 3239251.0]', 0.9575098814229249)},
 'addr1': {'Accuracy': ('None', 0.9154929577464789)},
 'addr2': {'Accuracy': ('(87.0, 96.0]', 0.9090909090909091)},
 'card1': {'Accuracy': ('(13044.0, 15111.0]', 0.9539267015706806)},
 'card2': {'Accuracy': ('None', 0.9310344827586207)},
 'card3': {'Accuracy': ('(150.0, 185.0]', 0.9087221095334685)},
 'card5': {'Accuracy': ('(126.0, 166.0]', 0.9616766467065868)},
 'dist1': {'Accuracy': ('(208.889, 4568.0]', 0.9599109131403119)},
 'dist2': {'Accuracy': ('(7.0, 9.0]', 0.8571428571428571)},
 'Count_1': {'Accuracy': ('(3.0, 7.0]', 0.9504854368932039)},
 'Count_2': {'Accuracy': ('(7.0, 5690.0]', 0.9535374868004224)},
 'Count_3': {'Accuracy': ('0', 0.96921071106208)},
 'Count_4': {'Accuracy': ('(1.0, 2250.0]', 0.8878718535469108)},
 'Count_5': {'Accuracy': ('[0, 1.0]', 0.9647382261534784)},
 'Count_6': {'Accuracy': ('(5.0, 2250.0]', 0.9632183908045977)},
 'Count_7': {'Accuracy': ('(1.0, 2252.0]', 0.8470149253731343)},
 'Count_8': {'Accuracy': ('(1.0, 3328.0]', 0.9001663893510815)},
 'Count_9': {'Accuracy': ('[0, 1.0]', 0.9671781756180733)}}
```


## Improving Model Performance Results: Overweighting

After using RIME to identify weaknesses of your model, it's time to improve your model's performance. One method of doing this is to increase the training weights of underperforming subsets. Let's try to increase the performance of subset `C` in the feature `Product_type`, which currently has an accuracy of ~91%.

```python
worst_subsets_for_metrics["Product_type"]
```

**Output**
```
{'Accuracy': ('C', 0.9137055837563451)}
```

### Training the Initial Model

We can proceed in the regular way to train the model.

First, we preprocess our train and test data for our model
```python
train_pre = preprocess_df(train_df)
train_preds = model.predict_proba(train_pre)[:, 1]

COL = 'Product_type'
VAL = 'C'
train_df_full = train_df.copy()
train_df_full['label'] = train_labels
train_df_full['preds'] = train_preds
```

And then, we adjust the subset sample weights and retrain
```python
sample_weights = (train_pre[COL] == VAL) + 1

import numpy as np
categorical_features_indices = np.where(train_pre.dtypes != np.float)[0]
new_model = catb.CatBoostClassifier(random_state=0, verbose=0)
new_model.fit(train_pre, train_labels, sample_weight=sample_weights, cat_features=categorical_features_indices)
```

### Comparing Improvements
We can define a new predict_dict function and create a new container to calculate updated metrics.

```python
def predict_dict_new_model(x: dict):
    """Predict dict function."""
    new_x = preprocess(x)
    new_x = pd.DataFrame(new_x, index=[0])
    return new_model.predict_proba(new_x)[0][1]

new_data_container = DataContainer.from_df(train_df, model_task=ModelTask.BINARY_CLASSIFICATION, labels=train_labels)
test_data_container = DataContainer.from_df(test_df, labels=test_labels, model_task=ModelTask.BINARY_CLASSIFICATION, ref_data=data_container)
new_container = TabularRunContainer.from_predict_dict_function(new_data_container, test_data_container, predict_dict_new_model, ModelTask.BINARY_CLASSIFICATION)
```

Calculating overall metrics, despite our rather simple adjustment, **the accuracy increases to ~96%**:

```python
new_worst_subsets_for_metrics = get_worst_subsets_for_metrics(new_data_container, [MetricName.ACCURACY])
new_worst_subsets_for_metrics["Product_type"]
```

**Output**
```
{'Accuracy': ('C', 0.9650974025974026)}
```
