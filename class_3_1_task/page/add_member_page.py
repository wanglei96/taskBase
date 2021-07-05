#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/7/4
 * @version: 1.0
 * @fileName: add_member_page.py
 * @author: 'WangLei'
"""
from selenium.webdriver.common.by import By

from class_3_1_task.page.base_page import BasePage


class AddMemberPage(BasePage):
    _page_url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
    _ele_username = (By.ID, 'username')
    _acctid = (By.ID, 'memberAdd_acctid')
    _phone = (By.ID, 'memberAdd_phone')
    _save = (By.CSS_SELECTOR, '.js_btn_save')

    def add_member(self, name, acctid, phone):
        """
        添加成员
        :param name: 姓名
        :param acctid: 唯一标识
        :param phone: 手机号码
        :return:
        """
        from class_3_1_task.page.contact_page import ContactPage
        # 输入姓名
        self.find_ele(self._ele_username).send_keys(name)
        # 输入唯一标识
        self.find_ele(self._acctid).send_keys(acctid)
        # 输入手机
        self.find_ele(self._phone).send_keys(phone)
        self.find_ele(self._save).click()
        return ContactPage(self.driver)


