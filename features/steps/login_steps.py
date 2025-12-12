from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# URL base de tu aplicación
BASE_URL = "https://www.saucedemo.com/"


@given('que abro la página de login')
def step_open_login_page(context):
    context.driver.get(BASE_URL)
    sleep(1)


@when('ingreso el usuario "{usuario}"')
def step_input_username(context, usuario):
    username_field = context.driver.find_element(By.ID, "user-name")
    username_field.clear()
    username_field.send_keys(usuario)


@when('ingreso la contraseña "{password}"')
def step_input_password(context, password):
    password_field = context.driver.find_element(By.ID, "password")
    password_field.clear()
    password_field.send_keys(password)


@when('hago click en el botón de Login')
def step_click_login(context):
    btn_login = context.driver.find_element(By.ID, "login-button")
    btn_login.click()
    sleep(1)


@then('debería ser redirigido al inventario')
def step_verify_inventory_redirect(context):
    current_url = context.driver.current_url
    assert "inventory" in current_url, f"La URL no contiene 'inventory'. Actual: {current_url}"


@then('debería ver el título "Products"')
def step_verify_title(context):
    title = context.driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products", f"Se esperaba 'Products' pero se encontró: {title}"


@then('debería ver el mensaje de error "{mensaje_error}"')
def step_verify_error_message(context, mensaje_error):
    error_div = context.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    texto_error = error_div.text.strip()
    assert mensaje_error in texto_error, f"Error esperado: {mensaje_error}, recibido: {texto_error}"
