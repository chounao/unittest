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
gys_bidding_order_url = 'https://staging.zcy.gov.cn/health/agreementsupply/bidding/bidding'
gys1_price = 40000
gys2_username = 'mingchao001'
gys2_password = 'wmc123456'
gys2_price = 43000
cgdw_username = 'ocean02'
cgdw_password = 'test123456'
stop_quote_partial_url = 'http://staging.zcy.gov.cn/health/api/test/endProtocolBiddingNow?requireId='
cgsw_bidding_list_url = 'https://staging.zcy.gov.cn/health/agreementsupply/list/list'
ghzx_username = 'ghzx'
ghzx_password = 'test123456'
ghzx_check_url = 'https://staging.zcy.gov.cn/health/expert-review/result-check-list'


@unittest.skip
class TestBiddingOrder0416(MyunitTest):
    """国和中心审核通过，竞价完成"""

    def test_bidding_order_0416(self):
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
        BiddingOrderManagement(self.driver).confirm_result('受理结果通过', cgsw_bidding_list_url)
        time.sleep(3)
        LoginPage(self.driver).again_login(ghzx_username, ghzx_password, ghzx_check_url)  # 切换到国和中心账号
        BiddingOrderManagement(self.driver).ghzx_check()  # 专家审核通过
        flag = BiddingOrderManagement(self.driver).check_submit_result_ghzx()
        self.assertTrue(flag, '专家审核通过后，状态变未变为竞价完成')
        if flag:
            BiddingOrderManagement(self.driver).get_img('test_0416_bidding_order_pass.png')
        else:
            BiddingOrderManagement(self.driver).get_img('test_0416_bidding_order_fail.png')









