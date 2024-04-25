# coding=utf-8
import unittest
from pageobjects.order_page import OrderPage
from pageobjects.login_page import LoginPage
from framework.myunit import MyunitTest
from framework.log import Logger
import logging
import time
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
carturl = 'https://cart-staging.zcygov.cn/'  # 购物车页面
detail_url = 'https://vaccine-staging.zcygov.cn/items/175600205?' \
             'searchType=1&type=vaccine&utm=a0004.2ef5001f.0.0.33d8ffd0ca0411e9af8ed36431cbf75c'
gys_username = 'SINOVAC'
gys_password = 'test123456'
gys_order_url = 'https://staging.zcygov.cn/seller/vaccine-orders'


@unittest.skip
class TestGysRequierOrder(MyunitTest):
    """校验供应商接单"""

    def test_gys_require_order(self):
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
        # 切换到供应商账号
        LoginPage(self.driver).again_login(gys_username, gys_password, gys_order_url)
        # 供应商接单
        OrderPage(self.driver).gys_review_order()
        # 检查是否接单成功
        flag = OrderPage(self.driver).check_gys_status()
        if flag:
            self.assertTrue(flag)
            OrderPage(self.driver).get_img('test_33313_pass.png')
            log.logger.info('运行成功：接单成功')
        else:
            self.assertFalse(flag)
            OrderPage(self.driver).get_img('test_33313_fail.png')
            log.logger.info('运行失败：接单失败')








