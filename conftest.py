import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

import pathlib
from datetime import datetime
import time

target = pathlib.Path("reports/screens")
target.mkdir(parents=True, exist_ok=True)

# ---------------------------
# FIXTURE: driver
# Inicializa el navegador Chrome en modo incógnito
# y lo cierra al finalizar la prueba.
# ---------------------------
@pytest.fixture
def driver():
    # Crear opciones del navegador (incluir configuración)
    options = Options()
    options.add_argument("--incognito")   # Abrir en modo incógnito

    # Inicializar el driver de Chrome con las opciones indicadas
    driver = webdriver.Chrome(options=options)

    # Entregar el driver a la prueba
    yield driver

    # Cerrar el navegador después de finalizar la prueba
    driver.quit()


# ---------------------------
# FIXTURE: login_in_driver
# Realiza el login usando el driver ya inicializado.
# Depende del fixture driver.
# ---------------------------
@pytest.fixture
def login_in_driver(driver, usuario, password):
    # Crear instancia de la página Login y ejecutar el login completo
    LoginPage(driver).abrir_pagina().login_completo(usuario, password)

    # Devolver el driver ya logueado para seguir usándolo en las pruebas
    return driver


# ---------------------------
# FIXTURE: url_base
# Devuelve la URL base de la API ReqRes para pruebas.
# ---------------------------
@pytest.fixture
def url_base():
    return "https://reqres.in/api"



#agrega contexto visual al reporte html

def pytest_html_results_table_header(cells):
    """Añade una columna 'URL' justo después de 'Test ID'."""
    cells.insert(2, 'URL')

def pytest_html_results_table_row(report, cells):
    """Rellena la columna con la URL almacenada en el atributo 'page_url'."""
    cells.insert(2, getattr(report, 'page_url', '-'))



#Crear hook (funcion que se ejecuta automaticamente)

@pytest.hookimpl(hookwrapper=True) #incorpora la funcion de captura de pantalla dentro del ccodigo de los tests
def pytest_runtest_makereport(item, call): #item representa al test, call contiene informacion de la ejecucion
    outcome = yield #yield es como un return pero que no termina el test, la pausa y guarda todo lo que estaba haciendo
    
    report = outcome.get_result()

    if report.when in ("setup","call") and report.failed:
        driver = item.funcargs.get("driver",None)
        
        if driver:
            timestamp_comun= datetime.now().strftime("%Y%m%d_%H%M%S")
            timestamp_unix = int(time.time())
            file_name= target / f"{report.when}_{item.name}_{timestamp_unix}.png"
            driver.save_screenshot(str(file_name))

   

