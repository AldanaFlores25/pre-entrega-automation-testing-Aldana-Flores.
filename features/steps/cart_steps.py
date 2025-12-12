
from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@given('que estoy logueado como "{usuario}" con contraseña "{password}"')
def step_login_background(context, usuario, password):
    """Realiza login automático para el Background."""
    context.login = LoginPage(context.driver)
    context.login.abrir_pagina()
    context.login.login_completo(usuario, password)
    context.inventory = InventoryPage(context.driver)

@when('agrego el producto "{nombre}" al carrito')
def step_add_product(context, nombre):
    """Agrega un único producto por nombre."""
    context.inventory.agregar_producto_por_nombre(nombre)

@when('agrego los siguientes productos al carrito:')
def step_add_multiple_products(context):
    """Agrega múltiples productos listados en la tabla."""
    for row in context.table:
        nombre_producto = row[0]
        context.inventory.agregar_producto_por_nombre(nombre_producto)

@then('el contador del carrito debería mostrar "{cantidad}"')
def step_verify_cart_counter(context, cantidad):
    """Verifica que el contador del carrito sea igual al esperado."""
    contador = context.inventory.obtener_conteo_carrito()
    assert str(contador) == cantidad, \
        f"Se esperaba {cantidad} pero el carrito muestra {contador}"

