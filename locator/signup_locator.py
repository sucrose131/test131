from selenium.webdriver.common.by import By
class signupLocator():
    SignUpLink = (By.CLASS_NAME, 'register')  # 登录按钮
    UserName = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/form/div[2]/div/div/div/input')  # 用户名输入框
    Account = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/form/div[3]/div/div/div/input')  # 账号输入框
    Password = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/form/div[4]/div/div/div/input')  # 密码输入框
    ConfirmSignUp = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/form/div[5]')  # 确认注册