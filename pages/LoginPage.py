import time

from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class LoginPage(PageObject):
    url = 'https://opensource-demo.orangehrmlive.com/'
    class_login_btn = 'orangehrm-login-button'
    att_name_username = '[name="username"]'
    att_name_password = '[name="password"]'

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.open_login_page()

    def open_login_page(self):
        self.driver.get(self.url)

    def click_login_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.class_login_btn).click()

    def efetuar_login(self, username='Admin', password='admin123'):
        self.driver.find_element(By.CSS_SELECTOR, self.att_name_username).send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, self.att_name_password).send_keys(password)
        self.click_login_btn()


