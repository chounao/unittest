# coding=utf-8
import unittest
from pageobjects.initate_order_management_page import OrderManagement
from pageobjects.cgdw_index_page import CgdwIndex
from framework.myunit import MyunitTest
from framework.log import Logger
import logging
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
# 购物车页面
carturl = 'https://medical-staging.zcy.gov.cn/medical/shoppingcart'
url = 'https://medical-staging.zcy.gov.cn/medical/search?' \
      'q=%E4%BA%91%E8%88%92002%E5%8C%BB%E7%96%97--%E6%99%AE%E6%9C%97X%E5%B0%84%E7%BA%BF%E6%9C%BAPLD5000A'


@unittest.skip
class TestInitateOrder0312(MyunitTest):
    """订购单-采购单位审核通过，生成-供应商待确认-状态的订购单"""

    def test_initate_order_0312(self):
        CgdwIndex(self.driver).openurl(carturl)  # 打开购物车地址
        CgdwIndex(self.driver).clearcart()  # 清空购物车
        CgdwIndex(self.driver).openurl(url)  # 打开商品详情页
        CgdwIndex(self.driver).addtocart()  # 商品添加到购物车
        CgdwIndex(self.driver).addorder()  # 进入订购单详情页
        OrderManagement(self.driver).add_initateorder(2, 2, '柏柏测试订购单')  # 生成待审核状态的订购单
        OrderManagement(self.driver).cgdw_check('同意')  # 审核通过
        flag = OrderManagement(self.driver).check_review()  # 检查是否生成待供应商确认的订购单
        self.assertTrue(flag, '采购单位审核失败')
        if flag:
            OrderManagement(self.driver).get_img('test_0312_initate_order_pass.png')
        else:
            OrderManagement(self.driver).get_img('test_0312_initate_order_fail.png')








