# coding=utf-8
import unittest
from pageobjects.order_page import OrderPage
from framework.myunit import MyunitTest
from framework.log import Logger
import logging
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


@unittest.skip
class TestClickMall(MyunitTest):
    """验证从工作台成功进入疫苗馆"""

    def test_vaccinehurl(self):
        self.driver.implicitly_wait(5)
        OrderPage(self.driver).clickmall()
        try:
            self.assertEqual(OrderPage(self.driver).get_title(), "二类疫苗", msg="验证不成功！")
        except Exception:
            OrderPage(self.driver).get_img('test_33302_fail.png')
            log.logger.info('运行失败：进入疫苗馆失败')
            raise
        else:
            OrderPage(self.driver).get_img('test_33302_pass.png')
            log.logger.info('运行成功：进入疫苗馆')




