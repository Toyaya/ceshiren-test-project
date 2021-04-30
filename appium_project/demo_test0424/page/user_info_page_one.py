from .base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
from .user_info_page_two import UserInfoPageTwo
from time import sleep

class UserInfoPageOne(BasePage):
    __user_element = (MobileBy.ID, "com.tencent.wework:id/h8g")
    def goto_user_one(self):
        self.driver.implicitly_wait(5)
        self.find(*self.__user_element).click()
        return UserInfoPageTwo(self.driver)






