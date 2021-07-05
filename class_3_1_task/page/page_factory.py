#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/7/5
 * @version: 1.0
 * @fileName: page_factory.py
 * @author: 'WangLei'
"""
from class_3_1_task.page.add_member_page import AddMemberPage
from class_3_1_task.page.contact_page import ContactPage
from class_3_1_task.page.main_page import MainPage

"""
页面工厂，根据页面名称获取入口页面
"""


class PageFactory:

    @staticmethod
    def entry_page(page_name):
        """
        根据页面名称返回入口页面类
        :param page_name: 页面名称
        :return:
        """
        try:
            page_dict = {
                'main_page': MainPage,      # 主页
                'contact_page': ContactPage,    # 通讯录页
                'add_member_page': AddMemberPage    # 添加成员页
            }
            return page_dict[page_name]()
        except:
            raise Exception("页面不存在！")

