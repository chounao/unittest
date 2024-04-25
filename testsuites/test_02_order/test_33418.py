# coding=utf-8
import unittest
from pageobjects.order_page import OrderPage
from framework.myunit import MyunitTest
from framework.log import Logger
import logging
import time
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
detail_url = 'https://vaccine-staging.zcygov.cn/items/175600205?' \
             'searchType=1&type=vaccine&utm=a0004.2ef5001f.0.0.33d8ffd0ca0411e9af8ed36431cbf75c'


@unittest.skip
class TestDetailInitateOrder(MyunitTest):
    """校验商品详情页面创建预购单"""

    def test_detail_initate_order(self):
        # 打开商品详情页
        OrderPage(self.driver).openurl(detail_url)
        time.sleep(2)
        try:
            # 点击立即下单按钮
            OrderPage(self.driver).ordertoinitate()
            time.sleep(3)
            nowurl = OrderPage(self.driver).getcurrenturl()
            log.logger.info(nowurl)
            self.assertIn('https://vaccine-staging.zcygov.cn/buyer/purchase-process?purchaseId=', nowurl,
                          msg='生成预购单失败！')
        except Exception:
            OrderPage(self.driver).get_img('test_33418_fail.png')
            log.logger.info('运行失败：生成预购单失败')
            raise
        else:
            OrderPage(self.driver).get_img('test_33418_pass.png')
            log.logger.info('运行成功：生成预购单成功')





