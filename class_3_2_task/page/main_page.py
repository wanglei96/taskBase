#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/7/21
 * @version: 1.0
 * @fileName: main_page.py
 * @author: 'WangLei'
"""
import allure
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from class_3_2_task.page.base_page import BasePage
from class_3_2_task.page.contact_page import ContactPage
from class_3_2_task.page.manage_contact import ManageContactPage


class MainPage(BasePage):
    _contact = (MobileBy.XPATH, '//*[contains(@text, "通讯录")]')

    def goto_addresslist(self):
        with allure.step('点击进入通讯录页面'):
            self.find_and_click(*self._contact)
        return ContactPage(self.driver)

