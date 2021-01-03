from selenium.webdriver.common.by import By


class TestArenaHomePage:
    def __init__(self, browser):
        self.browser = browser

    def verify_successful_login_testarena(self):
        admin = self.browser.find_element_by_css_selector("span.user-info small")
        assert admin.is_displayed()
