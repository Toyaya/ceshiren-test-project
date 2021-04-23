#####xpath定位：（文字全部匹配） //*[@text='工作台']
####xpath定位：（文字包含）  //*[contains(@text,'次外出')]

######adb logcat查看日志
#####滚动查找元素：
- self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));')

######查找5037端口：lsof -i tcp:5037
######kill pid


