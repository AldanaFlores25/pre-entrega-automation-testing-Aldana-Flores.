import requests     # Librería para hacer solicitudes HTTP
import pytest       # Librería para ejecutar tests automatizados


@pytest.mark.api                 # Marcador para filtrar tests de API
def test_patch_users(url_base, header_request):
    
    # Construimos la URL del recurso a actualizar (usuario con ID 2)
    url = f"{url_base}/2"

    # Datos que queremos modificar en el usuario
    data = {"name": "Jose"}

    # Enviamos la solicitud PATCH con headers y JSON
    response = requests.patch(url, headers=header_request, json=data)

    # ======================================
    # VALIDACIONES
    # ======================================

    # 1. Validamos el status code esperado
    assert response.status_code == 200, \
        f"Se esperaba 200 pero se obtuvo {response.status_code}"

    # 2. Convertimos la respuesta a JSON para leer los datos
    body = response.json()

    # 3. Validamos que el nombre recibido sea el mismo que enviamos
    assert body["name"] == data["name"], \
        f"El nombre devuelto ({body['name']}) no coincide con el enviado ({data['name']})"
