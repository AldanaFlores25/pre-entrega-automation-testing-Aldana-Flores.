import requests
from utils.logger import logger
import pytest

# ================================
# FIXTURES
# ================================

@pytest.fixture
def url_base():
    """
    Fixture que devuelve la URL base del servicio JSONPlaceholder.
    Se usa para construir todos los endpoints necesarios en los tests.
    """
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def request_headers():
    """
    Fixture que devuelve los headers necesarios para cada solicitud.
    Incluye:
      - Content-Type: Tipo de dato enviado
      - User-Agent: Identificación del cliente
    Esto ayuda a evitar bloqueos y mantener consistencia entre tests.
    """
    return {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
    }


# ================================
# TEST: GET USER
# ================================

def test_get_user(url_base, request_headers):
    """
    TEST: Validar que GET /users/2 devuelva:
      - Código HTTP 200
      - Un usuario cuyo id sea exactamente 2

    Este test incluye logs detallados:
      - Paso ejecutado
      - Resultado esperado
      - Resultado real obtenido
      - Mensajes de error si la validación falla
    """

    logger.info("===== INICIO TEST: GET USER =====")
    logger.info("Paso 1: Enviando GET a /users/2")

    # Se realiza la solicitud GET al endpoint
    response = requests.get(f"{url_base}/users/2", headers=request_headers)

    # Log de los resultados reales obtenidos
    logger.info(f"Resultado real - Status code recibido: {response.status_code}")
    logger.info(f"Resultado real - Body: {response.json()}")

    # Validación del status esperado
    expected_status = 200
    logger.info(f"Validación: Se esperaba status {expected_status}")

    if response.status_code != expected_status:
        logger.error(f" FALLÓ: Status esperado {expected_status}, recibido {response.status_code}")

    assert response.status_code == expected_status

    # Validación del ID devuelto
    expected_id = 2
    real_id = response.json().get("id")
    logger.info(f"Validación: Se esperaba ID = {expected_id}, recibido = {real_id}")

    if real_id != expected_id:
        logger.error(f" FALLÓ: ID esperado {expected_id}, recibido {real_id}")

    assert real_id == expected_id

    logger.info("TEST GET USER PASÓ EXITOSAMENTE\n")


# ================================
# TEST: CREATE USER
# ================================

def test_create_user(url_base, request_headers):
    """
    TEST: Validar creación de usuario mediante POST /users.

    JSONPlaceholder siempre responde:
      - Status 201 (Created)
      - Un objeto JSON que incluye un campo 'id' generado

    Este test registra:
      - Payload enviado
      - Status real
      - Body real
      - Validaciones y errores si hay fallas
    """

    logger.info("===== INICIO TEST: CREATE USER =====")
    logger.info("Paso 1: Enviando POST a /users")

    # Cuerpo enviado al crear usuario
    payload = {
        "name": "Jose",
        "username": "Profesor",
        "email": "jose@example.com"
    }

    logger.info(f"Payload enviado: {payload}")

    # Envío de POST
    response = requests.post(f"{url_base}/users", headers=request_headers, json=payload)

    # Log de lo recibido
    logger.info(f"Resultado real - Status code: {response.status_code}")
    logger.info(f"Resultado real - Body: {response.json()}")

    # Validación del status
    expected_status = 201
    logger.info(f"Validación: Se esperaba status {expected_status}")

    if response.status_code != expected_status:
        logger.error(f" FALLÓ: Status esperado {expected_status}, recibido {response.status_code}")

    assert response.status_code == expected_status

    # Validación del campo 'id'
    logger.info("Validación: Se esperaba que el response incluya un 'id' generado")

    if "id" not in response.json():
        logger.error(" FALLÓ: El campo 'id' NO está presente en la respuesta")

    assert "id" in response.json()

    logger.info(" TEST CREATE USER PASÓ EXITOSAMENTE\n")


# ================================
# TEST: DELETE USER
# ================================

def test_delete_user(url_base, request_headers):
    """
    TEST: Validar el DELETE /users/2.

    JSONPlaceholder no borra realmente, pero siempre devuelve:
      - 200 o 204

    Este test verifica que el status esté dentro de esos valores
    y registra con logger si la validación falla.
    """

    logger.info("===== INICIO TEST: DELETE USER =====")
    logger.info("Paso 1: Enviando DELETE a /users/2")

    # Solicitud DELETE
    response = requests.delete(f"{url_base}/users/2", headers=request_headers)

    # Log del resultado
    logger.info(f"Resultado real - Status code: {response.status_code}")

    # Estados válidos aceptados
    expected_statuses = [200, 204]
    logger.info(f"Validación: Se esperaba status {expected_statuses}")

    if response.status_code not in expected_statuses:
        logger.error(f" FALLÓ: Status esperado {expected_statuses}, recibido {response.status_code}")

    assert response.status_code in expected_statuses

    logger.info(" TEST DELETE USER PASÓ EXITOSAMENTE\n")
