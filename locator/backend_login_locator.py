from selenium.webdriver.common.by import By


class BackendLoginLocator:
    """后台登录页面元素定位器"""
    
    # 登录表单
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='请输入账号'] | //input[@name='username'] | //input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='请输入密码'] | //input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), '登录')] | //button[@type='submit']")
    
    # 后台首页标识
    DASHBOARD = (By.XPATH, "//div[contains(@class, 'dashboard')] | //div[contains(text(), '控制台')]")
    
    # 错误提示
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'error')] | //div[contains(@class, 'message')]")
