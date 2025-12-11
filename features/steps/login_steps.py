from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

@given('que estoy en la página de login')
def step_open_login(context):
    context.login = LoginPage(context.driver)
    context.login.abrir_pagina()

@when('ingreso usuario "{usuario}" y contraseña "{password}"')
def step_fill_login(context, usuario, password):
    context.login.completar_user(usuario)
    context.login.completar_pass(password)

@when('hago click en Login')
def step_click_login(context):
    context.login.hacer_click_button()

@then('debería ver el inventario')
def step_should_see_inventory(context):
    InventoryPage(context.driver)  # solo inicializamos
    assert "inventory.html" in context.driver.current_url
