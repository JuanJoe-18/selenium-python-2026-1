from behave import given, when, then
from pages.imdb_home_page import ImdbHomePage
from pages.imdb_results_page import ImdbResultsPage
from pages.imdb_movie_page import ImdbMoviePage

@given('que estoy en la página de inicio de IMDb')
def step_on_imdb_home(context):
    context.imdb_home = ImdbHomePage(context.driver)
    context.imdb_home.navigate_to_home()

@when('busco la película "{movie_title}"')
def step_search_movie(context, movie_title):
    context.imdb_home.search_movie(movie_title)

@when('hago clic en el primer resultado de película')
def step_click_first_movie(context):
    context.imdb_results = ImdbResultsPage(context.driver)
    context.imdb_results.click_first_result()

@then('debería ver el título de la película "{expected_title}"')
def step_verify_title(context, expected_title):
    context.imdb_movie = ImdbMoviePage(context.driver)
    actual_title = context.imdb_movie.get_movie_title()
    print(f"\nEXITO: Titulo encontrado: {actual_title}\n")
    assert expected_title.lower() in actual_title.lower(), f"Se esperaba '{expected_title}', pero se encontro '{actual_title}'"

@then('debería ver una calificación válida para la película')
def step_verify_rating(context):
    rating = context.imdb_movie.get_movie_rating()
    print(f"\nEXITO: Calificacion encontrada: {rating}\n")
    
    try:
        rating_value = float(rating)
        assert rating_value >= 0 and rating_value <= 10.0, f"Calificacion fuera de rango: {rating_value}"
    except ValueError:
        raise AssertionError(f"La calificacion no es un numero valido: {rating}")
