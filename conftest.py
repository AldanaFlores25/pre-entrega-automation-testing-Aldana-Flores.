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
# conftest.py

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
 """Fixture que proporciona un WebDriver configurado."""
 chrome_options = Options()
 # chrome_options.add_argument("--headless") # Para CI/CD
 chrome_options.add_argument("--no-sandbox")
 chrome_options.add_argument("--disable-dev-shm-usage")
 service = Service()
 driver = webdriver.Chrome(service=service, options=chrome_options)
 driver.maximize_window()
 driver.implicitly_wait(5)
 yield driver
 time.sleep(1) # Para ver el resultado final
 driver.quit()