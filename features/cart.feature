@ui
Feature: Funcionalidad del carrito
Verificar que los productos puedan agregarse correctamente al carrito
y que el contador refleje el total.

Background:
Given que estoy logueado como "standard_user" con contraseña "secret_sauce"

@ui @regression
Scenario: Agregar un producto al carrito
When agrego el producto "Sauce Labs Backpack" al carrito
Then el contador del carrito debería mostrar "1"

@ui @regression
Scenario: Agregar múltiples productos al carrito
When agrego los siguientes productos al carrito:
| Sauce Labs Backpack     |
| Sauce Labs Bike Light   |
| Sauce Labs Bolt T-Shirt |
Then el contador del carrito debería mostrar "3"
