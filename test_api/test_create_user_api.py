import pytest
import requests

BASE_URL = "https://reqres.in/api"


@pytest.mark.parametrize(
    "email, password, expected_status",
    [
        ("eve.holt@reqres.in", "cityslicka", 200),  # válido
        ("eve.holt@reqres.in", "", 400),            # email sin password
        ("", "cityslicka", 400),                    # password sin email
    ],
)
def test_login_api(email, password, expected_status):
    """
    Valida el endpoint de login de reqres.in
    """
    url = f"{BASE_URL}/login"
    payload = {"email": email, "password": password}

    response = requests.post(url, json=payload)
    assert response.status_code == expected_status, f"Se esperaba {expected_status}, se obtuvo {response.status_code}"

    if response.status_code == 200:
        data = response.json()
        assert "token" in data, "No se encontró el token en la respuesta"
        assert len(data["token"]) > 0, "El token está vacío"
