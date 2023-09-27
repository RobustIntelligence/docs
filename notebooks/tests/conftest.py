"""Configuration for pytest."""

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cluster-url",
        action="store",
        help="Endpoint for RIME server",
        type=str,
    )
    parser.addoption(
        "--api-key",
        action="store",
        help="The api key providing authentication to RIME service. Required "
             "for external uploads.",
        type=str,
    )
    parser.addoption(
        "--aws-integration-id",
        action="store",
        help="The AWS integration ID, as registered on RIME. Needed to "
             "access AWS resources from the tests",
        type=str,
    )
    parser.addoption(
        "--agent-id",
        action="store",
        default=None,
        help="An agent ID to run the tests with."
             " If not provided will use the default agent",
        type=str,
    )
    parser.addoption(
        "--sdk-version",
        action="store",
        default=None,
        help="The api key providing authentication to RIME service. Required "
        "for external uploads.",
    )
    parser.addoption(
        "--nb-path",
        action="store",
        default=None,
        help="The path of the notebook to test. Required.",
    )


@pytest.fixture
def cluster_url(request):
    return request.config.getoption("--cluster-url")


@pytest.fixture
def api_key(request):
    return request.config.getoption("--api-key")


@pytest.fixture
def aws_integration_id(request):
    return request.config.getoption("--aws-integration-id")

@pytest.fixture
def agent_id(request):
    return request.config.getoption("--agent-id")


@pytest.fixture
def sdk_version(request):
    return request.config.getoption("--sdk-version")

@pytest.fixture
def nb_path(request):
    return request.config.getoption("--nb-path")
