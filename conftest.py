# from base.load_yaml import clear_yaml
import pytest
# from test_locust.test.sql_demo import Sql_Base

# 在所有接口请求之前执行
# @pytest.fixture(scope="session",autouse=True)
# def claer_txt():
#     '''用来清除接口关联的参数'''
#     clear_yaml()

@pytest.fixture(scope="function")
def connet_sql():
    def _connet_sql(sql):
        # Sql = Sql_Base('47.108.161.233', 'root', 'root', 'study', 3306)
        # value = Sql.selectDb(sql)

        print("之前{}".format(sql))
        #yield
        # # #Sql.closeDb()
        #print("之后l")
    return _connet_sql
@pytest.fixture(scope="function")
def connet():
    print("之前")
    yield
    print("之后")