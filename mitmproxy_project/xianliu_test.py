import mitmproxy.http
from mitmproxy import ctx
import json


class Count:
    def __init__(self):
        self.sum = 0
        self.count = 0
        self.url = "https://bbs-api.mihoyo.com/post/wapi/userFavouritePost?"


    def request(self, flow: mitmproxy.http.HTTPFlow):
        if self.url in flow.request.url:
            self.sum = self.sum + 1
        else:
            ctx.log.info("没有请求")
        # 需要有个if判断

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if self.url in flow.request.url:
            response_data = json.loads(flow.response.text)
            ctx.log.info(f"总数!!!{self.sum}")
            if response_data['data']['list'][0]['post']['post_id'] == '6742971':
                self.count = self.count + 1
                ctx.log.info(f"出现次数!!!{self.count}")
            else:
                ctx.log.info("没有数据")





addons = [
    Count()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p', '8080', "-s", __file__])