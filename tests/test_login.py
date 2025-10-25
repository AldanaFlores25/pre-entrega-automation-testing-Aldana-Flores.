import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


def test_login(login_in_driver):
    try:
        driver = login_in_driver

        # Configurar espera implícita de hasta 5 segundos
        driver.implicitly_wait(3)

        assert "/inventory.html" in driver.current_url, "No se redirgio al inventario"

    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
 
    