import unittest


class EcshopLogin(unittest.TestCase):

    # @unittest.skip("此用例不执行")
    def test01_baili(self):
        # raise Exception("自定义异常")
        print("测试用例")
        # self.assertTrue(0)

    def test02_weiwie(self):
        print("测试微微")

    def test11_zhiliao(self):
        print("测试治疗")

if __name__ == '__main__':
    print("----")
    # unittest.main()
    unittest.main(defaultTest=["EcshopLogin.test11_zhiliao"])

    # 可以通过 python 20221204/logintest.py 进行执行
#     执行结果   . 代表成功   F 代表失败  E代表错误  S 跳过
