from selenium.webdriver.common.by import By #llamar selectores
from selenium.webdriver.support.ui import WebDriverWait #espera explicita
from selenium.webdriver.support import expected_conditions as EC #condiciones de la espera explicita
import time

class CartPage:

    # Selectores (localizadores de elementos dentro de la página del carrito)
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")         # Localiza todos los productos agregados al carrito
    _CART_ITEM_NAME = (By.CLASS_NAME,"inventory_item_name")  # Localiza el nombre del producto dentro del carrito

    def __init__(self,driver):
        self.driver = driver       # Guarda el driver para usarlo en los métodos
        self.wait = WebDriverWait(driver,10)  # Crea una espera explícita de hasta 10 segundos

    def obtener_productos_carrito(self):
        # Espera a que todos los elementos del carrito estén visibles en pantalla
        # Devuelve una lista de WebElements que representan cada producto en el carrito
        productos = self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEMS))
        return productos
    
    def obtener_nombre_producto_carrito(self):
        # Espera a que el nombre de un producto sea visible dentro del carrito
        # Devuelve solo el texto del nombre encontrado (primer producto visible)
        nombre_producto = self.wait.until(EC.visibility_of_element_located(self._CART_ITEM_NAME))
        return nombre_producto.text
