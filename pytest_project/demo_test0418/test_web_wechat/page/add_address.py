from selenium.webdriver.common.by import By
from .base_page import BasePage

class AddAddress(BasePage):
    __ele_party_name = (By.CSS_SELECTOR, '.jstree-anchor')

    def check_party(self):
        # 每次调用前刷新界面，确保获取最新的页面数据
        self.driver.refresh()
        # 获取当前部门名称
        party_name = self.find_all(self.__ele_party_name)
        party_name_list = [i.text for i in party_name]
        print(party_name_list)
        return party_name_list