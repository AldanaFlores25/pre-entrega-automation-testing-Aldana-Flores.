from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# ========================================
# BACKGROUND
# ========================================

@given('que estoy logueado como "{usuario}" con contraseña "{password}"')
def step_login_inventory(context, usuario, password):
    """Realiza login automático antes de cada escenario usando InventoryPage."""
    context.login = LoginPage(context.driver)
    context.login.abrir_pagina()
    context.login.login_completo(usuario, password)
    context.inventory = InventoryPage(context.driver)

# ========================================
# ESCENARIOS
# ========================================

@when("obtengo la lista de productos del inventario")
def step_get_products(context):
    """Obtiene todos los productos visibles en el inventario."""
    context.productos = context.inventory.obtener_todos_los_productos()

@then("debería ver al menos un producto visible")
def step_check_products_visible(context):
    """Valida que el inventario tenga al menos un producto."""
    assert len(context.productos) > 0, \
        "No se encontraron productos visibles en la página de inventario."

@when("agrego el primer producto del inventario")
def step_add_first_product(context):
    """Agrega el primer producto usando InventoryPage."""
    context.inventory.agregar_primer_producto()

@when('agrego el producto "{nombre}" al carrito')
def step_add_product_by_name_inventory(context, nombre):
    """Agrega un producto específico por su nombre."""
    context.inventory.agregar_producto_por_nombre(nombre)

@then('el contador del carrito debería mostrar "{cantidad}"')
def step_verify_cart_counter_inventory(context, cantidad):
    """Verifica que el contador del carrito sea el esperado."""
    contador = context.inventory.obtener_conteo_carrito()
    assert str(contador) == cantidad, \
        f"Se esperaba {cantidad} pero el carrito muestra {contador}"
