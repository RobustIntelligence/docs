# Tabular Custom Generic Tests

{{ custom_tests_intro }}
This Python file should expose a class named CustomBatchRunner, which should inherit from the DataTestBatchRunner interface that RIME defines.
After inheriting from this class you will need to implement 6 methods:
1. `_from_config`: this is a class method that takes in a TabularRunContainer and a config and returns the CustomBatchRunner initialized with a list of TestCases (see below for information on what a test is).
2. `_outputs_to_batch_res`: this method is responsible for aggregating the results from the individual TestCases run into a TestBatch result.
3. `description`: a property with a description of the test, only used in the UI.
4. `long_description`: a property with a long description of the test, only used in the UI.
5. `type`: a property with the type of the test, only used in the UI.

As mentioned above, this CustomBatchRunner will contain multiple TestCases.
These are a collection of test cases that will be aggregated inside the overall batch runner. 
As an example of this, if you write a specific test that you want to apply to each column in the dataset, it would make sense to have the BatchRunner be initialized with a list of tests, one for each feature.

The test cases that you define should inherit from the BaseTest class that RIME defines.
After inheriting from this class you will need to implement one method:
1. `run`: this method takes in a TabularRunContainer and returns a TestOutput (the result of the test) and a dictionary of extra info (that can be used when aggregating test results in the BatchRunner)


An example of a custom test file is below:

```python
"""Custom test batch runner."""
from typing import List, Tuple

from rime.core.schema import (
    CustomConfig,
    ImportanceLevel,
    Status,
    TableColumn,
    TestBatchResult,
    TestOutput,
)
from rime.core.test import BaseTest
from rime.tabular.data_tests.batch_runner import DataTestBatchRunner
from rime.tabular.data_tests.schema.result import DataTestBatchResult, DataTestOutput
from rime.tabular.profiler.run_containers import TabularRunContainer


# Signature should not be changed.
class CustomTest(BaseTest):
    def __init__(self, delta: int = 0):
        """Initialize with a delta between n_rows ref and eval."""
        super().__init__()
        self.delta = delta

    # Signature should not be changed.
    def run(self, run_container: TabularRunContainer) -> Tuple[TestOutput, dict]:
        ref_data_size = len(run_container.ref_data.df)
        eval_data_size = len(run_container.eval_data.df)
        if ref_data_size > eval_data_size + self.delta:
            status = Status.WARNING
            severity = ImportanceLevel.HIGH
        else:
            status = Status.PASS
            severity = ImportanceLevel.NONE
        test_output = DataTestOutput(
            self.id, status, {"Severity": severity}, severity, [],
        )
        return test_output, {}


# Signature should not be changed.
class CustomBatchRunner(DataTestBatchRunner):
    """TestBatchRunner for the CustomTest."""

    # Signature should not be changed.
    @classmethod
    def _from_config(
        cls, run_container: TabularRunContainer,  config: CustomConfig, category: str
    ) -> "DataTestBatchRunner":
        if config.params is None:
            delta = 0
        else:
            delta = config.params["delta"]
        tests = [CustomTest(delta=delta)]
        return cls(tests, category)

    # Signature should not be changed.
    def _outputs_to_batch_res(
        self,
        run_container: TabularRunContainer,
        outputs: List[DataTestOutput],
        extra_infos: List[dict],
        duration: float,
        return_extra_infos: bool,
    ) -> TestBatchResult:
        long_description_tabs = [
            {"title": "Description", "contents": self.long_description},
            {"title": "Why it Matters", "contents": "Explain why this test matters."},
            {
                "title": "Configuration", 
                "contents": "Explain how this test is configured."
            },
            {
                "title": "Example", 
                "contents": "Include an example of how this test works."
            },
        ]
        return DataTestBatchResult(
            self.type,
            self.description,
            long_description_tabs,
            self.category,
            outputs,
            [],
            duration,
            extra_infos,
            [TableColumn("Severity")],
            outputs[0].severity,
            show_in_test_comparisons=False,
        )

    # Signature should not be changed.
    @property
    def description(self) -> str:
        return "This is custom test"

    # Signature should not be changed.
    @property
    def long_description(self) -> str:
        return "This is a long description of a custom test."

    # Signature should not be changed.
    @property
    def type(self) -> str:
        return "Example Custom Test"

```
