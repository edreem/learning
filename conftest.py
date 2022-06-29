from base.load_yaml import read_yaml_key
import pytest
from base.request_util import RequestsUtil
import json
# from test_locust.test.sql_demo import Sql_Base
request = RequestsUtil()
read = read_yaml_key("Elab_bt_test","environment.yaml")
# 在所有接口请求之前执行
# @pytest.fixture(scope="session",autouse=True)
# def claer_txt():
#     '''用来清除接口关联的参数'''
#     clear_yaml()

# @pytest.fixture(scope="function")
# def connet_sql():
#     def _connet_sql(sql):
#         # Sql = Sql_Base('47.108.161.233', 'root', 'root', 'study', 3306)
#         # value = Sql.selectDb(sql)
#
#         print("之前{}".format(sql))
#         #yield
#         # # #Sql.closeDb()
#         #print("之后l")
#     return _connet_sql
# @pytest.fixture(scope="function")
# def connet():
#     print("之前")
#     yield
#     print("之后")
method = "post"
url = read + "/base/account/login"
data = {
    "account": "admin",
    "password": "sHH62docSdMsy8t/5OvDIg==",
    "adLogin": 0,
    "key": "FkLZ201dqdwDUmZR",
    "source": 0,
    "identification": "XwQLgrkvnFUrarqa",
    "kaptcha": "",
    "verificationCode": ""
}
data1 = json.dumps(data)
headers = {
    "content-type": "application/json"
}


@pytest.fixture(scope="session", autouse=True)
def login():
    """登录获取token"""
    res = request.request_send(method=method, url=url, data=data1)
    resp = res.text
    print(resp)
