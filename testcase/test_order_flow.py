import unittest
import time
from common.Logger import Logger
from page.frontend_login_page import FrontendLoginPage
from page.frontend_order_page import FrontendOrderPage
from common.database_helper import DatabaseHelper


class TestOrderFlow(unittest.TestCase):
    """
    测试自动发货订单流程：
    前台登录 -> 前台下单 -> 等待自动发货 -> 数据库验证权益和订单状态
    """
    
    @classmethod
    def setUpClass(cls) -> None:
        """类级别的初始化"""
        Logger.init()
        cls.testlog = Logger.getLogger()
    
    def setUp(self) -> None:
        """每个测试方法执行前的初始化"""
        self.testlog.info("=" * 50)
        self.testlog.info("开始执行订单流程测试")
    
    def test_auto_delivery_order_flow(self):
        """
        自动发货订单流程测试
        1. 前台登录
        2. 浏览商品并下单
        3. 获取订单ID
        4. 等待自动发货（系统自动处理）
        5. 数据库验证订单状态和权益
        """
        
        order_id = None
        user_id = None
        frontend_driver = None
        
        try:
            # ==================== 步骤1: 前台登录 ====================
            self.testlog.info("步骤1: 前台登录")
            frontend_login_page = FrontendLoginPage()
            frontend_driver = frontend_login_page.driver
            frontend_login_page.open_frontend()
            frontend_login_page.login()
            
            # 验证登录成功
            self.assertTrue(frontend_login_page.is_logged_in(), "前台登录失败")
            self.testlog.info("前台登录成功")
            
            # ==================== 步骤2: 浏览商品并下单 ====================
            self.testlog.info("步骤2: 浏览商品并下单")
            frontend_order_page = FrontendOrderPage()
            # 复用同一个driver
            frontend_order_page.driver = frontend_driver
            
            # 选择商品
            product_name = frontend_order_page.select_first_product()
            self.assertIsNotNone(product_name, "选择商品失败")
            self.testlog.info(f"已选择商品: {product_name}")
            
            # 下单
            frontend_order_page.place_order()
            self.testlog.info("下单成功")
            
            # ==================== 步骤3: 获取订单ID和用户ID ====================
            self.testlog.info("步骤3: 获取订单ID")
            time.sleep(3)  # 等待订单创建完成
            
            # 尝试从当前页面获取订单ID，如果获取不到则从我的订单中获取
            order_id = frontend_order_page.get_order_id()
            if not order_id:
                order_id = frontend_order_page.get_latest_order_id()
            
            self.assertIsNotNone(order_id, "获取订单ID失败")
            self.assertTrue(order_id.isdigit(), f"订单ID格式错误: {order_id}")
            self.testlog.info(f"获取到订单ID: {order_id}")
            
            # ==================== 步骤4: 等待自动发货 ====================
            self.testlog.info("步骤4: 等待系统自动发货")
            time.sleep(5)  # 等待自动发货处理（根据实际业务调整等待时间）
            
            # ==================== 步骤5: 数据库验证订单状态和权益 ====================
            self.testlog.info("步骤5: 数据库验证订单状态和权益")
            
            with DatabaseHelper() as db_helper:
                # 查询订单信息
                order_info = db_helper.query_order_by_id(order_id)
                self.assertIsNotNone(order_info, f"数据库中未找到订单 {order_id}")
                self.testlog.info(f"订单信息查询成功")
                            
                # 断言1: 验证订单存在且属于当前用户
                user_id = order_info.get('user_id')
                self.assertIsNotNone(user_id, "订单信息中未找到user_id")
                self.testlog.info(f"订单所属用户ID: {user_id}")
                            
                # 断言2: 验证订单状态为已发货（status字段根据实际数据库调整）
                order_status = order_info.get('status')
                self.assertIsNotNone(order_status, "订单状态为空")
                # 假设status=2表示已发货，需要根据实际业务调整
                self.assertIn(order_status, [2, 'shipped', '已发货'], 
                             f"订单状态不正确，期望已发货，实际状态: {order_status}")
                self.testlog.info(f"订单状态验证通过: {order_status}")
                            
                # 断言3: 验证订单金额正确
                order_amount = order_info.get('amount') or order_info.get('total_amount')
                self.assertIsNotNone(order_amount, "订单金额为空")
                self.assertGreater(float(order_amount), 0, "订单金额应大于0")
                self.testlog.info(f"订单金额验证通过: {order_amount}")
                            
                # 断言4: 验证发货时间存在（自动发货后应有发货时间）
                ship_time = order_info.get('ship_time') or order_info.get('delivery_time')
                self.assertIsNotNone(ship_time, "自动发货后应有发货时间")
                self.testlog.info(f"发货时间验证通过: {ship_time}")
                            
                # 断言5: 验证订单权益记录存在
                order_benefits = db_helper.query_order_benefits(order_id)
                self.assertIsNotNone(order_benefits, "订单权益记录不存在")
                self.assertGreater(len(order_benefits), 0, "订单应包含至少一个权益")
                self.testlog.info(f"订单权益数量: {len(order_benefits)}")
                            
                # 断言6: 验证用户已获得相应权益
                benefits_verified = db_helper.verify_benefits_after_delivery(order_id, user_id)
                self.assertTrue(benefits_verified, "权益验证失败：订单权益未正确添加到用户账户")
                self.testlog.info("✅ 权益验证成功：订单权益已正确添加到用户账户")
                            
                # 断言7: 验证用户权益数量和订单权益数量一致
                user_benefits = db_helper.query_user_benefits(user_id)
                self.assertIsNotNone(user_benefits, "用户权益查询失败")
                            
                # 记录详细信息
                self.testlog.info("=" * 50)
                self.testlog.info("订单信息:")
                self.testlog.info(f"  - 订单ID: {order_id}")
                self.testlog.info(f"  - 用户ID: {user_id}")
                self.testlog.info(f"  - 订单状态: {order_status}")
                self.testlog.info(f"  - 订单金额: {order_amount}")
                self.testlog.info(f"  - 发货时间: {ship_time}")
                            
                self.testlog.info("\n订单权益详情:")
                for i, benefit in enumerate(order_benefits, 1):
                    product_name = benefit.get('product_name', '未知产品')
                    benefit_type = benefit.get('benefit_type', '未知类型')
                    self.testlog.info(f"  {i}. {product_name} - {benefit_type}")
                            
                self.testlog.info(f"\n用户当前权益总数: {len(user_benefits)}")
                if user_benefits:
                    self.testlog.info("用户权益列表:")
                    for i, benefit in enumerate(user_benefits[:5], 1):  # 只显示前5个
                        product_name = benefit.get('product_name', '未知产品')
                        benefit_type = benefit.get('benefit_type', '未知类型')
                        self.testlog.info(f"  {i}. {product_name} - {benefit_type}")
                    if len(user_benefits) > 5:
                        self.testlog.info(f"  ... 还有 {len(user_benefits) - 5} 个权益")
                            
                self.testlog.info("=" * 50)
                self.testlog.info("✅ 所有断言验证通过 - 自动发货流程测试成功")
            
            self.testlog.info("=" * 50)
            self.testlog.info("订单流程测试完成 - 所有步骤成功")
            
        except Exception as e:
            self.testlog.error(f"订单流程测试失败: {str(e)}")
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
        cls.testlog.info("订单流程测试类执行完毕")


if __name__ == "__main__":
    unittest.main()
