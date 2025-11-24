import requests      # Librería para realizar solicitudes HTTP como GET, POST, PUT, DELETE, etc.
import pytest        # Framework usado para ejecutar y organizar tests automatizados


@pytest.mark.api     # Marcador que permite ejecutar este test filtrándolo con "-m api"
def test_post_users(url_base, header_request):

    # La URL base para crear usuarios (por ejemplo: https://reqres.in/api/users)
    url = f"{url_base}"

    # Datos que queremos enviar en el cuerpo del POST
    payload = {
        "name": "Jose",
        "job": "Profesor"
    }

    # Realiza la solicitud HTTP POST enviando:
    # - la URL del endpoint
    # - headers (como la API Key si hiciera falta)
    # - el payload convertido automáticamente a JSON
    response = requests.post(url, headers=header_request, json=payload)

    # ================================================================
    # VALIDACIONES DEL TEST
    # ================================================================

    # 1) Validamos que el servidor responda con 201 (Created),
    # lo cual indica que el recurso se creó correctamente
    assert response.status_code == 201, \
        f"Se esperaba código 201 y se obtuvo {response.status_code}"

    # Convertimos la respuesta del servidor en un diccionario Python
    data = response.json()

    # 2) Validamos que el valor de 'name' recibido sea el mismo que enviamos
    assert data["name"] == payload["name"], \
        f"El nombre enviado ({payload['name']}) no coincide con la respuesta ({data['name']})"

    # 3) Validamos que el servidor haya generado un ID para el nuevo usuario
    assert "id" in data, \
        "La respuesta no contiene un 'id', por lo que no parece haberse creado el recurso correctamente"
