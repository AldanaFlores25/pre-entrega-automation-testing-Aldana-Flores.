import pytest

# ============================================================
# FIXTURE: devuelve la URL base de la API
# ------------------------------------------------------------
# Cuando un test necesite este valor, simplemente debe
# incluirlo como argumento (por ejemplo: def test_x(url_base) )
# ============================================================
@pytest.fixture
def url_base():
    # Dirección principal del servicio para manejar usuarios
    return "https://reqres.in/api/users"


# ============================================================
# FIXTURE: devuelve los headers para la solicitud
# ------------------------------------------------------------
# Aquí podrias poner:
# - API Keys
# - tokens
# - información adicional
#
# Cualquier test que necesite este encabezado puede
# recibirlo como parámetro (por ejemplo: test_x(header_request))
# ============================================================
@pytest.fixture
def header_request():
    # Diccionario con encabezados HTTP
    return {"x-api-key": "reqres-free-v1"}
