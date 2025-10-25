import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_navegacion_catalogo(login_in_driver):
    try:
        driver = login_in_driver
        
        # Configurar espera implícita de hasta 5 segundos
        driver.implicitly_wait(5)

        # Verificar que el título de la página de inventario sea correcto
        assert driver.title == "Swag Labs", "El título de la página no coincide"

        # Verificar que existan productos visibles en la página
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No hay productos visibles en la página"

        # Guardar nombre y precio del primer producto
        primer_producto = products[0]
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

        print(f"Primer producto: {nombre_producto} - Precio: {precio_producto}")

        # Validar elementos importantes de la interfaz
        # Menú de navegación
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu.is_displayed(), "El menú no está presente en la página"

        # Filtros de ordenamiento
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed(), "El filtro de productos no está presente en la página"

    except Exception as e:
        print(f"Error en test_navegacion_inventario: {e}")
        raise
    finally:
        driver.quit()
