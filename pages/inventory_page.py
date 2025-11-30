from selenium.webdriver.common.by import By  # Permite seleccionar elementos por tipo (ID, CLASS_NAME, etc.)
from selenium.webdriver.support.ui import WebDriverWait  # Manejo de esperas explícitas
from selenium.webdriver.support import expected_conditions as EC  # Condiciones usadas en las esperas explícitas
import time

class InventoryPage:
    """
    Esta clase representa la página de inventario en SauceDemo.
    Aplicamos el patrón Page Object Model para mantener organizado
    el código y que las pruebas sean más mantenibles.
    """

    # ======================
    #  SELECTORES DE LA PÁGINA
    # ======================

    # Cada uno corresponde a elementos dentro del inventario de productos
    _INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")              # Cada tarjeta de producto
    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".inventory_item button") # Botón "Add to cart" dentro del producto
    _CART_COUNT = (By.CLASS_NAME, "shopping_cart_badge")              # Contador del carrito (aparece cuando hay productos)
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")               # Nombre de cada producto
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")                # Icono para ir al carrito

    def __init__(self, driver):
        """
        Constructor de la clase.
        Guardamos una referencia al driver y creamos una espera explícita
        por defecto de 10 segundos.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ======================
    #     MÉTODOS
    # ======================

    def obtener_todos_los_productos(self):
        """
        Espera a que los productos estén visibles en pantalla y luego los devuelve como lista.
        """
        self.wait.until( #condicional para esperar hasta que se carguen todos los lementos de la pagina
            EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS)
        )
        productos = self.driver.find_elements(*self._INVENTORY_ITEMS)
        return productos

    def obtener_nombres_productos(self):
        """
        Obtiene el texto (nombre) de cada producto listado en la página.
        Devuelve una lista con nombres.
        """
        productos = self.driver.find_elements(*self._ITEM_NAME)
        return [producto_nombre.text for producto_nombre in productos]

    def agregar_primer_producto(self):
        """
        Obtiene la lista de productos, toma el primero y hace clic en su botón "Add to cart".
        """
        # Esperamos que los productos sean visibles
        productos = self.wait.until(
            EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS)
        )

        # Dentro del primer producto buscamos su botón
        primer_boton_producto = productos[0].find_element(*self._ADD_TO_CART_BUTTON)
        primer_boton_producto.click()

    def agregar_producto_por_nombre(self, nombre_producto):
        """
        Recorre la lista de productos buscando uno cuyo nombre coincida
        (ignorando espacios extra).
        Si lo encuentra, hace clic en su botón 'Add to cart'.
        Si no, genera un error.
        """
        productos = self.driver.find_elements(*self._INVENTORY_ITEMS)

        for producto in productos:
            nombre = producto.find_element(*self._ITEM_NAME).text

            if nombre.strip() == nombre_producto.strip():
                boton = producto.find_element(*self._ADD_TO_CART_BUTTON)
                boton.click()
                return self  # Devuelve la página para permitir método encadenado
        
        # Si termina el ciclo sin encontrar el producto, lanzamos una excepción
        raise Exception(f"No se encontró el producto {nombre_producto}")

    def abrir_carrito(self):
        """
        Espera que el ícono del carrito sea clickeable y navega hacia él.
        """
        self.wait.until(
            EC.element_to_be_clickable(self._CART_LINK)
        ).click()

        return self

    def obtener_conteo_carrito(self):
        """
        Devuelve el número de productos que tiene el carrito.
        Si el contador no existe (carrito vacío), devuelve 0.
        """
        try:
            self.wait.until(
                EC.visibility_of_element_located(self._CART_COUNT)
            )
            contador_carrito = self.driver.find_element(*self._CART_COUNT)
            return int(contador_carrito.text)
        except:
            # Si el contador no está visible, significa que no hay nada en el carrito
            return 0
