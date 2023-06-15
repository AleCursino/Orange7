from pages.MenuPage import MenuPage
from pages.ReportListPage import ReportListPage


class TestOrderReportList:

    def test_order_report_list_order_desc(self, efetuar_login):
        menu_page = MenuPage(driver=efetuar_login.driver)
        menu_page.click_pim_option()
        menu_page.click_reports_btn()

        report_list = ReportListPage(driver=menu_page.driver)
        report_list.order_report_list_order_desc('Name', 'Decending')
        assert report_list.check_order_name_desc(), "A lista não está ordenada"
