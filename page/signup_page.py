from selenium.webdriver import ActionChains
from base.base_page import BasePage
from config.global_cfg import GlobalCfg
from locator.signup_locator import signupLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class signupPage(BasePage,signupLocator):
    def lopen(self):
        self.get(GlobalCfg.BASE_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def signup(self,username,account,pwd):
        self.find_element_click(*self.SignUpLink)#点击注册按钮
        timestamp = str(int(time.time()))
        self.find_element_sendkeys(*self.UserName, text=username)
        self.find_element_click(*self.Account)#点击账号输入框获取文本
        time.sleep(1)
        self.find_element_sendkeys(*self.Account, text=account)  # 输入账号
        self.find_element_click(*self.Password)#点击密码输入框获取文本
        time.sleep(1)
        self.find_element_sendkeys(*self.Password, text=pwd)  # 输入密码
        self.find_element_click(*self.ConfirmSignUp)  # 点击注册按钮
        time.sleep(2)









    def get_assert_txt(self,xpath):
        msg = self.find_element_text(By.XPATH, xpath)
        return msg