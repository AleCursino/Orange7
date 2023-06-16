import time

from pages.AddReportPage import AddReportPage
from pages.MenuPage import MenuPage
from pages.ReportListPage import ReportListPage


class TestAddReport:

    report_name = 'Jobs Report'
    display_field = 'Job'

    def test_add_new_report(self, efetuar_login):
        menu_page = MenuPage(driver=efetuar_login.driver)
        menu_page.click_pim_option()
        menu_page.click_reports_btn()
        new_report = AddReportPage(driver=menu_page.driver)
        new_report.click_add_report_btn()
        new_report.add_new_report(self.report_name, self.display_field)
        time.sleep(5)
        response = new_report.verify_details_new_report(self.report_name)
        assert response, "Report não encontrado"

        # pós-condição
        menu_page.click_reports_btn()
        new_report_list = ReportListPage(driver=menu_page.driver)
        new_report_list.delete_report(self.report_name)