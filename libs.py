import yaml

from testcase.task_manage.test_task_api import Testtask


class YamlRunner:
    def __init__(self):
        #discover testcase waiting for execute
        self.test_list = []
        self.api_client = Testtask()
        with open("testcase/task_manage/test_root.yaml") as f:
            self.test_list.append(yaml.safe_load(f))

    def run_test(self):
        case = self.test_list[0]
        #print(case)
        get_root_api = getattr(self.api_client, case['title'])
        res = get_root_api(**case['requests'])
        #print(res.status_code)
        assert res.status_code == case['respond']['status_code']
