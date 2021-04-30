from .base_page import BasePage
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import logging

class EditUserInfoPage(BasePage):

    def delete_member(self):
        try:
            self.driver.implicitly_wait(5)
            self.swipe_find('删除成员').click()
            self.swipe_find('确定').click()
            sleep(5)

        except NoSuchElementException:
            print("未找到元素")
            logging.error(u"未找到元素")




