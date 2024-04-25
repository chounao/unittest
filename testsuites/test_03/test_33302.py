# coding=utf-8
import unittest
import time
from pageobjects.login_page import LoginPage
from framework.driver import WDriver
from framework.log import Logger
import logging
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

index_url = 'http://sw-staging.zcygov.cn/service-platform/#/service/window/publish'


# @unittest.skip
class TestLogin(unittest.TestCase):
    """验证从工作台成功进入疫苗馆"""
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

    # def test_login(self):
    #     """用例标题：校验区疾控登录成功
    #        参数：用户名/密码 13777466979/test123456
    #        预期：登录成功
    #     """
    #     LoginPage(self.driver).login('15088888888', 'test123456')
    #     LoginPage(self.driver).openurl(index_url)
    #     LoginPage(self.driver).icons()




