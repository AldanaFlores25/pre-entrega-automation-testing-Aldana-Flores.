import pytest

# Lista de archivos de pruebas a ejecutar
test_files = [
    "test_login.py",
    "test_navegacion_catalogo.py",
    "test_carrito.py",
]

# Argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + ["--html=report.html", "--self-contained-html", "-v"]

# Ejecutar las pruebas
pytest.main(pytest_args)

