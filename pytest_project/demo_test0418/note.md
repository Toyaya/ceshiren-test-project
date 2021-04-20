![Image text](https://ceshiren.com/uploads/default/original/2X/6/6a3a86d8eccd1b840f8c661c298af193f66e75ca.jpeg)
- 用作描述业务场景
- 封装了页面包含的操作

#######po六大原则
（- 每个公共方法代表页面所提供的服务
- 不要暴露页面太多的细节
- 不要把断言和操作细节混用
- 方法可以return到新打开的页面
- 不要把整页的内容都放到PO中
- 相同的行为会产生不同的结果，可以封装不同结果）

- 方法意义
  - 用公共方法代表UI所提供的功能
  - 方法应该返回其他的PageObject或者返回用于断言的数据
  - 同样的行为不同的结果可以建模为不同的方法
  - 不要在方法内加断言
- 字段意义
  - 不要暴露页面内部的元素给外部
  - 不需要建模UI内的所有元素
  
![Image text](https://ceshiren.com/uploads/default/original/2X/5/5c1135ead535208a39ba55ee948f4f2dcfa64617.png)
![Image text](https://ceshiren.com/uploads/default/optimized/2X/7/7c3a554aca37b345a08e39de74223b30514ee429_2_1200x864.png)
- 每个黄色的区块，代表页面对象即 python 中的 class
- 每条线 的起始端， 代表页面所提供的方法
- 每条线的结束段， 代表页面返回的对象/ 返回的断言信息

#####链式调用