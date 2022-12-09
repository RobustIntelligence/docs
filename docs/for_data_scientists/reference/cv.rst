.. _cv_configuration:


CV Configuration
================================

RIME is very easy to run on your own CV data and model. The below references cover how to configure various components of RIME to run on any data and model.


RIME Configuration
--------------------------------
Configure the different RIME products to work with your model and data.

.. toctree::
   :maxdepth: 1

   cv/stress_testing.md
   cv/firewall_continuous_tests.md

Fine-tune the specifications for your inputs to RIME.

.. toctree::
   :maxdepth: 1

   cv/data_source.md
   cv/model_source.md
   cv/prediction_info.md
   cv/task_data_format.md
   cv/task_prediction_cache_format.md
   cv/specify_model_cv.md
   cv/specify_image_loading.md

Profiling Configuration
--------------------------------
Configure how RIME statistically analyzes your model and data. These configurations
are optional; RIME will automatically infer the profiling parameters if no
configuration is specified.

.. toctree::
   :maxdepth: 1

   cv/data_profiling.md

Tests Configuration
--------------------------------
Configure the tests that RIME runs. These configurations are optional; RIME will infer
the relevant tests and tune them automatically if no configuration is specified.

.. toctree::
   :maxdepth: 1

   cv/test_suite.rst
