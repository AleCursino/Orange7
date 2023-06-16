import time

from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ReportListPage(PageObject):

    att_report_name_filed = '[placeholder="Type for hints..."]'
    att_report_name_listbox = '[role="listbox"]'
    class_search_btn = 'orangehrm-left-space'
    class_table_card = 'oxd-table-card'
    class_cell_elements = 'oxd-table-cell'
    class_edit_page = 'orangehrm-main-title'
    css_select_include = '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(3) > div > div:nth-child(2) > div'
    class_label_include = 'oxd-label'
    class_dropdown_include = 'oxd-select-text'
    class_dropdown_value = 'oxd-select-text-input'
    att_dropdown_elements = '[role="option"]'
    class_save_button = 'orangehrm-left-space'
    xpath_reports_btn = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]'
    class_delete_button = 'bi-trash'
    class_header_col = 'oxd-table-header-cell'
    class_btn_sort = 'oxd-table-header-sort'
    class_component_sort = 'oxd-table-header-sort-dropdown-item'
    class_grid_action = 'oxd-table-cell-actions'
    class_edit_icon = 'bi-pencil-fill'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def find_report_by_name(self, reportname):
        self.driver.find_element(By.CSS_SELECTOR, self.att_report_name_filed).send_keys(reportname)
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, self.att_report_name_listbox).click()
        self.driver.find_element(By.CLASS_NAME, self.class_search_btn).click()
        time.sleep(3)
        card_elements = self.driver.find_elements(By.CLASS_NAME, self.class_table_card)
        if len(card_elements) == 0:
            raise Exception("Report não encontrado!")

        count_report = 0
        for item in card_elements:
            cell_elements = item.find_elements(By.CLASS_NAME, self.class_cell_elements)
            for cell in cell_elements:
                if reportname in cell.text:
                    count_report += 1

        if count_report == len(card_elements):
            return True
        else:
            return False

    def order_report_list_order_desc(self, column_name='Name', order_type='Decending'):
        row_elements = self.driver.find_elements(By.CLASS_NAME, self.class_header_col)
        for element in row_elements:
            if element.text == column_name:
                element.find_element(By.CLASS_NAME, self.class_btn_sort).click()
                time.sleep(4)
                menu_items = self.driver.find_elements(By.CLASS_NAME, self.class_component_sort)
                for order_item in menu_items:
                    if order_item.text == order_type:
                        order_item.click()
                        break
                break

    def check_order_name_desc(self):
        all_reports = self.driver.find_elements(By.CLASS_NAME, self.class_table_card)
        reports_list = []
        for i in range(len(all_reports)):
            css_name_element = '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.orangehrm-paper-container > div.orangehrm-container > div > div.oxd-table-body > div:nth-child('+ str(i+1) +') > div > div:nth-child(2) > div'
            name_element = self.driver.find_element(By.CSS_SELECTOR, css_name_element)
            reports_list.append(name_element.text)

        reports_list_copy = reports_list.copy()
        reports_list_upper = [x.upper() for x in reports_list]
        reports_list_copy_upper = [x.upper() for x in reports_list_copy]
        reports_list_copy_upper.sort(reverse=True)

        if reports_list_upper == reports_list_copy_upper:
            return True
        return False

    def select_include_item(self, item_to_be_select='Current and Past Employees'):
        grid_items = self.driver.find_elements(By.CSS_SELECTOR, self.css_select_include)
        time.sleep(2)
        for item in grid_items:
            if item.find_element(By.CLASS_NAME, self.class_label_include).text == 'Include':
                item.find_element(By.CLASS_NAME, self.class_dropdown_include).click()
                time.sleep(2)
                # Localizar o item específico no menu suspenso usando seu seletor
                menu_items = item.find_elements(By.CSS_SELECTOR, self.att_dropdown_elements)
                for menu_tem in menu_items:
                    if menu_tem.text == item_to_be_select:
                        menu_tem.click()
                        # tempo de sleep so para ver que o item foi selecionado corretamente
                        time.sleep(2)
                        break
                break

    def get_include_value(self):
        grid_items = self.driver.find_elements(By.CSS_SELECTOR, self.css_select_include)
        time.sleep(2)
        for item in grid_items:
            if item.find_element(By.CLASS_NAME, self.class_label_include).text == 'Include':
                selected_option = item.find_element(By.CLASS_NAME, self.class_dropdown_value).text
                return selected_option

    def edit_report(self, report_name):
        found_report = self.find_report_by_name(report_name)
        if not found_report:
            return False
        else:
            grid_actions = self.driver.find_elements(By.CLASS_NAME, self.class_grid_action)
            for item in grid_actions:
                item.find_element(By.CLASS_NAME, self.class_edit_icon).click()
                time.sleep(3)
            #validar que é estamos editando o relatório correto
            if self.driver.find_element(By.CLASS_NAME, self.class_edit_page).text == 'Edit Report':
                self.select_include_item('Current and Past Employees')
                time.sleep(3)
                self.driver.find_element(By.CLASS_NAME, self.class_save_button).click()
                time.sleep(3)
            else:
                return False

            return self.verify_edit_report(report_name, 'Current and Past Employees')

    def verify_edit_report(self, report_name, include_option):
        self.driver.find_element(By.XPATH, self.xpath_reports_btn).click()
        time.sleep(3)
        found_report = self.find_report_by_name(report_name)
        if not found_report:
            return False
        else:
            grid_actions = self.driver.find_elements(By.CLASS_NAME, self.class_grid_action)
            for item in grid_actions:
                item.find_element(By.CLASS_NAME, self.class_edit_icon).click()
                time.sleep(3)
            # validar que é estamos editando o relatório correto
            if self.driver.find_element(By.CLASS_NAME, self.class_edit_page).text == 'Edit Report':
                option = self.get_include_value()
                if option == include_option:
                    return True
                else:
                    return False

    def delete_report(self, report_name):
        found_report = self.find_report_by_name(report_name)
        if not found_report:
            return False
        else:
            self.driver.find_element(By.CLASS_NAME, self.class_delete_button).click()
            time.sleep(3)

            super().click_yes_delete_btn_modal()

            self.driver.find_element(By.CLASS_NAME, self.class_search_btn).click()
            time.sleep(3)
            card_elements = self.driver.find_elements(By.CLASS_NAME, self.class_table_card)
            if len(card_elements) == 0:
                return True
            else:
                return False
