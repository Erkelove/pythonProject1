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
        self.assertEqual(1==2)
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
        print('测试鲁班')
    # def tearDown(self) -> None:
    #     print('测试工作之后的收尾工作')
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('销毁日志，关闭数据库，销毁报告')
class print03():
    def test05(self):
        print('测试周围')


if __name__ == '__main__':

    # print('进入main')
    # print(sys.argv) #模块的完整路径
    # unittest.main(defaultTest=['print01.test02'],verbosity=1) #用main方法执行用例
    #使用测试套件执行用例1
    # suite = unittest.TestSuite()
    # suite.addTest(print01('test02'))
    # suite.addTest(print01('test01'))
    # unittest.main(defaultTest='suite')
    # #使用测试套件执行用例2
    # suite = unittest.TestSuite()
    # testcase = [print01("test01"), print01("test02")]
    # suite.addTests(testcase)
    # unittest.main(defaultTest='suite')

    # print(os.getcwd()) #获取当前模块所在的目录路径
    # 使用测试套件执行用例3
    suite = unittest.TestSuite()
    #找到当前目录下所有.py结尾的模块的用例放到测试加载器中
    testcase = unittest.defaultTestLoader.discover(start_dir=os.getcwd(), pattern='*.py')
    suite.addTests(testcase)
    #unittest.main(defaultTest='suite')
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())#获取当前的时间
    name = open(os.getcwd()+"/"+nowtime+"_report.html", "wb")#生成报告，wb二进制的方式
    #报告测试驱动器
    runner = HTMLTestRunner(stream=name, verbosity=2, title='测试报告', description='报告详情如下')
    runner.run(suite)