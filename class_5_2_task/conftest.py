"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/15 9:38 下午'
"""

import logging
import os
from datetime import datetime

import pytest


def pytest_configure(config):
    """更改生成报告和日志的路径"""
    # 获取日志文件名
    log_file = config.getoption('log_file') or config.getini('log_file') or '{}.log'
    now = datetime.now()
    # 修改文件名
    config.option.log_file = os.path.join(config.rootdir, 'logs',
                                          log_file.format(now.strftime('%Y%m%d')))
