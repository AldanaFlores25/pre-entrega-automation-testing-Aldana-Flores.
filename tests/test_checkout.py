# tests/test_checkout.py
import pytest
from pages.checkout_page import CheckoutPage
from utils.logger import logger
from faker import Faker

fake = Faker("es_ES")  # Genera datos aleatorios en español


@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_checkout(login_in_driver, usuario, password):
    driver = login_in_driver  # inicia la sesión ya logueado
    logger.info("INICIO TEST: flujo de checkout")

    checkout = CheckoutPage(driver)

    # Ir al carrito ANTES de hacer el checkout
    checkout.go_to_cart()

    # Click en botón Checkout
    checkout.click_checkout_from_cart()

    # Datos aleatorios
    first = fake.first_name()
    last = fake.last_name()
    postal = fake.postcode()

    logger.info(f"Datos generados: Nombre={first}, Apellido={last}, CP={postal}")

    # Completar formulario
    checkout.fill_checkout_information(first, last, postal)
    checkout.click_continue()

    # Validaciones del resumen
    subtotal_txt = checkout.get_summary_subtotal()
    tax_txt = checkout.get_summary_tax()
    total_txt = checkout.get_summary_total()

    logger.info(
        f"Resumen obtenido => Subtotal: {subtotal_txt} | Impuesto: {tax_txt} | Total: {total_txt}"
    )

    # Finalizar
    checkout.finish_checkout()

    # Validar
    assert checkout.is_order_complete(), "La orden no se completó correctamente"

    logger.info("FIN TEST: checkout")
