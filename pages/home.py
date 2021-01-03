from selenium.webdriver.common.by import By

class HomePage:

     # Inicjalizacja klasy - przekazanie drivera (przeglądarki)
    def __init__(self, browser):
        self.browser = browser


    def verify_post_count(self, expected_count):

        list_of_title_elements = self.browser.find_elements_by_class_name("post-title")

        # Asercja że lista ma 4 elementy
        assert len(list_of_title_elements) == expected_count

    def search(self, search_term):
        search_searchbar = self.browser.find_element_by_css_selector("input.gsc-input")
        search_button = self.browser.find_element_by_css_selector("input.gsc-search-button")
        # szukanie
        search_searchbar.send_keys(search_term)
        search_button.click()

    def click_label(self, label_name):
        label = self.browser.find_element_by_link_text(label_name)
        label.click()


    def click_first_post_title(self):
        post_titles = self.browser.find_elements_by_css_selector(".post-title a")
        post_titles[0].click()

    def click_read_more(self):
        read_more = self.browser.find_element_by_link_text("Read more »")
        read_more.click()

