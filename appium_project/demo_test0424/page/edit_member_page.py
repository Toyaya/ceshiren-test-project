from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from .base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self, name, phonenum):
        # input name
        # input phonenum
        # click 保存
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'姓名')]/../"
                  "android.widget.EditText").send_keys(name)
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'手机')]/..//"
                  "android.widget.EditText").send_keys(phonenum)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        from .add_member_page import AddMemberPage
        return AddMemberPage(self.driver)
