#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/6/27
 * @version: 1.0
 * @fileName: conftest.py
 * @author: 'WangLei'
"""
import logging
from typing import List

import pytest
import yaml

from class_2_2_task.python_code.Calculator import Calculator


@pytest.fixture(scope='class')
def get_clac(logger):
    clac = Calculator()
    logger.info('计算开始')
    yield clac
    logger.info('计算结束')


def pytest_collection_modifyitems(items: List):
    for item in items:
        # item.name 用例的名字
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # item.nodeid 用例的路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


@pytest.fixture(scope='class')
def logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    return logger
