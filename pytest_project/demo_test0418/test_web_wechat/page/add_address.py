from selenium.webdriver.common.by import By
from .base_page import BasePage
from .contact import ContactPage

class AddAddress(BasePage):
    # 上传文件
    __upload_file = (By.ID, 'js_upload_file_input')
    # 确认按钮
    __sure_upload_btn = (By.ID, 'submit_csv')
    # 前往查看按钮
    __goto_check_btn = (By.ID, 'reloadContact')


    def import_address_book(self):
        self.find(self.__upload_file).send_keys(r'/Users/xuxin.ma/Toyaya/ceshiren-test-project/pytest_project/demo_test0418/test_web_wechat/testcase/member.xlsx')
        self.driver.implicitly_wait(10)
        self.find(self.__sure_upload_btn).click()
        self.driver.implicitly_wait(10)
        self.find(self.__goto_check_btn).click()
        return ContactPage(self.driver)
