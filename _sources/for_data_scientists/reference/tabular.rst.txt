.. _tabular_configuration:


Tabular Configuration
================================

RIME is very easy to run on your own data and model. The below references cover how to configure various components of RIME to run on any data and model.

RIME Configuration
--------------------------------
Configure the different RIME products to work with your model and data.

.. toctree::
   :maxdepth: 1

   tabular/stress_testing.md
   tabular/continuous_testing.rst

Fine-tune the specifications for your inputs to RIME.

.. toctree::
   :maxdepth: 1

   tabular/task_data_format.md
   tabular/data_source.md
   tabular/model_source.md
   tabular/specify_model.md

Profiling Configuration
--------------------------------
Configure how RIME statistically analyzes your model and data. These configurations
are optional; RIME will automatically infer the profiling parameters if no
configuration is specified.

.. toctree::
   :maxdepth: 1

   tabular/data_profiling.md
   tabular/model_profiling.md
   tabular/subset_profiling.md
   tabular/performance_limitations.md

Tests Configuration
--------------------------------
Configure the tests that RIME runs. These configurations are optional; RIME will infer
the relevant tests and tune them automatically if no configuration is specified.

.. toctree::
   :maxdepth: 1

   tabular/tests.md

