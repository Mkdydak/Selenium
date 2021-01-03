from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PostPage:

    def __init__(self, browser):
        self.browser = browser

    def verify_comment_section_displayed(self):
        wait = WebDriverWait(self.browser, 10)
        grey_status_bar = (By.CLASS_NAME, 'comment-form')
        wait.until(expected_conditions.presence_of_element_located(grey_status_bar))