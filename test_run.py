import pytest

# Lista de archivos de pruebas a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_catalogo.py",
    "tests/test_carrito.py",
    "tests/test_carrito_json.py"
]

# Argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + ["--html=report.html", "--self-contained-html", "-v"]

# Ejecutar las pruebas
pytest.main(pytest_args)

