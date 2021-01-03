
class CheckAddedProject:
    def __init__(self, browser):
        self.browser = browser

    def check_added_project(self, search):
        menu_projects = self.browser.find_element_by_xpath('.//a[@class = "activeMenu" and text()="Projekty"]')
        menu_projects.click()
        search_bar = self.browser.find_element_by_id('search')
        search_bar.send_keys(search)

        search_button = self.browser.find_element_by_id('j_searchButton')
        search_button.click()

        table_project_name = self.browser.find_element_by_xpath('.//a[text()="MKD17"]')

        assert table_project_name.is_displayed()