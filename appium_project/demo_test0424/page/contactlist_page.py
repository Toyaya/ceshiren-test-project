from appium.webdriver.common.mobileby import MobileBy
import logging
from .add_member_page import AddMemberPage
from .base_page import BasePage
from.user_info_page_one import UserInfoPageOne


class ContactListPage(BasePage):
    # __member_element = (MobileBy.XPATH, "//*[@text='企业通讯录']/..//android.widget.RelativeLayout")
    __member_list = (MobileBy.XPATH,"//*[@text='我的客户']/../..//android.widget.ImageView")

    def goto_addmember(self):
        # click 添加成员
        self.swipe_find('添加成员').click()
        return AddMemberPage(self.driver)

    def goto_deletemember(self):
        many = len(self.finds(*self.__member_list))
        print(many)
        if many > 2:
            self.finds(*self.__member_list)[1].click()
            return UserInfoPageOne(self.driver)
        else:
            logging.error(u"没有可删除的联系人了！")


