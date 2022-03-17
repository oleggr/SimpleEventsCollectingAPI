from fastapi.testclient import TestClient


def test_successful_couriers_post(client: TestClient):
    response = client.get('/api/hello')
    assert response.status_code == 200
    assert response.json() == 'Hello, world!'
