# language: es
Feature: Manejo del inventario
  Como usuario logueado en SauceDemo
  Quiero ver y agregar productos al carrito
  Para continuar la compra

  Background:
    Given el usuario ha iniciado sesión correctamente

  Scenario: Ver todos los productos disponibles
    When obtengo la lista de productos
    Then debo ver al menos un producto visible

  Scenario: Agregar el primer producto del inventario
    When agrego el primer producto del inventario
    Then el carrito debe mostrar 1 producto

  Scenario Outline: Agregar un producto por nombre
    When agrego el producto "<nombre>"
    Then el carrito debe mostrar 1 producto

    Examples:
      | nombre                |
      | Sauce Labs Backpack  |
      | Sauce Labs Bike Light |