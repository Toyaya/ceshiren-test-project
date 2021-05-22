import json

import requests

class WeWork:
    def get_token(self, id, secret):
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                       params={"corpid": id,
                               "corpsecret": secret
                               })
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        self.token=r.json()["access_token"]
        print(self.token)

    def add_tag(self,tagname1,tagname2,groupname):
        r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                        params={"access_token":self.token},
                        json={
                            "group_name": groupname,
                            "tag": [
                                {
                                "name": tagname1},
                                {
                                "name": tagname2}
                            ]})
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        self.groupid=r.json()["tag_group"]["group_id"]
        print(self.groupid)
        self.tagid1=r.json()["tag_group"]["tag"][0]["id"]
        print(self.tagid1,"-------------")
        return r

    def edit_tag(self,new_name):
        r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
                        params={"access_token":self.token},
                        json={
                                "id": self.tagid1,
                                "name": new_name
                            })
        print(json.dumps(r.json(),indent=2,ensure_ascii=False))
        return r

    def del_tag(self):
        r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                        params={"access_token":self.token},
                        json={
                            "group_id": [
                                self.groupid
                            ]
                        })

        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r