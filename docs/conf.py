# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Markdown setup --------------------------------------------------------------

source_parsers = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

source_suffix = [".rst", ".md"]

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.abspath("../python/rime/"))
sys.path.insert(0, os.path.abspath("../python/external/"))


# -- Project information -----------------------------------------------------

project = "RIME"
copyright = "2022, Robust Intelligence"
author = "Robust Intelligence"

# This can be overriden with the -D in the Makefile
with open('../version.txt', 'r') as f:
    version = f.readline().strip('\n')

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.githubpages",
    "sphinx_markdown_tables",
    "sphinx.ext.napoleon",
    'sphinx_copybutton',
]

myst_enable_extensions = [
    'substitution',
]

autodoc_member_order = 'bysource'

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["README.md"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    'includehidden': False,
    'display_version': True,
}

html_context = {
    "display_github": False,  # Do not show 'Edit on GitHub'
    "commit": False,
}

html_show_sphinx = False
myst_heading_anchors = 4
# TODO: Fix the non-consecutive header level in our docs, until then
# disable the sphinx/myst warnings
suppress_warnings = ["myst.header"]

def setup(app):
    return

# -- Shared Substitutions ----------------------------------------------------

# See https://myst-parser.readthedocs.io/en/latest/syitax/optional.html#syntax-substitutions

tabular_ui_redirect = (
    "After this finishes running, you should be able to see the results in "
    "the web client,\nwhere they will be uploaded to the Default Project."
)

nlp_ui_redirect = (
    "After this finishes running, you should be able to see the results in "
    "the web client,\nwhere they will be uploaded to the Default Project."
)

tabular_config_note = (
    "For a full reference on the configuration file see the [Tabular "
    "Configuration Reference](/for_data_scientists/reference/tabular/stress_testing.md)."
)

nlp_config_note = (
    "For a full reference on the configuration file see the [NLP "
    "Configuration Reference](/for_data_scientists/reference/nlp/stress_testing.md)."
)

cv_config_note = (
    "For a full reference on the configuration file see the [CV "
    "Configuration Reference](/for_data_scientists/reference/cv/stress_testing.md)."
)

cli_note = (
    "For additional command line options, please see the [CLI Reference]"
    "(/local_trial/reference/cli.md)."
)

rime_library_setup_note = (
    "Be sure to complete the initial setup described in [RIME Data and Model "
    "Setup](rime_data_model_setup.md) before proceeding."
)

nlp_setup_extra_note = (
    "Please ensure that the extra RIME NLP dependencies have been installed "
    "from the `nlp_requirements.txt` file from [installation]"
    "(/local_trial/get_started/installation.md).\nIf you run into a "
    "`ModuleNotFoundError` at any point during this walkthrough, it is likely "
    "that you need to install the RIME NLP Extras!\n"
    "```bash\npip install -r nlp_requirements.txt\n```"
)

cv_setup_extra_note = (
    "Please ensure that the extra RIME CV dependencies have been installed "
    "from the `cv_requirements.txt` file from [installation]"
    "(/local_trial/get_started/installation.md).\nIf you run into a "
    "`ModuleNotFoundError` at any point during this walkthrough, it is likely "
    "that you need to install the RIME CV Extras!\n"
    "```bash\npip install -r cv_requirements.txt\n```"
)

fw_realtime_overview = (
    "1. Run AI Stress Testing\n"
    "2. Review and Download Auto-Configured AI Firewall Rules\n"
    "3. Setup a Firewall Client in a Jupyter Notebook\n"
    "4. Monitor Events\n"
)

fw_rules_review = (
    "AI Firewall Realtime is configured from a JSON configuration file (`rules.json`).\n"
    "This configuration is auto-generated based on the model and datasets that you provided\n"
    "to run AI Stress Testing.\n To view and download the JSON configuration file, click on "
    "\"Protect your model\".\n\n**At this step, copy the Firewall ID and download the "
    "`rules.json` files --- you will need them for later steps in this walkthrough.**\n\n"
    "Once downloaded, place `rules.json` in your `rime_trial/` folder"
)

fw_code_example = (
    "We provide an example to wrap your inference code with the Firewall code. The\n"
    "Firewall endpoint allows for incoming events to be monitored in the app.\n\n"
    "You will also see a field called \"Firewall Key\" on the configuration page.\n\n"
    "Keep this key in mind; we will be using it when we incorporate the firewall\n"
    "into the model inference code."
)

fw_notebook_setup = (
    "Within the tutorial directory, we'll want to open up a Jupyter notebook.\n"
    "```\n"
    "pip install notebook\n"
    "pip install ipykernel\n"
    "python -m ipykernel install --user --name=rime-venv\n"
    "jupyter notebook\n"
    "```\n\n"
    "When creating a new notebook, be sure to use the `rime-venv` kernel as opposed\n"
    "to the default `Python 3` kernel!"
)

sdk_client_setup = (
    "To begin, initialize the `Client` and point it to the location of your RIME backend.\n"
    "```python\n"
    "from rime_sdk import Client, ImageType\n"
    "\n"
    "rime_client = Client(\"rime.<YOUR_ORG_NAME>.rime.dev\", \"<YOUR_API_TOKEN>\")\n"
    "```"
)

rime_data_format_check_redirect = (
    "The Python SDK exposes a command-line utility that can **automatically validate** your input data:\n"
    "```bash\n"
    "rime-data-format-check <ARGS>\n\n\n"
    "Inspecting <REFERENCE_SET>\nDone!\n\n"
    "Inspecting <EVALUATION_SET>\nDone!\n\n"
    "\n---\n\n\n"
    "Your data should work with RIME!\n"
    "```\n"
    "**Instructions are available [here](/for_data_scientists/how_to_guides/troubleshooting/rime_data_format_check.md).**\n"
)

# TODO decide whether this is worth keeping and reusing
stress_test_bio = (
    "An **AI Stress Test** is a statistical evaluation of a machine learning "
    "model, designed to detect a specific vulnerability. At Robust "
    "Intelligence, we are constantly researching new vulnerabilities "
    "to test.\n\nFor a full list of available stress tests, see our "
    "[Test Bank](/for_data_scientists/explanation.rst)."
)

troubleshooting_local_installation_redirect = (
    "If you run into issues, please refer to our "
    "[Troubleshooting](/local_trial/how_to_guides/troubleshooting/installation.md) "
    "page for help! Additionally, your RI representative will be happy to assist "
    "--- feel free to reach out!"
)

troubleshooting_python_package_redirect = (
    "If you run into issues, please refer to our "
    "[Troubleshooting](/local_trial/how_to_guides/troubleshooting/python_package.md) "
    "page for help! Additionally, your RI representative will be happy to assist "
    "--- feel free to reach out!"
)

troubleshooting_python_sdk_redirect = (
    "If you run into issues, please refer to our "
    "[Troubleshooting](/for_data_scientists/how_to_guides/troubleshooting/sdk.md) "
    "page for help! Additionally, your RI representative will be happy to assist "
    "--- feel free to reach out!"
)

troubleshooting_admin_installation_redirect = (
    "If you run into issues, please refer to our "
    "[Troubleshooting](/for_admins/how_to_guides/troubleshooting/installation.md) "
    "page for help! Additionally, your RI representative will be happy to assist "
    "--- feel free to reach out!"
)

fw_how_to_intro = (
    "This guide will cover how to configure the AI Firewall to protect your model "
    "from \"bad\" input data in near-real time.\n\nSimilar to the AI Firewall "
    "Continuous Tests, AI Firewall for Realtime Events is automatically trained "
    "from an AI Stress Testing run."
)

fw_how_to_deploy_step = (
    "Next, click on \"Deploy AI Firewall\" and fill out the details. The step is "
    "the same as step 3 in the Firewall Continuous Tests tutorial. The AI "
    "Firewall you create can be used to monitor (Continuous Tests) or protect "
    "(Realtime Events) your model."
)

custom_tests_intro = (
    "With RIME, it is easy to specify custom tests. The below steps walk through how to "
    "do so. If you run into any difficulties, please contact your Robust Intelligence "
    "support engineer and they will assist you.\n\n First, you must define a custom test "
    "in a Python file. "
)

myst_substitutions = {
    "tabular_ui_redirect": tabular_ui_redirect,
    "nlp_ui_redirect": nlp_ui_redirect,
    "tabular_config_note": tabular_config_note,
    "nlp_config_note": nlp_config_note,
    "cv_config_note": cv_config_note,
    "cli_note": cli_note,
    "custom_tests_intro": custom_tests_intro,
    "rime_library_setup_note": rime_library_setup_note,
    "nlp_setup_extra_note": nlp_setup_extra_note,
    "cv_setup_extra_note": cv_setup_extra_note,
    "fw_realtime_overview": fw_realtime_overview,
    "fw_rules_review": fw_rules_review,
    "fw_code_example": fw_code_example,
    "fw_notebook_setup": fw_notebook_setup,
    "sdk_client_setup": sdk_client_setup,
    "rime_data_format_check_redirect": rime_data_format_check_redirect,
    "stress_test_bio": stress_test_bio,
    "troubleshooting_local_installation_redirect": troubleshooting_local_installation_redirect,
    "troubleshooting_python_package_redirect": troubleshooting_python_package_redirect,
    "troubleshooting_python_sdk_redirect": troubleshooting_python_sdk_redirect,
    "troubleshooting_admin_installation_redirect": troubleshooting_admin_installation_redirect,
    "fw_how_to_intro": fw_how_to_intro,
    "fw_how_to_deploy_step": fw_how_to_deploy_step
}
