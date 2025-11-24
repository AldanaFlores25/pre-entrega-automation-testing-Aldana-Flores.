import requests     # Librería para hacer solicitudes HTTP: GET, POST, PUT, PATCH, DELETE
import time         # Para medir tiempos de ejecución
import pytest        # Framework para ejecutar y organizar los tests automatizados


@pytest.mark.api     # Marcador para poder ejecutar este test filtrando con: pytest -m api
def test_put_users(url_base, header_request):

    # Construimos la URL final, agregando el ID del usuario a modificar
    url = f"{url_base}/2"

    # Datos que actualizaremos del usuario
    data = {
        "name": "Valentina",
        "job": "Tutora"
    }

    # ----------------------------
    # MEDIR TIEMPO DE RESPUESTA
    # ----------------------------
    # Guardamos el tiempo antes de enviar la solicitud
    inicio = time.time()

    # Realizamos la solicitud HTTP PUT enviando:
    # - headers (por ejemplo API key si fuera necesario)
    # - json con la información a actualizar
    response = requests.put(url, headers=header_request, json=data)

    # Calculamos la diferencia en segundos entre la solicitud y la respuesta
    tiempo_diff = time.time() - inicio

     
    # ================================================================
    # VALIDACIONES DEL TEST
    # ================================================================

    # 1) Validar que el servidor responda 200 (OK)
    assert response.status_code == 200, \
        f"Se esperaba código 200 y se obtuvo {response.status_code}"

    # 2) Validar que la API responda en menos de 2 segundos
    assert tiempo_diff < 2, \
        f"La API tardó demasiado: {tiempo_diff} segundos"

    # Convertimos la respuesta en diccionario Python
    body = response.json()

    # 3) Verificar que el campo 'updatedAt' esté presente en la respuesta
    assert "updatedAt" in body, \
        "El campo 'updatedAt' no se encontró en la respuesta"

    # 4) Verificar que el nombre recibido sea un string
    assert isinstance(body["name"], str), \
        "El campo 'name' no es una cadena de texto"

    # 5) Verificar que el nombre devuelto sea el mismo que enviamos
    assert body["name"] == data["name"], \
        f"El nombre recibido ({body['name']}) no coincide con el esperado ({data['name']})"
