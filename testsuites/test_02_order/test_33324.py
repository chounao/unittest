# coding=utf-8
import unittest
from pageobjects.order_page import OrderPage
from framework.myunit import MyunitTest
from framework.log import Logger
import logging
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
# 购物车页面
carturl = 'https://cart-staging.zcygov.cn/'


@unittest.skip
class TestClearCart(MyunitTest):
    """校验清空购物车"""

    def test_clearcart(self):
        OrderPage(self.driver).openurl(carturl)
        flag = OrderPage(self.driver).clearcart()
        if flag:
            self.assertTrue(flag)
            OrderPage(self.driver).get_img('test_33324_pass.png')
            log.logger.info('运行成功：清空购物车成功')
        else:
            self.assertFalse(flag)
            OrderPage(self.driver).get_img('test_33324_fail.png')
            log.logger.info('运行失败：清空购物车失败')





