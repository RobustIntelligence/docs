# Improving Model Performance

{{ rime_library_setup_note }}

## Overview

This tutorial will guide you through various ways to use RIME to improve model performance. For more information, please see [the corresponding reference](../reference/performance.rst).

## Preprocessing

The RIME Python Library offers standard preprocessing methods to automatically handle tasks like mapping categorical values to numbers or imputing null values.

To use preprocessing, simply import it and wrap your existing DataFrame:
```python
from rime.tabular.performance import preprocess_df
preprocessed_df = preprocess_df(df)
```

## Active Learning
RIME also contains some functionality for "active learning".

Concretely, RIME can take in an unlabeled dataset and model(s) and suggest points that would be high value to label.

To use this functionality, let's first import the relevant functions:

```python
from rime.tabular.performance import single_model_active_learning, two_model_active_learning
```

We can then get N points that would be high value to label:
```python
N = 10
indices_to_label = single_model_active_learning(df, model_wrapper, N)
```

This will give us the indices of the original dataframe that are high value to label.

We also expose some functionality to do this utilizing two models. This can be useful if you have two versions of a model (either trained over the same dataset or different slices). If we have a second container (`container_2`) we can then do:

```python
model_wrapper_2 = container_2.model.base_model
indices_to_label = two_model_active_learning(df, model_wrapper, model_wrapper_2, N)
```

This, like the previous function, will return some indices that are high value to label.

Note that for both these algorithms there is some randomness involved, and if you want to get deterministic results make sure to pass the `seed` parameter.
