.. _custom_tests:

Custom Tests
================================

In order to use the custom test functionality, you first need to define the custom test. This should be
exposed in a Python file.
We recommend using the custom tests from the pre-defined categories over the generic
custom tests whenever possible.
The structure of this file depends on the type of custom test you are writing
Please see below for detailed descriptions of each type of custom test.

.. toctree::
   :maxdepth: 1

   tabular_custom_tests.md
   tabular_custom_abnormal_inputs_tests.md
   nlp_custom_tests.md

Once this python file exists, you must make it accessible to the RIME server.
For example, you may have some internal way of managing RIME storage, or you might upload it through the SDK:

.. code-block:: python

    upload_path = client.upload_file("local/path/to/custom_test_file.py")

Then you should include the path in the test configuration for a given run.
This is done with the ``custom_tests`` key within either the ``tests_config_path`` or ``tests_config``.
Each custom test config should also specify a ``custom_test_type`` key, which should be one of ``GENERIC`` or ``ABNORMAL_INPUTS``
(defaults to ``GENERIC``).
In addition, you can optionally specify a ``custom_test_category`` key which will control which category the
custom test shows up under. If you do not specify anything, a default will be used based on the ``custom_test_type``
you provide.

Here is an example config:

.. code-block:: python

    "tests_config": {
        "custom_tests": [
            {
                "test_path": upload_path,
                "custom_test_category":  "Example Test Category 1"
            },
            {
                "custom_test_type": "ABNORMAL_INPUTS",
                "test_path": "s3://rime-blob-storage-bucket/path/to/custom_abnormal_inputs_test.py",
                "params": {
                    "arg_1": 5,
                    "arg_2": "example_argument_string"
                },
                "custom_test_category": "Example Test Category 2"
            }
        ]
    }
