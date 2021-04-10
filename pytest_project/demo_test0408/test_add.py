import pytest
from Calculator_demo import Calculator

'''
模块级(setup_module/teardown_module)模块始末，全局的（优先最高）
函数级(setup_function/teardown_function)只对函数用例生效(不在类中)
类级(setup_class/teardown_class)只在类中前后运行一次（在类中）
方法级(setup_method/teardown_methond)开始于方法始末（在类中）
类里面的（setup/teardown）运行在调用方法的前后
'''


class TestCal:
    def setup_class(self):
        print("setup")
        self.calc = Calculator()

    def teardown_class(self):
        print("teardown")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [0.1, 0.1, 0.2], [1000, 1000, 2000], [0, 1000, 1000]
    ], ids=['int1', 'float', 'bignum', 'zeronum'])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)


    def test_add1(self):
        #calc = Calculator()
        assert 0.2 == self.calc.add(0.1,0.1)

    def test_add2(self):
        # calc = Calculator()
        assert 2000 == self.calc.add(1000, 1000)

    def test_add2(self):
        # calc = Calculator()
        assert 1000 == self.calc.add(0, 1000)





