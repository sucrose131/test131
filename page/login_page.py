from selenium.webdriver import ActionChains
from base.base_page import BasePage
from config.global_cfg import GlobalCfg
from locator.login_locator import LoginLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage(BasePage,LoginLocator):
    def lopen(self):
        self.get(GlobalCfg.BASE_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def login(self,username,pwd):

        self.find_element_sendkeys(*self.UNSERNAME_BOX, text=username)  # 输入用户名
        print(*self.UNSERNAME_BOX)
        print(self.UNSERNAME_BOX)
        self.find_element_sendkeys(*self.PWD_BOX, text=pwd)  # 输入密码
        self.find_element_click(*self.SUBMIT_BTN)  # 点击登录按钮
        time.sleep(2)

    def get_assert_txt(self,xpath):
        msg = self.find_element_text(By.XPATH, xpath)
        return msg
