from pages.EmployeeListPage import EmployeeListPage
from pages.MenuPage import MenuPage


class TestEditEmployee:

    def test_edit_employee_by_name(self, add_employee):
        menu_page = MenuPage(driver=add_employee.driver)
        menu_page.click_employee_list_btn()

        employee_list = EmployeeListPage(driver=menu_page.driver)
        result = employee_list.edit_employee('Clauthucio', 'Chaves', 'Silva', 'ccsilva')
        assert result, "Erro na edição do funcionário"
