Input Data Format
=========================

## Automated Validation
{{ rime_data_format_check_redirect }}

---

## Supported File Formats

RIME Tabular currently supports both CSV (`.csv`) and [Parquet](https://parquet.apache.org/docs/file-format/) (`.parquet`), with task-specific nuances defined below. Input files should have header columns in string format --- these will be used as feature names.

RIME is most effective when both label and prediction column are provided; however, neither are required for most tasks\*.

## Requirements By Task

### Regression
- Labels should be any real number
- Predictions should be any real number

### Binary Classification
- Labels should be integer values 0 or 1
- Predictions should be float values (probabilities) between 0 and 1

### Multi-Class Classification
- Labels should be integers referring to class index
- Predictions should be an array summing to 1, with index **i** representing the probability of the **i**th class
- Predictions should be uploaded as a separate `.csv` or `.parquet` file, with columns corresponding to prediction classes

### Ranking
- \* **Labels are required**
- Labels should be any real number
- Predictions should be any real number
- `ranking_info` must be provided in the [data configuration](data_source.md)
