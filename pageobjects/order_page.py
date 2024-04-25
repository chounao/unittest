# coding=utf-8
from framework.base_page import BasePage
from framework.log import Logger
import logging
from data.order_data import OrderData
import time
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class OrderPage(BasePage):
    """采购单位前台页面"""
    # 点击工作台模块
    def clickmall(self):
        # 工作台模块
        BasePage(self.driver).click(OrderData.mall_selectors)
        time.sleep(3)

    def searchgoods(self, goodsname):
        BasePage(self.driver).insert_value(OrderData.search_selectors, goodsname)
        BasePage(self.driver).click(OrderData.vaccine_btn_selectors)

    def searchisexist(self):
        try:
            BasePage(self.driver).scrolls(OrderData.goodslink_selectors)
            time.sleep(3)
            return True
        except AttributeError:
            log.logger.exception('未找到元素 %s' % OrderData.goodslink_selectors, exc_info=True)
            return False

    def clearcart(self):
        # 点击商品名称
        try:
            # 点击第一个全选按钮
            time.sleep(3)
            self.driver.find_element_by_xpath('//input[@class="ant-checkbox-input"]').click()
            # BasePage(self.driver).click(OrderData.allbtn_selectors)
        except Exception:
            log.logger.exception('未找到全选按钮')
            # log.logger.exception('未找到全选按钮', exc_info=True)
            return True
        else:
            try:
                # 点击全部删除按钮
                BasePage(self.driver).click(OrderData.batchdeletebtn_selectors)
                # 点击确定删除按钮
                time.sleep(3)
                # BasePage(self.driver).click(OrderData.surebtn_selectors)
                self.driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-primary ant-btn-sm'
                                                  ' ant-btn-two-chinese-chars"]').click()
                log.logger.info('删除商品成功')
                return True
            except Exception:
                log.logger.info('删除商品失败')
                return False

    def addtocart(self):
        try:
            # 查找加入购物车按钮，并点击
            self.click_addtocart()
            time.sleep(7)
        except Exception:
            log.logger.exception('未找到加入购物车按钮', exc_info=True)
            raise
        else:
            # 加入购物车成功后，点击查看购物车按钮，查看购物车列表
            BasePage(self.driver).click(OrderData.checkcart_selectors)
            time.sleep(5)

    def ordertoinitate(self):
        try:
            # 查找立即下单按钮，并点击
            self.click_order()
        except Exception:
            log.logger.exception('未找到立即下单按钮', exc_info=True)
            raise

    def click_addtocart(self):
        # 查找加入购物车按钮，并点击
        BasePage(self.driver).scrolls(OrderData.addcart_selectors)
        BasePage(self.driver).click(OrderData.addcart_selectors)

    def click_order(self):
        # 查找立即下单按钮，并点击
        BasePage(self.driver).scrolls(OrderData.orderbtn_selectors)
        BasePage(self.driver).click(OrderData.orderbtn_selectors)

    def add_initateorder(self):
        # 提交预购单
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath('//input[@class="ant-checkbox-input"]').click()
        except Exception:
            log.logger.exception('未找到全选按钮', exc_info=True)
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-primary ant-btn-lg" '
                                              'and @type="button"]').click()
        except Exception:
            log.logger.exception('未找到预购单按钮', exc_info=True)

    # 提交预购单
    def submit_initateorder(self):
        self.select_placeholder()
        self.submit()

    def select_placeholder(self):
        # 选择部门审核人
        BasePage(self.driver).scrolls(OrderData.invoice_selectors)
        time.sleep(2)
        BasePage(self.driver).click(OrderData.select_placeholder_selectors)
        # BasePage(self.driver).click(OrderData.select_placeholder_selectors)
        BasePage(self.driver).click(OrderData.placeholder_selectors)
        # 点击提交
        BasePage(self.driver).scroll_click(OrderData.submit_selectors)

    def submit(self):
        # 确定提交
        BasePage(self.driver).click(OrderData.sure_selectors)
        BasePage(self.driver).click(OrderData.close_selectors)

    def check_initateorder(self):
        """检查列表页第一行是否有审核按钮"""
        try:
            texts = BasePage(self.driver).get_text(OrderData.purchaser_check_selectors)
        except Exception:
            log.logger.exception('未找审核按钮', exc_info=True)
            return False
        else:
            if texts == '部门审核':
                return True
            else:
                return False

    """关闭采宝"""
    def close_shrink(self):
        # 关闭采宝
        time.sleep(3)
        BasePage(self.driver).click(OrderData.shrink_selectors)
        time.sleep(3)

    """预购单部门审核"""
    def department_review(self):
        # self.close_shrink()
        # 点击部门审核
        BasePage(self.driver).scroll_rigth_click(OrderData.purchaser_check_selectors)
        # 点击提交审核意见
        BasePage(self.driver).scroll_click(OrderData.check_submit_selectors)
        # 确定提交
        self.submit()

    """预购单财务审核"""
    def finance_review(self):
        # self.close_shrink()
        # 点击财务审核
        BasePage(self.driver).scroll_rigth_click(OrderData.purchaser_check_selectors)
        # 点击提交审核意见
        BasePage(self.driver).scroll_click(OrderData.check_submit_selectors)
        # 确定提交
        self.submit()

    """预购单单位审核"""
    def unit_review(self):
        # self.close_shrink()
        # 点击单位审核
        BasePage(self.driver).scroll_rigth_click(OrderData.purchaser_check_selectors)
        # 点击提交审核意见
        BasePage(self.driver).scroll_click(OrderData.check_submit_selectors)
        # 确定提交
        self.submit()

    """提交订单"""
    def review_order(self):
        # self.close_shrink()
        # 点击确定订单
        BasePage(self.driver).scroll_rigth_click(OrderData.purchaser_check_selectors)
        # 点击确定订单按钮
        BasePage(self.driver).scroll_click(OrderData.submit_order_selectors)
        time.sleep(2)
        # 刷新页面
        BasePage(self.driver).refresh()

    def cancel_order(self):
        """供应商未接单状态，采购点完点击取消订单"""
        # 采购单位点击取消订单
        BasePage(self.driver).scroll_rigth_click(OrderData.order_operation_selectors)
        self.cancel_operate()

    def wait_cancel_order(self):
        """供应商已接单状态，采购点完点击取消订单"""
        # 采购单位点击取消订单
        BasePage(self.driver).scroll_rigth_click(OrderData.order_cancel_selectors)
        self.cancel_operate()

    def gys_cancel_order(self):
        """订单待取消状态，供应商取消订单"""
        # 供应商点击取消订单
        BasePage(self.driver).scroll_rigth_click(OrderData.gys_cancel_selectors)
        # 输入取消原因
        BasePage(self.driver).insert_value(OrderData.gys_cancel_reason_selectors, '供应商同意取消订单')
        # 点击确定取消按钮
        BasePage(self.driver).click(OrderData.gys_cancel_sure_selectors)
        BasePage(self.driver).refresh()

    def cancel_operate(self):
        """取消订单原因以及确实取消操作"""
        # 输入取消原因
        BasePage(self.driver).insert_value(OrderData.cancel_reason_selectors, '测试环境取消订单')
        # 点击确实按钮
        BasePage(self.driver).click(OrderData.cancel_submit_selectors)
        # 刷新页面
        BasePage(self.driver).refresh()

    def buy_again(self):
        """再次购买"""
        BasePage(self.driver).scroll_rigth_click(OrderData.buy_again_selectors)

    def check_buy_again(self):
        """再次购买"""
        try:
            texts = BasePage(self.driver).get_text(OrderData.cart_goodsname_selectors)
        except Exception:
            log.logger.exception('未找到甲型肝炎灭活疫苗0508商品', exc_info=True)
            return False
        else:
            if texts == '甲型肝炎灭活疫苗0508':
                return True
            else:
                return False

    def check_carturl(self):
        try:
            title = BasePage(self.driver).get_title()
        except Exception:
            log.logger.exception('未进入我的购物车页面', exc_info=True)
            return False
        else:
            if title == '我的购物车':
                return True
            else:
                return False

    """全部审核"""
    def all_review(self):
        self.department_review()
        self.finance_review()
        self.unit_review()

    def check_unit_review(self):
        """检查列表页第一行是否有审核按钮"""
        try:
            BasePage(self.driver).scrolls_right()
            texts = BasePage(self.driver).get_text(OrderData.purchaser_check_selectors)
        except Exception:
            log.logger.exception('未找打确定订单元素', exc_info=True)
            return False
        else:
            if texts == '确定订单':
                return True
            else:
                return False

    def check_department_review(self):
        """检查列表页第一行是否有审核按钮"""
        try:
            BasePage(self.driver).scrolls_right()
            texts = BasePage(self.driver).get_text(OrderData.purchaser_check_selectors)
        except Exception:
            log.logger.exception('财务审核', exc_info=True)
            return False
        else:
            if texts == '财务审核':
                return True
            else:
                return False

    def check_finance_review(self):
        """检查列表页第一行是否有审核按钮"""
        try:
            BasePage(self.driver).scrolls_right()
            texts = BasePage(self.driver).get_text(OrderData.purchaser_check_selectors)
        except Exception:
            log.logger.exception('单位审核', exc_info=True)
            return False
        else:
            if texts == '单位审核':
                return True
            else:
                return False

    def check_review_order(self):
        """检查列表页第一行是否有审核按钮"""
        try:
            BasePage(self.driver).scrolls_right()
            texts = BasePage(self.driver).get_text(OrderData.order_status_selectors)
        except Exception:
            log.logger.exception('未找到待供应商接单元素', exc_info=True)
            return False
        else:
            if str(texts).strip() == '待供应商接单':
                return True
            else:
                return False

    def check_cancel_order(self):
        """检查列表状态"""
        try:
            BasePage(self.driver).scrolls_right()
            texts = BasePage(self.driver).get_text(OrderData.order_status_selectors)
        except Exception:
            log.logger.exception('未找到订单取消元素', exc_info=True)
            return False
        else:
            if str(texts).strip() == '订单取消':
                return True
            else:
                return False

    def gys_review_order(self):
        # 点击接单按钮
        BasePage(self.driver).scroll_rigth_click(OrderData.gys_operate_selectors)
        # 弹窗-查找点击确认接单按钮
        BasePage(self.driver).scroll_click(OrderData.gys_requier_selectors)
        BasePage(self.driver).refresh()

    def check_gys_status(self):
        """检查列表状态"""
        try:
            BasePage(self.driver).scrolls_right()
            texts = BasePage(self.driver).get_text(OrderData.gys_status_selectors)
        except Exception:
            log.logger.exception('未找到待发货元素', exc_info=True)
            return False
        else:
            if str(texts).strip() == '待发货':
                return True
            else:
                return False

    def gys_send_goods(self):
        # 点击发货按钮
        BasePage(self.driver).scroll_rigth_click(OrderData.gys_send_goods_selectors)
        # 点击发货仓库-选择仓库
        BasePage(self.driver).scroll_click(OrderData.gys_warehouse_selectors)
        BasePage(self.driver).click(OrderData.gys_default_warehouse_selectors)
        # 添加运单号
        BasePage(self.driver).insert_value(OrderData.gys_shipmentno_selectors, '12222221')
        # 选择商品
        BasePage(self.driver).scroll_click(OrderData.gys_check_goods_selectors)
        # 添加批号
        BasePage(self.driver).click(OrderData.gys_add_batch_selectors)
        BasePage(self.driver).click(OrderData.gys_select_selectors)
        BasePage(self.driver).click(OrderData.gys_select_batch_selectors)
        # 添加发货商品数量
        BasePage(self.driver).insert_value(OrderData.gys_goodscount_selectors, 1)
        # 添加批号-确定
        BasePage(self.driver).click(OrderData.gys_batch_require_selectors)
        time.sleep(5)
        # 确认发货
        BasePage(self.driver).click(OrderData.gys_items_submit_selectors)
        time.sleep(5)

    def cgdw_revice_goods(self):
        """确认收货"""
        # 点击查看详情
        BasePage(self.driver).scroll_rigth_click(OrderData.order_operation_selectors)
        # 点击确认收货
        BasePage(self.driver).scroll_click(OrderData.revice_goods_selectors)
        # 选择温度验收完成
        BasePage(self.driver).click(OrderData.temperature_check_selectors)
        # 点击确认收货
        BasePage(self.driver).click(OrderData.sure_revice_selectors)
        BasePage(self.driver).back()
        BasePage(self.driver).refresh()

    def check_gys_send_status(self):
        """检查列表状态"""
        try:
            BasePage(self.driver).scrolls_right()
            texts = BasePage(self.driver).get_text(OrderData.gys_status_selectors)
        except Exception:
            log.logger.exception('未查找到全部发货元素', exc_info=True)
            return False
        else:
            if str(texts).strip() == '全部发货':
                return True
            else:
                return False

    def check_revice_order(self):
        """采购单位检查列表收货后状态"""
        try:
            BasePage(self.driver).scrolls_right()
            texts = BasePage(self.driver).get_text(OrderData.order_status_selectors)
        except Exception:
            log.logger.exception('未查找到待验收元素', exc_info=True)
            return False
        else:
            if str(texts).strip() == '待验收':
                return True
            else:
                return False

    def check_gys_cancel_order(self):
        """采购单位检查列表收货后状态"""
        try:
            BasePage(self.driver).scrolls_right()
            texts = BasePage(self.driver).get_text(OrderData.gys_status_selectors)
        except Exception:
            log.logger.exception('未查找到订单取消元素', exc_info=True)
            return False
        else:
            if str(texts).strip() == '订单取消':
                return True
            else:
                return False

    def cgdw_acceptance(self):
        """采购单位验收"""
        BasePage(self.driver).scroll_rigth_click(OrderData.order_operation_two_selectors)
        BasePage(self.driver).refresh()

    def check_acceptance(self):
        """采购单位检查列表验收后状态"""
        try:
            BasePage(self.driver).scrolls_right()
            texts = BasePage(self.driver).get_text(OrderData.order_status_selectors)
        except Exception:
            log.logger.exception('未查找到已验收元素', exc_info=True)
            return False
        else:
            if str(texts).strip() == '已验收':
                return True
            else:
                return False

    def check_reviews_order(self):
        try:
            BasePage(self.driver).scrolls_right()
            texts = BasePage(self.driver).get_text(OrderData.order_status_selectors)
        except Exception:
            log.logger.exception('未查找到待发货', exc_info=True)
            return False
        else:
            if str(texts).strip() == '待发货':
                return True
            else:
                return False


    #
    # def addorder(self):
    #     # 点击商品名称
    #     try:
    #         # 点击第一个全选按钮
    #         BasePage(self.driver).click(CgdwIndexData.allbtn_selector)
    #         # 点击生成订单按钮
    #         BasePage(self.driver).click(directBuy_selector)
    #         # BasePage(self.driver).current_handel()
    #         # 点击选择供应商下拉框
    #         BasePage(self.driver).click(selectgys_selector)
    #         # 选择柏柏自动化供应商
    #         BasePage(self.driver).click(selectbaibaigys_selector)
    #         # 点击其他处，收起下拉框
    #         BasePage(self.driver).click(foots_selector)
    #         time.sleep(2)
    #         # 点击全选
    #         BasePage(self.driver).click(allsupplier_selector)
    #         time.sleep(2)
    #         # 点击确定，跳转到订单详情页
    #         BasePage(self.driver).click(CgdwIndexData.dealersubmit_selector)
    #         time.sleep(7)
    #     except Exception:
    #         log.logger.exception('未查找到该商品', exc_info=True)
    #         raise
    #     else:
    #         currenturl = BasePage(self.driver).getcurrenturl()
    #         orderid = str(currenturl).split('=')[-1]
    #         return orderid
    #
    # def click_detail_bidding_btn(self, detail_url):
    #     """
    #     商品详情页，点击生成竞价单按钮
    #     :param detail_url: 商品详情页地址
    #     :return:
    #     """
    #     BasePage(self.driver).open(detail_url)
    #     try:
    #         BasePage(self.driver).click(CgdwIndexData.bidding_btn_selectors)  # 点击生成竞价单按钮
    #     except Exception:
    #         log.logger.exception('商品详情页未找到生成竞价单按钮或点击未跳转', exc_info=True)
    #         raise
    #
    # def click_detail_initate_btn(self, detail_url):
    #     """
    #     商品详情页，点击生成订单按钮
    #     :param detail_url: 商品详情页地址
    #     :return:
    #     """
    #     BasePage(self.driver).open(detail_url)
    #     try:
    #         BasePage(self.driver).scrolls(CgdwIndexData.initate_btn_selectors)
    #         BasePage(self.driver).click(CgdwIndexData.initate_btn_selectors)  # 点击生成订单按钮
    #     except Exception:
    #         log.logger.exception('商品详情页未找到生成订单按钮或点击未跳转', exc_info=True)
    #         raise
    #
    # def select_gys(self):
    #     """
    #     选择供货商
    #     :return:
    #     """
    #     # 点击选择供应商下拉框
    #     BasePage(self.driver).click(CgdwIndexData.select_btn_selectors)
    #     # 选择柏柏自动化供应商
    #     BasePage(self.driver).click(CgdwIndexData.select_gys_selectors)
    #     # 点击确定，跳转到订单详情页
    #     BasePage(self.driver).click(CgdwIndexData.dealersubmit_selector)
    #
    # def detail_create_initate(self, detail_url):
    #     """
    #     商品详情页，点击生成订单按钮，生成订购单
    #     :param detail_url: 商品详情页地址
    #     :return:
    #     """
    #     self.click_detail_initate_btn(detail_url)  # 点击生成订单按钮
    #     self.select_gys()  # 选择供货商：云舒001集团有限公司
    #

    #
    # def bidding_addorder(self, detail_url):
    #     BasePage(self.driver).open(detail_url)
    #     try:
    #         self.click_addtocart()  # 点击加入购物车按钮
    #     except Exception:
    #         log.logger.exception('商品详情页未加入购物车按钮或点击未跳转', exc_info=True)
    #         raise
    #     else:
    #         # 加入购物车成功后，点击查看购物车按钮，查看购物车列表
    #         BasePage(self.driver).click(CgdwIndexData.checkcart_button_selector)
    #         # 点击第一个全选按钮
    #         BasePage(self.driver).click(CgdwIndexData.allbtn_selector)
    #         # 点击生成订单按钮
    #         BasePage(self.driver).click(CgdwIndexData.shoppingcart_selector)
