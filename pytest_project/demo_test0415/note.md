#####复用浏览器(只有chrome）
'''
Google\ Chrome --remote-debugging-port=9222
'''
#####隐式等待：设置一个等待时间，轮询查找（默认0.5），元素是否出现，如果没出现就抛出异常
'''
self.driver.implicitly_wait(10)
'''
#####显示等待:在代码中定义等待条件，当条件发生时才继续执行代码。
- 每隔一段时间进行条件判断(默认0.5))，如果条件成立，则执行下一步，否则则继续等待，直到超过设置的最长时间。
'''
def wait_add(x):
    return len(driver.find_elements_by_link_text("添加成员")) >= 1
WebDriverWait(driver, 10).until(wait_add)
'''