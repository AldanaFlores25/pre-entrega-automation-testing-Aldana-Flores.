from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@given("el usuario ha iniciado sesión correctamente")
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")
    login = LoginPage(context.driver)
    login.login("standard_user", "secret_sauce")
    context.inventory = InventoryPage(context.driver)


@when("obtengo la lista de productos")
def step_impl(context):
    context.productos = context.inventory.obtener_todos_los_productos()


@then("debo ver al menos un producto visible")
def step_impl(context):
    assert len(context.productos) > 0, "No se encontraron productos en el inventario."


@when("agrego el primer producto del inventario")
def step_impl(context):
    context.inventory.agregar_primer_producto()


@then("el carrito debe mostrar 1 producto")
def step_impl(context):
    assert context.inventory.obtener_conteo_carrito() == 1, \
        "El carrito no contiene 1 producto."


@when('agrego el producto "{nombre}"')
def step_impl(context, nombre):
    context.inventory.agregar_producto_por_nombre(nombre)
