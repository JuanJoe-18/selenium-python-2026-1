from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class ImdbResultsPage(BasePage):
    FIRST_RESULT = (By.CSS_SELECTOR, "a.ipc-title-link-wrapper")

    def click_first_result(self):
        time.sleep(3) 
        self.click(self.FIRST_RESULT)
