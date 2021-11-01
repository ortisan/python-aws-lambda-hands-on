import pytest

from app import app

@pytest.fixture()
def event():
    return {
      "name": "Marcelo"
    }

def test_lambda_handler(event, mocker):
    ret = app.lambda_handler(event, "")
    assert ret == "Hello Marcelo"