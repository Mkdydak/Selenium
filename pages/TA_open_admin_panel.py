
class OpenAdminPanel:
    def __init__(self, browser):
        self.browser = browser

    def open_admin_panel(self):
        select_panel = self.browser.find_element_by_css_selector(".header_admin a")
        select_panel.click()
        projects_header = self.browser.find_element_by_xpath('.//h1[@class = "content_title" and text()="Projekty"]')
        assert projects_header.is_displayed()

