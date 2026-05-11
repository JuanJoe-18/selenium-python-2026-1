from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class ImdbHomePage(BasePage):
    URL = "https://www.imdb.com/"
    
    SEARCH_INPUT = (By.ID, "suggestion-search")

    def navigate_to_home(self):
        self.driver.get(self.URL)

    def search_movie(self, movie_title):
        element = self.find_element(self.SEARCH_INPUT)
        element.send_keys(movie_title)
        element.send_keys(Keys.RETURN)
