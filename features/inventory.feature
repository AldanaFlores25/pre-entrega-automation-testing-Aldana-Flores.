@ui
Feature: Manejo del inventario
Validar que los productos del inventario se muestren correctamente
y que puedan agregarse al carrito según su posición o nombre.

Background:
Given que estoy logueado como "standard_user" con contraseña "secret_sauce"

@ui @regression
Scenario: Ver todos los productos disponibles
When obtengo la lista de productos del inventario
Then debería ver al menos un producto visible

@ui @regression
Scenario: Agregar el primer producto del inventario
When agrego el primer producto del inventario
Then el contador del carrito debería mostrar "1"

@ui @regression
Scenario Outline: Agregar un producto por nombre
When agrego el producto "<nombre>" al carrito
Then el contador del carrito debería mostrar "1"

```
Examples:
  | nombre                  |
  | Sauce Labs Backpack     |
  | Sauce Labs Bike Light   |
  | Sauce Labs Bolt T-Shirt |
```
