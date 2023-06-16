from pages.MenuPage import MenuPage
from pages.ReportListPage import ReportListPage


class TestEditReport:

    def test_edit_report(self, add_new_report):
        menu_page = MenuPage(driver=add_new_report.driver)
        menu_page.click_pim_option()
        menu_page.click_reports_btn()

        report_list = ReportListPage(driver=menu_page.driver)
        result = report_list.edit_report('Jobs Report')
        assert result, "Erro na edição do report!"

        #pós-condição
        menu_page.click_reports_btn()
        report_list.delete_report('Jobs Report')


