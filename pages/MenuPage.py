from selenium.webdriver.common.by import By

from pages.PageObject import PageObject

class MenuPage(PageObject):

    att_pim_option = '[href="/web/index.php/pim/viewPimModule"]'
    xpath_add_employee_btn = '// *[ @ id = "app"] / div[1] / div[1] / header / div[2] / nav / ul / li[3]'
    xpath_employee_list_btn = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]'
    xpath_reports_btn = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def click_pim_option(self):
        self.driver.find_element(By.CSS_SELECTOR, self.att_pim_option).click()
    def click_add_employee_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_add_employee_btn).click()

    def click_employee_list_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_employee_list_btn).click()

    def click_reports_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_reports_btn).click()
