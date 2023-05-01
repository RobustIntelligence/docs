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
        "--sdk-version",
        action="store",
        default=None,
        help="The api key providing authentication to RIME service. Required "
        "for external uploads.",
    )


@pytest.fixture
def cluster_url(request):
    return request.config.getoption("--cluster-url")


@pytest.fixture
def api_key(request):
    return request.config.getoption("--api-key")


@pytest.fixture
def sdk_version(request):
    return request.config.getoption("--sdk-version")
