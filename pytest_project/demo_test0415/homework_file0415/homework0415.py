from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait


class TestDemo:
    def test_basepage(self,initcalc_class,get_data):
        driver = initcalc_class
        # print(get_data)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        for cookie in get_data:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        if len(driver.find_elements_by_id("js_tips")) >= 1:
            print("登录态过期，请重新登录")
        else:
            add_button = driver.find_elements_by_link_text("添加成员")
            def wait_add(x):
                return len(add_button) >= 1
            WebDriverWait(driver, 10).until(wait_add)
            # self.driver.implicitly_wait(10)
            sleep(5)
            driver.find_element_by_link_text("添加成员").click()
            driver.implicitly_wait(10)
            driver.find_element_by_id('username').send_keys("shatang")
            driver.find_element_by_id('memberAdd_acctid').send_keys("shatang")
            driver.find_element_by_id('memberAdd_phone').send_keys("13662767656")
            driver.find_element_by_link_text("保存").click()







