from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


@given("el usuario inició sesión y agregó un producto al carrito")
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")
    login = LoginPage(context.driver)
    login.login("standard_user", "secret_sauce")

    context.inventory = InventoryPage(context.driver)
    context.inventory.agregar_primer_producto()

    context.checkout = CheckoutPage(context.driver)


@when("navego al carrito")
def step_impl(context):
    context.checkout.go_to_cart()


@when("inicio el proceso de checkout")
def step_impl(context):
    context.checkout.click_checkout_from_cart()


@when("completo mis datos personales")
def step_impl(context):
    context.checkout.fill_checkout_information(
        first_name="Aldana",
        last_name="Flores",
        postal_code="1704"
    )


@when("avanzo al resumen")
def step_impl(context):
    context.checkout.click_continue()


@when("finalizo la compra")
def step_impl(context):
    context.checkout.finish_checkout()


@then("la compra debe completarse exitosamente")
def step_impl(context):
    assert context.checkout.is_order_complete(), \
        "La compra no se completó correctamente."
