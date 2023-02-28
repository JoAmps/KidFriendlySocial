import pytest
from main import server


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
    response = client.post('/register')
    assert response.status_code == 200


def test_login_endpoint(client):
    response = client.get('/login')
    assert response.status_code == 200


def test_any_other_endpoint_not_work(client):
    response = client.get('/predict')
    assert response.status_code != 200


def test_inference_endpoint(client):
    response = client.get('/inference')
    assert response.status_code == 200
