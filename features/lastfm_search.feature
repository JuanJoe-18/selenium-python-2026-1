# language: es
Característica: Buscar un artista en Last.fm y validar lanzamiento

  Escenario: Buscar a Bruno Mars y verificar la fecha de su ultimo lanzamiento
    Dado que estoy en la página de inicio de Last.fm
    Cuando busco al artista "Bruno Mars"
    Y hago clic en el primer resultado
    Entonces debería ver una fecha válida para su último lanzamiento
