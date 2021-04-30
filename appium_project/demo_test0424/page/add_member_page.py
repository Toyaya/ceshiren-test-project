from appium.webdriver.common.mobileby import MobileBy
from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep



class AddMemberPage(BasePage):

    def addmember_bymenual(self):
        # click 手动输入添加
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        from .edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

    def find_toast(self):
        # self.driver.implicitly_wait(5)
        toast = self.find(MobileBy.XPATH, "//*[@text='添加成功']")
        return toast.text

    def back_contactlist(self):
        def wait(x):
            return len(self.finds(MobileBy.XPATH, "//*[@text='添加成员']/../../../../android.widget.TextView")) >= 1

        WebDriverWait(self.driver, 10).until(wait)
        self.find(MobileBy.XPATH, "//*[@text='添加成员']/../../../../android.widget.TextView").click()





