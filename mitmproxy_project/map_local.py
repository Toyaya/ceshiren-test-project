"""HTTP-specific events."""
import json

import mitmproxy.http
from mitmproxy import http

class Events:


    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        # 匹配规则
        # if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" \
        #     in flow.request.url and "x=" in flow.request.url:
        #     with open("quote.json", encoding="utf-8") as f:
        flow.response = http.HTTPResponse.make(
            # 状态码
            200,
            # 响应体，传入的数据格式是string
            b"I'm a teapot",
            # 响应头
        )




    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        pass



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
