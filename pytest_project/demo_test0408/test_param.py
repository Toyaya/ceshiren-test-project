import pytest
# 测试用例命名规范
# 文件要在test_开头，或者_test结尾
# 类要以Test开头，方法要以test_开头
# 测试类不可以包含__init__()方法

# 常用参数
# pytest --collect-only 只收集用例
# pytest -k “add ” 匹配所有名称中包含add的用例（‘add or div’ ‘TestClass’）
# pytest -m mark标签名 标记, pytest -m mark标签名 -v/pytest -m login -v
# pytest - - junitxml=./result.xml 生成执行结果文件
# pytest --setup-show 回溯fixture的执行过程
# 更多的用法使用pytest —help查看帮助文档
#--lf 只执行上次失败的测试用例

def func(x):
    return x + 1

@pytest.mark.login
def test_answer():
    assert func(3) == 4

@pytest.mark.parametrize('key,result', [
    ['appium', 200], ['selenium', 200], ['requests', 200], ['docker', 300]
], ids=['a', 'b', 'c', 'd'])
def test_interface(key, result):
    url = f"http://ceshiren.com/key={key}"
    print(url, result)


@pytest.mark.parametrize('a,b', [
    [1, 1], [100, 100]
])
class TestDemo:
    def test_a(self, a, b):
        print(a, b)

    def test_b(self, a, b):
        print(a, b)


# a : int,string,float
# b:  1, 2, 3

# 笛卡尔积
@pytest.mark.parametrize('c', ['x', 'y', 'z'])
@pytest.mark.parametrize('b', [1, 2, 3])
@pytest.mark.parametrize('a,d', [['int', 'a'], ['string', 'b'], ['float', 'c']])
def test_ab(a, d, b, c):
    print(a, b, c, d)



