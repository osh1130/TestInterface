import pytest
import requests

from commons.request_util import RequestUtil
from commons.yaml_util import YamlUtil


# autouse=True，Then all methods are executed automatically
#@pytest.fixture(scope='function',autouse=False)
def execute_sql():
    """
    before setup，after tear_down
    """
    print('Function before executing sql language exact assertion!!!')
    # You can use yield to wake up the execution of teardown, implementing setup and teardown in combination with yield
    yield "success"
    print('The code that executes after the function')


class TestPost:
    @pytest.mark.smoke
    def test_id(self):
        dic = {"id": 1}
        YamlUtil().write_yaml(dic)

    #@pytest.mark.smoke
    def test_get_post(self, get_id):
        url = "http://jsonplaceholder.typicode.com/posts"
        params = get_id
        #print(params)
        res = RequestUtil().all_send_request(method="get", url=url, params=params)
        #print(res.json())