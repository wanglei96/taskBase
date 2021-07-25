#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/7/25
 * @version: 1.0
 * @fileName: editmember_page.py
 * @author: 'WangLei'
"""
import allure
from appium.webdriver.common.mobileby import MobileBy

from class_3_2_task.page.base_page import BasePage


class EditMemberPage(BasePage):
    _del_member = (MobileBy.XPATH, '//*[contains(@text, "删除成员")]')
    _confirm = (MobileBy.XPATH, '//*[contains(@text, "确定")]')

    def del_member(self):
        with allure.step('删除人员'):
            self.loop_find_and_click(*self._del_member)
            self.find_and_click(*self._confirm)
        from class_3_2_task.page.manage_contact import ManageContactPage
        return ManageContactPage(self.driver)






