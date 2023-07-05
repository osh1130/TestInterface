import pytest

#def read_yaml():
#    return [1]

@pytest.fixture(scope="function",autouse=False,params=[{"id":1},{"id":2}],name='get_id')
def get_param(request):
     return request.param