# coding=utf-8
import configparser
import os


class TestReadConfigFile(object):
    def __init__(self, filepath=None):
        if filepath:
            configpath = filepath
        else:
            configpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\config\config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(configpath)

    def get_config_value(self, section, option):
        """
        根据传入的section获取对应的value
        :param section: ini配置文件中用[]标识的内容
        :return:
        """
        # 获取项目绝对路径（\Users\admin\PycharmProjects\UITest）
        # root_dir = os.path.dirname(os.path.abspath('.'))
        # 获取文件的当前路径（\Users\admin\PycharmProjects\UITest\framework）
        # root_dir = os.path.split(os.path.realpath(__file__))[0]

        # 获取配置文件路径

        # browser = config.get('browserType', 'browserName')
        value = self.config.get(section, option)
        return value


if __name__ == '__main__':
    testReadConfigFile = TestReadConfigFile()
    result = testReadConfigFile.get_config_value('browserType', 'browserName')
    print(result)
