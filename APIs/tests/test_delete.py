import requests      # Importamos la librería requests para realizar peticiones HTTP
import pytest        # Importamos pytest para manejar pruebas automatizadas

# Marcamos el test con el tag "api" para poder ejecutarlo selectivamente si queremos.
@pytest.mark.api
def test_delete_users(url_base, header_request):
    
    # Construimos la URL completa agregando el ID del usuario que queremos eliminar.
    # url_base viene como parámetro desde un fixture en pytest.
    url = f"{url_base}/2"

    # Realizamos una solicitud DELETE al servidor:
    # - url: endpoint al cual llamamos
    # - headers: headers enviados, incluyendo posibles claves de autenticación
    response = requests.delete(url, headers=header_request)

    # VALIDACIONES (asserts)
    # Para una operación DELETE exitosa, muchos servicios REST devuelven
    # código 204 (No Content), lo que indica que la operación fue correcta
    # y no se retornó contenido en el cuerpo de la respuesta.
    assert response.status_code == 204
