from fastapi import status


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


def test_get_user_by_id(client):
    data = {
        "nombre": "user_name",
        "apellido": "user_last_name",
        "email": "testuser@example.com",
        "password": "testing",
        "is_active": False
    }

    response = client.post("/users/", json=data)
    response = client.get("/users/1/")
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"


def test_get_all_usuers(client):
    #Tenemos que tomar dos ya que no pueden tener el mismo correo
    first_data = {
        "nombre": "María",
        "apellido": "Gutiérrez",
        "email": "maria.gutierrez@example.com",
        "password": "Pa$$w0rd!",
        "is_active": True
    }

    second_data = {
        "nombre": "Juan",
        "apellido": "Pérez",
        "email": "juan.perez@example.com",
        "password": "MiP@ssw0rd",
        "is_active": True
    }

    client.post("/users/", json=first_data)
    client.post("/users/", json=second_data)

    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_user(client):
    data = {
        "nombre": "user_name",
        "apellido": "user_last_name",
        "email": "testuser@example.com",
        "password": "testing",
        "is_active": False,
        "rol": 1,
        "contrato": 1
    }

    response_client_set = client.post("/users/", json=data)

    new_data = {
        "nombre": "John",
        "apellido": "Doe",
        "email": "user@example.com",
        "is_active": True,
        "rol": 2
    }

    response = client.put("/users/1", json=new_data)

    assert response.json()["is_active"] != response_client_set.json(
    )["is_active"]


def test_delete_user_by_id(client):
    data = {
        "nombre": "user_name",
        "apellido": "user_last_name",
        "email": "testuser@example.com",
        "password": "testing",
        "is_active": False
    }

    client.post("/users/", json=data)

    response = client.delete("/users/1/")

    assert response.status_code == 204


#Revisar 

# def test_delete_user_by_email(client):
#     data = {
#         "nombre": "user_name",
#         "apellido": "user_last_name",
#         "email": "testuser@example.com",
#         "password": "testing",
#         "is_active": False
#     }

#     client.post("/users/", json=data)

#     response = client.delete("/users/testuser@example.com/")

#     assert response.status_code == 204
