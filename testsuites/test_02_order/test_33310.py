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
class TestReviewOrder(MyunitTest):
    """提交订单"""

    def test_review_order(self):
        # 清空购物车
        OrderPage(self.driver).openurl(carturl)
        OrderPage(self.driver).clearcart()
        # 添加商品到购物车
        OrderPage(self.driver).openurl(detail_url)
        time.sleep(5)
        OrderPage(self.driver).addtocart()
        # 生成预购单
        OrderPage(self.driver).add_initateorder()
        # 提交预购单
        OrderPage(self.driver).submit_initateorder()
        # 预购单审核
        OrderPage(self.driver).all_review()
        # 提交订单
        OrderPage(self.driver).review_order()

        # 检查预购单是否提交成功
        flag = OrderPage(self.driver).check_review_order()
        if flag:
            self.assertTrue(flag)
            OrderPage(self.driver).get_img('test_33310_pass.png')
            log.logger.info('运行成功：生成订单成功')
        else:
            self.assertFalse(flag)
            OrderPage(self.driver).get_img('test_33310_fail.png')
            log.logger.info('运行失败：生成订单失败')







