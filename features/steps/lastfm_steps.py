from behave import given, when, then
from pages.lastfm_home_page import LastfmHomePage
from pages.lastfm_results_page import LastfmResultsPage
from pages.lastfm_artist_page import LastfmArtistPage

@given('que estoy en la página de inicio de Last.fm')
def step_on_home_page(context):
    context.lastfm_home = LastfmHomePage(context.driver)
    context.lastfm_home.navigate_to_home()

@when('busco al artista "{artist_name}"')
def step_search_artist(context, artist_name):
    context.lastfm_home.search_artist(artist_name)

@when('hago clic en el primer resultado')
def step_click_first_result(context):
    context.lastfm_results = LastfmResultsPage(context.driver)
    context.lastfm_results.click_first_result()

@then('debería ver una fecha válida para su último lanzamiento')
def step_verify_release_date(context):
    context.lastfm_artist = LastfmArtistPage(context.driver)
    
    release_date = context.lastfm_artist.get_latest_release_date()
    
    print(f"\n EXITO: Fecha encontrada en la página: {release_date}\n")
    
    assert release_date is not None, "No se encontró el elemento de la fecha."
    assert len(release_date) > 0, "La fecha está vacía."
