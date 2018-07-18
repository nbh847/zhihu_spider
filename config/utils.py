# 配置信息
import logging
from config.setting import *
from logging import basicConfig, getLogger


class Utils:
    def __init__(self):
        self.logger = self.get_logger()

    @classmethod
    def get_logger(cls):
        level_dic = {'error': logging.ERROR, 'info': logging.INFO, 'warning': logging.WARNING,
                     'debug': logging.DEBUG, 'warn': logging.WARN}
        basicConfig(level=level_dic[MY_DEBUG_LEVEL])
        logger = getLogger(__name__)
        return logger
