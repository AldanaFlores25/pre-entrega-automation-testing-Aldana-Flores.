# language: es
Feature: Agregar al carrito

  Scenario: Agregar primer producto al carrito
    Given que estoy logueada
    When agrego el primer producto
    And abro el carrito
    Then debería ver 1 producto en el carrito
