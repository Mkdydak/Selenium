from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class SearchResultPage:

    # Inicjalizacja klasy - przekazanie drivera (przeglądarki)
    def __init__(self, browser):
        self.browser = browser

    def wait_for_load(self):
        wait = WebDriverWait(self.browser, 10)
        grey_status_bar = (By.CLASS_NAME, 'status-msg-body')
        wait.until(expected_conditions.visibility_of_element_located(grey_status_bar))

    def verify_post_count(self, expected_count):
        list_of_title_elements = self.browser.find_elements_by_class_name("post-title")
        assert len(list_of_title_elements) == expected_count

