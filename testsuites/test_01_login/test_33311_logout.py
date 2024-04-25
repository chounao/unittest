# coding=utf-8
import unittest
import time
from pageobjects.login_page import LoginPage
from framework.myunit import MyunitTest
from framework.base_page import BasePage
from framework.log import Logger
import logging
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


@unittest.skip
class TestLogout(MyunitTest):
    """校验账号退出成功"""
    def test_logout(self):
        """用例标题：退出账号
       参数：无
       预期：退出账号成功
        """
        try:
            LoginPage(self.driver).logout()
            self.assertEqual(LoginPage(self.driver).get_title(), "政采云，一站式政府采购云平台—登录相关", msg="验证不成功！")
        except Exception:
            BasePage(self.driver).get_img('logout_0116_fail.png')
            log.logger.info('运行失败：退出失败')
            raise
        else:
            BasePage(self.driver).get_img('logout_0116_pass.png')
            log.logger.info('运行成功：退出成功')

