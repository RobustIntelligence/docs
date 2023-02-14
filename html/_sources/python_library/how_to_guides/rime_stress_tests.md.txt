# AI Stress Tests

{{ rime_library_setup_note }}

## Overview

{{ stress_test_bio }}

All tests expose a `run_notebook` function, which returns outputs in a notebook-friendly format.
The return type is a dictionary with a few standard keys. The fundamental ones are:
- `status`: Will be one of `PASS`, `FAIL`, `WARNING`, or `SKIP`. Denotes the status of the test.
- `severity`: Will be one of `High`, `Medium`, `Low`, or `None`. Denotes the severity of the failure of the test (will be `None` if test did not fail).
- `params`: A dictionary of all the parameters of the test.
- `columns`: A list of column names that this test was run over.

Depending on their purpose, different tests may have additional keys for unique information.

## Unseen Categorical

As an example, we can run the **Unseen Categorical** test:
```python
from rime.tabular.tests import UnseenCategoricalTest
test = UnseenCategoricalTest(col_name="Device_operating_system")
test.run_notebook(container)
```
<b>Output</b>:
```
{'status': 'FAIL',
 'severity': 'Low',
 'params': {'_id': '4d2a94f6-d7aa-c547-b682-7e78fd71a79f',
  'model_impact_config': ObservedModelImpactConfig(severity_thresholds=None, min_num_samples=10),
  'col_name': 'Device_operating_system'},
 'columns': ['Device_operating_system'],
 'unseen_value_counts': Mac OS X 10_11_4    2
 Mac OS X 10.9       2
 Mac OS X 10_12_2    1
 Mac OS X 10_12_1    1
 Mac OS X 10.6       1
 Windows             1
 Mac OS X 10.10      1
 Name: Device_operating_system, dtype: int64,
 'failing_rows': [158, 1330, 1807, 2429, 2831, 4380, 4727, 7494, 9317],
 'num_failing_rows': 9}
```

## Duplicate Rows

Running the **Duplicate Rows** test:
```python
from rime.tabular.tests import DuplicateRowsTest
test = DuplicateRowsTest()
test.run_notebook(container)
```
<b>Output</b>:
```
This test passed because there are 0 duplicate row(s) in the evaluation data.
{'status': 'PASS',
 'severity': 'None',
 'Failing Rows': '0 (0.00%)',
 'params': {'_id': 'eccd9267-a47a-185c-58e4-eb88fea02ce7',
  'col_names': None,
  'severity_thresholds': (0.01, 0.05)},
 'columns': []}
```

## Non-Parametric Outliers

Running the **Non-Parametric Outliers** test on a numeric feature column:
```python
from rime.tabular.tests import NonParametricOutliersTest
test = NonParametricOutliersTest("TransactionAmt")
test.run_notebook(container)
```
<b>Output</b>:
```
{'status': 'FAIL',
 'severity': 'Low',
 'params': {'_id': 'af584cae-191e-8cfa-b9f1-50dfa0a188a3',
  'model_impact_config': ObservedModelImpactConfig(severity_thresholds=None, min_num_samples=10),
  'col_name': 'TransactionAmt',
  'min_normal_prop': 0.99,
  'baseline_quantile': 0.1,
  'perturb_multiplier': 1.0},
 'columns': ['TransactionAmt'],
 'lower_threshold': -30.1300916166291,
 'upper_threshold': 4396.228995809948,
 'failing_rows': [3302, 8373],
 'num_failing_rows': 2}
```

## Vulnerability

Running the **Vulnerability** (AKA single-feature change) test:
```python
from rime.tabular.tests import VulnerabilityTest
test = VulnerabilityTest("DeviceInfo")
test.run_notebook(container)
```
<b>Output</b>
```
This test passed because the average change in prediction caused by an unbounded manipulation of the feature DeviceInfo over a sample of 10 rows was 0.00555, which is below the warning threshold of 0.05.
{'status': 'PASS',
 'severity': 'None',
 'Average Prediction Change': 0.0055514594454474705,
 'params': {'_id': 'e94863f0-e938-4be9-5e9b-e64674edc3b1',
  'severity_level_thresholds': (0.05, 0.15, 0.25),
  'col_names': ['DeviceInfo'],
  'l0_constraint': 1,
  'linf_constraint': None,
  'sample_size': 10,
  'search_count': 10,
  'use_tqdm': False,
  'label_range': (0.0, 1.0),
  'scaled_min_impact_threshold': 0.05},
 'columns': ['DeviceInfo'],
 'sample_inds': [3344, 1712, 4970, 4480, 1498, 1581, 3531, 473, 9554, 2929],
 'avg_score_change': 0.0055514594454474705,
 'normalized_avg_score_change': 0.0055514594454474705}
```

## Feature Subset

Running the **Feature Subset** test:
```python
from rime.tabular.tests import FeatureSubsetTest
from rime.tabular.metric import AccuracyMetric
test = FeatureSubsetTest("DeviceType", AccuracyMetric, (0.1, 1.0, 1.0))
test.run_notebook(container)
```
<b>Output</b>
```
{'status': 'PASS',
 'severity': 'None',
 'params': {'_id': '48457123-e119-0d15-c942-e9cb31e54840',
  'metric_name': <MetricName.ACCURACY: 'accuracy'>,
  'metric_cls': rime.tabular.metric.shared_metrics.AccuracyMetric,
  'min_sample_size': 20,
  'perf_change_thresholds': (0.1, 1.0, 1.0),
  'perf_change_threshold': 0.1,
  'col_name': 'DeviceType'},
 'columns': ['DeviceType'],
 'num_failing': 0,
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

That's it!

**NOTE**: It's important to point out that while we loaded a pretrained model for convenience, the RIME Python Library can be used at any point during the prototyping workflow, whether that's during initial data exploration, or model training and iteration.
