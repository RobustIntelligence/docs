# Tabular Custom Abnormal Inputs Test

{{ custom_tests_intro }}
This Python file should expose a class named ``CustomAbnormalInputsBatchRunner``, which should inherit from the ``AbstractCustomAbnormalInputsBatchRunner`` interface that RIME defines.
After inheriting from this class you will need to implement 2 methods:
1. `batch_test_name`: this is a property that should be unique for each test.
Name collisions with existing tests will cause errors.
2. `abnormal_inputs_criteria`: this is a class method that takes in your reference and evaluation dataframes and outputs a `pd.Series` object with boolean values, indicating for each row in the `evaluation_set` whether the input is abnormal.
Your implementation can also take in additional arguments that you pass in through the `params` dictionary in your config.

```python
"""Simple custom abnormal inputs test example."""
import numpy as np
import pandas as pd

from rime.tabular.data_tests.custom.abnormal_inputs import (
    AbstractCustomAbnormalInputsBatchRunner,
)


class CustomAbnormalInputsBatchRunner(AbstractCustomAbnormalInputsBatchRunner):
    """This is a simple example custom abnormal inputs test.

    This example custom abnormal inputs test returns true for all rows in the eval set
    whose numerical value for any column is outside the range of the reference set
    for the specified column.
    You must implement `abnormal_input_criteria` and `batch_test_name` for this test to
    work.
    """

    @classmethod
    def abnormal_inputs_criteria(
        cls, ref_set: pd.DataFrame, eval_set: pd.DataFrame
    ) -> pd.Series:
        """Return booleans `pd.Series` with same length as `eval_set`."""
        # get columns with only numerical values
        column_flags = ref_set.apply(
            lambda s: pd.to_numeric(s, errors="coerce").notnull().all()
        )
        result = pd.Series(np.zeros(len(eval_set), dtype=bool))
        for i, column in enumerate(ref_set.columns):
            if column_flags[i]:
                below_threshold = eval_set[column] < ref_set[column].min()
                above_threshold = eval_set[column] > ref_set[column].max()
                failing_rows = below_threshold | above_threshold
                result |= failing_rows

        return result

    @property
    def batch_test_name(self) -> str:
        """Return name of test."""
        return "Simple Custom Outside Range"


```
There are also several optional methods whose implementation you can override depending on your needs.
1. `get_batch_args`: this is a class method that takes in your reference and evaluation dataframes and returns a list of key-word arguments to each run of your test.
You should implement this logic if you want to run the same `abnormal_inputs_criteria` over several tests but with different arguments.
`column_names` is a required key in each dictionary with corresponding value of a list of the column names that this test uses, and this value is used by RIME to help flag features for you.
All other arguments are passed to your implementation of `abnormal_inputs_crtieria`.
Your arguments should avoid name collisions with the keys in the `params` dictionary of your config.
2. `description`: this is a property that should return a short description of your test as a string.
3. `starter_string`: this is a property that should return a longer description of your test as a string.
4. `why_string`: this is a property that should return a string that explains why this test is useful.
5. `configuration_string`: this is a property that should return a string describing the configuration of the test.
6. `example_string`: this is a property that should return a string that gives an example of the use-case of this test.

Each of the strings can be formatted with HTML. The `starter_string`, `why_string`, `configuration_string`, an `example_stirng` properties are displayed in the "ⓘ More" pop-up.
```python
"""Advanced custom abnormal inputs test example."""
from typing import List

import pandas as pd

from rime.tabular.data_tests.custom.abnormal_inputs import (
    AbstractCustomAbnormalInputsBatchRunner,
)


class CustomAbnormalInputsBatchRunner(AbstractCustomAbnormalInputsBatchRunner):
    """This is an advanced example custom abnormal inputs test.

    This example custom abnormal inputs test runs a batch of tests where each test
    checks the evaluation data for numerical values that are outside the range of the
    In addition to the methods required by the simple example, you need to implement
    `get_batch_args`. Other functions are optional but helpful for
     interpreting the results from RIME.
    """

    @classmethod
    def abnormal_inputs_criteria(
        cls, ref_set: pd.DataFrame, eval_set: pd.DataFrame, column: str
    ) -> pd.Series:
        """Return booleans `pd.Series` with same length as `eval_set`."""
        min_val = ref_set[column].min()
        max_val = ref_set[column].max()
        return (eval_set[column] < min_val) | (eval_set[column] > max_val)

    @property
    def batch_test_name(self) -> str:
        """Return name of test."""
        return "Advanced Custom Outside Range"

    @classmethod
    def get_batch_args(
        cls, ref_set: pd.DataFrame, eval_set: pd.DataFrame
    ) -> List[dict]:
        """Return a list of kwargs to pass to each test.

        The `column_names` key is required and expects a list of column names that this
        test uses. All other kwargs are passed to `abnormal_inputs_criteria`.
        """
        column_flags = ref_set.apply(
            lambda s: pd.to_numeric(s, errors="coerce").notnull().all()
        )
        batch_args = []
        for i, column in enumerate(ref_set.columns):
            if column_flags[i]:
                batch_args.append({"column_names": [column], "column": column})
        return batch_args

    @property
    def description(self) -> str:
        """Return one sentence description of the test."""
        description = (
            "This test checks that the numeric features of the data points of the eval "
            "set are in the range of the numeric features of the data points of the "
            "reference set."
        )
        return description
```
