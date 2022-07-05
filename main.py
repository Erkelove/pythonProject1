# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


# 按间距中的绿色按钮以运行脚本。
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

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
    testcase = unittest.defaultTestLoader.discover(start_dir=os.getcwd()+'/UnitTest', pattern='*.py')
    suite.addTests(testcase)
    #unittest.main(defaultTest='suite')
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())#获取当前的时间
    name = open(os.getcwd()+"/UnitTest/"+nowtime+"_report.html", "wb")#生成报告，wb二进制的方式
    #报告测试驱动器
    runner = HTMLTestRunner(stream=name, verbosity=2, title='测试报告', description='报告详情如下')
    runner.run(suite)
