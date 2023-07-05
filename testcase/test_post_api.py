import pytest
import requests

from commons.request_util import RequestUtil
from commons.yaml_util import YamlUtil


class TestPostApi:
    id = 1
    #def setup_class(self):
        #print('Each class is executed once before, typically to create log objects, create database connections, and so on')
        #print("setup_class")

    # setup_method和setup的功能一样，一起用时在setup之前执行
    def setup(self):
        #print('Do this once before each use case: typically to open a browser, load a web page, start a log for use cases, etc')
        print("setup")

    def teardown(self):
        #print('This is done after each use case: typically to close the browser, end the log of the use case, etc')
        print("teardown")

    #def teardown_class(self):
        #print('This is performed once after each class, typically to destroy log objects, destroy database connections, and so on')
        #print("teardown_class")

    def test_filter_post(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        data = {
            "userid": 1,
            # "token": YamlUtil().read_yaml("access_token")
        }
        res = requests.get(url=url, data=data)
        #print(res.json())

#if __name__ == '__main__':  # 程序执行的入口
#    TestPostApi()