# coding=utf-8
import os
import time
import getcwds
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from framework.log import Logger
import logging


log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
orderidlist = []


class BasePage(object): # 如果没有明确要继承的类，默认继承object，当然这里留空也行
    """基类封装其他页面都会用到的方法"""
    def __init__(self, driver):
        self.driver = driver

    def open(self, url='https://login-staging.zcygov.cn/login'):
        """打开登录页"""
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(3)
            log.logger.info('%s 正常打开url' % url)
        except Exception as e:
            log.logger.exception(e, exc_info=True)
            raise ValueError('%s 打开地址错误，请检查！' % url)
        return self.driver

    def openurl(self, url):
        """定义打开url方法"""
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(3)
            log.logger.info('%s 地址正常打开' % url)
        except Exception as e:
            log.logger.exception(e, exc_info=True)
            raise ValueError('%s 打开地址错误，请检查！' % url)
        return self.driver

    def get_img(self, filename):
        """获取截图"""
        abpath = getcwds.get_cwds()
        failimagepath = os.path.join(abpath, 'reports\screenshots\\fail')
        passimagepath = os.path.join(abpath, 'reports\screenshots\pass')
        # print('failimageiath...'+failimagepath)
        list_value = []
        lists = filename.split('.')
        for value in lists:
            list_value.append(value)
        if list_value[1] == 'png' or list_value[1] == 'jpg' or list_value[1] == 'PNG' or list_value[1] == 'JPG':
            if 'fail' in list_value[0].split('_'):
                try:
                    self.driver.save_screenshot(os.path.join(failimagepath, filename))
                except Exception:
                    log.logger.exception('保存截图失败 !', exc_info=True)
                else:
                    log.logger.info(
                        '截图 [%s] 成功保存在 [%s]' % (filename, failimagepath))
            elif 'pass' in list_value[0]:
                try:
                    self.driver.save_screenshot(os.path.join(passimagepath, filename))
                except Exception:
                    log.logger.exception('保存截图失败 !', exc_info=True)
                else:
                    log.logger.info(
                        '截图 [%s] 成功保存在 [%s]' % (filename, passimagepath))
            else:
                log.logger.info('保存截图失败由于 [%s] 格式不正确' % filename)
        else:
            log.logger.info(
                '文件名 [%s] 格式不正确导致保存失败, 请检查!' % filename)

    # 清空浏览器缓存
    def clear_cookie(self):
        cookies = self.driver.get_cookies()
        self.driver.delete_all_cookies()

    # 查找元素
    def find_element(self, selector):
        """定位页面元素位置的方法"""
        by = selector[0]
        value = selector[1]
        element = None
        try:
            if by == 'id' or by == 'name' or by == 'class' or by == 'tag' or by == 'link' or by == 'plink' or by == 'css' or by == 'xpath':
                if by == 'id':
                    element = WebDriverWait(self.driver, 10, 0.5).until(
                        EC.visibility_of(self.driver.find_element_by_id(value)))
                elif by == 'name':
                    element = WebDriverWait(self.driver, 10, 0.5).until(
                        EC.visibility_of(self.driver.find_element_by_name(value)))
                elif by == 'class':
                    element = WebDriverWait(self.driver, 10, 0.5).until(
                        EC.visibility_of(self.driver.find_element_by_class_name(value)))
                elif by == 'tag':
                    element = WebDriverWait(self.driver, 10, 0.5).until(
                        EC.visibility_of(self.driver.find_element_by_tag_name(value)))
                elif by == 'link':
                    element = WebDriverWait(self.driver, 10, 0.5).until(
                        EC.visibility_of(self.driver.find_element_by_link_text(value)))
                elif by == 'plink':
                    element = WebDriverWait(self.driver, 10, 0.5).until(
                        EC.visibility_of(self.driver.find_element_by_partial_link_text(value)))
                elif by == 'css':
                    element = WebDriverWait(self.driver, 10, 0.5).until(
                        EC.visibility_of(self.driver.find_element_by_css_selector(value)))
                elif by == 'xpath':
                    element = WebDriverWait(self.driver, 10, 0.5).until(
                        EC.visibility_of(self.driver.find_element_by_xpath(value)))
                else:
                    raise NameError("请输入可查找的元素.")
                # log.logger.info('元素查找成功:%s' % selector[1])
            return element
        except Exception as e:
            log.logger.exception('查找元素超时:%s' % selector[1], exc_info=True)
            raise e

    # 查找一组元素
    def find_elements(self, timeout, poll_frequency, selector):
        """

        :param timeout: 超时的总时长
        :param poll_frequency:循环去查询的间隙时间
        :param selector:查找的元素内容
        :return:
        """
        by = selector[0]
        value = selector[1]
        elelist = []
        try:
            if by == 'id' or by == 'name' or by == 'class' or by == 'tag' or by == 'link' or by == 'plink' or by == 'css' or by == 'xpath':
                if by == 'id':
                    elelist = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.visibility_of_any_elements_located((By.ID, value)))
                elif by == 'name':
                    elelist = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.visibility_of_any_elements_located((By.NAME, value)))
                elif by == 'class':
                    elelist = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.visibility_of_any_elements_located((By.CLASS_NAME, value)))
                elif by == 'tag':
                    elelist = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.visibility_of_any_elements_located((By.TAG_NAME, value)))
                elif by == 'link':
                    elelist = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.visibility_of_any_elements_located((By.LINK_TEXT, value)))
                elif by == 'plink':
                    elelist = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.visibility_of_any_elements_located((By.PARTIAL_LINK_TEXT, value)))
                elif by == 'css':
                    elelist = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.visibility_of_any_elements_located((By.CSS_SELECTOR, value)))
                elif by == 'xpath':
                    elelist = WebDriverWait(self.driver, timeout, poll_frequency).until(
                        EC.visibility_of_any_elements_located((By.XPATH, value)))
                else:
                    raise NameError("请输入可查找的元素.")
                log.logger.info('元素查找成功:%s' % selector[1])
            return elelist
        except Exception as e:
            log.logger.exception('查找元素超时!', exc_info=True)
            raise e

    # 这是封装的公共方法。封装的元素定位方法需要传一个数组，数组下标第一个是定位方式，第二个是具体的值。元素定位写在封装的元素操作里面，不写在后面页面类里是因为方便在页面类里面重复使用元素。
    def find_element_nowait(self, selector):
        """定位页面元素位置的方法"""
        by = selector[0]
        value = selector[1]
        element = None
        try:
            if by == 'id' or by == 'name' or by == 'class' or by == 'tag' or by == 'link' or by == 'plink' or by == 'css' or by == 'xpath':
                if by == 'id':
                    element = self.driver.find_element_by_id(value)
                elif by == 'name':
                    element = self.driver.find_element_by_name(value)
                elif by == 'class':
                    element = self.driver.find_element_by_class_name(value)
                elif by == 'tag':
                    element = self.driver.find_element_by_tag_name(value)
                elif by == 'link':
                    element = self.driver.find_element_by_link_text(value)
                elif by == 'plink':
                    element = self.driver.find_element_by_partial_link_text(value)
                elif by == 'css':
                    element = self.driver.find_element_by_css_selector(value)
                elif by == 'xpath':
                    element = self.driver.find_element_by_xpath(value)
                else:
                    raise NameError("请输入可查找的元素.")
                log.logger.info('元素查找成功:%s' % selector[1])
            return element
        except Exception as e:
            log.logger.exception('查找元素超时!', exc_info=True)
            raise e

    # 显性等待时间
    def webdriverwait(self, maxtime, mintime, selector):
        element = self.find_element_nowait(selector)
        WebDriverWait(self.driver, maxtime, mintime).until(EC.visibility_of(element))
        return element

    # 清除文本框
    def clear(self, selector):
        element = self.find_element(selector)
        element.clear()
        log.logger.info("清除文本框内容成功%s" % selector[1])

    def insert_value(self, selector, value):
        """文本框输入内容"""

        element = self.find_element(selector)  # 调用封装的定位元素方法
        self.clear(selector)
        element.send_keys(value)
        log.logger.info('输入的内容：%s' % value)

    def click(self, selector):
        """封装click()方法"""
        element = self.find_element(selector)
        element.click()
        log.logger.info('点击元素成功%s' % selector[1])

    # 点击列表中的某一个元素
    def click_list(self, selector, n):
        """封装click()方法"""
        element = self.find_elements(10, 0.5, selector)[n]
        element.click()
        log.logger.info('点击元素成功%s' % selector[1])

    def get_text(self, selector):
        """封装text方法"""
        element = self.find_element(selector)
        texts = element.text
        log.logger.info('获取元素内容: %s' % texts)
        return texts

    def get_texts(self, selector, n):
        """封装text方法"""
        element = self.find_elements(10, 0.5, selector)[n]
        texts = element.text
        log.logger.info('获取元素内容: %s' % texts)
        return texts

    # sleep（）--在用
    def sleep(self, secondes):
        """封装sleep()方法"""
        time.sleep(secondes)
        log.logger.info('暂停 %d 秒' % secondes)

    # 获取浏览器标题--在用
    def get_title(self):
        """封装title()方法"""
        title = self.driver.title
        log.logger.info('当前窗口的title是: %s' % title)
        return title

    # 关闭浏览器全部标签页--在用
    def quit(self):
        self.driver.quit()
        log.logger.info('关闭浏览器')

    # 关闭当前标签页--在用
    def close(self):
        try:
            self.driver.close()
            log.logger.info("关闭当前标签页.")
        except ZeroDivisionError as e:
            log.logger.exception('退出浏览器失败', exc_info=True)
            raise e

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        log.logger.info('浏览器前进操作')

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        log.logger.info('浏览器后退操作')

    # 刷新浏览器操作
    def refresh(self):
        self.driver.refresh()
        log.logger.info('刷新页面')

    # 隐式等待-设置超时时间
    def wait(self, seconds="60"):
        self.driver.implicitly_wait(seconds)
        log.logger.info("wait for %d seconds." % seconds)

    def is_element_visible(self, selector):
        try:
            elememt = self.find_element(selector)
            WebDriverWait(self.driver, 10).until(EC.visibility_of(elememt))
            log.logger.info('找到元素 %s' % selector)
            return True
        except AttributeError:
            log.logger.exception('未找到元素 %s' % selector, exc_info=True)
            return False

    # 获取当前url
    def getcurrenturl(self):
        log.logger.info('获取当前url %s' % self.driver.current_url)
        return self.driver.current_url

    '''
    将页面滚动条移动到页面任意位置
    '''
    def scroll(self, top=random.randint(100, 999)):
        topsize = top
        js = "var q=document.documentElement.scrollTop="+str(topsize)
        return self.driver.execute_script(js)

    # 切换到新窗口
    def current_handel(self):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to.window(handle)

    # 操作失败时弹出的alert
    def handle_alert(self):
        try:
            alert = self.driver.switch_to_alert()
            text = alert.text
            alert.accept()
        except Exception as e:
            log.logger.exception('弹出弹窗失败', exc_info=True)
            raise e
        else:
            log.logger.info('弹出弹窗成功，内容为: %s!' % text)
            return text

    # 滚动页面，查找元素
    def scrolls(self, selector):
        t = True
        n = 400
        while t and n <= 10000:
            self.driver.implicitly_wait(10)
            self.driver.execute_script("window.scrollBy(" + str(n-400) + "," + str(n) + ")")
            self.find_element(selector)
            t = False
            # break
            n += 400

    # 滚动页面到最右侧
    def scrolls_right(self):
        return self.driver.execute_script("window.scrollTo(document.body.scrollWidth,0)")

    # 滚动页面到顶部
    def scrolls_up(self,):
        return self.driver.execute_script("window.scrollTo(0,0)")

    # 滚动页面到底部
    def scrolls_down(self,):
        return self.driver.execute_script("0,document.body.scrollHeight")


    # 滚动查找并点击元素
    def scroll_click(self, selector):
        self.scrolls(selector)
        self.click(selector)

    # 横向滚动查找并点击元素
    def scroll_rigth_click(self, selector):
        self.scrolls_right()
        self.click(selector)

    def scrollilst(self, selector):
        t = True
        n = 500
        while t and n <= 10000:
            try:
                self.driver.implicitly_wait(10)
                self.driver.execute_script("window.scrollBy(" + str(n-500) + "," + str(n) + ")")
                self.find_element(selector)
                time.sleep(1)
                t = False
                log.logger.info('查找元素成功')
                # break
            except Exception as e:
                log.logger.exception('查找元素失败', exc_info=True)
                raise e
            finally:
                n += 1000

    # 列表中添加元素
    def addorderlist(self, orderid):
        orderidlist.append(orderid)
        return orderidli拿st

    # 查询列表最后一个元素
    def selectpoplist(self):
        print('orderidlist......' + str(orderidlist))
        return orderidlist[-1]

    # 查找元素，后键盘做点击ENTER操作
    def click_enter(self, selector):
        element = self.find_element(selector)  # 调用封装的定位元素方法
        element.send_keys(Keys.ENTER)

    # 去掉style样式，下面是css定位（）
    def style_none(self):
        js = 'document.querySelector("div.ant-upload.ant-upload-select.ant-upload-select-picture-card > ' \
             'span > input[type=file]").style="";'
        return self.driver.execute_script(js)










