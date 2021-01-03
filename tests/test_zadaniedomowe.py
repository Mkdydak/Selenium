import pytest
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.TA_add_project import TestAddNewProject
from pages.TA_login_page import LoginPage
from pages.TA_log_home_page import TestArenaHomePage
from pages.TA_open_admin_panel import OpenAdminPanel
from pages.TA_add_project import TestAddNewProject
from pages.TA_check_project import CheckAddedProject



@pytest.fixture()
def browser():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    # otwarcie strony
    browser.get("http://demo.testarena.pl")
    # zwracanie obiektu z przeglądarką
    yield browser
    # zamknięcie przeglądarki
    browser.quit()


def test_zadanie_domowe(browser):
    login_page = LoginPage(browser)
    login_page.login('administrator@testarena.pl', 'sumXQQ72$L')

    arena_home = TestArenaHomePage(browser)
    arena_home.verify_successful_login_testarena()

    admin_panel = OpenAdminPanel(browser)
    admin_panel.open_admin_panel()

    add_project = TestAddNewProject(browser)
    add_project.add_new_project('MKD17', 17)

    check_project = CheckAddedProject(browser)
    check_project.check_added_project('MKD17')
















