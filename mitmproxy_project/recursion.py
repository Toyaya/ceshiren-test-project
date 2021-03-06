"""HTTP-specific events."""
import json

import mitmproxy.http
from mitmproxy import http

class Events:


    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        #匹配规则  #

        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" \
                    in flow.request.url and "x=" in flow.request.url:
            base_data = json.loads(flow.response.text)
            new_data = self.recursion(base_data,0)
            #这步返回给客户端
            flow.response.text = json.dumps(new_data)

    def recursion(self, data, int_data = 1):
        """

        :param data: 原始的数据
        :param int_data: 倍增的倍数
        :return: 在原始数据基础之上，修改float 类型，对float 类型做数据翻倍操作
        """
        #
        if isinstance(data, dict):
            # 如果是字典类型，继续递归value值
            for k, v in data.items():
                data[k] = self.recursion(v, int_data)
        elif isinstance(data, list):
            # 递归算法，如果是list 就继续遍历列表中的元素
            # data_new = []
            # for item in data:
            #     data_new.append(handle_data(item))
            # data_new = []
            # for i in data:
            #     data_new.append(recursion(i))

            # 40行~42 行等同于45行
            data = [self.recursion(i, int_data) for i in data]
        elif isinstance(data, float):
            # 对浮点型做倍增
            data = data * int_data
        else:
            data = data

        return data

addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    #使用debug模式启动mitmdump
    # mitmdump(['-p', '8080', '-s', __file__])
    #mitmdump -p 8080 -s /Users/lixu/project/hogwarts/HogwartsSDET18/test_mock/mitm_s.py
    # 端口需要使用字符串
    mitmdump(['-p', '8080', "-s", __file__])
