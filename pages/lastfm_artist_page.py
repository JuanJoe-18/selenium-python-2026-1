from selenium.webdriver.common.by import By
from .base_page import BasePage
import re

class LastfmArtistPage(BasePage):
    BODY = (By.TAG_NAME, "body")
    
    def get_latest_release_date(self):
        element = self.find_element(self.BODY)
        text = element.text
        match = re.search(r'\b(20\d{2})\b', text)
        if match:
            return match.group(0)
        return "No encontrada"
