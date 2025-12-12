import pytest

@pytest.fixture
def url_base():
    url = "https://reqres.in/api/users"
    return url

@pytest.fixture
def header_base():
    header = {"x-api-key": "reqres_b051f5730fb6412998dc75c3079ddb08"}
    return header