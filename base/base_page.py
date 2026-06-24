from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from common.download_helper import DOWNLOAD_PATH
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from common.Logger import Logger
from config.global_cfg import GlobalCfg
import traceback
class BasePage():
    # def __init__(self):
    #     self.driver=webdriver.Edge()
    #     self.logger=Logger.getLogger()
    #     pass
    def __init__(self):
        options = Options()
        options.add_experimental_option("prefs", {
            "download.default_directory": DOWNLOAD_PATH,  # 关键设置
            "download.prompt_for_download": False,
            "safebrowsing.enabled": True
        })
        self.driver = webdriver.Edge(options=options)
        self.logger = Logger.getLogger()#获取日志对象

    def get(self,url):#打开页面
        try:
            self.driver.get(url)
        except:
            self.save_screenshot()
            self.logger.error("页面打开失败："+url)
            self.logger.error(traceback.print_exc())

    def close(self):#关闭页面
        try :
            self.driver.close()
        except:
            self.save_screenshot()
            self.logger.error("关闭页面失败："+self.driver.current_url)
            self.logger.error(traceback.print_exc())

    def refresh(self):#刷新页面
        try:
            self.driver.refresh()
        except:
            self.save_screenshot()
            self.logger.error("刷新失败：")
            self.logger.error(traceback.print_exc())
    def quit(self):#关闭浏览器
        try :
            self.driver.quit()
        except:
            self.save_screenshot()
            self.logger.error("关闭浏览器失败：")
            self.logger.error(traceback.print_exc())

    def is_element(self, *args):#判断元素是否存在
        try:
            WebDriverWait(self.driver,2).until(EC.visibility_of_element_located(args))
            self.driver.find_element(*args)
            return True
        except:
            return False
    def find_element(self,*args):#定位元素
        try:
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(args))#等待元素加载完成
            ele=self.driver.find_element(*args)
            return ele
        except:
            self.save_screenshot()
            self.logger.error("元素定位失败:"+str(args))
            self.logger.error(traceback.print_exc())
            return None

    def find_elements(self, *args):#定位元素组
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(args))
            ele = self.driver.find_elements(*args)
            return ele
        except:
            self.save_screenshot()
            self.logger.error("元素组定位失败:" + str(args))
            self.logger.error(traceback.print_exc())
            return None


    def find_element_sendkeys(self,*args,**kwargs):

        try:
            self.find_element(*args).send_keys(kwargs['text'])#
        except:
            self.save_screenshot()
            self.logger.error("填写数据失败:" + str(args)+" 数据是："+kwargs['text'])
            self.logger.error(traceback.print_exc())

    def find_element_click(self, *args):
        try:
            self.find_element(*args).click()
        except:
            self.save_screenshot()
            self.logger.error("点击失败:" + str(args))
            self.logger.error(traceback.print_exc())
    def find_element_text(self, *args):
        try:
            text=self.find_element(*args).text
            return text
        except:
            self.save_screenshot()
            self.logger.error("获取元素内容文本失败:" + str(args))
            self.logger.error(traceback.print_exc())
            return None
    def save_screenshot(self):
        try:
            self.driver.save_screenshot(GlobalCfg.IMG_PATH)
        except:
            self.logger.error("截图失败:" + self.driver.current_url)
            self.logger.error(traceback.print_exc())

