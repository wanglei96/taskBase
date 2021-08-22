#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/8/22
 * @version: 1.0
 * @fileName: run_test.py
 * @author: 'WangLei'
"""
import subprocess

import pytest


def run_test():
    """
    运行测试
    :return:
    """
    # 启动测试
    pytest.main(
        ['-s', '-q', '--alluredir', 'result/data', '--clean-alluredir'])
    # 生成allure报告
    subprocess.run(['allure', 'generate', 'result/data', '-o', 'result/report', '--clean'], shell=True)


run_test()



