#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/8/22
 * @version: 1.0
 * @fileName: api_demo.py
 * @author: 'WangLei'
"""
import jmespath

from class_5_2_task.interface.base import Base
from class_5_2_task.utils.tools import Tools


class ApiDemo(Base):

    def __init__(self):
        # 拼接url
        # get接口url
        self.get_url = self.host + jmespath.search('ApiDemo.get_demo.url', self.config_data)
        # post接口url
        self.post_url = self.host + jmespath.search('ApiDemo.post_demo.url', self.config_data)

    def get_demo(self):
        """
        /get接口封装
        :return:
        """
        # 发送请求
        resp = self.get(url=self.get_url)
        # 断言结果
        Tools.assertion('ApiDemo.get_demo', resp.status_code, resp.json())
        return resp.json()

    def post_demo(self):
        """
        /post接口封装
        :return:
        """
        # 发送请求
        resp = self.post(url=self.post_url)
        # 断言结果
        Tools.assertion('ApiDemo.post_demo', resp.status_code, resp.json())
        return resp.json()


if __name__ == "__main__":
    demo = ApiDemo()
    demo.get_demo()
    demo.post_demo()