from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest 

from pages.login_page import LoginPage

# importamos faker
from faker import Faker

# inicializamos Faker para generar datos aleatorios
fake = Faker()


# Parametrizamos el test con dos combinaciones de datos falsos
# Cada caso contiene:
#   usuario, nombre de usuario generado
#   password, contraseña generada
#   debe_funcionar, indica si el login debería pasar o fallar
@pytest.mark.parametrize("usuario,password,debe_funcionar", [
    # Caso 1: usuario y password válidos pero no existentes en el sistema → debe fallar
    (
        fake.user_name(),
        fake.password(length=8, special_chars=True, upper_case=True, lower_case=True, digits=True), #genera password con los requisitos especificos
        False  
    ),
    # Caso 2: credenciales totalmente aleatorias, también debe fallar
    (
        fake.user_name(),
        fake.password(),
        False
    ),
])
def test_login_validation(login_in_driver, usuario, password, debe_funcionar):
    
    # Driver inicializado desde el fixture login_in_driver
    driver = login_in_driver

    # Si esperamos que el login funcione:
    if debe_funcionar == True:
        
        # Verificamos si estamos en la página del inventario
        assert "/inventory.html" in driver.current_url, \
            "No se redirigió al inventario aunque el login debía funcionar"

    # Si esperamos que el login falle:
    elif debe_funcionar == False:

        # Obtenemos el mensaje de error mostrado en la pantalla
        mensaje_error = LoginPage(driver).obtener_error()

        # Validamos que el texto sea el esperado
        assert "Epic sadface" in mensaje_error, \
            "El mensaje de error no se está mostrando como debería" #si el mensaje de error no aparece p no es como deberia ser, nos salta este  mensaje
