#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/7/21
 * @version: 1.0
 * @fileName: membermessage_page.py
 * @author: 'WangLei'
"""
import allure
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from faker import Faker

from class_3_2_task.page.base_page import BasePage


class MemberMessagePage(BasePage):
    _member_name = (MobileBy.XPATH, '//*[contains(@text, "姓名")]/..//*[contains(@text, "必填")]')
    _member_phone = (MobileBy.XPATH, '//*[contains(@text, "手机")]/..//*[contains(@text, "必填")]')
    _save = (MobileBy.XPATH, '//*[contains(@text, "保存")]')

    def write_message(self, name, phone):
        with allure.step('输入人员信息完成添加'):
            self.find_and_send(*self._member_name, name)
            # time.sleep(2)
            self.find_and_send(*self._member_phone, phone)
            self.find_and_click(*self._save)
        from class_3_2_task.page.addmember_page import AddMemberPage
        return AddMemberPage(self.driver)