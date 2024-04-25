# coding=utf-8
import unittest
from pageobjects.bidding_order_management_page import BiddingOrderManagement
from pageobjects.cgdw_index_page import CgdwIndex
from framework.myunit import MyunitTest
import time
from framework.log import Logger
import logging
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
# 商品详情页：云舒002医疗--康瑞德X射线诊断剂量计
detail_url = 'https://medical-staging.zcy.gov.cn/medical/detail?itemId=9383084&goodsId=86135&supplierCode=1000462820'


@unittest.skip
class TestBiddingOrder0411(MyunitTest):
    """发起竞价单"""

    def test_bidding_order_0411(self):
        CgdwIndex(self.driver).click_detail_bidding_btn(detail_url)
        time.sleep(3)
        BiddingOrderManagement(self.driver).add_bidding_order(2, 2, 2, 2, '柏柏测试竞价单')  # 生成竞价单待审核状态的竞价单
        flag = BiddingOrderManagement(self.driver).check_biddingorder()  # 检查是否生成竞价单待审核状态的竞价单
        self.assertTrue(flag, '竞价单提交失败')
        if flag:
            BiddingOrderManagement(self.driver).get_img('test_0411_bidding_order_pass.png')
        else:
            BiddingOrderManagement(self.driver).get_img('test_0411_bidding_order_fail.png')








