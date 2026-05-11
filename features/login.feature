# language: es
Característica: Funcionalidad de Inicio de Sesión
  Escenario: Inicio de sesión exitoso con credenciales válidas
    Dado que el usuario está en la página de inicio de sesión
    Cuando el usuario inicia sesión con credenciales válidas
    Entonces el usuario debería ser redirigido a la página de inventario

  Escenario: Inicio de sesión fallido con credenciales inválidas
    Dado que el usuario está en la página de inicio de sesión
    Cuando el usuario inicia sesión con credenciales inválidas
    Entonces se debería mostrar un mensaje de error

  Escenario: Credenciales de inicio de sesión vacías
    Dado que el usuario está en la página de inicio de sesión
    Cuando el usuario inicia sesión con credenciales vacías
    Entonces se debería mostrar un mensaje de error
