import yaml
from selenium import webdriver


class BasePage:
    """
    把页面重复的步骤抽离出来，封装，比如driver 的实例化
    """
    # 没有参数传入， 会取默认None ,如果有参数传入,会取传入的参数
    def __init__(self, base_driver=None):
        """
        driver 重复实例化会 导致页面启动多次
        解决driver 重复实例化的问题
        :param base_driver:
        """
        if base_driver == None:
            # 实例化 driver
            self.driver = webdriver.Chrome()
            # 访问扫码登录页面
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            # with open("data.yaml", encoding="UTF-8") as f:
            #     yaml_data = yaml.safe_load(f)
            #     print(yaml_data)
            yaml_data = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850305931047'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850305931047'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '2823939020'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324992447047'}, {'domain': '.qq.com', 'expiry': 1619090612, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1290886337.1618986436'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'd-lzaB6WuE_HXNsZwfpz7GYs93HvGmCPtpyjy_VOnyTdk3xDOFo2KTJHjMQ8JhUx'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a9260545'}, {'domain': '.qq.com', 'expiry': 1620801631, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False, 'value': 'o0632731678'}, {'domain': '.qq.com', 'expiry': 1619004267, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1619004207'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '451628101405614'}, {'domain': 'work.weixin.qq.com', 'expiry': 1619017970, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': 'lc941q'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'pNr1IUSKWr'}, {'domain': '.qq.com', 'expiry': 1620801631, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': False, 'value': '00010000c94284c620a987b9c8f451dc3b47383a46c4a29adae5cccda176776e705bf906a19de5b5a5d9caf6'}, {'domain': '.work.weixin.qq.com', 'expiry': 1621596215, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1682076212, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.140272644.1618118883'}, {'domain': '.work.weixin.qq.com', 'expiry': 1646392713, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'ivEPslMbxQl3PXI54waWyAd1E5rysfnLrF2K8nJjCN1WgcMagsh49lETK7Oz7T2lBinv-FSj1icyxqKxjPDNrIgHRPPsEUKhQwUYchiNMNYOjryRl93oArSsNQuqqdfLbH8znBDt3WxAZZawpv1rwO1zDKEpRb278mFGsW-YdJnmdG6bmDs7fPiz1vOM0vv8LowayTN5oP38Clhi7cx2cKyM-doH8bIqF1tV70YuVS06xLyk5FXb3vHUG241-pJ7HAfHu9oMW6CTWGHeWtKktw'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650540206, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618217974,1618986436,1618995682,1619004207'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1619596462, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '18116036673'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'ff7f7b568ad13cc95aac97e34d2f704a4382fa7dc13efc84f2a0de5a81b3f8eb'}]
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # 隐式等待，每一次调用find 方法，就会轮询查找元素是否存在
            self.driver.implicitly_wait(3)
        else:
            self.driver = base_driver

    def find(self, by, ele = None):
        """
        :param by: 定位方式 css, xpath, id
        :param ele: 元素定位信息
        :return:
        """
        # 两种传入定位元素的方式，提高代码的兼容性
        # 如果传入的是元祖,那就只有一个参数
        if ele == None:
            # 比如传入(By.ID, "username")
            # * 的作用是 解元祖 self.driver.find_element(*username) 等同于
            # self.driver.find_element(By.ID, "username")
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, ele)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

