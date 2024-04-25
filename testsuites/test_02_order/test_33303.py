# coding=utf-8
import unittest
from pageobjects.order_page import OrderPage
from framework.myunit import MyunitTest
from framework.log import Logger
import logging
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
index_url = 'https://vaccine-staging.zcygov.cn/?fcid=4244&normal=2&type=vaccine&' \
            'utm=a0004.2ef5001f.0.0.bfa5af50ca0311e9ac3f4365eda56d93'
goodsname = '甲型肝炎灭活疫苗0508'


@unittest.skip
class TestSearchGoods(MyunitTest):
    """校验搜索疫苗商品‘甲型肝炎灭活疫苗0508’"""

    def test_searchgoods(self):
        self.driver.implicitly_wait(5)
        try:
            OrderPage(self.driver).openurl(index_url)
            OrderPage(self.driver).searchgoods(goodsname)
            flag = OrderPage(self.driver).searchisexist()
            self.assertTrue(flag, msg='验证不成功！')
        except Exception:
            OrderPage(self.driver).get_img('test_33303_fail.png')
            log.logger.info('运行失败：甲型肝炎灭活疫苗0508搜索成功')
            raise
        else:
            OrderPage(self.driver).get_img('test_33303_pass.png')
            log.logger.info('运行成功：甲型肝炎灭活疫苗0508搜索成功')





