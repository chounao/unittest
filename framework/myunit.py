'''
Code description：unittest framwork
Create time：
Developer：
'''

from framework.driver import WDriver
import unittest
from pageobjects.login_page import LoginPage
from framework.log import Logger
import logging


log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class MyunitTest(unittest.TestCase):
    """

    """

    # add by xuechao at 2018.09.19
    @classmethod
    def setUpClass(cls):  # 一个测试类(文件)执行一次打开浏览器, 节约每个用例打开一次浏览器的时间

        cls.driver = WDriver().chromeDriver()
        cls.driver.maximize_window()
        # cls.driver.set_window_size(1280, 800)
        log.logger.info('opened the browser successed!')
    # ----------------------------

    def setUp(self):
        """

        :return:
        """
        login = LoginPage(self.driver)
        login.open_login()
        LoginPage(self.driver).login()
        log.logger.info('************************starting run test cases************************')

    def tearDown(self):
        """

        :return:
        """
        self.driver.refresh()
        log.logger.info('************************test case run completed************************')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        log.logger.info('quit the browser success!')


# if __name__ == '__main__':
#     unittest.main()
