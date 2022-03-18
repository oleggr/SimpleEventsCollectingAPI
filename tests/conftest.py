import os
import pytest
from fastapi.testclient import TestClient

from app.app import app
from app.database.services.abstract import DBHandler


@pytest.fixture(scope="session")
def drop_db_file():
    """
    Drop DB for tests
    """
    os.remove(DBHandler.DB_FILENAME)
    DBHandler().create_tables()


@pytest.fixture(scope="session")
def client():
    """
    Create test client for FastAPI app
    """
    with TestClient(app) as client:
        yield client
