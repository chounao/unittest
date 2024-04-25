# coding=utf-8
import time
import unittest
import package.HTMLTestRunner
import os
import getcwds
from framework.log import Logger
import logging


log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


# 用HTMLTestRunner 实现的测试报告
def testreport():
    """

    :return:
    """
    currtime = time.strftime('%Y-%m-%d %H_%M_%S')
    abpath = getcwds.get_cwds()
    reportpath = os.path.join(abpath, 'reports\\testReport')
    filename = reportpath + r'\report' + currtime + '.html'
    # print('reportpath路径啊啊啊啊啊' + reportpath)
    try:
        fp = open(filename, 'wb')
    except Exception :
        log.logger.exception('[%s] open error cause Failed to generate test report' % filename)
    else:
        runner = package.HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description='自动化测试演示报告')
        # runner = package.HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description='自动化测试演示报告', retry=1)
        log.logger.info('successed to generate test report [%s]' % filename)
        return runner, fp, filename


def all_case():
    abpath = getcwds.get_cwds()
    # case_path = os.path.join(abpath, 'testsuites')
    # case_path = os.path.join(abpath, 'testsuites/test_01_login/')
    # case_path = os.path.join(abpath, 'testsuites/test_02_order/')
    case_path = os.path.join(abpath, 'testsuites/test_03/')
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    # print('case_path路径啊啊啊啊啊'+case_path)
    return discover

