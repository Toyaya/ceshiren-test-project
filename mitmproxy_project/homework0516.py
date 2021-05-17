import json
import mitmproxy.http

class Page:

    def response(self,flow:mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?" in flow.request.url and "x=" in flow.request.url:
            data = json.loads(flow.response.text)
            data["data"]["items"][0]["quote"]["name"] = "toyaya1"
            data["data"]["items"][1]["quote"]["name"] = "toyaya2"
            data["data"]["items"][2]["quote"]["name"] = "toyaya3"
            data["data"]["items"][3]["quote"]["name"] = "toyaya4"

            data["data"]["items"][0]["quote"]["current"] = "0"

            data["data"]["items"][0]["quote"]["percent"] = "0.01"
            data["data"]["items"][1]["quote"]["percent"] = "0"
            data["data"]["items"][2]["quote"]["percent"] = "-3.00"
            data["data"]["items"][3]["quote"]["percent"] = "65.9287626373839393003039383873737373"

            flow.response.text = json.dumps(data)


addons = [
    Page()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p', '1130', "-s", __file__])


