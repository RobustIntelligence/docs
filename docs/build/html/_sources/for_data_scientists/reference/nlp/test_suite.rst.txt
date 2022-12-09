.. _nlp_test_suite:

Tests Configuration
================================

Each NLP task supports its own unique set of RIME tests. To configure these tests, modify one of the example configurations provided in this guide and save it in a JSON file. Then, include the file's path in the ``tests_config_path`` property of the `RIME CLI config`_, or specify the config directly in the ``tests_config`` property. Below is an overview of the global configuration properties shared by all tasks, followed by links to each task's default testing suite.

.. _`RIME CLI config`: stress_testing.html#Arguments

Global Configuration Options
--------------------------------

- ``categories``: List, *default* = ``[]``

    Test categories to run. Options include `Abnormal Inputs`, `Adversarial`, `Data Cleanliness`, `Data Poisoning Detection`, `Drift`, `Model Performance`, `Subset Performance`, and `Transformations`.

- ``run_default``: Optional[bool], *default* = ``null``

    Whether to run default categories or not. Defaults to `True` if no `categories` are specified, `False` if any are. The default categories are `Data Cleanliness`, `Model Performance`, `Subset Performance`, and `Transformations`.

- ``global_sample_size``: int or ``null``, *default* = ``null``

   If an integer value is provided, override the ``sample_size`` argument for **all** tests requiring model inference at runtime (i.e., attacks and transformation tests).

- ``target_text_keys``: List[str] or ``null``, *default* = ``null``

   If a list of strings is provided, override the ``target_text_keys`` argument for **all** tests that perturb input text (i.e., attacks and transformation tests).

- ``metadata_tests``: Dict[str, dict] or ``null``, *default* = ``null``

   A dictionary of configuration tests to run. The keys are the names of the tests and the values are dictionaries of configuration options for the test. For instance, for a numeric metadata feature 'age', the following configuration would be valid for the distribution drift test:
   
      ``metadata_tests: {'age_distribution': {"drift_metrics": [{"distance_metric": "Population Stability Index","severity_threshold": [0.1,0.2,0.4]}}]}}``


Task-Specific Configuration Options
-----------------------------------

Below are detailed descriptions of the unique testing suite configurations for each supported NLP task.

.. toctree::
   :maxdepth: 2

   tasks_test_suite/named_entity_recognition.md
   tasks_test_suite/text_classification.md
   tasks_test_suite/natural_language_inference.md
