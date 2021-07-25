#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/7/21
 * @version: 1.0
 * @fileName: test_contact.py
 * @author: 'WangLei'
"""
import allure
from faker import Faker

from class_3_2_task.page.app import App


@allure.feature('企业微信测试')
class TestContact:

    def setup_class(self):
        self.app = App()
        self.faker = Faker('zh-CN')
        self.name = self.faker.name()
        self.phone = self.faker.phone_number()

    def setup(self):
        self.main = self.app.start()

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.stop()

    @allure.story("添加联系人测试")
    def test_addcontact(self):
        assert self.main.goto_main().goto_addresslist().goto_addmember().\
               click_addmember_menual().write_message(self.name, self.phone).get_tip() == "添加成功"

    @allure.story("删除联系人测试")
    def test_delcontact(self):
        contact_ls = self.main.goto_main().goto_addresslist().goto_managercontact_page().\
            goto_editmemberpage(self.name).del_member().get_contact_membersname()
        assert self.name not in contact_ls
