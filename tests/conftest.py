import time

import pytest

from pages.AddReportPage import AddReportPage
from pages.LoginPage import LoginPage
from pages.AddEmployeePage import AddEmployeePage
from pages.MenuPage import MenuPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Set browser")

@pytest.fixture()
def choose_browser(request):
    selected_browser = request.config.getoption("--browser").lower()
    yield selected_browser

@pytest.fixture()
def open_login(choose_browser):
    login_page = LoginPage(browser=choose_browser)
    yield login_page
    login_page.close()

@pytest.fixture()
def efetuar_login(open_login):
    open_login.efetuar_login()
    yield open_login

@pytest.fixture()
def add_employee(efetuar_login):
    menu_page = MenuPage(driver=efetuar_login.driver)
    menu_page.click_pim_option()
    menu_page.click_add_employee_btn()
    time.sleep(5)
    new_employee = AddEmployeePage(driver=menu_page.driver)
    new_employee.add_new_employee('Clauthucio', 'Chaves', 'Silva')
    yield new_employee

@pytest.fixture()
def add_new_report(efetuar_login):
    menu_page = MenuPage(driver=efetuar_login.driver)
    menu_page.click_pim_option()
    menu_page.click_reports_btn()
    new_report = AddReportPage(driver=menu_page.driver)
    new_report.click_add_report_btn()
    new_report.add_new_report('Jobs Report', 'Job')
    yield new_report


