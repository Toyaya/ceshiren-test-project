import json

import requests

from service.demo_test0523.api.base_api import BaseApi


class WeWork(BaseApi):
    # 可以不用加的，只是为了声明类型，python也开始支持类型了，是python3的一个技巧
    token: str = None

    def get_token(self):
        # r = requests.get(
        #     "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        #     params={
        #         "corpid": "wwd6da61649bd66fea",
        #         "corpsecret": "heLiPlmyblHRiKAgGWZky7MMvyld3d3QMUl5ra7NBZU"
        #     }
        # )

        # 具体的api对象通过这样的设计，可以实现数据化，为以后的自动生成垫定了一个好的基础
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            'method': 'get',
            "params": {
                "corpid": "ww6ce86bcfb747cf03",
                "corpsecret": "6aR7ZF7U3I2--0wlE0Qp3f-fqM7QH3yr850Zx5_X0g4"
            }
        }
        r = self.request(data)
        # print(r.status_code)
        assert r.status_code == 200
        self.token = r.json()['access_token']
        return self.token
        # print(self.token)

# if __name__ == '__main__':
#     we = WeWork()
#     we.get_token()

