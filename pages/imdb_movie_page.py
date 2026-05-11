from selenium.webdriver.common.by import By
from .base_page import BasePage

class ImdbMoviePage(BasePage):
    TITLE_ELEMENT = (By.CSS_SELECTOR, "[data-testid='hero__primary-text']")
    RATING_ELEMENT = (By.CSS_SELECTOR, "[data-testid='hero-rating-bar__aggregate-rating__score']")
    
    def get_movie_title(self):
        element = self.find_element(self.TITLE_ELEMENT)
        return element.text.strip()
        
    def get_movie_rating(self):
        element = self.find_element(self.RATING_ELEMENT)
        text = element.text.strip()
        # El texto suele venir como "8.8\n/10" o "8.8/10", tomamos solo el número principal
        return text.split('\n')[0].split('/')[0].strip()
