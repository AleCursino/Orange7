from pages.MenuPage import MenuPage
from pages.ReportListPage import ReportListPage


class TestEditReport:

    def test_delete_report(self, add_new_report):
        menu_page = MenuPage(driver=add_new_report.driver)
        menu_page.click_pim_option()
        menu_page.click_reports_btn()

        report_list = ReportListPage(driver=menu_page.driver)
        result = report_list.delete_report('QA Report')
        assert result, "Erro ao excluir o report!"
