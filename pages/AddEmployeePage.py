from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class AddEmployeePage(PageObject):

    #url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee'
    att_first_name = '[name="firstName"]'
    att_middle_name = '[name="middleName"]'
    att_last_name = '[name="lastName"]'
    class_save_button = 'orangehrm-left-space'
    class_employee_name = 'orangehrm-edit-employee-name'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def add_new_employee(self, firstname='João',middlename='Mauricio', lastname='Souza'):
        self.driver.find_element(By.CSS_SELECTOR, self.att_first_name).send_keys(firstname)
        self.driver.find_element(By.CSS_SELECTOR, self.att_middle_name).send_keys(middlename)
        self.driver.find_element(By.CSS_SELECTOR, self.att_last_name).send_keys(lastname)
        self.driver.find_element(By.CLASS_NAME, self.class_save_button).click()

    def verify_details_new_employee(self, firstname='João', lastname='Souza'):
        return self.driver.find_element(By.CLASS_NAME, self.class_employee_name).text == firstname + ' ' + lastname


