from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWX:
    def setup(self):
        # 初始化
        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "bf090a1c"
        caps["settings[waitForIdleTimeout]"] = 0
        caps["noReset"] = "true"
        # 客户端与服务端建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 隐式等待,更智能，中间任何时间等到某个元素都停止查找，继续往后执行，
        # 每次调用find_element的时候都会激活这种等待方式
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 资源消毁
        self.driver.quit()



    # def test_daka(self):
    #     # 测试用例
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
    #     # 强制等待
    #     # sleep(5)
    #     # uiautomator的定位方式，android 原生的定位方式，滚动查找某个 文字
    #     self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
    #                              'new UiScrollable(new UiSelector()'
    #                              '.scrollable(true).instance(0)).'
    #                              'scrollIntoView(new UiSelector().'
    #                              'text("打卡").instance(0));').click()
    #     # self.driver.update_settings({'waitForIdleTimeout':0})
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '次外出')]").click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")

    def test_add(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/ays").send_keys("砂糖1")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f4m").send_keys("13772127771")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()



