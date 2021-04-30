from faker import Faker

from ..page.app import  App

from ..utils.contact_info import ContactInfo


class TestContact:
    # def setup_class(self):
    #     self.contactinfo = ContactInfo()
    #     self.app = App()
    #
    # def setup(self):
    #     # 启动 app
    #     self.main = self.app.start().goto_main()
    #
    # def teardown(self):
    #     self.app.restart()
    #
    # def teardown_class(self):
    #     self.app.stop()

    # def test_addcontact(self):
    #     name = self.contactinfo.get_name()
    #     phonenum = self.contactinfo.get_phonenum()
    #     self.main.goto_contactlist().goto_addmember().addmember_bymenual().edit_member(name, phonenum).find_toast()


    def test_addcontact(self,initcalc_class,initcalc_fake):
        contactinfo = initcalc_fake
        name = contactinfo.get_name()
        phonenum = contactinfo.get_phonenum()
        main = initcalc_class
        su = main.goto_main().goto_contactlist().goto_addmember().addmember_bymenual().edit_member(name, phonenum).find_toast()
        assert '添加成功' in su


    def test_deletecontact(self,initcalc_class):
        main = initcalc_class
        su = main.goto_main().goto_contactlist().goto_deletemember().goto_user_one().goto_user_two().delete_member()



