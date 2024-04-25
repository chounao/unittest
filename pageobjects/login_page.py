# coding=utf-8
from framework.read_config import TestReadConfigFile
from framework.base_page import BasePage
from framework.log import Logger
from selenium.webdriver.common.action_chains import ActionChains
from data.login_data import LoginPageData
import time
import logging


log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class LoginPage(BasePage):
    def open_login(self):
        test_read_config_file = TestReadConfigFile()
        url = test_read_config_file.get_config_value('stagingData', 'URL')
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(5)
            log.logger.info('%s 打开登录地址成功' % url)
        except Exception as e:
            log.logger.exception(e, exc_info=True)
            raise ValueError('%s 打开登录地址错误，请检查' % url)
        return self.driver

    def login(self, username='13777466979', password='test123456'):
        # def login(self, username='15088888888', password='test123456'):
        """登录"""
        # 获取用户名、密码输入框
        BasePage(self.driver).insert_value(LoginPageData.username_selectors, username)
        BasePage(self.driver).insert_value(LoginPageData.password_selectors, password)
        # 点击登录
        BasePage(self.driver).click(LoginPageData.login_selectors)

    def logout(self):
        """退出"""
        time.sleep(2)
        BasePage(self.driver).scroll_rigth_click(LoginPageData.quit_postion_selectors)
        BasePage(self.driver).click(LoginPageData.logout_selectors)

    def order_logout(self):
        """退出"""
        BasePage(self.driver).scroll_rigth_click(LoginPageData.order_quit_postion_selectors)
        BasePage(self.driver).click(LoginPageData.logout_selectors)

    def again_login(self, username, password, url):
        """

        :param username: 新账号用户名
        :param password: 新账号密码
        :param url: 新地址
        :return:
        """
        LoginPage(self.driver).open_login()
        LoginPage(self.driver).clear_cookie()
        LoginPage(self.driver).login(username, password)  # 登录新账号
        BasePage(self.driver).openurl(url)

    # def icons(self):
    #     BasePage(self.driver).style_none()
    #     BasePage(self.driver).insert_value(LoginPageData.test_icon_selectors, u'D:\icon.png')
