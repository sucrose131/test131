from selenium.webdriver.common.by import By


class FrontendLoginLocator:
    """前台登录页面元素定位器"""
    
    # 登录入口
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), '登录')] | //div[contains(text(), '登录')]")
    
    # 登录表单
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='请输入手机号'] | //input[@type='tel'] | //input[@name='phone']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='请输入密码'] | //input[@type='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), '登录')] | //button[@type='submit']")
    
    # 用户信息
    USER_INFO = (By.XPATH, "//div[contains(@class, 'user-info')] | //span[contains(@class, 'username')]")
    
    # 提示信息
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'error')] | //div[contains(@class, 'message')]")
