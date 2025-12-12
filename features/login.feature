@ui
Feature: Autenticación en la plataforma
Permitir que los usuarios accedan con credenciales válidas
y mostrar errores adecuados cuando las credenciales son incorrectas.

Background:
Given que abro la página de login

@smoke @ui
Scenario: Login exitoso con credenciales válidas
When ingreso el usuario "standard_user"
And ingreso la contraseña "secret_sauce"
And hago click en el botón de Login
Then debería ser redirigido al inventario
And debería ver el título "Products"

@ui
Scenario Outline: Intentos fallidos de login
When ingreso el usuario "<usuario>"
And ingreso la contraseña "<contraseña>"
And hago click en el botón de Login
Then debería ver el mensaje de error "<mensaje_error>"

```
Examples:
  | usuario         | contraseña     | mensaje_error                                                |
  | wrong_user      | wrong_pass     | Epic sadface: Username and password do not match            |
  | locked_out_user | secret_sauce   | Epic sadface: Sorry, this user has been locked out.         |
  |                 |                | Epic sadface: Username is required                          |
```
