import unittest
import os

class EcshopLogin(unittest.TestCase):

    #测试用例
    def test01_xiaoming(self):
        print("测试小明")

    # 测试用例
    def test02_weiwei(self):
        print("测试微微")

# 测试用例
    def test10_xiaohongi(self):
        print("测试小红")

if __name__ =='__main__':
    suite = unittest.TestSuite()
    testcase = unittest.defaultTestLoader.discover(start_dir=os.getcwd(),pattern='*.py')
    suite.addTests(testcase)
    unittest.main(defaultTest='suite')
    unittest.TextTestRunner().run(suite) #两个调用方法结果相同没有区别
#
# 1.命令行运行方式：python -m unittest -v ecshop_login.EcshopLogin  -k *_weiwei
# python -m        以脚本的方式去运行一个门模块
#
# python -v        --version 意思是更详细的输出结果
#
# ecshop_login.EcshopLogin        模块名.类名.方法名
#
# -k匹配模式：
#
#        1.通配符：-k *_weiwei
#
#         2.字符串：-k weiwei
#
# 适合集成jenkins的时候使用，所有的命令行的方式都叫非GUI的方式
#
# postman:非GUI,newman
#
# jmeter:jmeter的命令
#
# 2.使用unittest.main方法，以模块的方式运行
#
# 配置pycharm的环境，或者使用python 模块名.py方式运行
#
# if __name__ =='__main__':
#     print('__________')
#     unittest.main()
# 读懂执行的结果：
#
# .        成功
#
# F        失败       self.assertTrue(0)
#
# E        错误        raise Exception(”自定义异常”)
#
# S        跳过        @unittest.skip("此用例不执行")
#
# 用例执行顺序：
#
# 按照ASCLL码的规则：【0-9 A-Z a-z】A=65, a=97
#
# 所以用例命名以01-09，在10-99
#
# 框架底层原理：
#
# module='__main__',    测试用例所在的路劲 __main__表示当前模块
# defaultTest=None,     待测用例的名称，默认是所有
# 例：defaultTest=["EcshopLogin.test01_xiaoming"]
# argv=None,            接受外部的参数
# testRunner=None,      测试运行器，默认TextTestRunner-文本格式
# testLoader=loader.defaultTestLoader,     指定使用默认的测试用例加载器，
# exit=True,            是否在测试完成之后结束python程序
# verbosity=1,           类似-v 有0，1,2,
# failfast=None,         失败的时候是否终止测试
# catchbreak=None,        是否捕获复制
# buffer=None,             是否捕获输出流
# warnings=None, *,         是否显示警告信息
# tb_locals=False
# 只运行部分用例使用什么测试套件：
#
# 3.单个用例：
#
# if __name__ =='__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(EcshopLogin("test01_xiaoming"))
#     suite.addTest(EcshopLogin("test02_weiwei"))
#     #unittest.main(defaultTest='suite')两个调用方法结果相同没有区别
#     unittest.TextTestRunner().run(suite)
# 4.用例集：
#
# if __name__ =='__main__':
#     suite = unittest.TestSuite()
#     testcase = [EcshopLogin("test01_xiaoming"),EcshopLogin("test10_xiaohongi")]
#     suite.addTests(testcase)
#     unittest.main(defaultTest='suite')
# 5.文件下以.py结尾所有用例：
#
# #print(os.getcwd())获取路径
#
# if __name__ =='__main__':
#     suite = unittest.TestSuite()
#     testcase =unittest.defaultTestLoader.discover(start_dir=os.getcwd(),pattern='*.py')
#     suite.addTests(testcase)
#     unittest.main(defaultTest='suite')

