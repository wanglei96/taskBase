#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/8/22
 * @version: 1.0
 * @fileName: base.py
 * @author: 'WangLei'
"""
import requests

from class_5_2_task.utils.tools import Tools
from class_5_2_task.utils.setting import DATA_DIR, LOGGER
from class_5_2_task.utils.config_data import load_yaml


class Base:
    # 日志
    logger = LOGGER
    # 配置数据读取
    config_data = load_yaml(DATA_DIR)
    # 获取host
    host = config_data['host']

    def get(self, url, params=None, **kwargs):
        """
        封装get请求
        :param url:
        :param params:
        :param kwargs:
        :return:
        """
        self.logger.info(f'请求方式：get \n请求地址：{url} \n请求参数：{params}')
        # 发送get请求
        resp = requests.get(url, params=params, **kwargs)
        # 收集数据到allure报告中
        Tools.save_data(url, params, resp.content)
        self.logger.info(f"响应码：{resp.status_code} \n响应内容：{resp.content}")
        return resp

    def post(self, url, data=None, json=None, **kwargs):
        """
        封装post请求
        :param url:
        :param data:
        :param json:
        :param kwargs:
        :return:
        """
        # 日志只打印有数据的参数
        datas = json
        if data:
            datas = data
        self.logger.info(f'请求方式：post \n请求地址：{url} \n请求参数：{datas}')
        # 发送post请求
        resp = requests.post(url, data=data, json=json, **kwargs)
        # 收集数据到allure报告中
        Tools.save_data(url, datas, resp.content)
        self.logger.info(f"响应码：{resp.status_code} \n响应内容：{resp.content}")
        return resp


if __name__ == "__main__":
    pass