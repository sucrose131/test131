from base.base_page import BasePage
from config.global_cfg import GlobalCfg
from locator.frontend_login_locator import FrontendLoginLocator
import time


class FrontendLoginPage(BasePage, FrontendLoginLocator):
    """前台登录页面对象"""
    
    def open_frontend(self):
        """打开前台首页"""
        self.get(GlobalCfg.FRONTEND_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(2)
    
    def login(self, username=None, password=None):
        """
        前台登录
        :param username: 用户名，默认使用配置中的前台账号
        :param password: 密码，默认使用配置中的前台密码
        """
        if username is None:
            username = GlobalCfg.FRONTEND_USERNAME
        if password is None:
            password = GlobalCfg.FRONTEND_PASSWORD
        
        try:
            # 点击登录按钮
            self.find_element_click(*self.LOGIN_BUTTON)
            time.sleep(1)
            
            # 输入用户名
            self.find_element_sendkeys(*self.USERNAME_INPUT, text=username)
            time.sleep(0.5)
            
            # 输入密码
            self.find_element_sendkeys(*self.PASSWORD_INPUT, text=password)
            time.sleep(0.5)
            
            # 点击提交
            self.find_element_click(*self.SUBMIT_BUTTON)
            time.sleep(2)
            
            self.logger.info(f"前台登录成功: {username}")
        except Exception as e:
            self.logger.error(f"前台登录失败: {str(e)}")
            raise
    
    def get_user_info(self):
        """获取用户信息"""
        try:
            user_info = self.find_element_text(*self.USER_INFO)
            return user_info
        except:
            return None
    
    def is_logged_in(self):
        """判断是否已登录"""
        return self.is_element(*self.USER_INFO)
