# pages/cart_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Page Object Model: Cart Page (https://www.saucedemo.com/cart.html)
    
    """

    # ====== Localizadores ======
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    _CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    _CHECKOUT_BTN = (By.ID, "checkout")
    _CART_TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        """Inicializa el CartPage con el WebDriver y una espera explícita."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ====== Validaciones ======
    def validar_pagina_carrito(self):
        """Verifica que estamos en la página del carrito."""
        titulo = self.wait.until(
            EC.visibility_of_element_located(self._CART_TITLE)
        ).text
        assert titulo == "Your Cart", f"El título esperado era 'Your Cart', se encontró: {titulo}"

    # ====== Métodos de lectura ======
    def obtener_productos(self):
        """Devuelve una lista de elementos 'cart_item'."""
        return self.driver.find_elements(*self._CART_ITEMS)

    def obtener_nombres_productos(self):
        """Devuelve una lista con los nombres de los productos en el carrito."""
        productos = self.obtener_productos()
        nombres = [p.find_element(*self._ITEM_NAME).text for p in productos]
        return nombres

    def obtener_precios_productos(self):
        """Devuelve una lista con los precios de los productos en el carrito."""
        productos = self.obtener_productos()
        precios = [p.find_element(*self._ITEM_PRICE).text for p in productos]
        return precios

    # ====== Acciones ======
    def volver_al_inventario(self):
        """Hace clic en 'Continue Shopping' y vuelve al inventario."""
        self.wait.until(EC.element_to_be_clickable(self._CONTINUE_SHOPPING_BTN)).click()
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def iniciar_checkout(self):
        """Hace clic en 'Checkout' y navega a la página del formulario de compra."""
        self.wait.until(EC.element_to_be_clickable(self._CHECKOUT_BTN)).click()
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)
