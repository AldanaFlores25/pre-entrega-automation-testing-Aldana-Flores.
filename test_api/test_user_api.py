import requests

BASE_URL = "https://reqres.in/api"


def test_users_api():
    """
    Valida que la respuesta de /api/users?page=1 contenga los campos esperados.
    """
    url = f"{BASE_URL}/users?page=1"
    response = requests.get(url)

    assert response.status_code == 200, f"Se esperaba 200, se obtuvo {response.status_code}"

    data = response.json()
    assert "data" in data, "No se encontró el campo 'data' en la respuesta"

    for user in data["data"]:
        for field in ["id", "email", "first_name", "last_name", "avatar"]:
            assert field in user, f"Falta el campo '{field}' en el usuario {user}"

        # Validar que el avatar termine en .jpg
        assert user["avatar"].endswith(".jpg"), f"El avatar no termina en .jpg: {user['avatar']}"
