# coding=utf-8
import unittest
from pageobjects.bidding_order_management_page import BiddingOrderManagement
from pageobjects.cgdw_index_page import CgdwIndex
from pageobjects.login_page import LoginPage
from framework.base_page import BasePage
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
gys_bidding_order_url = 'https://staging.zcy.gov.cn/health/agreementsupply/bidding/bidding'  # 供应商竞价单列表页
gys_bargaining_url = 'https://staging.zcy.gov.cn/trading-health-index/#/bargain/bargainList'  # 供应商议价列表页
gys1_price = 40000
gys2_username = 'mingchao001'
gys2_password = 'wmc123456'
gys2_price = 43000
cgdw_username = 'ocean02'
cgdw_password = 'test123456'
stop_quote_partial_url = 'http://staging.zcy.gov.cn/health/api/test/endProtocolBiddingNow?requireId='
cgdw_bidding_list_url = 'https://staging.zcy.gov.cn/health/agreementsupply/list/list'
ghzx_username = 'ghzx'
ghzx_password = 'test123456'
ghzx_check_url = 'https://staging.zcy.gov.cn/health/expert-review/result-check-list'


@unittest.skip
class TestBiddingOrder0418(MyunitTest):
    """供货商同意二次议价"""

    def test_bidding_order_0418(self):
        CgdwIndex(self.driver).click_detail_bidding_btn(detail_url)
        order_id = BiddingOrderManagement(self.driver).add_bidding_order(2, 2, 2, 2, '柏柏测试竞价单')  # 生成竞价单待审核状态的竞价单
        time.sleep(3)
        CgdwIndex(self.driver).openurl(initate_check_url)  # 进入竞价单审核列表
        BiddingOrderManagement(self.driver).cgdw_check('同意')  # 审核通过
        time.sleep(3)
        LoginPage(self.driver).again_login(gys_username, gys_password, gys_bidding_order_url)  # 切换到供应商账号-报价单列表
        BiddingOrderManagement(self.driver).show_promise_gys(gys1_price)
        time.sleep(3)
        LoginPage(self.driver).again_login(gys2_username, gys2_password, gys_bidding_order_url)  # 切换到供应商账号-报价单列表
        BiddingOrderManagement(self.driver).show_promise_gys(gys2_price)
        time.sleep(3)
        stop_quote_url = str(stop_quote_partial_url) + str(order_id)
        log.logger.info('stop_quote_url.....%s' % stop_quote_url)
        LoginPage(self.driver).again_login(cgdw_username, cgdw_password, stop_quote_url)  # 切换到采购单位账号
        time.sleep(80)
        BiddingOrderManagement(self.driver).apply_for_bargaining('申请议价', cgdw_bidding_list_url)  # 申请议价
        time.sleep(3)
        LoginPage(self.driver).again_login(gys_username, gys_password, gys_bargaining_url)  # 切换供应商账号-议价列表
        BiddingOrderManagement(self.driver).gys_determin_bargaining(100)  # 供货商回复议价
        time.sleep(3)
        LoginPage(self.driver).again_login(cgdw_username, cgdw_password, cgdw_bidding_list_url)  # 切换到采购单位账号
        flag = BiddingOrderManagement(self.driver).check_bargain_sucess_cgdw()
        self.assertTrue(flag, '申请议价不成功')
        if flag:
            BiddingOrderManagement(self.driver).get_img('test_0418_bidding_order_pass.png')
        else:
            BiddingOrderManagement(self.driver).get_img('test_0418_bidding_order_fail.png')









