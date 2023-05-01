# Robust Intelligence Demo Notebooks

This folder contains a directory of all the notebooks used for RI demos, as well as tests for the notebooks.

## Demo Notebooks

## Testing Notebooks

Whenever a new notebook is added, please add a corresponding test to `tests/test_notebooks.py`. These unit tests
go through every demo notebook in this folder and checks that there are no errors executing the notebooks,
when provided a `--cluster-url` and `--api-key`.

Example Usage:
`pytest -o log_cli=true -s tests/test_notebooks.py --cluster-url rime.staging.rime.dev --api-key <API_KEY> --verbose`

This will run the tests while also logging the cells being executed.

**Important Note**: By default, the notebooks will pip install the latest public version of `rime-sdk`.
If you wish to the latest version (e.g. the latest release cut `0.17.0rc9`), you will manually need to
set `rime-sdk==<version>` in the pip install command.
