from selenium.webdriver.common.by import By
class LoginLocator():
    LINK_BT=(By.CLASS_NAME,'btnBox')#登录按钮
    Log_in_directly=(By.XPATH,"/html/body/div[1]/div[1]/div[2]/form/div[5]")#直接登录
    UNSERNAME_BOX = (By.CLASS_NAME,'el-input__inner')#用户名输入框
    PWD_BOX=(By.XPATH,"/html/body/div/div[1]/div[2]/form/div[3]/div/div/div/input")#密码输入框
    SUBMIT_BTN=(By.XPATH, "/html/body/div[1]/div[1]/div[2]/form/div[5]")#提交按钮
    QUIT_BTN=(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/ul/li[4]")#退出按钮
    MINE = (By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/div[2]/span")  # 我的
    Confirm_to_exit = (By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/button[2]")#确认退出
    CANCEL = (By.CLASS_NAME,"el-checkbox__inner")#取消按钮



