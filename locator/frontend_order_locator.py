from selenium.webdriver.common.by import By


class FrontendOrderLocator:
    """前台商品浏览和下单页面元素定位器"""
    
    # 商品列表
    PRODUCT_LIST = (By.XPATH, "//div[contains(@class, 'product')] | //div[contains(@class, 'goods')]")
    FIRST_PRODUCT = (By.XPATH, "(//div[contains(@class, 'product')] | //div[contains(@class, 'goods')])[1]")
    
    # 商品详情
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product-name')] | //h1")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'price')] | //span[contains(@class, 'amount')]")
    
    # 购买按钮
    BUY_BUTTON = (By.XPATH, "//button[contains(text(), '立即购买')] | //button[contains(text(), '购买')]")
    ADD_TO_CART = (By.XPATH, "//button[contains(text(), '加入购物车')]")
    
    # 订单确认页面
    SUBMIT_ORDER = (By.XPATH, "//button[contains(text(), '提交订单')] | //button[contains(text(), '去支付')]")
    
    # 订单信息
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'order-no')] | //span[contains(text(), '订单号')]/following-sibling::*")
    ORDER_STATUS = (By.XPATH, "//div[contains(@class, 'order-status')] | //span[contains(@class, 'status')]")
    
    # 我的订单
    MY_ORDERS = (By.XPATH, "//div[contains(text(), '我的订单')] | //a[contains(text(), '订单')]")
    ORDER_LIST = (By.XPATH, "//div[contains(@class, 'order-item')]")
    FIRST_ORDER = (By.XPATH, "(//div[contains(@class, 'order-item')])[1]")
    
    # 确认收货
    CONFIRM_RECEIVE = (By.XPATH, "//button[contains(text(), '确认收货')]")
    
    # 权益展示
    BENEFITS_DISPLAY = (By.XPATH, "//div[contains(@class, 'benefit')] | //div[contains(@class, 'rights')]")
    USER_BENEFITS = (By.XPATH, "//div[contains(@class, 'my-benefits')] | //div[contains(text(), '我的权益')]")
