from selenium.webdriver import Chrome

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, administrator_email, administrator_password):
        login_bar = self.browser.find_element_by_id("email")
        password_bar = self.browser.find_element_by_id("password")
        login_button = self.browser.find_element_by_id("login")

        login_bar.send_keys(administrator_email)
        password_bar.send_keys(administrator_password)
        login_button.click()

