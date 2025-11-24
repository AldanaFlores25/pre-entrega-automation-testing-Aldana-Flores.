from selenium.webdriver.common.by import By #llamar selectores
from selenium.webdriver.support.ui import WebDriverWait #espera explicita
from selenium.webdriver.support import expected_conditions as EC #condiciones de la espera explicita
class LoginPage:
    
    # URL base de la página de login
    URL = "https://www.saucedemo.com/"

    # Selectores de los elementos del formulario de login
    _USER_INPUT = (By.ID,"user-name")        # Campo donde se ingresa el usuario
    _PASS_INPUT = (By.ID,"password")         # Campo donde se ingresa la contraseña
    _LOGIN_BUTTON = (By.ID, "login-button")  # Botón para iniciar sesión


    def __init__(self,driver):
        self.driver = driver                       # Guardamos el driver para usarlo en la clase
        self.wait = WebDriverWait(driver,10)       # Espera explícita por si los elementos tardan en aparecer

    def abrir_pagina(self):
        # Abre la página principal del login usando el driver
        self.driver.get(self.URL)
        return self                                # Retorna la instancia para permitir el encadenamiento de métodos
    
    def completar_user(self,usuario):
        # Espera hasta que el input del usuario sea visible
        input = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        input.clear()                              # Limpia el campo antes de escribir
        input.send_keys(usuario)                   # Escribe el usuario recibido como parámetro
        return self
    
    def completar_pass(self,password):
        # Busca el input de password sin necesidad de espera explícita
        input = self.driver.find_element(*self._PASS_INPUT)
        input.clear()                              # Limpia el campo antes de escribir
        input.send_keys(password)                  # Escribe la contraseña recibida como parámetro
        return self
    
    def hacer_click_button(self):
        # Hace clic en el botón de login
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self

    def login_completo(self,usuario,password):
        # Realiza un login completo en un solo método:
        # 1) Ingresa usuario
        # 2) Ingresa contraseña
        # 3) Hace clic en iniciar sesión
        self.completar_user(usuario)
        self.completar_pass(password)
        self.hacer_click_button()
        return self
    
    def obtener_error(self):
        # Espera a que aparezca el mensaje de error del login
        # Localiza el elemento <h3> dentro del contenedor de error
        div_error = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,".error-message-container h3"))
        )
        return div_error.text                      # Devuelve el texto del mensaje de error