import requests      # Importamos la librería para hacer solicitudes HTTP
import pytest        # Importamos pytest para ejecutar pruebas automatizadas


# Marcamos el test como "skip" para que NO se ejecute por ahora.
# Esto permite dejarlo en el código sin que falle mientras está en desarrollo.
@pytest.mark.skip(reason="Desactivada porque sigue en desarrollo")
def test_get_users(url_base, header_request):

    # Construimos la URL completa usando la base y el ID del usuario
    url = f"{url_base}/2"

    # Realizamos una solicitud GET al endpoint
    response = requests.get(url, headers=header_request)

    # VALIDACIÓN 1:
    # Afirmamos que el código de estado de la respuesta sea 200 (OK)
    assert response.status_code == 200

    # Convertimos la respuesta a formato JSON para poder leerla como diccionario
    data = response.json()

    # VALIDACIÓN 2:
    # Confirmamos que el JSON incluya la clave "data"
    assert "data" in data

    # VALIDACIÓN 3:
    # Revisamos que la lista dentro de "data" tenga al menos un elemento
    assert len(data["data"]) > 0
