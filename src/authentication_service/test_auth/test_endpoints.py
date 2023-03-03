import pytest
from api import server
import json


@pytest.fixture
def client():
    with server.test_client() as client:
        yield client


@pytest.fixture(scope='module')
def test_app():
    # Set up: start the app
    server.config['TESTING'] = True
    with server.test_client() as client:
        yield client
    # Teardown: stop the app
    print("Stopping the app")


def test_register_endpoint(client):
    headers = {"Content-Type": "application/json"}
    user = {"email": "user1@gmail.com ", "password": "user1"}
    response = client.post('/register', headers=headers, data=json.dumps(user))
    assert response.status_code == 200


def test_login_endpoint(client):
    headers = {"Content-Type": "application/json"}
    user = {"email": "user1@gmail.com ", "password": "user1"}
    response = client.post('/login', headers=headers, data=json.dumps(user))
    assert response.status_code == 200


def test_any_other_endpoint_not_work(client):
    response = client.get('/predict')
    assert response.status_code != 200
