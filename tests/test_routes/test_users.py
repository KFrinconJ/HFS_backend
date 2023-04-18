import json


def test_create_user(client):
    data = {
        "nombre": "user_name",
        "apellido": "user_last_name",
        "email": "testuser@example.com",
        "password": "testing",
        "is_active": False
    }
    response = client.post("/users/", json=data)
    assert response.status_code == 200
    assert response.json()["nombre"] == "user_name"
    assert response.json()["apellido"] == "user_last_name"
    assert response.json()["email"] == "testuser@example.com"
    assert response.json()["is_active"] == False