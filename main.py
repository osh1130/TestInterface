# This is a sample Python script.
import os
import time
import pytest


if __name__ == '__main__':
    #runner = YamlRunner()
    #runner.run_test()
    # YamlUtil().read_yaml()
    pytest.main()
    time.sleep(1)
    os.system("allure generate  ./temps -o reports --clean")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
