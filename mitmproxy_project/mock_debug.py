"""HTTP-specific events."""
import json

import mitmproxy.http


class Events:
    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        """
            An HTTP CONNECT request was received. Setting a non 2xx response on
            the flow will return the response to the client abort the
            connection. CONNECT requests and responses do not generate the usual
            HTTP handler events. CONNECT requests are only valid in regular and
            upstream proxy modes.
        """
        pass

    def requestheaders(self, flow: mitmproxy.http.HTTPFlow):
        """
            HTTP request headers were successfully read. At this point, the body
            is empty.
        """
        pass
    #
    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        pass

    def responseheaders(self, flow: mitmproxy.http.HTTPFlow):
        """
            HTTP response headers were successfully read. At this point, the body
            is empty.
        """
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        # 实现rewrite，重写响应数据信息
        # 判断请求的url 是否包含指定的url信息
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            # 拿到响应数据信息
            # flow.response.text 是str 属性，所以如果要是操作
            # 这个对象的话，必须转换为python 字典的数据结构
            # 否则就只能使用和str 相关的 方法
            data = json.loads(flow.response.text)
            data["data"]["items"][0]["quote"]["name"] = "hogwartsssssssssss"
            flow.response.text = json.dumps(data)
        # if "http://stuq.ceshiren.com:8089/report/showMapLocal" in flow.request.url:
        #     flow.response.text = '{"resultCode":1,"message":"成功","data":"hogwarts"}'
        #     print(flow.response.text)

    def error(self, flow: mitmproxy.http.HTTPFlow):
        """
            An HTTP error has occurred, e.g. invalid server responses, or
            interrupted connections. This is distinct from a valid server HTTP
            error response, which is simply a response with an HTTP error code.
        """
        pass


addons = [Events()]
if __name__ == '__main__':

    from mitmproxy.tools.main import mitmdump
    # 使用debug模式启动mitmdump
    # 需要传入的是一个列表，列表包含命令行所使用的启动参数信息
    # 端口传入必须为字符串的格式
    #mitmdump -p 8888 -s /Users/lixu/project/HogwartsLG7/test_mock/mitm_s.py
    mitmdump(['-p', '8080', '-s', __file__])
