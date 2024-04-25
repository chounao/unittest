# coding=utf-8
import unittest
from pageobjects.initate_order_management_page import OrderManagement
from pageobjects.cgdw_index_page import CgdwIndex
from framework.myunit import MyunitTest
from framework.log import Logger
from pageobjects.login_page import LoginPage
import time
import logging
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
# 购物车页面
carturl = 'https://medical-staging.zcy.gov.cn/medical/shoppingcart'
googds_detail_url = 'https://medical-staging.zcy.gov.cn/medical/search?' \
      'q=%E4%BA%91%E8%88%92002%E5%8C%BB%E7%96%97--%E6%99%AE%E6%9C%97X%E5%B0%84%E7%BA%BF%E6%9C%BAPLD5000A'
username = 'mingchao001'
password = 'wmc123456'
initate_order_url = 'https://staging.zcy.gov.cn/health/agreementsupply/purchaseOrder/supplierList'


@unittest.skip
class TestInitateOrder0314(MyunitTest):
    """供应商生成待确认状态的直购单"""

    def test_gsy_initate_order_0314(self):
        CgdwIndex(self.driver).openurl(carturl)  # 打开购物车地址
        CgdwIndex(self.driver).clearcart()  # 清空购物车
        CgdwIndex(self.driver).openurl(googds_detail_url)  # 打开商品详情页
        CgdwIndex(self.driver).addtocart()  # 商品添加到购物车
        CgdwIndex(self.driver).addorder()  # 进入订购单详情页
        OrderManagement(self.driver).add_initateorder(2, 2, '柏柏测试订购单')  # 生成待审核状态的订购单
        OrderManagement(self.driver).cgdw_check('同意')  # 审核通过，生成待供应商确认状态的订购单
        time.sleep(5)
        LoginPage(self.driver).again_login(username, password, initate_order_url)
        flag = OrderManagement(self.driver).check_confirm_gys()  # 检查是否生成待审核状态的订购单（列表第一行）
        self.assertTrue(flag, '供应商生成待确认状态订购单失败')
        if flag:
            OrderManagement(self.driver).get_img('test_0314_gsy_initate_order_pass.png')
        else:
            OrderManagement(self.driver).get_img('test_0314_gsy_initate_order_fail.png')
        time.sleep(5)







