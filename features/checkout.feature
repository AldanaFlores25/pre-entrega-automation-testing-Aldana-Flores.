@ui @regression
Feature: Checkout
Validar el flujo completo de compra en SauceDemo,
incluyendo datos personales, resumen y finalización del pedido.

Background:
Given que estoy logueado como "standard_user" con contraseña "secret_sauce"
And agrego el primer producto del inventario
And navego al carrito

@ui @regression
Scenario: Completar un checkout válido
When inicio el proceso de checkout
And completo mis datos de checkout con nombre "Aldana", apellido "Flores" y codigo "1704"
And avanzo al resumen del checkout
And finalizo la compra
Then la compra debería finalizar correctamente

@ui @regression
Scenario Outline: Checkout inválido por datos incompletos
When inicio el proceso de checkout
And completo mis datos de checkout con nombre "<nombre>", apellido "<apellido>" y codigo "<codigo>"
And avanzo al resumen del checkout
Then debería ver un mensaje de error en el checkout

```
Examples:
  | nombre  | apellido | codigo |
  |         | Flores   | 1704   |
  | Aldana  |          | 1704   |
  | Aldana  | Flores   |        |
```
