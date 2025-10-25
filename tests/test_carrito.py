import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_carrito(login_in_driver):
    try:
        driver = login_in_driver
        
        # Configurar espera implícita de hasta 5 segundos
        driver.implicitly_wait(5)

        # Encuentra todos los productos
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No hay productos visibles en la página"

        # Tomamos el primer producto
        primer_producto = products[0]

        # Guardamos nombre y precio del producto
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

        # Añadir al carrito
        boton_add = primer_producto.find_element(By.CSS_SELECTOR, "button.btn_inventory")
        boton_add.click()

        # Verificar que el contador del carrito se incrementó a 1
        contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert contador_carrito == "1", "El contador del carrito no se actualizó correctamente"

        # Navegar al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Verificar que el producto aparezca en el carrito
        carrito_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(carrito_items) > 0, "No hay productos en el carrito"


    except Exception as e:
        print(f"Error en test_carrito: {e}")
        raise
    finally:
        driver.quit()
