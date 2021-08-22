#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/8/22
 * @version: 1.0
 * @fileName: tools.py
 * @author: 'WangLei'
"""
import json

import allure
import jmespath

from class_5_2_task.utils.config_data import load_yaml
from class_5_2_task.utils.setting import DATA_DIR, LOGGER


class Tools(object):
    """
    allure 相关方法封装
    """

    @staticmethod
    def save_data(url, request_data, response_data, precondition_name=None):
        """
        测试步骤写入测试报告
        :param url: 请求地址
        :param request_data: 请求数据
        :param response_data: 响应数据
        :param precondition_name: 前置条件名称
        :return:
        """
        # precondition_name不为None，写入前置条件
        if precondition_name is not None:
            with allure.step(f"前置条件：{precondition_name}"):
                pass
        # 保存url
        with allure.step(f"请求地址：{url}"):
            pass
        # 保存数据
        with allure.step(f'请求参数：{json.dumps(request_data)}'):
            pass
        # 保存返回数据
        with allure.step(f"返回结果：{response_data}"):
            pass

    @staticmethod
    def assertion(api_path: jmespath, status_code: int, response: dict):
        """
        自动断言封装
        :param status_code: 状态码
        :param response: 接口响应内容
        :param api_path: 接口路径, 类名.方法名 的jmespath
        :return:
        """
        # 读取测试数据
        data = load_yaml(DATA_DIR)
        # 查找指定接口数据
        api_data = jmespath.search(api_path, data)
        # 响应类型为json时，自动进行下述断言，其他类型待定
        response_type = api_data['response_type']
        if response_type == 'json':
            # 响应码
            assert_code = api_data['assert']['code']
            # 响应体校验数据
            assert_data = api_data['assert']['body']
            # 断言响应码
            assert assert_code == status_code, f'预期值：{assert_code}，实际值：{status_code}'
            LOGGER.info(f'code预期值：{assert_code}，实际值：{status_code}')
            # 断言响应体
            for k, v in assert_data.items():
                # 实际值
                act = jmespath.search(k, response)
                assert jmespath.search(k, response) == v, f'预期值：{v}，实际值：{act}'
                LOGGER.info(f'{k}预期值：{v}，实际值：{act}')
        # 其他类型，待定
        else:
            pass





