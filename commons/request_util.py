import requests


class RequestUtil:
    sess = requests.session()
    def all_send_request(self, method, url, **kwargs):
        print("---------------")
        res = RequestUtil.sess.request(method, url, **kwargs)
        return res