import os
import sys
import time
import unittest

#模块级别的夹具
# def setUpModule():
#     print('模块级别的前置夹具')
#
# def tearDownModule():
#     print('模块级别的后置夹具')
from HTMLTestRunner import HTMLTestRunner

from UnitTest.my_unit import MyUnit

#@unittest.skip("此类暂不执行")
class print01(MyUnit):
    age = 23
    # @classmethod #类方法装饰器
    # def setUpClass(cls) -> None:
    #     print('创建日志，连接数据库，创建报告')
    #
    # def setUp(self) -> None:
    #     print('测试工作之前的准备工作')
    #@unittest.skip('此命令不执行')

    def test01(self):
        """测试知了"""
        #self.assertEqual(1==2)
        #raise  Exception("自定义异常") #抛出异常的操作
        #self.assertTrue(0)  # 断言判断为错
        print('测试知了')

    @unittest.skip("微微老师")
    def test02(self):
        #self.assertTrue(0)  # 断言判断为错
        print('测试微微')

    @unittest.skipIf(age>18 and age<25,"如果鲁班在18到25岁之间就忽略")
    def test03(self):
        print('测试鲁班')

    #@unittest.skipUnless(age<18 and age>25,"如果鲁班未成年忽略")
    def test04(self):
        """测试鲁班"""
        print('测试鲁班')
    # def tearDown(self) -> None:
    #     print('测试工作之后的收尾工作')
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('销毁日志，关闭数据库，销毁报告')
# class print03():
#     def test05(self):
#         print('测试周围')
