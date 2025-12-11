# language: es
Feature: Checkout
  Como usuario con productos en el carrito
  Quiero completar los pasos del checkout
  Para finalizar la compra correctamente

  Background:
    Given el usuario inició sesión y agregó un producto al carrito

  Scenario: Completar un checkout válido
    When navego al carrito
    And inicio el proceso de checkout
    And completo mis datos personales
    And avanzo al resumen
    And finalizo la compra
    Then la compra debe completarse exitosamente
