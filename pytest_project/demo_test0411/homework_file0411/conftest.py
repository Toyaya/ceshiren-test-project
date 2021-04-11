import pytest
import yaml
from Calculator_demo import Calculator

#int的数据
def get_datas_int():
    with open("../datas/calc_int.yaml") as f:
        datas = yaml.safe_load(f)
    return datas

@pytest.fixture(params=get_datas_int()['int_datas'], ids=get_datas_int()['ids'])
def get_datas_int_calc(request):
    return request.param


#float数据
def get_datas_float():
    with open("../datas/calc_float.yaml") as f:
        datas = yaml.safe_load(f)
    return datas

@pytest.fixture(params=get_datas_float()['int_datas'], ids=get_datas_float()['ids'])
def get_datas_float_calc(request):
    return request.param

#div数据
def get_datas_div():
    with open("../datas/calc_div.yaml") as f:
        datas = yaml.safe_load(f)
    return datas

@pytest.fixture(params=get_datas_div()['int_datas'], ids=get_datas_div()['ids'])
def get_datas_div_calc(request):
    return request.param


@pytest.fixture(scope='class')
def initcalc_class():
    # setup
    print("setup")
    calc = Calculator()
    yield calc
    # teardown
    print("teardown")

def pytest_collection_modifyitems(session,config,items):
    print("这是收集所用用例的方法！！！")
    print(items)
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

