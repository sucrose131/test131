from base.base_page import BasePage
from config.global_cfg import GlobalCfg
from locator.frontend_register_locator import FrontendRegisterLocator
import time


class FrontendRegisterPage(BasePage, FrontendRegisterLocator):
    """前台注册页面对象"""
    
    def open_register_page(self):
        """打开注册页面"""
        self.get(GlobalCfg.FRONTEND_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(2)
    
    def register(self, phone, verification_code, password=None):
        """
        用户注册
        :param phone: 手机号
        :param verification_code: 验证码
        :param password: 密码，默认使用配置中的密码
        """
        if password is None:
            password = GlobalCfg.REGISTER_PASSWORD
        
        try:
            # 点击注册按钮
            self.find_element_click(*self.REGISTER_BUTTON)
            time.sleep(1)
            
            # 输入手机号
            self.find_element_sendkeys(*self.PHONE_INPUT, text=phone)
            time.sleep(0.5)
            
            # 输入验证码
            self.find_element_sendkeys(*self.VERIFICATION_CODE_INPUT, text=verification_code)
            time.sleep(0.5)
            
            # 输入密码
            self.find_element_sendkeys(*self.PASSWORD_INPUT, text=password)
            time.sleep(0.5)
            
            # 确认密码（如果存在）
            if self.is_element(*self.CONFIRM_PASSWORD_INPUT):
                self.find_element_sendkeys(*self.CONFIRM_PASSWORD_INPUT, text=password)
                time.sleep(0.5)
            
            # 点击提交
            self.find_element_click(*self.SUBMIT_BUTTON)
            time.sleep(3)
            
            self.logger.info(f"用户注册成功: {phone}")
        except Exception as e:
            self.logger.error(f"用户注册失败: {str(e)}")
            raise
    
    def is_registered_successfully(self):
        """判断是否注册成功"""
        return self.is_element(*self.SUCCESS_MESSAGE)
