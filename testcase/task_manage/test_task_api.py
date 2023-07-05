from commons.request_util import RequestUtil


class Testtask:
    def get_root(self,method,url):
        res = RequestUtil().all_send_request(method=method, url=url)
        #print(res.json())
        return res
