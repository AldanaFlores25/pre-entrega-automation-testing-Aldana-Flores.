from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@given("que estoy logueada")
def step_login(context):
    context.login = LoginPage(context.driver)
    context.login.abrir_pagina()
    context.login.login_completo("standard_user", "secret_sauce")
    context.inventory = InventoryPage(context.driver)

@when("agrego el primer producto")
def step_add_first(context):
    context.inventory.agregar_primer_producto()

@when("abro el carrito")
def step_open_cart(context):
    context.inventory.abrir_carrito()
    context.cart = CartPage(context.driver)

@then("debería ver 1 producto en el carrito")
def step_check_cart(context):
    assert len(context.cart.obtener_productos_carrito()) == 1
