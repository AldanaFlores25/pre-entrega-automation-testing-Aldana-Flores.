from selenium.webdriver.common.by import By #llamar selectores
from selenium import webdriver #definir navegador
import pytest 

from utils.datos import leer_csv_login #usar funcion para leer csv
from pages.login_page import LoginPage #importa las funciones de la pagina de login


@pytest.mark.parametrize("usuario,password,debe_funcionar",leer_csv_login("datos/data_login.csv")) #parametrizacion e indicacion de que traiga los datos del archivo csv
def test_login_validation(login_in_driver,usuario,password,debe_funcionar): #funcion de login
    driver = login_in_driver
    print(debe_funcionar)
    if debe_funcionar == 'True': #condiciones: si es verdadero el "debe funcionar"
        assert "/inventory.html" in driver.current_url, "No se redirgio al inventario" #asercion: te redirige al inventario, si no se valida salta el mensaje
    elif debe_funcionar == 'False': #si es falso tiene que saltar un mensaje de error
        mensaje_error = LoginPage(driver).obtener_error()
        assert "Epic sadface" in mensaje_error, "el mensaje de error no se esta mostrando" #si el mensaje de error no salta, te sale un mensaje avisando el fallo
    