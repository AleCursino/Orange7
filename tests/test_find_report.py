from pages.MenuPage import MenuPage
from pages.ReportListPage import ReportListPage


class TestFindReport:

    def test_find_report_by_name(self, efetuar_login):
        menu_page = MenuPage(driver=efetuar_login.driver)
        menu_page.click_pim_option()
        menu_page.click_reports_btn()

        report_list = ReportListPage(driver=menu_page.driver)
        response = report_list.find_report_by_name('PIM Sample Report')
        assert response, "Report não encontrado"
