#####元素定位

'''
//*代表任何字符，相对定位，找子孙节点
/绝对定位，只找子节点
'''
- 测试步骤三要素：
  - 定位、交互、断言
  
 #####动态页面配置参数："settings[waitForIdleTimeout]"页面处于空闲状态的超时时长
 #####定位：
- id 定位（优先级最高）
- XPath 定位（速度慢，定位灵活）
- Accessibility ID 定位（content-desc）
- Uiautomator 定位（仅Android 速度快，语法复杂）
- predicate 定位（仅 iOS ）

######skipDeviceInitialization跳过设备的初始化（包的安装，运行setting app）
#####dontStopAppOnReset每次执行的时候不重新打开，接着上次的页面

#####xpath表达式常用用法：
- 逻辑运算符 （not、and 、or等）
- 表达式 （contains、ends_with、starts_with等）

#####相对定位：

- //* ：当前页面所以字符串

- //*[contains(@resource-id, ‘login’)]（重点）

- //*[@text=‘登录’] （重点）

- //*[contains(@resource-id, ‘login’) and contains(@text, ‘登录’)] （重点）

- //*[contains(@text, ‘登录’) or contains(@class, ‘EditText’)]（了解）

- //*[ends-with(@text,'号') ] | //*[starts-with(@text,'姓名') ] 两个定位的集合列表（了解）

- //*[@clickable=“true"]//android.widget.TextView[string-length(@text)>0 and string-length(@text)<20]（了解）

- //*[contains(@text, ‘看点')]/ancestor::*//*[contains(@class, ‘EditText’)] （轴）（了解）获取前面匹配元素的所以祖辈元素

#####原生定位：原生定位
- Android 原生定位-Uiautomator

  - 官网：https://developer.android.com/reference/android/support/test/uiautomator/UiSelector.html

  - 写法：’new UiSelector().text(“text")'


- iOS 原生定位-PredicateString

  - 例如：

  - name == '测试'
  
  
#####Toast 定位:
- appium使用uiautomator底层的机制来分析抓取toast，并且把toast放到控件树里面，但本身并不属于控件。

- automationName：uiautomator2

- 使用xpath查找

  - //*[@class='android.widget.Toast']

  - //*[contains(@text, "xxxxx")]
  
//*[contains(@text,'姓名']/../*[@text='必填  ']:/../代表向上找父节点再找子节点

