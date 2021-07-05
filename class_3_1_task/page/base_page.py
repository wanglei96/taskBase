#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/7/4
 * @version: 1.0
 * @fileName: base_page.py
 * @author: 'WangLei'
"""
import logging

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class BasePage:
    _page_url = ''

    def __init__(self, driver=None):
        if driver is None:
            options = webdriver.ChromeOptions()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
            self.driver.get(self._page_url)
            self.driver.implicitly_wait(5)
            logger.info(f"打开页面{self._page_url}")
        else:
            self.driver: WebDriver = driver

    def find_ele(self, position: tuple):
        """
        封装find_element方法，增加显示等待判断
        :param position: （定位方式，值）
        :return:
        """
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(position))
            return self.driver.find_element(*position)
        except:
            logger.info(f"{position}定位失败！")
            raise Exception(f"{position}定位失败！")

    def find_eles(self, position: tuple):
        """
        封装find_elements方法，增加显示等待判断
        :param position:
        :return:
        """
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(position))
            return self.driver.find_elements(*position)
        except:
            logger.info(f"{position}定位失败！")
            raise Exception(f"{position}定位失败！")