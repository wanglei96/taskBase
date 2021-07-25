#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/7/25
 * @version: 1.0
 * @fileName: manage_contact.py
 * @author: 'WangLei'
"""
from time import sleep

import allure
from appium.webdriver.common.mobileby import MobileBy

from class_3_2_task.page.base_page import BasePage
from class_3_2_task.page.editmember_page import EditMemberPage


class ManageContactPage(BasePage):
    _member_ls = (MobileBy.XPATH, '//*[@class="android.widget.ListView"]//*[@class="android.widget.TextView"]')

    def goto_editmemberpage(self, member_name):
        with allure.step('点击人员进入成员信息编辑页面'):
            self.find_and_click(MobileBy.XPATH, f'//*[contains(@text, "{member_name}")]')
        return EditMemberPage(self.driver)

    def get_contact_membersname(self):
        with allure.step('获取通讯录人员名称列表'):
            sleep(2)
            count_ls = self.finds(*self._member_ls)
        return [el.get_attribute('text') for el in count_ls]