# coding=utf-8
from framework.base_page import BasePage
from framework.log import Logger
import logging
from data.order_management_data import OrderManagementData


log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
health_selectors = ['css', '.zcy-icon.icon-app_icon_ylqx']  # 工


class OrderManagement(BasePage):
    """订购单管理页面"""

    def modify_goodsnum(self, goodsnum):
        """修改商品数量"""
        log.logger.info('修改商品数量为:%s' % goodsnum)
        BasePage(self.driver).insert_value(OrderManagementData.quantity_selectors, goodsnum)

    def modify_controlprice(self, price):
        """修改商品数量"""
        log.logger.info('修改意向单价为:%s' % price)
        BasePage(self.driver).insert_value(OrderManagementData.controlPrice_selectors, price)

    def check_is_group_buying(self):
        """判断是否集团采购=否"""
        log.logger.info('是否集团采购=否')
        BasePage(self.driver).click(OrderManagementData.grop_buying_selectors)
        BasePage(self.driver).click(OrderManagementData.no_grop_buying_selectors)

    def addplan(self):
        """添加列表中第一个采购计划"""
        log.logger.info('添加采购计划')
        BasePage(self.driver).scrolls(OrderManagementData.add_plan_selectors)  # 下划找到采购计划
        BasePage(self.driver).click(OrderManagementData.add_plan_selectors)  # 点击添加采购计划按钮
        BasePage(self.driver).click_list(OrderManagementData.plan_button_selectors, 0)  # 选择第一个采购计划
        BasePage(self.driver).click(OrderManagementData.save_plan_selectors)  # 保存采购计划

    def add_require_title(self, title):
        """
        添加订购单标题
        :param title: 订购单标题
        :return:
        """
        BasePage(self.driver).scrolls(OrderManagementData.require_title_selectors)
        BasePage(self.driver).insert_value(OrderManagementData.require_title_selectors, title)

    def select_address(self):
        """
        选择收货地址
        :return:
        """
        BasePage(self.driver).scrolls(OrderManagementData.select_address_selectors)  # 下滑找到收货地址
        BasePage(self.driver).click_list(OrderManagementData.select_address_selectors, 1)  # 点击选择收货地址

    def add_address_quantity(self, goodsnum):
        """
        添加收货数量
        :param goodsnum: 收货数量
        :return:
        """
        BasePage(self.driver).scrolls(OrderManagementData.address_quantity_selectors)
        BasePage(self.driver).insert_value(OrderManagementData.address_quantity_selectors, goodsnum)
        BasePage(self.driver).click(OrderManagementData.blank_selectors)

    def submit(self):
        """
        提交意见审核
        :return:
        """
        BasePage(self.driver).scrolls(OrderManagementData.submit_selectors)
        BasePage(self.driver).click(OrderManagementData.submit_selectors)  # 意见审核-提交

    def sure_submit(self):
        """
        确认提交意见审核
        :return:
        """
        BasePage(self.driver).click(OrderManagementData.sure_sumbit_selectors)  # 弹出窗口-确定提交

    def check_initateorder(self):
        """检查列表页第一行是否有审核按钮"""
        texts = BasePage(self.driver).get_text(OrderManagementData.purchaser_check_selectors)
        if texts == '审核':
            return True
        else:
            return False

    def add_initateorder(self, goodsnum, addressgoodsnum, title):
        """
        提交预购单
        :param goodsnum: 商品数量
        :param addressgoodsnum: 收货地址对应数量
        :param title: 订单购标题
        :return:
        """
        self.modify_goodsnum(goodsnum)
        self.check_is_group_buying()
        try:
            self.addplan()
        except Exception:
            log.logger.exception('无可用采购计划', exc_info=True)
            raise
        else:
            self.add_require_title(title)
            self.select_address()
            self.add_address_quantity(addressgoodsnum)
            self.submit()
            self.sure_submit()

    def add_initateorde_yijia(self, goodsnum, price, addressgoodsnum, title):
        """
        提交预购单
        :param goodsnum: 商品数量
        :param price: 意向单价
        :param addressgoodsnum: 收货地址对应数量
        :param title: 订单购标题
        :return:
        """
        self.modify_goodsnum(goodsnum)
        self.modify_controlprice(price)
        self.check_is_group_buying()
        try:
            self.addplan()
        except Exception:
            log.logger.exception('无可用采购计划', exc_info=True)
            raise
        else:
            self.add_require_title(title)
            self.select_address()
            self.add_address_quantity(addressgoodsnum)
            self.submit()
            self.sure_submit()

    def purchaser_click(self):
        """列表页点击审核，进入页面"""
        BasePage(self.driver).click(OrderManagementData.purchaser_check_selectors)

    def begin_check_click(self):
        """订购审核页，点击最下方的开始审核"""
        BasePage(self.driver).click(OrderManagementData.begin_check_selectors)

    def insert_check_opinion(self, value):
        """
        审核输入框，输入内容
        :param value: 输入框中输入内容
        :return:
        """
        BasePage(self.driver).insert_value(OrderManagementData.check_opinion_selectors, value)

    def cgdw_check(self, value):
        """
        采购单位审核通过
        :param value: 审核意见
        :return:
        """
        try:
            self.purchaser_click()
        except Exception:
            log.logger.exception('未生成待审核状态订购单', exc_info=True)
            raise
        else:
            self.begin_check_click()
            self.insert_check_opinion(value)
            self.submit()
            self.sure_submit()

    def check_review(self):
        """
        检查列表页第一行状态，是否为待供应商确认
        :return:
        """
        texts = BasePage(self.driver).get_text(OrderManagementData.status_selectors)
        if texts == '供应商待确认':
            return True
        else:
            return False

    def remove_initateorder(self):
        """
        点击撤回订购单
        :return:
        """
        BasePage(self.driver).click(OrderManagementData.remove_selectors)

    def comfire_remove(self, value):
        """
        确认撤回
        :param value: 输入框中输入内容
        :return:
        """
        # 撤回窗口-输入框输入撤回理由
        BasePage(self.driver).insert_value(OrderManagementData.remove_reason_selectors, value)
        # 点击确定按钮
        BasePage(self.driver).click(OrderManagementData.confirm_remove_selectors)

    def cgdw_remove(self, value):
        """
        采购单位撤回订购单
        :param value: 撤回理由
        :return:
        """
        try:
            self.remove_initateorder()
        except Exception:
            log.logger.exception('未生成待供应商确认状态订购单', exc_info=True)
            raise
        else:
            self.comfire_remove(value)

    def check_remove(self):
        """
        检查列表页第一行状态，是否为已撤回
        :return:
        """
        texts = BasePage(self.driver).get_text(OrderManagementData.status_selectors)
        if texts == '已撤回':
            return True
        else:
            return False

    def check_confirm_gys(self):
        """
        检查列表页第一行状态，是否为待确认
        :return:
        """
        texts = BasePage(self.driver).get_text(OrderManagementData.confirm_gsy_selectors)
        if texts == '确认':
            return True
        else:
            return False

    def click_check_confirm_gys(self):
        log.logger.info('点击供应商-订购单管理-确认按钮')
        BasePage(self.driver).click(OrderManagementData.confirm_gsy_selectors)  # 点击供应商-订购单管理-确认按钮

    def accept_gsy(self):
        BasePage(self.driver).scrolls(OrderManagementData.accept_gsy_selectors)
        BasePage(self.driver).click(OrderManagementData.accept_gsy_selectors)  # 点击供应商-订购单管理-接受按钮
        BasePage(self.driver).click(OrderManagementData.accept_ok_gsy_selectors)  # 点击供应商-订购单管理-接受-弹窗-同意按钮
        BasePage(self.driver).click(OrderManagementData.accept_ok_submit_gsy_selectors)  # 点击供应商-订购单管理-接受-同意-确定

    def gys_confirm_initate_order(self):
        """
        供应商确认直购单
        :return:
        """
        try:
            self.click_check_confirm_gys()
        except Exception:
            log.logger.exception('该数据不是待确认状态的订购单或不能确认', exc_info=True)
            raise
        else:
            self.accept_gsy()
            log.logger.info('确认订购单')

    def check_ghzx_status_gys(self):
        """
        检查列表页第一行状态，是否为专家结果审核
        :return:
        """
        texts = BasePage(self.driver).get_text(OrderManagementData.status_gsy_selectors)
        if texts == '专家结果审核':
            return True
        else:
            return False

    def check_examine_ghzx(self):
        """
        检查列表页第一行状态，是否为专家结果审核
        :return:
        """
        texts = BasePage(self.driver).get_text(OrderManagementData.examine_ghzx_selectors)
        if texts == '审核':
            return True
        else:
            return False

    def click_examine_ghzx(self):
        log.logger.info('国合中心点击订购单审核按钮')
        BasePage(self.driver).click(OrderManagementData.examine_ghzx_selectors)  # 点击供应商-订购单管理-确认按钮

    def click_submit_ghzx(self):
        log.logger.info('国合中心审核同意，并点击提交按钮')
        BasePage(self.driver).click(OrderManagementData.submit_audits_selectors)  # 点击供应商-订购单管理-确认按钮

    def click_begin_check_ghzx(self):
        """订购审核页，点击最下方的开始审核"""
        BasePage(self.driver).click(OrderManagementData.begin_audit_check_selectors)

    def ghzx_examine_initate_order(self, suggest):
        try:
            self.click_examine_ghzx()  # 点击列表页-审核按钮
        except Exception:
            log.logger.exception('未找到审核按钮或点击审核按钮失败', exc_info=True)
            raise
        else:
            self.click_begin_check_ghzx()  # 采购结果审核-点击最下方-开始审核按钮
            self.insert_check_opinion(suggest)  # 国和中心输入审核意见
            self.click_submit_ghzx()  # 点击提交按钮

    def check_examined_status_ghzx(self):
        """
        检查列表页第一行状态，是否为订购完成
        :return:
        """
        texts = BasePage(self.driver).get_text(OrderManagementData.examined_status_ghzx_selectors)
        if texts == '订购完成':
            return True
        else:
            return False

    def check_status_cgdw(self):
        """
        检查列表页第一行状态，是否为订购完成
        :return:
        """
        texts = BasePage(self.driver).get_text(OrderManagementData.order_finally_status_cgdw_selectors)
        if texts == '订购完成':
            return True
        else:
            return False

    def check_status_gys(self):
        """
        检查列表页第一行状态，是否为已成交
        :return:
        """
        texts = BasePage(self.driver).get_text(OrderManagementData.status_gsy_selectors)
        if texts == '已成交':
            return True
        else:
            return False
