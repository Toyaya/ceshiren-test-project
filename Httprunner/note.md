##### har2case mulu/xxx.har 默认生出pytest python格式
##### har2case mulu/xxx.har -2j 生出json格式
##### har2case mulu/xxx.har -2y 生出yaml格式

#####.with_jmespath("body.data.list.0.id","id")   参数化关联：把提取出来的值 命名为id。 后续通过$id来引用。和.extract().with_jmespath
#####.with_jmespath("cookie.Jwt-Token","token") jmespath不支持-（短线）。需要写成.with_jmespath('cookie."Jwt-Token"',"token")
"${fuction()}"引用debugtalk里的函数
#####.export()输出,方便其他用例引用 。作用域为当前py文件
.call()时，传参默认为当前py文件的传参

```
calss TestCaseXx(HttpRunner):
  
  config = Config("testcase description").verify(False).variables(**{
    "uid":"68851" #全局变量
  })
  
  teststeps = [
  step(
  RunRequest("用例名称")
  .post("url")
  .with_headers(
    **{
    header
    }
  )
  .with_json({json})
  .extract() #从相应里面提取东西
  .with_variables(**{
  "name":"toya"})   #定义局部变量
  .with_jmespath("body.data.list.0.id","id") 
  .validate()#校验
  .assert_equal("status_code",200)
  .teardown_hook("${function()}","return_value")#后置处理，运行一个函数，把返回值赋值
    
)
]

```
#####查看测试报告
- 默认pytest  hrun har/login.yml --html=login.html
- allure报告：①安装：pip install "httprunner[allure]" 或者 pip install allure-pytest ②运行：hrun testcase --alluredir=allurereports/ ; allure serve allurereports

#####性能测试
- 安装：pip install "httprunner[locust]" 或者 pip install locust
- 运行: locust -f testcases/mubu_login_test.py


