# coding=utf-8
import unittest
from pageobjects.order_page import OrderPage
from framework.myunit import MyunitTest
from framework.log import Logger
import logging
import time
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
carturl = 'https://cart-staging.zcygov.cn/'  # 购物车页面
detail_url = 'https://vaccine-staging.zcygov.cn/items/175600205?' \
             'searchType=1&type=vaccine&utm=a0004.2ef5001f.0.0.33d8ffd0ca0411e9af8ed36431cbf75c'


@unittest.skip
class TestBuyAgain(MyunitTest):
    """校验待供应商接单状态，采购单位再次购买"""

    def test_buy_again(self):
        # 打开商品详情页
        OrderPage(self.driver).openurl(detail_url)
        time.sleep(2)
        OrderPage(self.driver).ordertoinitate()
        # 提交预购单
        OrderPage(self.driver).submit_initateorder()
        # 预购单审核
        OrderPage(self.driver).all_review()
        # 提交订单
        OrderPage(self.driver).review_order()
        # 再次购买
        OrderPage(self.driver).buy_again()
        # 检查再次购买是否跳转成功
        flag1 = OrderPage(self.driver).check_buy_again()
        flag2 = OrderPage(self.driver).check_carturl()
        flag = flag1 & flag2
        if flag:
            self.assertTrue(flag)
            OrderPage(self.driver).get_img('test_33346_pass.png')
            log.logger.info('运行成功：再次购买跳转成功')
        else:
            self.assertFalse(flag)
            OrderPage(self.driver).get_img('test_33346_fail.png')
            log.logger.info('运行失败：再次购买跳转失败')









