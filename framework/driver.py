'''
Code description：save all driver info
Create time：
Developer：
'''

from selenium import webdriver
import sys
from framework.read_config import TestReadConfigFile
from framework.log import Logger
import logging
import os
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class WDriver(object):

    # Firefox driver
    def fireFoxDriver(self):
        """

        :return:
        """
        try:
            self.driver = webdriver.Firefox()
        except Exception as e:
            log.logger.exception('FireFoxDriverServer.exe executable needs to be in PATH. Please download!', exc_info=True)
            raise e
        else:
            log.logger.info('%s:found the Firefox driver successed !' % self.driver)
            return self.driver

    # chrom driver
    def chromeDriver(self):
        """

        :return:
        """
        try:
            browser_driver_path = os.path.join(os.path.abspath(os.getcwd()), 'drivers/chromedriver.exe')
            # 无界面python
            # chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--headless')
            # self.driver = webdriver.Chrome(browser_driver_path, chrome_options=chrome_options)
            # 有界面模式
            self.driver = webdriver.Chrome(browser_driver_path)
        except Exception as e:
            log.logger.exception('ChromeDriverServer.exe executable needs to be in PATH. Please download!',
                                 exc_info=True)
            raise e
        else:
            log.logger.info('found the chrome driver [%s] successed !' % self.driver)
            return self.driver

    # Ie driver
    def ieDriver(self):
        """

        :return:
        """
        try:
            self.driver = webdriver.Ie()
        except Exception as e:
            log.logger.exception('IEDriverServer.exe executable needs to be in PATH. Please download!',
                                 exc_info=True)
            raise e
        else:
            log.logger.info('found the IE driver [%s] successed !' % self.driver)
            return self.driver


if __name__ == '__main__':
    WDrive=WDriver()
    WDrive.chromeDriver()

