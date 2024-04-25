# coding=utf-8
import time
from framework.base_page import BasePage
from framework.log import Logger
from data.cgdw_index_data import CgdwIndexData
import logging


log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
health_selectors = ['css', '.zcy-icon.icon-app_icon_ylqx']  # 工作台医疗采购按钮
returnhealth_selectors = ['css', '.icon-zcy.icon-fhylg']  # 返回医疗馆按钮
zhigougoods_selector = ['class', 'J_search-input']  # 前台首页搜索输入框
searchbtn_selector = ['class', 'search-btn']  # 前台首页搜索按钮
zhigoulink_selector = ['link', '云舒002医疗--普朗X射线机PLD5000A']  # 搜索出的直购商品


cartgoods_selector = ['class', 'shoppingcart-goods-span']  # 购物车中商品的classname

batchdeletebtn_selector = ['name', 'batchDeleteBtn'] # 购物车页面-全部删除按钮
surebtn_selector = ['class', 'delete-submit']  # 购物车页面-全部删除-确定按钮
directBuy_selector = ['id', 'directBuy']  # 购物车页面-选择商品-点击生成订单按钮
selectgys_selector = ['class', 'select2-selection__arrow']  # 购物车页面-选择商品-点击生成订单按钮-选择供应商下拉框
# 购物车页面-选择商品-点击生成订单按钮-选择供应商下拉框-选择柏柏自动化供应商
selectbaibaigys_selector = ['xpath', '//ul[@role="tree"]/li[contains(text(),"云舒001集团有限公司")]']
foots_selector = ['class', 'modal-footer']  # 购物车页面-选择商品-点击生成订单按钮-选择供应商下拉框-选择柏柏自动化供应商-页面随机点击下，让下拉框消失
allsupplier_selector = ['name', 'all-supplier-checkbox']  # 购物车页面-选择商品-点击生成订单按钮-选择供应商下拉框-全选按钮


class CgdwIndex(BasePage):
    """采购单位前台页面"""
    # 点击工作台医疗采购模块
    def clickhealth(self):

        try:
            # 滚动找到医疗采购元素
            BasePage(self.driver).scrolls(health_selectors)
            # 点击医疗采购按钮
            time.sleep(5)
            BasePage(self.driver).click(health_selectors)
            time.sleep(5)
        except Exception:
            log.logger.exception('医疗采购按钮未找到', exc_info=True)
            raise
        else:
            log.logger.info('找到医疗采购按钮')
            self.driver.implicitly_wait(2)

    # 点击返回医疗采购菜单
    def clickreturnhealth(self):

        try:
            # 滚动找到医疗采购元素
            BasePage(self.driver).click(returnhealth_selectors)
        except Exception as e:
            log.logger.exception('返回医疗馆按钮未找到', exc_info=True)
            raise e
        else:
            log.logger.info('找到返回医疗馆按钮')

    def searchzhigougoods(self, value):
        try:
            # 找到输入框，输入商品名称’
            BasePage(self.driver).insert_value(zhigougoods_selector, value)
            # 点击医疗采购按钮
            BasePage(self.driver).click(searchbtn_selector)
        except Exception:
            log.logger.exception('搜索元素未找到', exc_info=True)
            raise
        else:
            log.logger.info('搜索元素已找到')

    def searchisexist(self):
        try:
            BasePage(self.driver).scrolls(zhigoulink_selector)
            # BasePage(self.driver).is_element_visible(zhigoulink_selector)
            # BasePage(self.driver).click(zhigoulink_selector)
            time.sleep(5)
            return True
        except AttributeError:
            log.logger.exception('未找到元素 %s' % zhigoulink_selector, exc_info=True)
            return False

    def addtocart(self):
        # 点击商品名称
        BasePage(self.driver).scrolls(zhigoulink_selector)
        BasePage(self.driver).click(zhigoulink_selector)
        # 切换到新开页面
        BasePage(self.driver).current_handel()
        try:
            # 查找加入购物车按钮，并点击
            self.click_addtocart()
        except Exception:
            log.logger.exception('未找到加入购物车按钮', exc_info=True)
            raise
        else:
            # 加入购物车成功后，点击查看购物车按钮，查看购物车列表
            BasePage(self.driver).click(CgdwIndexData.checkcart_button_selector)
            time.sleep(7)
            log.logger.info('搜索元素已找到')

    def clearcart(self):
        # 点击商品名称
        try:
            # 查看购物车列表中，商品的数量
            # counts = len(BasePage(self.driver).find_elements(10, 0.5, cartgoods_selector))
            # log.logger.info('counts = %s' % counts)
            # ele = BasePage(self.driver).find_element(allbtn_selector)
            # 点击第一个全选按钮
            BasePage(self.driver).click(CgdwIndexData.allbtn_selector)
            # log.logger.info(type(ele))
        except Exception:
            log.logger.exception('未查找到该元素', exc_info=True)
            return True
        else:
            try:
                # 点击全部删除按钮
                BasePage(self.driver).click(batchdeletebtn_selector)
                # 点击确定删除按钮
                BasePage(self.driver).click(surebtn_selector)
                log.logger.info('删除商品成功')
                return True
            except Exception:
                log.logger.info('删除商品失败')
                return False

    def addorder(self):
        # 点击商品名称
        try:
            # 点击第一个全选按钮
            BasePage(self.driver).click(CgdwIndexData.allbtn_selector)
            # 点击生成订单按钮
            BasePage(self.driver).click(directBuy_selector)
            # BasePage(self.driver).current_handel()
            # 点击选择供应商下拉框
            BasePage(self.driver).click(selectgys_selector)
            # 选择柏柏自动化供应商
            BasePage(self.driver).click(selectbaibaigys_selector)
            # 点击其他处，收起下拉框
            BasePage(self.driver).click(foots_selector)
            time.sleep(2)
            # 点击全选
            BasePage(self.driver).click(allsupplier_selector)
            time.sleep(2)
            # 点击确定，跳转到订单详情页
            BasePage(self.driver).click(CgdwIndexData.dealersubmit_selector)
            time.sleep(7)
        except Exception:
            log.logger.exception('未查找到该商品', exc_info=True)
            raise
        else:
            currenturl = BasePage(self.driver).getcurrenturl()
            orderid = str(currenturl).split('=')[-1]
            return orderid

    def click_detail_bidding_btn(self, detail_url):
        """
        商品详情页，点击生成竞价单按钮
        :param detail_url: 商品详情页地址
        :return:
        """
        BasePage(self.driver).open(detail_url)
        try:
            BasePage(self.driver).click(CgdwIndexData.bidding_btn_selectors)  # 点击生成竞价单按钮
        except Exception:
            log.logger.exception('商品详情页未找到生成竞价单按钮或点击未跳转', exc_info=True)
            raise

    def click_detail_initate_btn(self, detail_url):
        """
        商品详情页，点击生成订单按钮
        :param detail_url: 商品详情页地址
        :return:
        """
        BasePage(self.driver).open(detail_url)
        try:
            BasePage(self.driver).scrolls(CgdwIndexData.initate_btn_selectors)
            BasePage(self.driver).click(CgdwIndexData.initate_btn_selectors)  # 点击生成订单按钮
        except Exception:
            log.logger.exception('商品详情页未找到生成订单按钮或点击未跳转', exc_info=True)
            raise

    def select_gys(self):
        """
        选择供货商
        :return:
        """
        # 点击选择供应商下拉框
        BasePage(self.driver).click(CgdwIndexData.select_btn_selectors)
        # 选择柏柏自动化供应商
        BasePage(self.driver).click(CgdwIndexData.select_gys_selectors)
        # 点击确定，跳转到订单详情页
        BasePage(self.driver).click(CgdwIndexData.dealersubmit_selector)

    def detail_create_initate(self, detail_url):
        """
        商品详情页，点击生成订单按钮，生成订购单
        :param detail_url: 商品详情页地址
        :return:
        """
        self.click_detail_initate_btn(detail_url)  # 点击生成订单按钮
        self.select_gys()  # 选择供货商：云舒001集团有限公司

    def click_addtocart(self):
            # 查找加入购物车按钮，并点击
            BasePage(self.driver).scrolls(CgdwIndexData.addcart_selector)
            BasePage(self.driver).click(CgdwIndexData.addcart_selector)

    def bidding_addorder(self, detail_url):
        BasePage(self.driver).open(detail_url)
        try:
            self.click_addtocart()  # 点击加入购物车按钮
        except Exception:
            log.logger.exception('商品详情页未加入购物车按钮或点击未跳转', exc_info=True)
            raise
        else:
            # 加入购物车成功后，点击查看购物车按钮，查看购物车列表
            BasePage(self.driver).click(CgdwIndexData.checkcart_button_selector)
            # 点击第一个全选按钮
            BasePage(self.driver).click(CgdwIndexData.allbtn_selector)
            # 点击生成订单按钮
            BasePage(self.driver).click(CgdwIndexData.shoppingcart_selector)
