# module 对应模块级别
# @pytest.fixture(scope="module")
# def a():
#     print("测试auto")


# @pytest.mark.usefixtures('connectDb')
def test_search(connectDb):
    print(connectDb)
    print("搜索")


def test_add_cart():
    print("添加购物车")


def test_order(login, connectDb):
    username, pasword = login
    print(username, pasword)
    print("订单")
