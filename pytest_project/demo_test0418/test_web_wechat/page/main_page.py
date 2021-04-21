from selenium.webdriver.common.by import By
from .add_member import AddMemberPage
from .base_page import BasePage
from  .contact import ContactPage
from .add_address import AddAddress



class MainPage(BasePage):
    """
    用公共方法代表UI所提供的功能
    """
    # __ele_contact = (By.ID, "menu_contacts")

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        self.driver.find_element(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        # 返回要跳转页面的实例对象

        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return AddMemberPage(self.driver)

    def goto_upload_member(self):
        self.driver.find_elements(By.CSS_SELECTOR, ".index_service_cnt_item")[1].click()
        return AddAddress(self.driver)

