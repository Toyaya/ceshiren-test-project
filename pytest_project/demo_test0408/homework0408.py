import pytest
from Calculator_demo import Calculator

class TestCal:
    def setup_class(self):
        print("setup")
        self.calc = Calculator()

    def teardown_class(self):
        print("teardown")

    @pytest.mark.parametrize('a,b,expect1', [
        [1, 1, 2], [0.1, 0.1, 0.2], [1000, 1000, 2000], [0, 1000, 1000]
    ], ids=['int1', 'float', 'bignum', 'zeronum'])
    def test_add(self, a, b, expect1):
        assert expect1 == self.calc.add(a, b)

    @pytest.mark.parametrize('c,d,expect2',[[6, 3, 2],[3,0,'Fail'],[1,0.1,10],[0.1,5,0.02],[-10,2,-5],[10,-5,-2],[0,2,0],[0,-5,0]])
    def test_div(self, c, d, expect2):
        if d == 0:
            pytest.xfail(reason='除数不能为0')
        else:
            assert expect2 == self.calc.div(c, d)






