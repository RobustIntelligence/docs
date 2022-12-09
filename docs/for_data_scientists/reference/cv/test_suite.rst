.. _cv_test_suite:

Tests Configuration
================================

Each CV task supports its own unique set of RIME tests. To configure these tests, modify one of the example configurations provided in this guide and save it in a JSON file. Then, include the file's path in the ``tests_config_path`` property of the `RIME CLI config`_. Below is an overview of the global configuration properties shared by all tasks, followed by links to each task's default testing suite.

.. _`RIME CLI config`: stress_testing.html#Arguments

Global Configuration Options
--------------------------------

- ``categories``: List, *default* = ``[]``

    Test categories to run. Options include `Abnormal Inputs`, `Adversarial`, `Data Cleanliness`, `Data Poisoning Detection`, `Drift`, `Model Performance`, `Subset Performance`, and `Transformations`.

- ``run_default``: Optional[bool], *default* = ``null``

    Whether to run default categories or not. Defaults to `True` if no `categories` are specified, `False` if any are. The default categories are `Data Cleanliness`, `Model Performance`, `Subset Performance`, and `Transformations`.

- ``global_sample_size``: int or ``null``, *default* = ``null``

   If an integer value is provided, override the ``sample_size`` argument for **all** tests requiring model inference at runtime (i.e., attacks and transformation tests).


Task-Specific Configuration Options
-----------------------------------

Below are detailed descriptions of the unique testing suite configurations for each supported CV task.

.. toctree::
   :maxdepth: 2

   tasks_test_suite/image_classification.md
   tasks_test_suite/object_detection.md
