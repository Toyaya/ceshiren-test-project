import pytest
from ..page.main_page import MainPage



class TestAddMember:
    """
    编写测试用例
    """
    def setup_class(self):
        self.main_page = MainPage()


    # 1. 实现测试数据和页面对象分离
    # @pytest.mark.parametrize("username, accid, phone",[("伊泽2", "00903", "13344445527")])
    # def test_add_member(self, username, accid, phone):
    #            # 1. 跳转到添加成员页面  2. 添加成员   3. 获取成员列表
    #     name_list = self.main_page.goto_add_member().add_member(username, accid, phone).get_contact_list()
    #     assert username in name_list

    # @pytest.mark.parametrize("username, accid, phone",[("伊泽瑞尔11", "00901", "13344445555")])
    # def test_add_member_fail(self, username, accid, phone):
    #     data_list = self.main_page.goto_add_member().add_member_fail(username, accid, phone)
    #     err = [i for i in data_list if i != ""]
    #     assert "伊泽瑞尔" in err[0]

    @pytest.mark.parametrize("name", [("岁岁")])
    def test_add_part(self,name):
        party = self.main_page.goto_contact().goto_add_party().add_department(name).check_party()
        assert name in party






    # def test_xxx(self):
    #     main_page = MainPage()
    #     main_page.goto_add_member().add_xxx().add_member()
