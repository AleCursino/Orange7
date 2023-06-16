from pages.MenuPage import MenuPage
from pages.ReportListPage import ReportListPage


class TestFindReport:

    def test_find_report_by_name(self, add_new_report):
        menu_page = MenuPage(driver=add_new_report.driver)
        menu_page.click_reports_btn()

        report_list = ReportListPage(driver=menu_page.driver)
        response = report_list.find_report_by_name('Jobs Report')
        assert response, "Report não encontrado"

        # pós-condição
        menu_page.click_reports_btn()
        report_list.delete_report('Jobs Report')
