from .wework_api import WeWork


class TestWeWork:
    def setup_class(self):
        self.wework=WeWork()
        self.wework.get_token("ww37968f3659208e26", "ufKs6x_eUCsbXKY2A9ble799VrjjqnBoC-AcI2UnVnU")

    #新建group和tag
    def test_add_tag(self):
        r=self.wework.add_tag("autotag1","autotag2","autogroup")
        assert r.json()["errcode"] == 0
    #编辑tagname
    def test_edit_tag(self):
        r=self.wework.edit_tag("edited_tagname")
        assert r.json()["errcode"]==0
    #删除整个group
    def test_del_tag(self):
        r=self.wework.del_tag()
        assert r.json()["errcode"] == 0
