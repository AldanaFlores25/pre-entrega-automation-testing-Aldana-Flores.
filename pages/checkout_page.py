# pages/checkout_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger


class CheckoutPage:

    # ▬▬▬▬▬▬ Selectores ▬▬▬▬▬▬
    _CART_ICON = (By.ID, "shopping_cart_container")             # icono del carrito (arriba a la derecha)
    _CHECKOUT_BUTTON = (By.ID, "checkout")                      # botón en /cart.html
    _FIRST_NAME = (By.ID, "first-name")
    _LAST_NAME = (By.ID, "last-name")
    _POSTAL_CODE = (By.ID, "postal-code")
    _CONTINUE = (By.ID, "continue")
    _CANCEL = (By.ID, "cancel")
    _SUMMARY_SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    _SUMMARY_TAX = (By.CLASS_NAME, "summary_tax_label")
    _SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    _FINISH = (By.ID, "finish")
    _COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    _ERROR_MSG = (By.CSS_SELECTOR, ".error-message-container")
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _BACK_HOME_BUTTON = (By.ID, "back-to-products")

    # Constructor
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Navegación 
    def go_to_cart(self):
        """Navega al carrito desde cualquier página luego del login."""
        logger.info("Navegando al carrito…")
        self.wait.until(EC.element_to_be_clickable(self._CART_ICON)).click()

    # Paso 1: Carrito → Checkout 
    def click_checkout_from_cart(self):
        """Hace click en Checkout dentro del carrito."""
        logger.info("Click en 'Checkout' desde el carrito")
        btn = self.wait.until(EC.element_to_be_clickable(self._CHECKOUT_BUTTON))
        btn.click()

    #  Paso 2: Información del cliente 
    def fill_checkout_information(self, first_name, last_name, postal_code):
        logger.info(f"Completando formulario de checkout: {first_name} {last_name} {postal_code}")

        self.wait.until(EC.visibility_of_element_located(self._FIRST_NAME)).clear()
        self.driver.find_element(*self._FIRST_NAME).send_keys(first_name)

        self.wait.until(EC.visibility_of_element_located(self._LAST_NAME)).clear()
        self.driver.find_element(*self._LAST_NAME).send_keys(last_name)

        self.wait.until(EC.visibility_of_element_located(self._POSTAL_CODE)).clear()
        self.driver.find_element(*self._POSTAL_CODE).send_keys(postal_code)

    def click_continue(self):
        logger.info("Click en 'Continue' para ir al resumen")
        self.wait.until(EC.element_to_be_clickable(self._CONTINUE)).click()

    def get_error_message(self):
        try:
            el = self.wait.until(EC.visibility_of_element_located(self._ERROR_MSG))
            msg = el.text.strip()
            logger.info(f"Mensaje de error detectado: {msg}")
            return msg
        except Exception:
            return None

    #  Paso 3: Resumen de compra 
    def get_summary_subtotal(self):
        txt = self.wait.until(EC.visibility_of_element_located(self._SUMMARY_SUBTOTAL)).text
        logger.info(f"Subtotal: {txt}")
        return txt

    def get_summary_tax(self):
        txt = self.wait.until(EC.visibility_of_element_located(self._SUMMARY_TAX)).text
        logger.info(f"Tax: {txt}")
        return txt

    def get_summary_total(self):
        txt = self.wait.until(EC.visibility_of_element_located(self._SUMMARY_TOTAL)).text
        logger.info(f"Total: {txt}")
        return txt

    # Paso 4: Finalizar orden 
    def finish_checkout(self):
        logger.info("Click en 'Finish' para completar la orden")
        self.wait.until(EC.element_to_be_clickable(self._FINISH)).click()

    def is_order_complete(self):
        try:
            header = self.wait.until(EC.visibility_of_element_located(self._COMPLETE_HEADER)).text
            logger.info(f"Pantalla de finalización detectada: {header}")
            return True
        except Exception:
            logger.error("No se mostró la pantalla de finalización")
            return False

    #  Utilidades
    def get_cart_items(self):
        items = self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEMS))
        logger.info(f"Productos en carrito: {len(items)}")
        return items

    def get_cart_item_names(self):
        elems = self.get_cart_items()
        names = []
        for item in elems:
            try:
                name_el = item.find_element(By.CLASS_NAME, "inventory_item_name")
                names.append(name_el.text.strip())
            except Exception:
                logger.warning("No se pudo leer el nombre de un item")
        logger.info(f"Nombres en carrito: {names}")
        return names
