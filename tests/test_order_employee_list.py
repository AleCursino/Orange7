
from pages.EmployeeListPage import EmployeeListPage
from pages.MenuPage import MenuPage


class TestOrderEmployeeList:

    def test_order_employee_list_order_asc(self, efetuar_login):
        menu_page = MenuPage(driver=efetuar_login.driver)
        menu_page.click_pim_option()
        menu_page.click_employee_list_btn()

        employee_list = EmployeeListPage(driver=menu_page.driver)
        employee_list.order_employee_list_order_asc('First (& Middle) Name', 'Ascending')
        assert employee_list.check_order_first_name_asc(), "A lista não está ordenada"
