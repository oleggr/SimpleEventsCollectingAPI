from fastapi import status
from fastapi.testclient import TestClient


def test_successful_add_tariff(client: TestClient, drop_db_file):
    tariff_json = {
        "name": "Максимум",
        "start_date": "2021-11-15",
        "end_date": "2030-01-01",
        "minutes": 800,
        "sms": 500,
        "traffic": 16384,
    }
    response = client.post('/api/add/tariff', json=tariff_json)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"tariff id": 1}


def test_successful_get_tariff(client: TestClient):
    tariff_json = {
        "id": 1,
        "name": "Максимум",
        "start_date": "2021-11-15",
        "end_date": "2030-01-01",
        "minutes": 800,
        "sms": 500,
        "traffic": 16384,
    }
    response = client.get('/api/get/tariff/1')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == tariff_json


update_json = {
    "name": "БезПереплат",
    "minutes": 300,
    "sms": 150,
    "traffic": 1024,
}

updated_tariff_json = {
    "id": 1,
    "name": "БезПереплат",
    "start_date": "2021-11-15",
    "end_date": "2030-01-01",
    "minutes": 300,
    "sms": 150,
    "traffic": 1024,
}


def test_successful_update_tariff(client: TestClient):
    response = client.patch('/api/update/tariff/1', json=update_json)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == 'Tariff successfully updated'

    response = client.get('/api/get/tariff/1')
    assert response.json() == updated_tariff_json


def test_unsuccessful_update_tariff(client: TestClient):
    response = client.patch('/api/update/tariff/55', json=update_json)
    assert response.status_code == status.HTTP_304_NOT_MODIFIED
    assert response.json() == 'Tariff was not updated'


def test_delete_tariff(client: TestClient):
    response = client.delete('/api/delete/tariff/1')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == 'Tariff successfully deleted'

    response = client.get('/api/get/tariff/1')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == 'Tariff not exist'
