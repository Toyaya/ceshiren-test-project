import pytest


@pytest.fixture(params=[['tom', 123], ['jerry', 456], ['linda', 789]],
                ids=['tom', 'jerry', 'linda'])
def login(request):
    # request 是固定的写法，request.param
    return request.param
    # print("login")


# fixture提供给测试用例参数
def test_login(login):
    print(login)
