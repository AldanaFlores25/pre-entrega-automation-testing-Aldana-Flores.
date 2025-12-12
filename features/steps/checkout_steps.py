from behave import given, when, then
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage

@given('que estoy logueado como "{user}" con contraseña "{password}"')
def step_impl(context, user, password):
    context.login = LoginPage(context.driver)
    context.inventory = InventoryPage(context.driver)
    context.login.open_login_page()
    context.login.login(user, password)
    assert context.inventory.is_inventory_page_displayed(), "ERROR: No se mostró el inventario luego del login."

@given('agrego el primer producto del inventario')
def step_impl(context):
    context.inventory = InventoryPage(context.driver)
    context.inventory.add_first_product_to_cart()

@given('navego al carrito')
def step_impl(context):
    context.inventory.open_cart()
    context.cart = CartPage(context.driver)
    assert context.cart.is_cart_page_displayed(), "ERROR: No se pudo acceder al carrito."

@when('inicio el proceso de checkout')
def step_impl(context):
    context.cart = CartPage(context.driver)
    context.cart.click_checkout_button()
    context.checkout = CheckoutPage(context.driver)
    assert context.checkout.is_checkout_page_displayed(), "ERROR: No se abrió la pantalla de checkout."

@when('completo mis datos de checkout con nombre "{nombre}", apellido "{apellido}" y codigo "{codigo}"')
def step_impl(context, nombre, apellido, codigo):
    context.checkout = CheckoutPage(context.driver)
    context.checkout.fill_personal_info(nombre, apellido, codigo)

@when('avanzo al resumen del checkout')
def step_impl(context):
    context.checkout = CheckoutPage(context.driver)
    context.checkout.click_continue()
    assert context.checkout.is_overview_page_displayed(), "ERROR: No se mostró la pantalla de overview."

@when('finalizo la compra')
def step_impl(context):
    context.checkout = CheckoutPage(context.driver)
    context.checkout.finish_checkout()

@then('la compra debería finalizar correctamente')
def step_impl(context):
    context.checkout = CheckoutPage(context.driver)
    assert context.checkout.is_order_complete_page_displayed(), "ERROR: La compra no se completó."
    assert context.checkout.is_order_complete_message_displayed(), "ERROR: No se mostró el mensaje de compra completada."

@then('debería ver un mensaje de error en el checkout')
def step_impl(context):
    context.checkout = CheckoutPage(context.driver)
    assert context.checkout.error_message_is_displayed(), "ERROR: No se mostró un mensaje de error en el checkout."
