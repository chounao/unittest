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
gys_username = 'mingchao001'
gys_password = 'wmc123456'
gys_initate_order_url = 'https://staging.zcy.gov.cn/health/agreementsupply/purchaseOrder/supplierList'


@unittest.skip
class TestInitateOrderYiJia(MyunitTest):
    """直购单-意向单价小于协议单价，供应商生成有议价标识的直购单"""

    def test_gsy_confirm_initate_order_yijia(self):
        CgdwIndex(self.driver).openurl(carturl)  # 打开购物车地址
        CgdwIndex(self.driver).clearcart()  # 清空购物车
        CgdwIndex(self.driver).openurl(googds_detail_url)  # 打开商品详情页
        CgdwIndex(self.driver).addtocart()  # 商品添加到购物车
        CgdwIndex(self.driver).addorder()  # 进入订购单详情页
        OrderManagement(self.driver).add_initateorde_yijia(2, 70000, 2, '柏柏测试订购单')  # 生成待审核状态的订购单
        OrderManagement(self.driver).cgdw_check('同意')  # 审核通过，生成待供应商确认状态的订购单
        time.sleep(5)
        LoginPage(self.driver).again_login(gys_username, gys_password, gys_initate_order_url)
        OrderManagement(self.driver).click_check_confirm_gys()  # 点击确认，进入订购单详情页
        try:
            self.assertIn('有议价', self.driver.page_source, msg='验证不成功！')
        except Exception:
            CgdwIndex(self.driver).get_img(' test_0316_gsy_confirm_initate_order_yijia_fail.png')
            raise
        else:
            CgdwIndex(self.driver).get_img(' test_0316_gsy_confirm_initate_order_yijia_pass.png')
            log.logger.info('生成有议价订购单成功')
        time.sleep(15)







