#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/7/4
 * @version: 1.0
 * @fileName: test_add_member.py
 * @author: 'WangLei'
"""
from faker import Faker

from class_3_1_task.page.page_factory import PageFactory


class TestAddMember:

    def setup_class(self):
        self.fake = Faker(locale='zh_CN')

    def setup(self):
        # 随机生成姓名
        self.username = self.fake.name()
        # 随机生成电话
        self.phone = self.fake.phone_number()

    def test_main_add_member(self):
        assert self.username in PageFactory().entry_page('main_page').goto_add_member().add_member(
            self.username, self.phone, self.phone
        ).get_contact_list()

    def test_contact_add_member(self):
        assert self.username in PageFactory().entry_page('main_page').goto_contact().goto_add_member().add_member(
            self.username, self.phone, self.phone
        ).get_contact_list()
