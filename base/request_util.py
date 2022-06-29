import requests
import json


class RequestsUtil:
    session = requests.session()

    def request_send(self, method, url, data=None, **kwargs):
        method = str(method).lower()
        res = None
        if method == "get":
            try:
                res = RequestsUtil.session.request(method=method, url=url, params=data, **kwargs)
            except Exception as e:
                print("请求失败" % e)
        elif method == "post":
            if data:
                str_data = json.dumps(data)
            res = RequestsUtil.session.request(method=method, url=url, data=str_data, **kwargs)
        else:
            pass
        return res
