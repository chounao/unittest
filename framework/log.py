# coding=utf-8
import logging
import time
import os

log_path = os.path.join(os.path.abspath(os.getcwd()), 'reports/logs')


class Logger:
    def __init__(self, logger, CmdLevel=logging.INFO, FileLevel=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)  # 设置日志输出的默认级别
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # 获取本地时间，转换为设置的格式
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 文件的命名
        self.logname = os.path.join(log_path, '%s.log' % rq)

        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, encoding='utf-8')
        fh.setLevel(FileLevel)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(FileLevel)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)



# if __name__ == "__main__":
#     log = Logger()
#     log.logger.info("---测试开始----")
#     log.logger.info("输入密码")
#     log.logger.warning("----测试结束----")
