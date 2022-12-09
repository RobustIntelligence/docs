Specify a Custom NLP Dataloader
==========================

RIME supports custom data loading logic to be specified in a compatible Python file. This exposes functions to translate your custom dataset format into something supported by the Stress Testing framework and Firewall. To use this functionality, configure the [data_info](data_source) properties of the RIME JSON config by setting ``"type": "custom"`` and ``"load_path": "path/to/dataloader.py``. Within that dataloader file, the following functions are required:

- `get_ref_data() -> Iterable[dict]`: RIME calls this function to load the *reference* dataset into memory. 
    Each dictionary in the returned iterable represents a single data point containing the key-value pairs expected by the target NLP task. See the [data format requirements](task_data_format) for the task-specific input expectations.

- `get_eval_data() -> Iterable[dict]`: RIME calls this function to load the *evaluation/production* dataset into memory. 
    The data format should conform to that provided in `get_ref_data()`.


For example, assume your NLP data is stored as a table in a BigQuery database, 


```python
"""Logic to load datasets from a BigQuery database."""
from typing import Iterable
from google.cloud import bigquery

def _load_data_from_big_query_database(table_name: str) -> Iterable[dict]:
    """Return the RIME-formatted data from the specified table."""
    # Construct a BigQuery client object.
    client = bigquery.Client()
    # RIME Expects "text", "label", and "probabilities"
    # keys for the text classification task. Map from
    # the dataset columns to the RIME model input format
    col2rime_key_map = {
        "datetime": "timestamp",
        "transcript": "text",
        "ground_truth": "label",
        "probs": "probabilities",
    }

    # TODO: Set table_id to the fully-qualified table ID in standard
    # SQL format, including the project ID and dataset ID.
    table_id = f"my-nlp-data.project_id.{table_name}"

    rows = client.list_rows(table_id)
    for row in rows:
        yield {rime_key: row.get(key) for key, rime_key in col2rime_key_map.items()}


def get_ref_data() -> Iterable[dict]:
    """Fetch the reference set data from the database."""
    return _load_data_from_big_query_database("model_training_data")


def get_eval_data() -> Iterable[dict]:
    """Fetch the evaluation set data from the database."""
    return _load_data_from_big_query_database("production_test_data")
```