import unittest

#继续该类的类就可以直接使用类中的夹具，夹具的封装
class MyUnit(unittest.TestCase):
    @classmethod  # 类方法装饰器
    def setUpClass(cls) -> None:
        print('创建日志，连接数据库，创建报告')

    def setUp(self) -> None:
        print('测试工作之前的准备工作')

    def tearDown(self) -> None:
        print('测试工作之后的收尾工作')

    @classmethod
    def tearDownClass(cls) -> None:
        print('销毁日志，关闭数据库，销毁报告')