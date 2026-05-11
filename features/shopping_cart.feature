# language: es
Característica: Funcionalidad de agregar al carrito
  Escenario: El usuario agrega un producto al carrito
    Dado que he iniciado sesión en la página de inventario
    Cuando agrego el producto "Sauce Labs Backpack" al carrito
    Entonces debería ver 1 artículo en el carrito
