# coding=utf-8
import unittest
from pageobjects.bidding_order_management_page import BiddingOrderManagement
from pageobjects.cgdw_index_page import CgdwIndex
from pageobjects.login_page import LoginPage
from framework.myunit import MyunitTest
import time
from framework.log import Logger
import logging
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
# 商品详情页：云舒002医疗--康瑞德X射线诊断剂量计
detail_url = 'https://medical-staging.zcy.gov.cn/medical/detail?itemId=9383084&goodsId=86135&supplierCode=1000462820'
initate_check_url = 'https://staging.zcy.gov.cn/health/agreementsupply/list/listCheck'  # 菜单-竞价单审核列表
gys_username = 'mingchao001'
gys_password = 'wmc123456'
gys_bidding_order_url = 'https://staging.zcy.gov.cn/health/agreementsupply/bidding/bidding'


@unittest.skip
class TestBiddingOrder0413(MyunitTest):
    """供货商生成未报价状态的竞价单"""

    def test_bidding_order_0413(self):
        CgdwIndex(self.driver).click_detail_bidding_btn(detail_url)
        time.sleep(3)
        BiddingOrderManagement(self.driver).add_bidding_order(2, 2, 2, 2, '柏柏测试竞价单')  # 生成竞价单待审核状态的竞价单
        CgdwIndex(self.driver).openurl(initate_check_url)  # 进入竞价单审核列表
        BiddingOrderManagement(self.driver).cgdw_check('同意')  # 审核通过
        time.sleep(5)
        LoginPage(self.driver).again_login(gys_username, gys_password, gys_bidding_order_url)  # 切换到供应商账号-报价单列表
        flag = BiddingOrderManagement(self.driver).check_biddingorder_status_gys()  # 检查供应商是否生成未报价态的竞价单
        self.assertTrue(flag, '供应商生成报价单失败')
        if flag:
            BiddingOrderManagement(self.driver).get_img('test_0413_bidding_order_pass.png')
        else:
            BiddingOrderManagement(self.driver).get_img('test_0413_bidding_order_fail.png')









