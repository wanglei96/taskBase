#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/7/4
 * @version: 1.0
 * @fileName: main_page.py
 * @author: 'WangLei'
"""
from selenium.webdriver.common.by import By

from class_3_1_task.page.add_member_page import AddMemberPage
from class_3_1_task.page.base_page import BasePage
from class_3_1_task.page.contact_page import ContactPage


class MainPage(BasePage):
    _page_url = 'https://work.weixin.qq.com/wework_admin/frame#index'
    _ele_goto_contact = (By.ID, 'menu_contacts')
    _goto_add_member = (By.CLASS_NAME, 'index_service_cnt_item_title')

    def goto_contact(self):
        """
        跳转到通讯录
        :return: 通讯录页面类
        """
        self.find_ele(self._ele_goto_contact).click()
        return ContactPage(self.driver)

    def goto_add_member(self):
        """
        添加成员
        :return: 添加成员页面类
        """
        self.find_ele(self._goto_add_member).click()
        return AddMemberPage(self.driver)
