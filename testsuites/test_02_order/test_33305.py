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
class TestCartInitateOrder(MyunitTest):
    """校验购物车页面创建预购单"""

    def test_cart_initate_order(self):
        # 清空购物车
        OrderPage(self.driver).openurl(carturl)
        OrderPage(self.driver).clearcart()
        # 添加商品到购物车
        OrderPage(self.driver).openurl(detail_url)
        time.sleep(3)
        OrderPage(self.driver).addtocart()
        try:
            OrderPage(self.driver).add_initateorder()
            time.sleep(5)
            nowurl = OrderPage(self.driver).getcurrenturl()
            log.logger.info(nowurl)
            self.assertIn('https://staging.zcygov.cn/buyer/purchase-process?purchaseId=', nowurl,
                          msg='生成预购单失败！')
        except Exception:
            OrderPage(self.driver).get_img('test_33305_fail.png')
            log.logger.info('运行失败：生成预购单失败')
            raise
        else:
            OrderPage(self.driver).get_img('test_33305_pass.png')
            log.logger.info('运行成功：生成预购单成功')





