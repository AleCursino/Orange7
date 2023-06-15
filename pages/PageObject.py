from selenium import webdriver
from selenium.webdriver.common.by import By


class PageObject:

    class_option_popup_delete = 'orangehrm-modal-footer'

    def __init__(self, driver=None, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'safari':
                self.driver = webdriver.Safari()
            else:
                raise Exception('Browser não suportado!!')
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def is_page(self, url):
        is_url = self.driver.current_url == url
        return is_url

    def click_yes_delete_btn_modal(self):
        option = 'Yes, Delete'
        options_popup_delete = self.driver.find_elements(By.CLASS_NAME, self.class_option_popup_delete)
        for i in range(len(options_popup_delete)):
            current_option = options_popup_delete[i]
            if option in current_option.text:
                current_option.click()
