import time

from selenium.webdriver.common.by import By

from pages.AddEmployeePage import AddEmployeePage
from pages.MenuPage import MenuPage


class TestNewEmployee:

    #fazer login
    #entrar na página do addemployee
    #preencher os campos e salvar
    firstname = 'Maria'
    middlename = 'Bernadete'
    lastname = 'Alencar'

    def test_add_new_employee(self, efetuar_login):
        menu_page = MenuPage(driver=efetuar_login.driver)
        menu_page.click_pim_option()
        menu_page.click_add_employee_btn()
        new_employee = AddEmployeePage(driver=menu_page.driver)
        new_employee.add_new_employee(self.firstname, self.middlename, self.lastname)
        time.sleep(5)
        response = new_employee.verify_details_new_employee(self.firstname, self.lastname)
        assert response, "Funcionário não encontrado"









