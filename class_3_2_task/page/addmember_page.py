#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/7/21
 * @version: 1.0
 * @fileName: addmember_page.py
 * @author: 'WangLei'
"""
import allure
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from class_3_1_task.page.base_page import BasePage
from class_3_2_task.page.membermessage_page import MemberMessagePage


class AddMemberPage(BasePage):

    def click_addmember_menual(self):
        with allure.step('点击添加成员按钮'):
            self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "手动输入添加")]').click()
        return MemberMessagePage(self.driver)

    def get_tip(self):
        with allure.step('获取toast弹窗信息'):
            info = self.driver.find_element(MobileBy.XPATH,
                                            "//*[@class='android.widget.Toast']")
            result = info.get_attribute('text')
        return result