import pytest
from ..page.main_page import MainPage
import allure


@allure.feature("企业微信网页版测试")
class TestAddMember:
    """
    编写测试用例
    """
    def setup_class(self):
        self.main_page = MainPage()


    # 1. 实现测试数据和页面对象分离
    @allure.story("验证添加成员")
    @pytest.mark.parametrize("username, accid, phone",[("伊泽2", "00903", "13344445527")])
    def test_add_member(self, username, accid, phone):
               # 1. 跳转到添加成员页面  2. 添加成员   3. 获取成员列表
        name_list = self.main_page.goto_add_member().add_member(username, accid, phone).get_contact_list()
        assert username in name_list

    @allure.story("验证添加成员失败")
    @pytest.mark.parametrize("username, accid, phone",[("伊泽瑞尔11", "00901", "13344445555")])
    def test_add_member_fail(self, username, accid, phone):
        data_list = self.main_page.goto_add_member().add_member_fail(username, accid, phone)
        err = [i for i in data_list if i != ""]
        assert "伊泽瑞尔" in err[0]

    @allure.story("验证添加部门")
    @pytest.mark.parametrize("name", [("岁岁2")])
    def test_add_part(self,name):
        party = self.main_page.goto_contact().goto_add_party().add_party(name).check_party()
        assert name in party

    @allure.story("验证批量上传文件添加成员")
    def test_upload_member(self):
        address_name = self.main_page.goto_upload_member().import_address_book().get_contact_list()
        assert address_name != []




