# language: es
Feature: Login en SauceDemo

  Scenario: Login exitoso
    Given que estoy en la página de login
    When ingreso usuario "standard_user" y contraseña "secret_sauce"
    And hago click en Login
    Then debería ver el inventario