
class TestAddNewProject:
    def __init__(self, browser):
        self.browser = browser

    def add_new_project(self, project_name, prefix):
        add_button = self.browser.find_element_by_xpath('.//a[@class = "button_link" and text()="Dodaj projekt"]')
        add_button.click()

        add_project_name = self.browser.find_element_by_id("name")
        new_prefix = self.browser.find_element_by_id("prefix")
        save_button = self.browser.find_element_by_id("save")

        add_project_name.send_keys(project_name)
        new_prefix.send_keys(prefix)
        save_button.click()

    def verify_successful_add_project(self):
        filter_button = self.browser.find_element_by_id("j_info_box")
        assert filter_button.is_displayed()
