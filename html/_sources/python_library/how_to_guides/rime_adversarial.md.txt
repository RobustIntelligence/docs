# Adversarial Attacks

{{ rime_library_setup_note }}

## Overview

Besides offering a comprehensive suite of stress tests, the RIME Python Library also offers a wide suite of adversarial attacks for tabular data.

An **Adversarial Attack** is a series of input perturbations designed to significantly alter model predictions.

In this walkthrough, we will attempt to invert the predictions of the Binary Classification model we've been using for the [IEEE-CIS Fraud Detection](https://www.kaggle.com/c/ieee-fraud-detection) example.

For more information, check out the [documentation](../reference/adversarial.rst) for different types of attacks and their parameters. Additionally, a pre-configured RIME Adversarial Jupyter notebook is included in the trial bundle.

## Running an Adversarial Attack
We can access the components we need from the `container` as follows:
```python
black_box_model = container.model.base_model
columns = container.data_profile.columns
```

`black_box_model` is our model wrapper, which we will be attacking. `columns` is our profile of the data, which allows our attacks to know how to manipulate data points in order to attack them.

We now import the attack algorithm we want to use.

```python
from rime.tabular.attacks.combination import TabularCombinationAttack
```

Next, we initialize the attack algorithm with parameters of our choosing. For more information on each attack's parameters, please reference the [documentation](../reference/adversarial.rst).

```python
import numpy as np
target_score = .5
max_queries = np.inf
attack = TabularCombinationAttack(black_box_model, target_score, max_queries, columns)
```

We can now run the attack! In the example below, we loop over the first 10 rows, set a target label equal to the opposite of their true label, and then run the attack algorithm trying to push the score towards that label.

```python
from rime.tabular.attacks.runner import run_attack_loop

sample_size = 10
attack_results, indices = run_attack_loop(attack, container, sample_size)
```

Finally we can explore the results of the attack. Looking at one attack result, we can see the initial row and its score, the final attacked row and its score, as well as a list of features that were changed.

```python
from rime.tabular.attacks.notebook import parse_attack_result

attack_result = attack_results[0]

parse_attack_result(attack_result)
```

**Output**
```
{'initial_row': Timestamp                           1726190.0
 Product_type                                H
 Card_company                             visa
 Card_type                               debit
 Purchaser_email_domain             icloud.com
 Recipient_email_domain             icloud.com
 Device_operating_system            iOS 11.0.3
 Browser_version            mobile safari 11.0
 Resolution                          2048x1536
 DeviceInfo                         iOS Device
 DeviceType                             mobile
 TransactionAmt                           25.0
 TransactionID                       3067158.0
 addr1                                   264.0
 addr2                                    87.0
 card1                                  5066.0
 card2                                   302.0
 card3                                   150.0
 card5                                   226.0
 dist1                                     NaN
 dist2                                     NaN
 Count_1                                   1.0
 Count_2                                   1.0
 Count_3                                   0.0
 Count_4                                   1.0
 Count_5                                   0.0
 Count_6                                   1.0
 Count_7                                   0.0
 Count_8                                   1.0
 Count_9                                   0.0
 dtype: object,
 'initial_score': 0.01294191171910275,
 'final_row': Timestamp                           1726190.0
 Product_type                                H
 Card_company                             visa
 Card_type                               debit
 Purchaser_email_domain             icloud.com
 Recipient_email_domain             icloud.com
 Device_operating_system            iOS 11.0.3
 Browser_version            mobile safari 11.0
 Resolution                          2048x1536
 DeviceInfo                         iOS Device
 DeviceType                             mobile
 TransactionAmt                           25.0
 TransactionID                       3067158.0
 addr1                                   264.0
 addr2                                    87.0
 card1                                  5066.0
 card2                                   302.0
 card3                                   150.0
 card5                                   226.0
 dist1                                     NaN
 dist2                                     NaN
 Count_1                                4161.0
 Count_2                                   1.0
 Count_3                                   0.0
 Count_4                                   1.0
 Count_5                                   0.0
 Count_6                                   1.0
 Count_7                                   0.0
 Count_8                                   1.0
 Count_9                                   0.0
 dtype: object,
 'final_score': 0.6861326700487259,
 'changes': [{'col': 'Count_1', 'initial_value': 1.0, 'final_value': 4161.0}]}
```
## Improving Adversarial Robustness with Attack Results

### Fetching Adversarial Training Examples
The RIME Python Library provides additional training examples that can make your model more robust to adversarial attacks.

After running our attack loop, we can get a dataframe of our attacks and their appropriate labels as training examples.
We can then concatenate our new training examples to our old training examples in order to get a new training set for our model.

```python
from rime.tabular.attacks.notebook import get_df_from_attack_results

additional_train_data = get_df_from_attack_results(attack_results)
additional_train_labels = train_labels[indices].reset_index(drop=True)

new_train_data = pd.concat([train_df, additional_train_data]).reset_index(drop=True)
new_train_labels = pd.concat([train_labels, additional_train_labels]).reset_index(drop=True)
```

### Retraining a New Model

Using the new training data, we can train a new model.

```python
new_train_pre = preprocess_df(new_train_data)

categorical_features_indices = np.where(new_train_pre.dtypes != np.float)[0]
new_model = catb.CatBoostClassifier(random_state=0, verbose=0)
new_model.fit(new_train_pre, new_train_labels, cat_features=categorical_features_indices)
```

Just as we did before, we can define prediction functions for our new model and create new RunContainers.

```python
def predict_dict_new_model(x: dict):
    """Predict dict function."""
    new_x = preprocess(x)
    new_x = pd.DataFrame(new_x, index=[0])
    return new_model.predict_proba(new_x)[0][1]

new_data_container = DataContainer.from_df(new_train_data, model_task=ModelTask.BINARY_CLASSIFICATION, labels=new_train_labels)
test_data_container = DataContainer.from_df(test_df, labels=test_labels, model_task=ModelTask.BINARY_CLASSIFICATION, ref_data=data_container)
new_container = TabularRunContainer.from_predict_dict_function(new_data_container, test_data_container, predict_dict_new_model, ModelTask.BINARY_CLASSIFICATION)
```

### Comparing Improvements

To see the improvements to robustness after training a new model with the provided data,
we can compare the results of vulnerability tests.
```python
from rime.tabular.tests import VulnerabilityTest
test = VulnerabilityTest('Count_1')
test.run_notebook(container)
```

```python
new_test = VulnerabilityTest('Count_1')
new_test.run_notebook(new_container)
```

The corresponding outputs are below:

**Original Output**
```
This test raised a warning (with severity level Medium) because the average change in prediction caused by an unbounded manipulation of the feature Count_1 over a sample of 10 rows was 0.191, which is above the warning threshold of 0.05.
{'status': 'FAIL',
 'severity': 'Medium',
 'Average Prediction Change': 0.190968872875789,
 'params': {'_id': '72a49795-32db-540d-91b3-67ab6ef9eff5',
  'severity_level_thresholds': (0.05, 0.15, 0.25),
  'col_names': ['Count_1'],
  'l0_constraint': 1,
  'linf_constraint': None,
  'sample_size': 10,
  'search_count': 10,
  'use_tqdm': False,
  'label_range': (0.0, 1.0),
  'scaled_min_impact_threshold': 0.05},
 'columns': ['Count_1'],
 'sample_inds': [3344, 1712, 4970, 4480, 1498, 1581, 3531, 473, 9554, 2929],
 'avg_score_change': 0.190968872875789,
 'normalized_avg_score_change': 0.190968872875789}
```

**Retrained Output**
```
This test passed because the average change in prediction caused by an unbounded manipulation of the feature Count_1 over a sample of 10 rows was 0.026, which is below the warning threshold of 0.05.
{'status': 'PASS',
 'severity': 'None',
 'Average Prediction Change': 0.026220177655675303,
 'params': {'_id': '72a49795-32db-540d-91b3-67ab6ef9eff5',
  'severity_level_thresholds': (0.05, 0.15, 0.25),
  'col_names': ['Count_1'],
  'l0_constraint': 1,
  'linf_constraint': None,
  'sample_size': 10,
  'search_count': 10,
  'use_tqdm': False,
  'label_range': (0.0, 1.0),
  'scaled_min_impact_threshold': 0.05},
 'columns': ['Count_1'],
 'sample_inds': [3344, 1712, 4970, 4480, 1498, 1581, 3531, 473, 9554, 2929],
 'avg_score_change': 0.026220177655675303,
 'normalized_avg_score_change': 0.026220177655675303}
```

As shown above, a test that failed previously with "Medium" severity now passes, displaying an increased robustness of the retrained model.

## Highlighted Extra Features

### Validity Function
RIME attacks will try to use only perturbations that result in valid data, but often there can be higher-order constraints on validity that the attack will not pick up on its own. To enforce these types of constraints, you can implement a `validity_function()`.

This function should take as input a dictionary representing a row of data (i.e. keys will be feature names, and values will be feature values) and return a boolean that indicates whether the point is "valid".

In our fraud example, we might need to enforce a constraint that the rows with value `american express` for the `Card_company` feature must have value `credit` for the `Card_type` feature. To encode this, we could use the validity function:

```python
def validity_function(x: dict) -> bool:
    if x['Card_company'] == 'american express' and x['Card_type'] == 'credit':
        return True
    return False
```

We can then pass this function to the attack using the `validity_function` keyword argument:
```python
attack = TabularCombinationAttack(black_box_model, target_score, max_queries, columns, validity_function=validity_function)
```
