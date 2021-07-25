"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/15 9:38 下午'
"""
import logging

import pytest


@pytest.fixture(scope='class')
def logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    return logger
