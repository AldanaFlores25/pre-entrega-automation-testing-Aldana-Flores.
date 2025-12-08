import pytest

# Lista de archivos de pruebas a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_inventory.py",
    "tests/test_cart.py",
    "tests/test_cart_json.py",
    "tests/test_checkout.py",
    "tests/test_api_jsonplaceholder.py"
    
]

# Argumentos usando stylesheet externo
pytest_args = test_files + [
    "--html=report.html",
    "--css=assets/style.css",    # vincula el css externo para personalizar el reporte
    "-v"
]

pytest.main(pytest_args)
