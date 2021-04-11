import allure



#
# def test_get_datas(get_datas_calc):
#     print(get_datas_calc)
@allure.feature("计算器")
class TestDemo:
    @allure.story("整数相加")
    def test_add_int(self, initcalc_class, get_datas_int_calc):
        assert get_datas_int_calc[2] == initcalc_class.add(get_datas_int_calc[0], get_datas_int_calc[1])

    @allure.story("浮点数相加")
    def test_add_float(self, initcalc_class, get_datas_float_calc):
        assert get_datas_float_calc[2] == round(initcalc_class.add(get_datas_float_calc[0], get_datas_float_calc[1]),2)

    @allure.story("相除")
    def test_div(self, initcalc_class, get_datas_div_calc):
        try:
            assert get_datas_div_calc[2] == initcalc_class.div(get_datas_div_calc[0], get_datas_div_calc[1])
        except ZeroDivisionError:
            print("除数为0")







