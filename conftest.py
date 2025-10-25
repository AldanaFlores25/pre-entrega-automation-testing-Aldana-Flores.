# definicmos funciones reutilizables
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_usuario():
    """Inicia sesión en SauceDemo y devuelve el driver logueado"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Validar que se redirigió correctamente
    assert "/inventory.html" in driver.current_url, "Error: no se redirigió al inventario"

    return driver  # devolvemos el driver ya abierto y logueado


#podemos tambien guardar otras utilidades

import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    LoginPage(driver).abrir_pagina().login_completo("standard_user","secret_sauce")
    return driver