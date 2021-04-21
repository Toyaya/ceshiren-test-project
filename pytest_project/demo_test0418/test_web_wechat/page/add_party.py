from selenium.webdriver.common.by import By
from .base_page import BasePage
from .add_address import AddAddress

class AddPartyPage(BasePage):

    __party_name = (By.CSS_SELECTOR, '[name=name]')
    __party_select_btn = (By.CSS_SELECTOR, '.js_parent_party_name')
    __party_select_item = (By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688849985688939_anchor']")
    __confirm = (By.CSS_SELECTOR, '.ww_dialog_foot .ww_btn_Blue')


    def add_department(self,name):
        self.find(self.__party_name).send_keys(name)
        self.driver.implicitly_wait(10)
        self.find(self.__party_select_btn).click()
        self.find(self.__party_select_item).click()
        self.find(self.__confirm).click()
        return AddAddress(self.driver)




