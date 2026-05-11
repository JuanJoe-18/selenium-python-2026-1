from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class LastfmResultsPage(BasePage):
    FIRST_RESULT = (By.PARTIAL_LINK_TEXT, "Bruno Mars")

    def click_first_result(self):
        time.sleep(3)
        self.click(self.FIRST_RESULT)
