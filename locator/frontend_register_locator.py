from selenium.webdriver.common.by import By


class FrontendRegisterLocator:
    """前台注册页面元素定位器"""
    
    # 注册入口
    REGISTER_BUTTON = (By.XPATH, "//span[contains(normalize-space(),'立即注册')]")
    
    # 注册输入框 1电话号码 2验证码 3名称 4密码 5确认密码
    PHONE_INPUT = (By.XPATH, "//uni-view[position()=2]/uni-view[position()=2]/uni-input[position()=1]/div[position()=1]/input[position()=1]")
    VERIFICATION_CODE_INPUT = (By.XPATH, "/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[3]/uni-view[2]/uni-input/div/input")
    NAME = (By.XPATH, "/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[4]/uni-view[2]/uni-input/div/input")
    PASSWORD_INPUT = (By.XPATH, "/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[5]/uni-view[2]/uni-input/div/input")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[6]/uni-view[2]/uni-input/div/input")

    #服务人输入框;勾选按钮
    SERVICE_STAFF = (By.XPATH, "/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view[1]/uni-view[1]/uni-input/div/input")
    NO_SERVICE_STAFF = (By.XPATH, "/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view[1]/uni-view[1]/uni-input/div/input")

    # 获取验证码按钮
    GET_CODE_BUTTON = (By.XPATH, "/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[3]/uni-view[2]/uni-view")
    
    # 提交按钮
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), '注册')] | //button[@type='submit']")
    
    # 提示信息
    SUCCESS_MESSAGE = (By.XPATH, "/html/body/div[3]/uni-toast/div")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'error')] | //div[contains(@class, 'message')]")
