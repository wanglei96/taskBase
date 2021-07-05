#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/7/4
 * @version: 1.0
 * @fileName: contact_page.py
 * @author: 'WangLei'
"""
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from class_3_1_task.page.add_member_page import AddMemberPage
from class_3_1_task.page.base_page import BasePage


class ContactPage(BasePage):
    _page_url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
    _ele_goto_add_member = (By.CSS_SELECTOR, ".ww_operationBar a:nth-child(2)")
    _row_list = (By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
    _member_fixedTip = (By.CSS_SELECTOR, '.member_fixedTip')

    def goto_add_member(self):
        """
        跳转添加成员页面
        :return: AddMember类
        """
        # 加这个强制等待，解决点击会不跳转问题，find_ele封装了显示等待没有解决该问题
        sleep(2)
        self.find_ele(self._ele_goto_add_member).click()
        return AddMemberPage(self.driver)

    def get_contact_list(self):
        """
        获取成员列表
        :return: 成员名字列表
        """
        # 不加这个强制等待，从通讯录添加成员用例，获取的成员名称列表是''，find_eles封装了显示等待没有解决该问题
        sleep(2)
        row_list = self.find_eles(self._row_list)
        name_list = [i.text for i in row_list]
        # print(name_list)
        return name_list
