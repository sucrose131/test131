from common.Logger import Logger
from page.login_page import LoginPage
from common import RichyExcelRW
from config.global_cfg import GlobalCfg
import time
from unittestreport import TestRunner
import unittest

Logger.init()
RichyExcelRW.rinit(GlobalCfg.CASE_FILE)

# 选择要执行的测试用例
# 选项1: 执行所有测试用例
# testcase = unittest.defaultTestLoader.discover(start_dir="./testcase", pattern="test_*.py")

# 选项2: 执行特定的测试文件
# testcase = unittest.defaultTestLoader.discover(start_dir="./testcase", pattern="test_order_flow.py")  # 自动发货订单流程测试
# testcase = unittest.defaultTestLoader.discover(start_dir="./testcase", pattern="test_login.py")  # 登录测试
# testcase = unittest.defaultTestLoader.discover(start_dir="./testcase", pattern="test_signup.py")  # 注册测试
testcase = unittest.defaultTestLoader.discover(start_dir="./testcase", pattern="test_register_and_order.py")  # 注册下单完整流程测试

runner = TestRunner(
    testcase,
    filename=GlobalCfg.REPORT_NAME,
    report_dir=GlobalCfg.REPORT_PATH,
    title="华数生物自动化测试报告",
    tester="131",
    templates=2
)
runner.run(thread_count=1, count=1)  # 指定并发线程数和执行次数

# 发送邮件报告（可选）
# runner.send_email(host="smtp.qq.com",
#                   port=465,
#                   user="你的邮箱@qq.com",
#                   password="alg123412bab",
#                   to_addrs=["对方的邮箱@qq.com",""])

