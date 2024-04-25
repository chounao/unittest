# coding=utf-8
import unittest
import time
from pageobjects.login_page import LoginPage
from framework.driver import WDriver
from framework.log import Logger
import logging
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


# @unittest.skip
class TestLogin(unittest.TestCase):
    """校验区疾控登录成功"""

    @classmethod
    def setUpClass(cls):  # 一个测试类(文件)执行一次打开浏览器, 节约每个用例打开一次浏览器的时间
        cls.driver = WDriver().chromeDriver()
        cls.driver.maximize_window()
        log.logger.info('启动浏览器成功')

    def setUp(self):
        self.login = LoginPage(self.driver)
        self.login.open_login()
        log.logger.info('************************starting run test cases************************')

    @classmethod
    def tearDownClass(cls):
        # def tearDown(self):
        time.sleep(5)
        LoginPage(cls.driver).quit()

    def test_login(self):
        """用例标题：校验区疾控登录成功
           参数：用户名/密码 13777466979/test123456
           预期：登录成功
        """
        LoginPage(self.driver).login()
        try:
            self.assertEqual(LoginPage(self.driver).get_title(), "政采云，一站式政府采购云平台-引导页", msg="验证不成功！")
        except Exception:
            self.login.get_img('login_33301_fail.png')
            raise
        else:
            self.login.get_img('login_33301_pass.png')
            log.logger.info('运行成功：用户名正确,密码正确,登录成功')

    #
