from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from .base_page import BasePage


class AddMemberPage(BasePage):

    def addmember_bymenual(self):
        # click 手动输入添加
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        from .edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

    def find_toast(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")
        # return True
