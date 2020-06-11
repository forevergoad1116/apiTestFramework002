# 生成测试报告时，是要先执行测试用例的
# 我们可以把测试用例添加到测试套件中，然后执行测试套件生成测试报告


# 1 导包
import os
import unittest

import HTMLTestRunner_PY3


import time

# os.path.dirname(os.path.abspath(__file__)) 可以定位到当前项目的目录
from script.test_add import TestIHRMEmployee
from script.test_login import TestIHRMLogin

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2 创建测试套件
suite = unittest.TestSuite()
# 3 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestIHRMLogin))
suite.addTest(unittest.makeSuite(TestIHRMEmployee))
# 4 定义测试报告的目录和报告名称
report_path = BASE_DIR + "/report/tpshop{}.html".format(time.strftime('%Y%m%d %H%M%S'))
# 5 使用HTMLTestRunner_PY3生成测试报告
with open(report_path, mode='wb') as f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title="tpshop登录接口功能测试",
                                               description="这是一个更加美观的报告，前提是连上互联网")
    # 使用实例化的runner运行测试套件，生成测试报告
    runner.run(suite)

# # 1.导包
# import os
# import time
# import unittest
# from BeautifulReport import BeautifulReport
#
# # 2.组织要运行得测试套件
# import app
#
# suite = unittest.TestLoader().discover( app.BASE_DIR + "/script", pattern="test*.py")
#
# # 3.定义测试报告的文件名
# file_name = "test-{}.html".format(time.strftime("%Y%m%d%H%M%S"))
#
# # 4.实例化BeautifulReport的实例运行测试生成报告
# # filename:测试报告的文件名
# # description:测试报告描述可以理解标题
# # log_path:测试报告生成路径
# # dir = app.BASE_DIR + "/report"
# BeautifulReport(suite).report(filename=file_name, description="员工测试", log_path=r'C:\Users\Administrator\Desktop\apiTestFramework\report')
