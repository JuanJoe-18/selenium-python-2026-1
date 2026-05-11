from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class LastfmHomePage(BasePage):
    URL = "https://www.last.fm/es/"
    
    SEARCH_TOGGLE = (By.CSS_SELECTOR, ".masthead-search-toggle")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#masthead-search-field")

    def navigate_to_home(self):
        self.driver.get(self.URL)

    def search_artist(self, artist_name):
        self.click(self.SEARCH_TOGGLE)
        element = self.find_element(self.SEARCH_INPUT)
        element.send_keys(artist_name)
        element.send_keys(Keys.RETURN)
