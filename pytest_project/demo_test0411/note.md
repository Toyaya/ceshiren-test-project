####1、0408的作业解析：
#####区分int，float（取前几位四舍五入round(pi,2),Decimal(x,y)x指的是整数部分加小数部分的总长度,y表示小数部分的位数）
'''
try:
except Exception:( except ZeroDivisionError(除数等于0的报错方式):)
'''

####2、yaml：
- yaml.safe_load()读取yaml文件

####3、fixture：
- def login()添加装饰器@pytest.fixture()，实现参数化@pytest.fixture(params=[])
- ①<可以拿到返回数据>在测试用例def test_add_card(login)增加需要进行前置条件的函数
- ②@pytest.mark.usefixtures('login)
-  有选择性的使用前置条件

####Fixture 是为了测试⽤例的执⾏，初始化⼀些数据和⽅法
- 1、类似 setUp, tearDown 功能，但⽐ setUp, tearDown 更灵活
- 2、直接通过函数名字调⽤或使用装饰器@pytest.mark.usefixtures(‘test1’)
- 3、允许使用多个Fixture
- 4、使用 autouse 自动应用，如果要返回值，需要传fixture函数名eg：@pytest.fixture(autouse=true)
- 5、作用域（session>module>class>function）@pytest.fixture(scope=model) 
- -setup-show 回溯 fixture 的执行过程
- yield后面的内容是teardown

####4、pytest conftest.py 文件的用法
- 1、conftest.py文件名是不能换的
- 2、放在项目下是全局的数据共享的地方（全局的配置和前期工作都可以写在这里）
- 3、一般来说，conftest.py是用来存放fixture 方法的
- 4、conftest.py 文件就近生效（如果 在不同的文件夹下都有conftest.py）,离测试文件最近的那个conftest.py 生效)

####5、pytest 插件
- pip install pytest-ordering  控制用例的执行顺序 @pytest.mark.first
- pip install pytest-dependency   控制用例的依赖关系
- pip install pytest-xdist    分布式并发执行测试用例
- pip install pytest-rerunfailures   失败重跑
- pip install pytest-assume              多重较验
- pip install pytest-random-order  用例随机执行
- pip intall  pytest-html                    测试报告 

####6、pytest hook 函数
- 常用的hook 介绍
- pytest_collection_modifyitems
- item.name = item.name.encode('utf-8').decode('unicode-escape')
- item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')