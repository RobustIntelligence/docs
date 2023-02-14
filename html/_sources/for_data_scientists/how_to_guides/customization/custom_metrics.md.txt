# Custom Metrics

This feature is currently in beta and is subject to change in an upcoming release.
In order to use the custom metrics functionality, you first need to create a python file that contains
the function used to calculate the custom metric. This function should be named `custom_metric_func`,
and the interface this function is expected to expose is below:

```python
"""Custom metric definition."""
from typing import Optional

import numpy as np
import pandas as pd


def custom_metric_func(
    df: Optional[pd.DataFrame],
    labels: Optional[pd.Series],
    preds: Optional[np.ndarray],
    preds_index: Optional[pd.Index],
    query_ids: Optional[pd.Series],
) -> Optional[float]:
    """Return a custom metric.
    Args:
        df: Optional pd.DataFrame of data, will be the full data.
        labels: Optional pd.Series of labels, if exists will have the same length
            as df.
        preds: Optional np.array of predictions, if exists may be a subset of the
            full df.
        preds_index: Optional pd.Index of predictions, if exists will have the same
            length as `preds`. Can be used to align the predictions with rows in the
            df.
        query_ids: Optional pd.Series of query ids, if exists will have the same
            length as `df`.
    Returns:
        an optional float corresponding to the metric to be tracked.
    """
```

The arguments passed to this function depend on the your configured data and task.
The function should return `None` whenever the provided arguments are insufficent, such as when labels are required but not available.

NOTE: for unstructured data (NLP/CV) the dataframe will contain information about user-defined metadata for
each datapoint and any profiled attributes. For tabular data, the dataframe will be the raw features.

After defining this function, you then need to specify it in the CLIConfig. The place to specify it is
in the `model_profiling_info` section. Specifically, it should look like:


```json
  "model_profiling_info": {
    "custom_metrics": {"NAME_OF_METRIC": "path/to/file.py"}
  },
```

Replace `NAME_OF_METRIC` with the name of the metric (this is how it will show up in the UI). Replace `path/to/file.py`
with the path to the python file you created in the above step.
