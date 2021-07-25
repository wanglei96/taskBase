#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/7/21
 * @version: 1.0
 * @fileName: base_page.py
 * @author: 'WangLei'
"""
import logging

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver

logger = logging.getLogger()


class BasePage:

    def __init__(self, driver: WebDriver=None):
        self.driver = driver

    def find(self, by, value):
        logger.info(f"定位元素{by}-{value}")
        return self.driver.find_element(by, value)

    def finds(self, by, value):
        logger.info(f"定位多个元素{by}-{value}")
        return self.driver.find_elements(by, value)

    def find_and_click(self, by, value):
        self.find(by, value).click()
        logger.info(f"点击元素{value}")

    def find_and_send(self, by, value, text):
        self.find(by, value).send_keys(text)
        logger.info(f"输入内容{text}")

    def loop_find_and_click(self, by, value):
        size = self.driver.get_window_size()
        while True:
            try:
                self.find_and_click(by, value)
                logger.info("找到了！")
                break
            except:
                logger.info(f"没有找到元素{by}-{value}")
                logger.info("屏幕下滑")
                TouchAction(self.driver).press(x=size['width']/3, y=size['height']*4/5).wait(100).move_to(
                    x=size['width']/3, y=size['height']/5).wait(100).release().perform()

    def back(self, num=3):
        for i in range(0, num):
            self.driver.back()