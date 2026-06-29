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
    
    def click_register_button(self):
        """点击注册按钮进入注册表单"""
        self.find_element_click(*self.REGISTER_BUTTON)
        time.sleep(1)
    
    def fill_basic_info(self, phone, name="测试用户", password=None):
        """
        填写注册基本信息（不含验证码）
        :param phone: 手机号
        :param name: 姓名，默认"测试用户"
        :param password: 密码，默认使用配置中的密码

        """
        if password is None:
            password = GlobalCfg.REGISTER_PASSWORD
        
        self.find_element_sendkeys(*self.PHONE_INPUT, text=phone)
        time.sleep(0.5)
        
        self.find_element_sendkeys(*self.NAME, text=name)
        time.sleep(0.5)
        
        self.find_element_sendkeys(*self.PASSWORD_INPUT, text=password)
        time.sleep(0.5)
        
        if self.is_element(*self.CONFIRM_PASSWORD_INPUT):
            self.find_element_sendkeys(*self.CONFIRM_PASSWORD_INPUT, text=password)
            time.sleep(0.5)
    
    def click_get_verification_code(self):
        """点击获取验证码按钮（触发系统发送验证码）"""
        self.find_element_click(*self.GET_CODE_BUTTON)
        time.sleep(3)
    
    def fill_verification_code(self, verification_code):
        """填写验证码"""
        self.find_element_sendkeys(*self.VERIFICATION_CODE_INPUT, text=verification_code)
        time.sleep(0.5)
    
    def submit_register(self):
        """提交注册表单"""
        self.find_element_click(*self.SUBMIT_BUTTON)
        time.sleep(3)
    
    def register(self, phone, verification_code, password=None):
        """
        用户注册（完整流程）- 用于向后兼容
        :param phone: 手机号
        :param verification_code: 验证码
        :param password: 密码，默认使用配置中的密码
        """
        if password is None:
            password = GlobalCfg.REGISTER_PASSWORD
        
        try:
            self.click_register_button()
            self.fill_basic_info(phone, password=password)
            self.click_get_verification_code()
            self.fill_verification_code(verification_code)
            self.submit_register()
            
            self.logger.info(f"用户注册成功: {phone}")
        except Exception as e:
            self.logger.error(f"用户注册失败: {str(e)}")
            raise
    
    def is_registered_successfully(self):
        """判断是否注册成功"""
        return self.is_element(*self.SUCCESS_MESSAGE)
