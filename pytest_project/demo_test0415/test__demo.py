from selenium import webdriver
import yaml

'''
class  TestDemo:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)#隐式等待

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").click()
        self.driver.find_element_by_id("kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element_by_id("su").click()
        ele = self.driver.find_element_by_link_text("霍格沃兹测试学院 – 软件自动化测试开发培训_接口性能测试")
        assert ele
'''

class TestWork:

    def test_Wework(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("menu_contacts").click()
        print(self.driver.get_cookies())


    # def test_cookie(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    #     cookies =  [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850305931047'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'pk7yYMn2atfRV49W1XcE2dI5ow9fbe1YA_OMyMCT4YfBIaD6dPxeZukdAaUgwDD1f87Uu3SUQaFf7GYzRlEBuXTWf-0DRRhx5KvR7KR2iEC7jtlBTmxOkjmvinySozfdUMgK709QwbxTBumRVIvAjDNEOSxKNnwq6Jkw4Snu5JSiG-gKHxqqRWAmezEDGOKB938qfPwk97LRTBFQQf6BBDsHAI3jQHaVxg5DWU6vRp_Fln-TmZzJB3FJqol6cGfoJgcZ2DdN3P3chuVLBAu-Xg'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850305931047'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324992447047'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'd-lzaB6WuE_HXNsZwfpz7MNgKVnMt6PYi5jCFZYsC7ra5j_zh3Us4RFG1apCXXsz'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a658683'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650026803, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1620648524, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '632731678'}, {'domain': '.qq.com', 'expiry': 2147483700, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '80fe570a60836359d8db1653eb9d728f1fbff3558b410deae7d992ca27df258c'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '6775768636'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650028331, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618490816,1618492331'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'IEr9I0SiWL'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618492331'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '83272147670897'}, {'domain': 'work.weixin.qq.com', 'expiry': 1618522339, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '66j6na0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '1143702528'}, {'domain': '.work.weixin.qq.com', 'expiry': 1621084903, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
    #     for cookie in cookies:
    #         # print(cookie)
    #         self.driver.add_cookie(cookie)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    #
    #
    # def test_cookie_v2(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    #     with open("data.yaml",encoding="UTF-8") as f:
    #         yaml_data = yaml.safe_load(f)
    #         for cookie in yaml_data:
    #             print(cookie)
    #             self.driver.add_cookie(cookie)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")












