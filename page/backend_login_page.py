from base.base_page import BasePage
from config.global_cfg import GlobalCfg
from locator.backend_login_locator import BackendLoginLocator
import time


class BackendLoginPage(BasePage, BackendLoginLocator):
    """后台登录页面对象"""
    
    def open_backend(self):
        """打开后台登录页面"""
        self.get(GlobalCfg.BACKEND_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(2)
    
    def login(self, username=None, password=None):
        """
        后台登录
        :param username: 用户名，默认使用配置中的后台账号
        :param password: 密码，默认使用配置中的后台密码
        """
        if username is None:
            username = GlobalCfg.BACKEND_USERNAME
        if password is None:
            password = GlobalCfg.BACKEND_PASSWORD
        
        try:
            # 输入用户名
            self.find_element_sendkeys(*self.USERNAME_INPUT, text=username)
            time.sleep(0.5)
            
            # 输入密码
            self.find_element_sendkeys(*self.PASSWORD_INPUT, text=password)
            time.sleep(0.5)
            
            # 点击登录
            self.find_element_click(*self.LOGIN_BUTTON)
            time.sleep(3)
            
            self.logger.info(f"后台登录成功: {username}")
        except Exception as e:
            self.logger.error(f"后台登录失败: {str(e)}")
            raise
    
    def is_logged_in(self):
        """判断是否已登录到后台"""
        return self.is_element(*self.DASHBOARD)
