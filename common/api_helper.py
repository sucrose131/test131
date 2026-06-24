import requests
from config.global_cfg import GlobalCfg
from common.Logger import Logger


class ApiHelper:
    """API请求帮助类"""
    
    def __init__(self):
        self.logger = Logger.getLogger()
        self.session = requests.Session()
        self.backend_base_url = GlobalCfg.BACKEND_URL.rstrip('/')
        self.token = None

    def backend_login(self, username=None, password=None):
        """
        后台登录获取token
        :param username: 用户名，默认使用配置中的后台账号
        :param password: 密码，默认使用配置中的后台密码
        :return: token或None
        """
        if username is None:
            username = GlobalCfg.BACKEND_USERNAME
        if password is None:
            password = GlobalCfg.BACKEND_PASSWORD

        url = f"{self.backend_base_url}{GlobalCfg.BACKEND_LOGIN_API}"
        params = {
            'username': username,
            'password': password
        }

        try:
            self.logger.info(f"开始后台登录: {url}")
            response = self.session.post(url, json=params, timeout=10)  # ← 改1：get改成post，params改成json
            response.raise_for_status()

            result = response.json()
            self.logger.info(f"后台登录响应: {result}")

            # 根据实际接口返回结构调整，假设返回格式为 {"code": 200, "data": {"token": "xxx"}}
            if result.get('code') == 200 or result.get('success'):
                self.token = result.get('data', {}).get('token')
                if self.token:
                    self.logger.info("后台登录成功，获取到token")
                    # 设置后续请求的认证头
                    self.session.headers.update({'Authorization': f'Bearer {self.token}'})
                    return self.token
                else:
                    self.logger.error("登录成功但未获取到token")
                    return None
            else:
                self.logger.error(f"后台登录失败: {result.get('message', '未知错误')}")
                return None

        except Exception as e:
            self.logger.error(f"后台登录异常: {str(e)}")
            return None

    def recharge_user(self, user_id, amount=None):
        """
        后台给用户充值
        :param user_id: 用户ID
        :param amount: 充值金额，默认使用配置中的金额
        :return: 是否充值成功
        """
        if not self.token:
            self.logger.error("未登录，请先调用backend_login获取token")
            raise Exception("未登录，无法充值")

        if amount is None:
            amount = GlobalCfg.RECHARGE_AMOUNT

        url = f"{self.backend_base_url}{GlobalCfg.BACKEND_RECHARGE_API}"
        params = {
            'id': user_id,
            'type': 1,
            'balance': amount
        }

        try:
            self.logger.info(f"开始充值，用户ID: {user_id}, 金额: {amount}")
            response = self.session.post(url, json=params, timeout=10)  # ← 改这里：params 改成 json
            response.raise_for_status()

            result = response.json()
            self.logger.info(f"充值响应: {result}")

            # 根据实际接口返回结构调整
            if result.get('code') == 200 or result.get('success'):
                self.logger.info(f"用户 {user_id} 充值成功，金额: {amount}")
                return True
            else:
                error_msg = result.get('message', '未知错误')
                self.logger.error(f"用户 {user_id} 充值失败: {error_msg}")
                raise Exception(f"充值失败: {error_msg}")

        except Exception as e:
            self.logger.error(f"充值异常: {str(e)}")
            raise
    
    
    def close(self):
        """关闭session"""
        self.session.close()
        self.logger.info("API session已关闭")
    
    def __enter__(self):
        """支持上下文管理器"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文时关闭session"""
        self.close()


if __name__ == "__main__":
    # 测试API调用
    with ApiHelper() as api:
        token = api.backend_login()
        if token:
            print(f"登录成功，token: {token}")
            # 测试发货（需要提供实际的订单ID）
            # success = api.ship_order(order_id=123)
            # print(f"发货结果: {success}")
