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
goodsname = '甲型肝炎灭活疫苗0508'


@unittest.skip
class TestAddCart(MyunitTest):
    """校验商品‘甲型肝炎灭活疫苗0508’加入购物车"""

    def test_addcart(self):
        OrderPage(self.driver).openurl(carturl)
        OrderPage(self.driver).clearcart()
        try:
            OrderPage(self.driver).openurl(detail_url)
            time.sleep(5)
            OrderPage(self.driver).addtocart()
            self.assertIn(goodsname, self.driver.page_source, msg='验证不成功！')
        except Exception:
            OrderPage(self.driver).get_img('test_33304_fail.png')
            log.logger.info('运行失败：加入购物车成功')
            raise
        else:
            OrderPage(self.driver).get_img('test_33304_pass.png')
            log.logger.info('运行成功：加入购物车成功')



