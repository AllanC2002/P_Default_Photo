import pytest
from unittest.mock import patch, MagicMock
from main import app as flask_app

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client

@patch("services.functions.conection_mongo")
def test_assign_default_photo_success(mock_conection_mongo, client):
    mock_db = MagicMock()
    mock_conection_mongo.return_value = mock_db

    # Simulate that the default image exists in the database
    mock_db.Images.find_one.return_value = {"_id": "default_image_id", "name": "Default photo"}
    
    # Simulate that the update operation is successful
    mock_db.UserPhotos.update_one.return_value = None

    response = client.post("/default-photo", json={"Id_User": "user123"})
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Default photo assigned to user user123"
