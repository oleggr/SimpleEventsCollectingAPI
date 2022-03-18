import pytest
from fastapi import status
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def custom_local_user(client: TestClient):
    user_json = {
        "balance": 100.0,
        "creation_date": "2010-12-01",
        "age": 10,
        "city": "Moscow",
        "tariff": 1
    }
    response = client.post('/api/add/user', json=user_json)
    return response.json()['user id']


def test_successful_add_event(client: TestClient, custom_local_user):
    event_json = {
        "time": "2021-12-12",
        "id_user": custom_local_user,
        "service_type": 1,
        "volume": 100,
    }
    response = client.post('/api/add/event', json=event_json)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"event id": 1}


def test_unsuccessful_add_event(client: TestClient):
    event_json = {
        "time": "2021-12-12",
        "id_user": 123,
        "service_type": 1,
        "volume": 100,
    }
    response = client.post('/api/add/event', json=event_json)
    assert response.json() == 'Event was not recorded'


def test_successful_get_event(client: TestClient, custom_local_user):
    event_json = {
        "id": 1,
        "id_user": custom_local_user,
        "time": "2021-12-12",
        "service_type": 1,
        "volume": 100,
    }
    response = client.get('/api/get/event/1')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == event_json


update_json = {
    "volume": 250,
}

updated_event_json = {
    "id": 1,
    "time": "2021-12-12",
    "id_user": 1,
    "service_type": 1,
    "volume": 250,
}


def test_successful_update_event(client: TestClient):
    response = client.patch('/api/update/event/1', json=update_json)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == 'Event successfully updated'

    response = client.get('/api/get/event/1')
    assert response.json() == updated_event_json


def test_unsuccessful_update_event(client: TestClient):
    response = client.patch('/api/update/event/123', json=update_json)
    assert response.status_code == status.HTTP_304_NOT_MODIFIED
    assert response.json() == 'Event was not updated'


def test_delete_event(client: TestClient):
    response = client.delete('/api/delete/event/1')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == 'Event successfully deleted'

    response = client.get('/api/get/event/1')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == 'Event not exist'
