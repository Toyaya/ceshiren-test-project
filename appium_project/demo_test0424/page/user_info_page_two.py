from .base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
from .edit_user_info_page import EditUserInfoPage
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import logging

class UserInfoPageTwo(BasePage):
    __edit_element = (MobileBy.XPATH, "//*[@text='编辑成员']")
    def goto_user_two(self):
        try:
            self.driver.implicitly_wait(5)
            self.find(*self.__edit_element).click()
            return EditUserInfoPage(self.driver)

        except NoSuchElementException:
            print("未找到元素")
            logging.error(u"未找到元素")






