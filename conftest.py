import pytest
from client.api_client import APIHandler


@pytest.fixture()
def api_handler():
    return APIHandler()



