####1、pytest 规则(测试用例命名规范)
- 文件要在test_开头，或者_test结尾
- 类要以Test开头，方法要以test_开头
- 测试类不可以包含__init__()方法

####2、pytest 常用的命令行参数
- pytest --collect-only 只收集用例
- pytest -k “add ” 匹配所有名称中包含add的用例（‘add or div’ ‘TestClass’）
- pytest -m mark标签名 标记
- pytest - - junitxml=./result.xml 生成执行结果文件
- pytest --setup-show 回溯fixture的执行过程

####3、
#####模块级(setup_module/teardown_module)模块始末，全局的（优先最高）
#####函数级(setup_function/teardown_function)只对函数用例生效(不在类中)
#####类级(setup_class/teardown_class)只在类中前后运行一次（在类中）
#####方法级(setup_method/teardown_methond)开始于方法始末（在类中）
#####类里面的（setup/teardown）运行在调用方法的前后

####4、参数化
- 待测试的输入和输出是一组数据, 可以把测试数据组织起来,用不同的测试数据调用相同的测试方法
####5、数据驱动
- 数据驱动就是数据的改变从而驱动自动化测试的执行，最终引起测试结果的改变。

####6、参数化的用法
- 参数化装饰函数
- ids参数增加可读性
- 叠加参数化

####7、mark.parametrize参数化
- 场景：测试数据是传⼊的，测试的预期结果也是传⼊的，⼆个不同的参数⼀⼀对应，输⼊的数据经过调⽤执⾏后结果是否与预期⼀致
- 解决：使⽤mark中的@pytest.mark.parametrize进⾏参数化和数据驱动更灵活
- 应用：
-- 1、在方法，类上加上装饰器都可以，
-- 2、另外组合方式可以实现更多测试用例的自动生成
'''
@pytest.mark.parametrize('b', [1, 2, 3])
'''


