import time
import unittest
from page.login_page import LoginPage
from ddt import ddt,data,unpack
from common.RichyExcelRW import rdata
from common.Logger import Logger
@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass
    def setUp(self) -> None:
        self.page = LoginPage()  # 实例化登录页面
        self.page.lopen()  # 打开登录页面
        self.testlog = Logger.getLogger()  # 实例化日志对象
        pass
    @rdata("login")#读取login.xlsx中的数据
    @unpack#对测试数据进行解包处理，让测试方法能以独立参数的形式接收数据。
    def test_login_case(self,id,username,pwd,element,check):
        """ 测试登录"""
        self.page.login(username,pwd)#登录
        print("正在执行用例","账号:",username,"密码:",pwd)
        msg=self.page.get_assert_txt(element)#获取元素文本
        try:
            self.assertIn(check, msg)
            self.testlog.debug("断言" + check + " 验证成功")
        except:
            self.testlog.debug("断言 " + check + " 不在 " + msg + " 中 验证失败")
            raise
        pass

    def tearDown(self) -> None:
        self.page.quit()

        pass

    @classmethod
    def tearDownClass(cls) -> None:

        pass