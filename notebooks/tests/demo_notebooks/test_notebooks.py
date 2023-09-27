"""Testing for demo notebooks."""
import glob
import logging
import re
from pathlib import Path
from typing import List, Optional

import pytest
from testbook import testbook
from testbook.client import TestbookNotebookClient

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

API_TOKEN_REGEX = r"API_TOKEN\s*=\s*['\"]{2}"
CLUSTER_URL_REGEX = r"CLUSTER_URL\s*=\s*['\"]{2}"
AWS_INTEGRATION_ID_REGEX = r"AWS_INTEGRATION_ID\s*=\s*['\"]{2}"
AGENT_ID_REGEX = r"AGENT_ID\s*=\s*['\"]{2}"


def _fmt_long_string(s: str, max_len: int = 100) -> str:
    """Helper function for formatting a long string."""
    return s[:max_len] + "..."


def _contains_token(cell_source: str) -> bool:
    """Check if source contains the token and/or url."""
    return (
        re.search(API_TOKEN_REGEX, cell_source) is not None
        and re.search(CLUSTER_URL_REGEX, cell_source) is not None
    )


def _contains_sdk_install(cell_source: str) -> bool:
    """Check if source contains the rime_sdk pip install command."""
    return (
        "!pip install rime-sdk" in cell_source or "%pip install rime-sdk" in cell_source
    )


def run_notebook(
    tb: TestbookNotebookClient,
    api_key: str,
    cluster_url: str,
    aws_integration_id: str,
    agent_id: Optional[str],
    sdk_version: Optional[str],
) -> None:
    """Run through cells in notebook, inserting special fields.

    Specifically, find api_token and cluster_url fields, and insert
    our own values.

    """
    cell_dicts: List[dict] = tb.cells
    # NOTE: go through each cell, execute.
    # except when API_TOKEN/CLUSTER_URL is found.
    for idx, cell_dict in enumerate(cell_dicts):
        source = cell_dict["source"]
        contains_token = _contains_token(source)
        contains_sdk_install = _contains_sdk_install(source)
        # NOTE: assume api_token and rime_sdk are specified in separate cells for now
        if contains_token and contains_sdk_install:
            raise ValueError(
                "Cannot contain both api_token/cluster_url specification "
                "and pip install rime_sdk in same cell."
            )
        if contains_token:
            source = re.sub(CLUSTER_URL_REGEX, f"CLUSTER_URL = '{cluster_url}'", source)
            source = re.sub(API_TOKEN_REGEX, f"API_TOKEN = '{api_key}'", source)
            source = re.sub(AWS_INTEGRATION_ID_REGEX, f"AWS_INTEGRATION_ID = '{aws_integration_id}'", source)
            if agent_id:
                source = re.sub(AGENT_ID_REGEX, f"AGENT_ID = '{agent_id}'", source)
            # inject and execute new code
            logger.info(
                f"Running cell with API_TOKEN/CLUSTER_URL replaced: {_fmt_long_string(source)}"
            )
            tb.inject(source, pop=True)
        elif contains_sdk_install and sdk_version is not None:
            source = source.replace("rime-sdk", f"rime-sdk=={sdk_version}")
            # inject and execute new code
            logger.info(
                f"Running cell with new SDK version: {_fmt_long_string(source)}"
            )
            tb.inject(source, pop=True)
        else:
            # run cell normally
            logger.info(f"Running cell: {_fmt_long_string(source)}")
            tb.execute_cell(idx)


def test_notebook(
    nb_path: str, api_key: str, cluster_url: str, aws_integration_id: str, agent_id: Optional[str], sdk_version: Optional[str],
):
    """Test demo notebook."""
    with testbook(nb_path, execute=False, timeout=None) as tb:
        run_notebook(tb, api_key, cluster_url, aws_integration_id, agent_id, sdk_version)
