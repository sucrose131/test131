import time
import unittest
from page.signup_page import signupPage
from ddt import ddt,data,unpack
from common.RichyExcelRW import rdata, ridata
from common.Logger import Logger
@ddt
class TestSignup(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass
    def setUp(self) -> None:
        self.page = signupPage()  # 实例化SignupPage类
        self.page.lopen()  # 打开登录页面
        self.testlog = Logger.getLogger()  # 实例化日志对象
        pass

    @rdata("signup")#读取signup.xlsx文件中的数据
    @unpack  # 对测试数据进行解包处理，让测试方法能以独立参数的形式接收数据。
    def test_signup_case(self, id, username, account, pwd, element, check):
        """测试注册功能"""
        # 对id为1和3的加时间戳
        if str(id) in ['1', '3'] and "timestamp" in account:#判断id是否为1或3是否包含"timestamp"
            timestamp = str(int(time.time()))
            account = account.replace("timestamp", timestamp)#使用字符串的 replace 方法，将 account 字符串中的 "timestamp" 替换为实际的时间戳

        # 注册操作
        self.page.signup(username, account, pwd)
        print("正在执行用例","账号:",username,"密码:",pwd)
        #断言部分
        msg = self.page.get_assert_txt(element)
        try:
            self.assertIn(check, msg)
            self.testlog.debug("断言 " + check + " 验证成功")
        except:
            self.testlog.debug(f"断言 {check} 不在 {msg} 中，验证失败")
            raise
        self.testlog.debug(f"实际使用的账号: {account}")


        pass

    def tearDown(self) -> None:
        self.page.quit()

        pass

    @classmethod
    def tearDownClass(cls) -> None:

        pass
