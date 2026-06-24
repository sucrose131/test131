from base.base_page import BasePage
from locator.frontend_order_locator import FrontendOrderLocator
import time
import re


class FrontendOrderPage(BasePage, FrontendOrderLocator):
    """前台订单页面对象"""
    
    def browse_products(self):
        """浏览商品列表"""
        try:
            products = self.find_elements(*self.PRODUCT_LIST)
            if products:
                self.logger.info(f"找到 {len(products)} 个商品")
                return products
            else:
                self.logger.warning("未找到商品列表")
                return []
        except Exception as e:
            self.logger.error(f"浏览商品失败: {str(e)}")
            return []
    
    def select_first_product(self):
        """选择第一个商品"""
        try:
            self.find_element_click(*self.FIRST_PRODUCT)
            time.sleep(2)
            product_name = self.find_element_text(*self.PRODUCT_NAME)
            self.logger.info(f"已选择商品: {product_name}")
            return product_name
        except Exception as e:
            self.logger.error(f"选择商品失败: {str(e)}")
            return None
    
    def place_order(self):
        """下单购买"""
        try:
            # 点击购买按钮
            self.find_element_click(*self.BUY_BUTTON)
            time.sleep(2)
            
            # 提交订单
            self.find_element_click(*self.SUBMIT_ORDER)
            time.sleep(3)
            
            self.logger.info("订单提交成功")
        except Exception as e:
            self.logger.error(f"下单失败: {str(e)}")
            raise
    
    def get_order_id(self):
        """获取订单ID"""
        try:
            order_text = self.find_element_text(*self.ORDER_NUMBER)
            # 从文本中提取订单号（假设订单号是数字）
            order_id = re.search(r'\d+', order_text)
            if order_id:
                self.logger.info(f"获取到订单ID: {order_id.group()}")
                return order_id.group()
            else:
                self.logger.warning("未找到订单ID")
                return None
        except Exception as e:
            self.logger.error(f"获取订单ID失败: {str(e)}")
            return None
    
    def go_to_my_orders(self):
        """进入我的订单页面"""
        try:
            self.find_element_click(*self.MY_ORDERS)
            time.sleep(2)
            self.logger.info("已进入我的订单页面")
        except Exception as e:
            self.logger.error(f"进入我的订单失败: {str(e)}")
            raise
    
    def get_latest_order_id(self):
        """获取最新订单ID"""
        try:
            # 进入我的订单
            self.go_to_my_orders()
            
            # 获取第一个订单
            order_element = self.find_element(*self.FIRST_ORDER)
            if order_element:
                order_text = order_element.text
                # 提取订单号
                order_id = re.search(r'\d+', order_text)
                if order_id:
                    self.logger.info(f"获取到最新订单ID: {order_id.group()}")
                    return order_id.group()
            
            self.logger.warning("未找到订单")
            return None
        except Exception as e:
            self.logger.error(f"获取最新订单ID失败: {str(e)}")
            return None
    
    def confirm_receive(self):
        """确认收货"""
        try:
            # 进入我的订单
            self.go_to_my_orders()
            time.sleep(1)
            
            # 点击确认收货按钮
            self.find_element_click(*self.CONFIRM_RECEIVE)
            time.sleep(2)
            
            self.logger.info("已确认收货")
        except Exception as e:
            self.logger.error(f"确认收货失败: {str(e)}")
            raise
    
    def check_benefits(self):
        """查看用户权益"""
        try:
            # 点击我的权益
            self.find_element_click(*self.USER_BENEFITS)
            time.sleep(2)
            
            # 获取权益列表
            benefits = self.find_elements(*self.BENEFITS_DISPLAY)
            if benefits:
                self.logger.info(f"找到 {len(benefits)} 个权益")
                benefit_list = [benefit.text for benefit in benefits]
                return benefit_list
            else:
                self.logger.warning("未找到权益信息")
                return []
        except Exception as e:
            self.logger.error(f"查看权益失败: {str(e)}")
            return []
