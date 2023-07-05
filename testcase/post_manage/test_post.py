import pytest
import requests

from commons.request_util import RequestUtil
from commons.yaml_util import YamlUtil

class TestPost:
    id = 1


    #@pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml("testcase\post_manage\get_post.yaml"))
    def test_01_get_post(self,caseinfo):
        #print(caseinfo)
        url = caseinfo["request"]["url"]
        method = caseinfo["request"]["method"]
        params = caseinfo["request"]["params"]
        res = RequestUtil().all_send_request(method=method, url=url, params=params)
        #print(res.json())

    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml("testcase\post_manage\post_post.yaml"))
    def test_02_post_post(self, caseinfo):
        #print(caseinfo)
        url = caseinfo["request"]["url"]
        method = caseinfo["request"]["method"]
        data = caseinfo["request"]["data"]
        headers = caseinfo["request"]["headers"]
        res = RequestUtil().all_send_request(method=method, url=url, data=data,headers = headers)
        # print(res.json())

    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml("testcase\post_manage\put_post.yaml"))
    def test_03_put_post(self, caseinfo):
        # print(caseinfo)
        url = caseinfo["request"]["url"] + str(TestPost.id)
        method = caseinfo["request"]["method"]
        data = caseinfo["request"]["data"]
        headers = caseinfo["request"]["headers"]
        res = RequestUtil().all_send_request(method=method, url=url, data=data, headers=headers)
        #print(res.json())

    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml("testcase\post_manage\patch_post.yaml"))
    def test_04_patch_post(self, caseinfo):
        # print(caseinfo)
        url = caseinfo["request"]["url"] + str(TestPost.id)
        method = caseinfo["request"]["method"]
        data = caseinfo["request"]["data"]
        headers = caseinfo["request"]["headers"]
        res = RequestUtil().all_send_request(method=method, url=url, data=data, headers=headers)
        #print(res.json())

    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml("testcase\post_manage\delete_post.yaml"))
    def test_05_delete_post(self, caseinfo):
        # print(caseinfo)
        url = caseinfo["request"]["url"] + str(TestPost.id)
        method = caseinfo["request"]["method"]
        res = RequestUtil().all_send_request(method=method, url=url)
        #print(res.json())

