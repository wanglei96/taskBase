#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/7/21
 * @version: 1.0
 * @fileName: contact_page.py
 * @author: 'WangLei'
"""
import allure
from appium.webdriver.common.mobileby import MobileBy

from class_3_2_task.page.addmember_page import AddMemberPage
from class_3_2_task.page.base_page import BasePage
from class_3_2_task.page.manage_contact import ManageContactPage


class ContactPage(BasePage):
    _add_member = (MobileBy.XPATH, '//*[contains(@text, "添加成员")]')
    _manager = (MobileBy.XPATH,
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.RelativeLayout[2]/android.widget.TextView")

    def goto_addmember(self):
        with allure.step('点击进入添加成员页面'):
            self.find_and_click(*self._add_member)
        return AddMemberPage(self.driver)

    def goto_managercontact_page(self):
        with allure.step('点击进入通讯录管理页面'):
            self.find_and_click(*self._manager)
        return ManageContactPage(self.driver)