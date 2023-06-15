import time

from pages.EmployeeListPage import EmployeeListPage
from pages.MenuPage import MenuPage


class TestFindEmployee:

    def test_find_employee_by_name(self, add_employee):
        menu_page = MenuPage(driver=add_employee.driver)
        menu_page.click_employee_list_btn()

        employee_list = EmployeeListPage(driver=menu_page.driver)
        response = employee_list.find_employee_by_name('Clauthucio')
        assert response, "Funcionário não encontrado"

