from selenium.webdriver.common.by import By
from .base_page import BasePage
from .add_party import AddPartyPage



class ContactPage(BasePage):

    __ele_addparty_top = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    __ele_addparty = (By.CSS_SELECTOR, ".js_create_party")

    def get_contact_list(self):
        # 获取的是元素列表
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        #print(ele_list)
        name_list= []
        # 遍历元素列表，通过元素的text 属性，提取文本数据信息
        for ele in ele_list:
            name_list.append(ele.text)
        #print(name_list)
        return name_list

    def goto_add_party(self):
        self.driver.implicitly_wait(10)
        self.find(self.__ele_addparty_top).click()
        self.driver.implicitly_wait(10)
        self.find(self.__ele_addparty).click()
        return AddPartyPage(self.driver)


    def check_party(self):
        # 每次调用前刷新界面，确保获取最新的页面数据
        self.driver.refresh()
        # 获取当前部门名称
        party_name = self.find_all(self.__ele_party_name)
        dp_name_list = [i.text for i in party_name]
        return dp_name_list


