#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/7/21
 * @version: 1.0
 * @fileName: app.py
 * @author: 'WangLei'
"""
from appium import webdriver
from faker import Faker

from class_3_2_task.page.base_page import BasePage
from class_3_2_task.page.main_page import MainPage


class App(BasePage):

    def start(self):
        if self.driver is None:
            print("driver is None")
            desire_cap = {
                "platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": 'true',
                "unicodeKeyboard": 'true',
                "resetKeyboard": 'true',
                "ensureWebviewsHavePages": True
            }
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desire_cap)
            self.driver.implicitly_wait(5)
        else:
            print("driver is not None")
            self.driver.launch_app()
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)




