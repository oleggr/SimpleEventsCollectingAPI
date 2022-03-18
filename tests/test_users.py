from fastapi import status
from fastapi.testclient import TestClient


def test_successful_add_user(client: TestClient, drop_db_file):
    user_json = {
        "balance": 100.0,
        "creation_date": "2010-12-01",
        "age": 10,
        "city": "Moscow",
        "tariff": 1
    }
    response = client.post('/api/add/user', json=user_json)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"user id": 1}


def test_successful_get_user(client: TestClient):
    user_json = {
        "id": 1,
        "balance": 100.0,
        "creation_date": "2010-12-01",
        "age": 10,
        "city": "Moscow",
        "tariff": 1
    }
    response = client.get('/api/get/user/1')
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    del response_json['last_activity']
    assert response_json == user_json


update_json = {
    "balance": 250.0,
    "age": 15,
}

updated_user_json = {
    "id": 1,
    "balance": 250.0,
    "creation_date": "2010-12-01",
    "age": 15,
    "city": "Moscow",
    "tariff": 1
}


def test_successful_update_user(client: TestClient):
    response = client.patch('/api/update/user/1', json=update_json)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == 'User successfully updated'

    response = client.get('/api/get/user/1')
    response_json = response.json()
    del response_json['last_activity']
    assert response_json == updated_user_json


def test_unsuccessful_update_user(client: TestClient):
    response = client.patch('/api/update/user/55', json=update_json)
    assert response.status_code == status.HTTP_304_NOT_MODIFIED
    assert response.json() == 'User was not updated'


def test_delete_user(client: TestClient):
    response = client.delete('/api/delete/user/1')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == 'User successfully deleted'

    response = client.get('/api/get/user/1')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == 'User not exist'
