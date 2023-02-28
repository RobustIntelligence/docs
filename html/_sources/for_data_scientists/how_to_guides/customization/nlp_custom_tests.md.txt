# NLP Generic Custom Tests

{{ custom_tests_intro }}
This Python file should expose a class named CustomBatchRunner, which should inherit from the TestBatchRunner interface that RIME defines.
After inheriting from this class you will need to implement 6 methods:
1. `_from_config`: this is a class method that takes in a RunContainer and a config and returns the CustomBatchRunner initialized with a list of TestCases (see below for information on what a test is).
2. `table_columns_to_show`: this property is responsible for telling the UI which columns to show in the test case table.
3. `description`: a property with a description of the test, only used in the UI.
4. `long_description`: a property with a long description of the test, only used in the UI.
5. `type`: a property with the type of the test, only used in the UI.

As mentioned above, this CustomBatchRunner will contain multiple TestCases.
These are a collection of test cases that will be aggregated inside the overall batch runner. 
As an example of this, if you write a specific test that you want to apply to each column in the dataset, it would make sense to have the BatchRunner be initialized with a list of tests, one for each feature.

The test cases that you define should inherit from the BaseTest class that RIME defines.
After inheriting from this class you will need to implement one method:
1. `run`: this method takes in a UnstructuredRunContainer and returns a TestOutput (the result of the test) and a dictionary of extra info (that can be used when aggregating test results in the BatchRunner)

An example of a custom test file is below:

```python
"""Test batch runner for custom tests."""

from typing import List, Tuple

from rime.core.schema import (
    CustomConfig,
    ImportanceLevel,
    Status,
    TableColumn,
    TestCategory,
    TestOutput,
)
from rime.core.test import BaseTest
from rime.nlp.model_tests.batch_runner import TestBatchRunner
from rime.nlp.run_container import RunContainer


class CustomTest(BaseTest):
    def __init__(self, delta: int = 0):
        """Initialize with a delta between n_rows ref and eval."""
        super().__init__()
        self.delta = delta

    def run(self, run_container: RunContainer, silent_errors: bool = False) -> Tuple[TestOutput, dict]:
        ref_count = len(run_container.ref_data_container.data)
        eval_count = len(run_container.eval_data_container.data)
        if ref_count > eval_count + self.delta:
            status = Status.WARNING
            severity = ImportanceLevel.HIGH
        else:
            status = Status.PASS
            severity = ImportanceLevel.NONE
        table_info_dict = {
            "Severity": severity,
            "Info": "Compare size of datasets",
            "Key Detail": f"Size of reference data: {ref_count}",
        }
        test_output = TestOutput(self.id, status, table_info_dict, severity, [],)
        return test_output, {}


class CustomBatchRunner(TestBatchRunner):
    """TestBatchRunner for the CustomTest."""

    @classmethod
    def _from_config(
        cls, run_container: RunContainer, config: CustomConfig
    ) -> "CustomBatchRunner":
        if config.params is None:
            delta = 0
        else:
            delta = config.params["delta"]
        return cls([CustomTest(delta=delta)])

    @property
    def table_columns_to_show(self) -> List[TableColumn]:
        """Return the types of info to show in the test case table."""
        return [TableColumn(name) for name in ["Info", "Severity", "Key Detail"]]

    @property
    def description(self) -> str:
        return "This is custom test"

    @property
    def long_description(self) -> str:
        return "This is a long description of a custom test."

    @property
    def type(self) -> str:
        return "customer custom test"

```