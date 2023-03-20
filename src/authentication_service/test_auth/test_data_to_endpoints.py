import json
import pytest
import random
from api import server
import warnings
warnings.filterwarnings("ignore")


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


def test_registeration_new_user_succesfully_registered(client):
    random_numbers = random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)
    values = ''.join(map(str, random_numbers))
    email = f"user{values}@gmail.com"
    password = values
    headers = {"Content-Type": "application/json"}
    user = {"email": email, "password": password}
    response = client.post('/register', headers=headers, data=json.dumps(user))
    assert response.get_data(as_text=True) == 'You have successfully registered!'


def test_registeration_account_already_exists(client):
    headers = {"Content-Type": "application/json"}
    user = {"email": "user1@gmail.com ", "password": "user1"}
    response = client.post('/register', headers=headers, data=json.dumps(user))
    assert response.get_data(as_text=True) == "Account already exists!"


def test_registeration_incorrect_email_format(client):
    headers = {"Content-Type": "application/json"}
    user = {"email": "user1xys", "password": "user1"}
    response = client.post('/register', headers=headers, data=json.dumps(user))
    assert response.get_data(as_text=True) == 'Invalid email address!'
