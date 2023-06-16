import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.PageObject import PageObject


class AddReportPage(PageObject):

    xpath_add_report_btn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    att_report_name_field = '[placeholder="Type here ..."]'
    css_selection_display_fields = '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(5) > div > div:nth-child(1) > div'
    class_save_button = 'orangehrm-left-space'
    class_report_title = 'orangehrm-main-title'
    class_label_display = 'oxd-label'
    class_dropdown_display = 'oxd-select-text'
    att_dropdown_elements = '[role="option"]'
    css_plus_display_btn = 'div.orangehrm-report-criteria:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def click_add_report_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_add_report_btn).click()

    def select_display_fields_item(self, item_to_be_select='Job'):
        grid_items = self.driver.find_elements(By.CSS_SELECTOR, self.css_selection_display_fields)
        time.sleep(2)
        for item in grid_items:
            if item.find_element(By.CLASS_NAME, self.class_label_display).text == 'Select Display Field Group':
                item.find_element(By.CLASS_NAME, self.class_dropdown_display).click()
                time.sleep(2)
                # Localizar o item específico no menu suspenso usando seu seletor
                menu_items = item.find_elements(By.CSS_SELECTOR, self.att_dropdown_elements)
                for menu_tem in menu_items:
                    if menu_tem.text == item_to_be_select:
                        menu_tem.click()
                        # tempo de sleep so para ver que o item foi selecionado corretamente
                        time.sleep(2)
                        break
                break

    def click_plus_display_fields_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self. css_plus_display_btn).click()
        # tempo de sleep so para ver que a opcão foi selecionada corretamente
        time.sleep(2)

    def fill_name_new_report(self, reportName='Jobs Report'):
        self.driver.find_element(By.CSS_SELECTOR, self.att_report_name_field).send_keys(reportName)

    def click_save_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.class_save_button).click()

    def add_new_report(self, reportName='Jobs Report', item_to_be_select='Job'):
        self.fill_name_new_report(reportName)
        self.select_display_fields_item(item_to_be_select)
        self.click_plus_display_fields_btn()
        self.click_save_btn()

    def verify_details_new_report(self, reportName='Jobs Report'):
        return self.driver.find_element(By.CLASS_NAME, self.class_report_title).text == reportName

