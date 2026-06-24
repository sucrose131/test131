import unittest
import time
import random
from common.Logger import Logger
from page.frontend_register_page import FrontendRegisterPage
from page.frontend_login_page import FrontendLoginPage
from page.frontend_order_page import FrontendOrderPage
from common.api_helper import ApiHelper
from common.database_helper import DatabaseHelper


class TestRegisterAndOrderFlow(unittest.TestCase):
    """
    测试完整注册下单流程：
    注册 → 登录 → 后台充值 → 前台下单 → 数据库验证权益和身份
    """
    
    @classmethod
    def setUpClass(cls) -> None:
        """类级别的初始化"""
        Logger.init()
        cls.testlog = Logger.getLogger()
    
    def setUp(self) -> None:
        """每个测试方法执行前的初始化"""
        self.testlog.info("=" * 60)
        self.testlog.info("开始执行注册下单流程测试")
        
        # 生成随机手机号（每次测试使用不同的手机号）
        # 格式：181 + 8位随机数字
        random_suffix = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        self.test_phone = f"181{random_suffix}"
        self.test_password = "abcd1234"
        self.testlog.info(f"本次测试使用手机号: {self.test_phone}")
    
    def test_register_recharge_order_flow(self):
        """
        完整注册下单流程测试
        1. 从数据库获取验证码
        2. 前台注册
        3. 前台登录
        4. 后台API充值
        5. 前台下单
        6. 等待自动发货
        7. 数据库验证权益和身份
        """
        
        order_id = None
        user_id = None
        frontend_driver = None
        
        try:
            # ==================== 步骤1: 从数据库获取验证码 ====================
            self.testlog.info("步骤1: 从数据库获取验证码")
            time.sleep(2)  # 等待验证码生成（假设已提前发送）
            
            with DatabaseHelper() as db_helper:
                verification_code = db_helper.query_verification_code(self.test_phone)
                self.assertIsNotNone(verification_code, f"未找到手机号 {self.test_phone} 的验证码")
                self.testlog.info(f"获取到验证码: {verification_code}")
            
            # ==================== 步骤2: 前台注册 ====================
            self.testlog.info("步骤2: 前台注册")
            register_page = FrontendRegisterPage()
            frontend_driver = register_page.driver
            register_page.open_register_page()
            register_page.register(self.test_phone, verification_code, self.test_password)
            
            # 验证注册成功
            self.assertTrue(register_page.is_registered_successfully(), "前台注册失败")
            self.testlog.info("前台注册成功")
            
            # ==================== 步骤3: 前台登录 ====================
            self.testlog.info("步骤3: 前台登录")
            login_page = FrontendLoginPage()
            login_page.driver = frontend_driver  # 复用同一个driver
            login_page.login(self.test_phone, self.test_password)
            
            # 验证登录成功
            self.assertTrue(login_page.is_logged_in(), "前台登录失败")
            self.testlog.info("前台登录成功")
            
            # ==================== 步骤4: 获取用户ID并后台充值 ====================
            self.testlog.info("步骤4: 后台API充值")
            
            # 从数据库获取用户ID
            with DatabaseHelper() as db_helper:
                user_info = db_helper.query_user_by_phone(self.test_phone)
                self.assertIsNotNone(user_info, f"数据库中未找到用户 {self.test_phone}")
                user_id = user_info.get('id')
                self.assertIsNotNone(user_id, "用户信息中未找到id")
                self.testlog.info(f"获取到用户ID: {user_id}")
            
            # 调用后台API充值
            with ApiHelper() as api_helper:
                # 后台登录获取token
                token = api_helper.backend_login()
                self.assertIsNotNone(token, "后台API登录失败，未获取到token")
                self.testlog.info("后台API登录成功，已获取token")
                
                # 调用充值接口
                recharge_success = api_helper.recharge_user(user_id)
                self.assertTrue(recharge_success, f"用户 {user_id} 充值失败")
                self.testlog.info(f"用户 {user_id} 充值成功")
            
            # ==================== 步骤5: 前台下单 ====================
            self.testlog.info("步骤5: 前台浏览商品并下单")
            order_page = FrontendOrderPage()
            order_page.driver = frontend_driver  # 复用同一个driver
            
            # 选择商品
            product_name = order_page.select_first_product()
            self.assertIsNotNone(product_name, "选择商品失败")
            self.testlog.info(f"已选择商品: {product_name}")
            
            # 下单
            order_page.place_order()
            self.testlog.info("下单成功")
            
            # ==================== 步骤6: 获取订单ID并等待自动发货 ====================
            self.testlog.info("步骤6: 获取订单ID并等待自动发货")
            time.sleep(3)  # 等待订单创建完成
            
            # 获取订单ID
            order_id = order_page.get_order_id()
            if not order_id:
                order_id = order_page.get_latest_order_id()
            
            self.assertIsNotNone(order_id, "获取订单ID失败")
            self.assertTrue(order_id.isdigit(), f"订单ID格式错误: {order_id}")
            self.testlog.info(f"获取到订单ID: {order_id}")
            
            # 等待自动发货
            time.sleep(5)  # 等待自动发货处理（根据实际业务调整等待时间）
            self.testlog.info("等待自动发货完成")
            
            # ==================== 步骤7: 数据库验证权益和身份 ====================
            self.testlog.info("步骤7: 数据库验证权益和身份")
            
            with DatabaseHelper() as db_helper:
                # 断言1: 验证订单存在
                order_info = db_helper.query_order_by_id(order_id)
                self.assertIsNotNone(order_info, f"数据库中未找到订单 {order_id}")
                self.testlog.info("✅ 断言1通过: 订单存在")
                
                # 断言2: 验证订单属于当前用户
                order_user_id = order_info.get('user_id')
                self.assertEqual(order_user_id, user_id, 
                               f"订单用户ID不匹配，期望: {user_id}, 实际: {order_user_id}")
                self.testlog.info("✅ 断言2通过: 订单属于当前用户")
                
                # 断言3: 验证订单状态为已发货
                order_status = order_info.get('order_status')
                self.assertIsNotNone(order_status, "订单状态为空")
                self.assertIn(order_status, [4], 
                             f"订单状态不正确，期望已发货，实际状态: {order_status}")
                self.testlog.info(f"✅ 断言3通过: 订单状态为已发货 ({order_status})")
                
                # 断言4: 验证订单金额正确
                order_amount = order_info.get('actual_amount') or order_info.get('total_amount')
                self.assertIsNotNone(order_amount, "订单金额为空")
                self.assertGreater(float(order_amount), 0, "订单金额应大于0")
                self.testlog.info(f"✅ 断言4通过: 订单金额正确 ({order_amount})")
                
                # 断言5: 验证发货时间存在
                ship_time = order_info.get('shipping_time')
                self.assertIsNotNone(ship_time, "自动发货后应有发货时间")
                self.testlog.info(f"✅ 断言5通过: 发货时间存在 ({ship_time})")
                
                # 断言6: 验证订单权益记录存在
                order_benefits = db_helper.query_order_benefits(order_id)
                self.assertIsNotNone(order_benefits, "订单权益记录不存在")
                self.assertGreater(len(order_benefits), 0, "订单应包含至少一个权益")
                self.testlog.info(f"✅ 断言6通过: 订单权益记录存在 (共{len(order_benefits)}个)")
                
                # 断言7: 验证用户已获得相应权益
                benefits_verified = db_helper.verify_benefits_after_delivery(order_id, user_id)
                self.assertTrue(benefits_verified, "权益验证失败：订单权益未正确添加到用户账户")
                self.testlog.info("✅ 断言7通过: 用户已获得订单权益")
                
                # 断言8: 验证用户身份与数据库一致
                # 假设预期身份为"普通会员"，需要根据实际业务调整
                expected_identity = "个人消费者"  # 新注册用户默认等级 level=0
                identity_verified = db_helper.verify_user_identity(user_id, expected_identity)
                self.assertTrue(identity_verified, 
                              f"用户身份验证失败，期望: {expected_identity}")
                self.testlog.info(f"✅ 断言8通过: 用户身份验证通过 ({expected_identity})")
                
                # 记录详细信息
                self.testlog.info("=" * 60)
                self.testlog.info("测试结果汇总:")
                self.testlog.info(f"  - 手机号: {self.test_phone}")
                self.testlog.info(f"  - 用户ID: {user_id}")
                self.testlog.info(f"  - 订单ID: {order_id}")
                self.testlog.info(f"  - 订单状态: {order_status}")
                self.testlog.info(f"  - 订单金额: {order_amount}")
                self.testlog.info(f"  - 发货时间: {ship_time}")
                self.testlog.info(f"  - 权益数量: {len(order_benefits)}")
                self.testlog.info(f"  - 用户身份: {expected_identity}")
                
                self.testlog.info("\n订单权益详情:")
                for i, benefit in enumerate(order_benefits, 1):
                    product_name = benefit.get('product_name', '未知产品')
                    benefit_type = benefit.get('benefit_type', '未知类型')
                    self.testlog.info(f"  {i}. {product_name} - {benefit_type}")
                
                self.testlog.info("=" * 60)
                self.testlog.info("✅ 所有断言验证通过 - 注册下单流程测试成功")
            
        except Exception as e:
            self.testlog.error(f"注册下单流程测试失败: {str(e)}")
            self.testlog.error(f"错误详情: {e.__traceback__.tb_lineno} 行")
            raise
        
        finally:
            # 清理资源
            try:
                if frontend_driver:
                    frontend_driver.quit()
                    self.testlog.info("浏览器已关闭")
            except Exception as e:
                self.testlog.error(f"关闭浏览器时出错: {str(e)}")
    
    def tearDown(self) -> None:
        """每个测试方法执行后的清理"""
        self.testlog.info("测试方法执行完毕")
    
    @classmethod
    def tearDownClass(cls) -> None:
        """类级别的清理"""
        cls.testlog.info("注册下单流程测试类执行完毕")


if __name__ == "__main__":
    unittest.main()
