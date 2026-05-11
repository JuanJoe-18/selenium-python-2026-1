# language: es
Característica: Buscar una película en IMDb y validar su calificación

  Escenario: Buscar la película "Inception" y verificar su título y calificación
    Dado que estoy en la página de inicio de IMDb
    Cuando busco la película "Inception"
    Y hago clic en el primer resultado de película
    Entonces debería ver el título de la película "Inception"
    Y debería ver una calificación válida para la película
