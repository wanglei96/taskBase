#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/8/22
 * @version: 1.0
 * @fileName: test_demo.py
 * @author: 'WangLei'
"""
import allure

from class_5_2_task.interface.api_demo import ApiDemo
from class_5_2_task.utils.setting import LOGGER


@allure.feature('ApiDemo测试集')
class TestApiDemo:

    def setup_class(self):
        self.api = ApiDemo()
        LOGGER.info('***测试开始***')

    def teardown_class(self):
        LOGGER.info('***测试结束***')

    @allure.story('get接口测试')
    def test_get(self):
        self.api.get_demo()

    @allure.story('post接口测试')
    def test_post(self):
        self.api.post_demo()




