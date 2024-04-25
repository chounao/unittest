# coding=utf-8
from framework.base_page import BasePage
from framework.log import Logger
import logging
from pageobjects.login_page import LoginPage
from data.bidding_order_management_data import BiddingOrderManagementData
from selenium.webdriver.common.keys import Keys
import time

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
health_selectors = ['css', '.zcy-icon.icon-app_icon_ylqx']  # 工


class BiddingOrderManagement(BasePage):
    """竞价单管理页面"""

    def modify_goodsnum(self, goodsnum):
        """修改商品数量"""
        log.logger.info('修改商品数量为:%s' % goodsnum)
        BasePage(self.driver).insert_value(BiddingOrderManagementData.quantity_selectors, goodsnum)

    def check_is_group_buying(self):
        """判断是否集团采购=否"""
        log.logger.info('是否集团采购=否')
        BasePage(self.driver).click(BiddingOrderManagementData.grop_buying_selectors)
        BasePage(self.driver).click(BiddingOrderManagementData.no_grop_buying_selectors)

    def addplan(self, num):
        """添加列表中第一个采购计划"""
        log.logger.info('添加采购计划')
        BasePage(self.driver).scrolls(BiddingOrderManagementData.add_plan_selectors)  # 下划找到采购计划
        BasePage(self.driver).click(BiddingOrderManagementData.add_plan_selectors)  # 点击添加采购计划按钮
        BasePage(self.driver).click_list(BiddingOrderManagementData.plan_button_selectors, 0)  # 选择第一个采购计划
        BasePage(self.driver).click(BiddingOrderManagementData.save_plan_selectors)  # 保存采购计划
        BasePage(self.driver).scrolls(BiddingOrderManagementData.plan_num_selectors)  # 下划找到采购计划
        BasePage(self.driver).insert_value(BiddingOrderManagementData.plan_num_selectors, num)  # 添加采购计划数量

    def add_require_title(self, title):
        """
        添加竞价单标题
        :param title: 竞价单标题
        :return:
        """
        BasePage(self.driver).scrolls(BiddingOrderManagementData.require_title_selectors)
        BasePage(self.driver).insert_value(BiddingOrderManagementData.require_title_selectors, title)

    def modify_bidding_cycle(self, cycle):
        """修改竞价周期"""
        log.logger.info('修改竞价周期为:%s个小时' % cycle)
        BasePage(self.driver).scrolls(BiddingOrderManagementData.bidding_cycle_selectors)  # 下滑找到收货地址
        BasePage(self.driver).insert_value(BiddingOrderManagementData.bidding_cycle_selectors, cycle)

    def select_address(self):
        """
        选择收货地址
        :return:
        """
        BasePage(self.driver).scrolls(BiddingOrderManagementData.select_address_selectors)  # 下滑找到收货地址
        BasePage(self.driver).click_list(BiddingOrderManagementData.select_address_selectors, 1)  # 点击选择收货地址

    def add_address_quantity(self, goodsnum):
        """
        添加收货数量
        :param goodsnum: 收货数量
        :return:
        """
        BasePage(self.driver).scrolls(BiddingOrderManagementData.address_quantity_selectors)
        BasePage(self.driver).insert_value(BiddingOrderManagementData.address_quantity_selectors, goodsnum)
        BasePage(self.driver).click(BiddingOrderManagementData.blank_selectors)

    def submit(self):
        """
        提交意见审核
        :return:
        """
        BasePage(self.driver).scrolls(BiddingOrderManagementData.submit_selectors)
        BasePage(self.driver).click(BiddingOrderManagementData.submit_selectors)  # 意见审核-提交

    def sure_submit(self):
        """
        确认提交意见审核
        :return:
        """
        BasePage(self.driver).click(BiddingOrderManagementData.sure_sumbit_selectors)  # 弹出窗口-确定提交

    def add_bidding_order(self, goodsnum, plannum, cycle, addressgoodsnum, title):
        """
        提交竞价单
        :param goodsnum: 商品数量
        :param plannum: 使用采购计划数量
        :param cycle: 订购周期
        :param addressgoodsnum: 收货地址对应数量
        :param title: 竞价单标题
        :return:
        """
        self.modify_goodsnum(goodsnum)
        log.logger.info(str(BasePage(self.driver).getcurrenturl()).split('=')[1])
        order_id = str(BasePage(self.driver).getcurrenturl()).split('=')[1]
        self.check_is_group_buying()
        try:
            self.addplan(plannum)
        except Exception:
            log.logger.exception('无可用采购计划', exc_info=True)
            raise
        else:
            self.add_require_title(title)
            self.select_address()
            self.modify_bidding_cycle(cycle)
            self.add_address_quantity(addressgoodsnum)
            self.submit()
            self.sure_submit()
            return order_id

    def check_biddingorder(self):
        """检查列表页第一行状态是否是竞价单待审核"""
        texts = BasePage(self.driver).get_text(BiddingOrderManagementData.status_selectors)
        if texts == '竞价单待审核':
            return True
        else:
            return False

    def bidding_check_click(self):
        """列表页点击审核，进入页面"""
        BasePage(self.driver).click(BiddingOrderManagementData.bidding_check_selectors)

    def begin_check_click(self):
        """订购审核页，点击最下方的开始审核"""
        BasePage(self.driver).click(BiddingOrderManagementData.begin_check_selectors)

    def bargaining_select(self):
        """订购审核页，点击最下方的开始审核"""
        BasePage(self.driver).click(BiddingOrderManagementData.bargaining_selectors)
        BasePage(self.driver).click(BiddingOrderManagementData.date_input_selectors)
        BasePage(self.driver).click(BiddingOrderManagementData.select_hour_selectors)
        BasePage(self.driver).click(BiddingOrderManagementData.click_hour_selectors)

    def insert_check_opinion(self, value):
        """
        审核输入框，输入内容
        :param value: 输入框中输入内容
        :return:
        """
        BasePage(self.driver).insert_value(BiddingOrderManagementData.check_opinion_selectors, value)

    def cgdw_check(self, value):
        """
        采购单位审核通过
        :param value: 审核意见
        :return:
        """

        try:
            self.bidding_check_click()
        except Exception:
            log.logger.exception('未生成竞价单待审核状态订购单或者点击竞价单审核无效', exc_info=True)
            raise
        else:
            self.begin_check_click()
            self.insert_check_opinion(value)
            self.submit()
            self.sure_submit()

    def check_biddingorder_status(self):
        """检查竞价单审核列表页第一行状态是否是报价中"""
        texts = BasePage(self.driver).get_text(BiddingOrderManagementData.status_selectors)
        if texts == '报价中':
            return True
        else:
            return False

    def check_biddingorder_status_gys(self):
        """检查供货商-报价单列表页第一行状态是否是未报价，操作按钮=报价"""
        texts = BasePage(self.driver).get_text(BiddingOrderManagementData.offer_btn_selectors)
        if texts == '报价  ':
            return True
        else:
            return False

    def offer_btn_click_gys(self):
        BasePage(self.driver).click(BiddingOrderManagementData.offer_btn_selectors)  # 点击供应商-报价单列表报价

    def quote_price(self, quote_price):
        # 输入单价报价
        BasePage(self.driver).scrolls(BiddingOrderManagementData.quote_price_selectors)
        BasePage(self.driver).insert_value(BiddingOrderManagementData.quote_price_selectors, quote_price)
        # 键盘点击ENTER
        time.sleep(3)
        BasePage(self.driver).click_enter(BiddingOrderManagementData.quote_price_selectors)

    def show_promise_btn_click_gys(self):
        BasePage(self.driver).click(BiddingOrderManagementData.show_promise_selectors)  # 点击供应商-报价单列表报价
        BasePage(self.driver).click(BiddingOrderManagementData.create_confirm_selectors)  # 报价承诺-确定按钮

    def show_promise_gys(self, quote_price):
        # 供应商报价
        self.offer_btn_click_gys()
        self.quote_price(quote_price)
        self.show_promise_btn_click_gys()

    def result_click(self, cgsw_bidding_list_url):

        BasePage(self.driver).open(cgsw_bidding_list_url)  # 打开竞价单列表页面
        self.cgdw_result()  # 点击采购单位-竞价单列表页第一行-结果确认按钮

    def check_promise_status_cgdw(self, cgsw_bidding_list_url):
        """检查采购单位-竞价单列表页-结果确认-预成交供货商是否是云舒001集团有限公司"""
        self.result_click(cgsw_bidding_list_url)
        BasePage(self.driver).scrolls(BiddingOrderManagementData.selectric_gys_selectors)
        texts = BasePage(self.driver).get_text(BiddingOrderManagementData.selectric_gys_selectors)
        if texts == '云舒001集团有限公司':
            return True
        else:
            return False

    def result_submit_click(self):
        BasePage(self.driver).click(BiddingOrderManagementData.result_submit_selectors)

    def accept_ok_submit_cgsw(self):
        BasePage(self.driver).click(BiddingOrderManagementData.accept_ok_submit_cgsw_selectors)

    def confirm_result(self, value, cgsw_bidding_list_url):
        self.result_click(cgsw_bidding_list_url)
        self.begin_check_click()  # 点击最下方-提交审核按钮
        self.insert_check_opinion(value)  # 输入情况说明
        self.result_submit_click()  # 点击提交按钮
        self.accept_ok_submit_cgsw()  # 确认提交

    def check_confirm_result_ghzx(self):
        """检查采购单位-竞价单列表页第一行状态是否是专家结果审核"""
        texts = BasePage(self.driver).get_text(BiddingOrderManagementData.ghzx_stauts_selectors)
        if texts == '专家结果审核':
            return True
        else:
            return False

    def ghzx_check_btn_click(self):
        """点击国和中心列表-审核按钮"""
        BasePage(self.driver).click(BiddingOrderManagementData.examine_ghzx_selectors)

    def ghzx_submit_audit(self):
        """国和中心审核页面-开始审核-提交"""
        BasePage(self.driver).click(BiddingOrderManagementData.begin_audit_check_selectors)  # 点击开始审核
        BasePage(self.driver).click(BiddingOrderManagementData.submit_audits_selectors)  # 点击提交按钮

    def ghzx_check(self):
        self.ghzx_check_btn_click()
        self.ghzx_submit_audit()

    def check_submit_result_ghzx(self):
        """检查国合中心-采购结果审核第一行状态是否是竞价完成"""
        texts = BasePage(self.driver).get_text(BiddingOrderManagementData.examined_status_ghzx_selectors)
        if str(texts).strip() == '竞价完成':
            return True
        else:
            return False

    def apply_for_bargaining(self, value, cgsw_bidding_list_url):
        """采购单位申请议价"""
        self.result_click(cgsw_bidding_list_url)
        self.begin_check_click()  # 点击最下方-提交审核按钮
        self.bargaining_select()  # 选择申请议价
        self.insert_check_opinion(value)  # 输入情况说明
        self.result_submit_click()  # 点击提交按钮
        self.accept_ok_submit_cgsw()  # 确认提交

    def check_bargain_status_gys(self):
        """检查供货商议价列表第一行状态是否是议价中"""
        texts = BasePage(self.driver).get_text(BiddingOrderManagementData.bargaining_status_selectors)
        if texts == '议价中':
            return True
        else:
            return False

    def gys_reply_bargaining_click(self):
        """供货商点击议价列表-回复议价按钮"""
        BasePage(self.driver).click(BiddingOrderManagementData.reply_bargaining_selectors)

    def submit_bargaining(self, bargainprice):
        """
        同意议价-输入议价单价-提交
        :param bargainprice:议价单价
        :return:
        """
        BasePage(self.driver).scrolls(BiddingOrderManagementData.bargainprice_selectors)
        BasePage(self.driver).insert_value(BiddingOrderManagementData.bargainprice_selectors, bargainprice)  # 输入议价单价
        BasePage(self.driver).click(BiddingOrderManagementData.bargainprice_submit_selectors)  # 点击提交按钮
        BasePage(self.driver).click(BiddingOrderManagementData.bargainprice_determin_selectors)  # 点击确定按钮

    def gys_determin_bargaining(self, bargainprice):
        self.gys_reply_bargaining_click()
        self.submit_bargaining(bargainprice)

    def cgdw_result(self):
        BasePage(self.driver).click(BiddingOrderManagementData.result_selectors)  # 点击采购单位-竞价单列表页第一行-结果确认按钮

    def check_bargain_sucess_cgdw(self):
        """检查采购单位确认结果中，是否有议价成功标识"""
        self.cgdw_result()  # 点击采购单位-竞价单列表页第一行-结果确认按钮
        BasePage(self.driver).scrolls(BiddingOrderManagementData.bargaining_success_selectors)
        texts = BasePage(self.driver).get_text(BiddingOrderManagementData.bargaining_success_selectors)
        if texts == '议价成功':
            return True
        else:
            return False

    def cgdw_determin_bargaining(self, value):
        self.cgdw_result()  # 点击采购单位-竞价单列表页第一行-结果确认按钮
        self.begin_check_click()  # 点击最下方-提交审核按钮
        self.insert_check_opinion(value)  # 输入情况说明
        self.result_submit_click()  # 点击提交按钮
        self.accept_ok_submit_cgsw()  # 确认提交

    # def again_login(self, username, password, url):
    #     """
    #
    #     :param username: 新账号用户名
    #     :param password: 新账号密码
    #     :param url: 新地址
    #     :return:
    #     """
    #     LoginPage(self.driver).logout()  # 账号退出
    #     LoginPage(self.driver).login(username, password)  # 登录新账号
    #     BasePage(self.driver).openurl(url)
    #
    # def check_review(self):
    #     """
    #     检查列表页第一行状态，是否为待供应商确认
    #     :return:
    #     """
    #     texts = BasePage(self.driver).get_text(OrderManagementData.status_selectors)
    #     if texts == '供应商待确认':
    #         return True
    #     else:
    #         return False
    #
    # def remove_initateorder(self):
    #     """
    #     点击撤回订购单
    #     :return:
    #     """
    #     BasePage(self.driver).click(OrderManagementData.remove_selectors)
    #
    # def comfire_remove(self, value):
    #     """
    #     确认撤回
    #     :param value: 输入框中输入内容
    #     :return:
    #     """
    #     # 撤回窗口-输入框输入撤回理由
    #     BasePage(self.driver).insert_value(OrderManagementData.remove_reason_selectors, value)
    #     # 点击确定按钮
    #     BasePage(self.driver).click(OrderManagementData.confirm_remove_selectors)
    #
    # def cgdw_remove(self, value):
    #     """
    #     采购单位撤回订购单
    #     :param value: 撤回理由
    #     :return:
    #     """
    #     try:
    #         self.remove_initateorder()
    #     except Exception:
    #         log.logger.exception('未生成待供应商确认状态订购单', exc_info=True)
    #         raise
    #     else:
    #         self.comfire_remove(value)
    #
    # def check_remove(self):
    #     """
    #     检查列表页第一行状态，是否为已撤回
    #     :return:
    #     """
    #     texts = BasePage(self.driver).get_text(OrderManagementData.status_selectors)
    #     if texts == '已撤回':
    #         return True
    #     else:
    #         return False
