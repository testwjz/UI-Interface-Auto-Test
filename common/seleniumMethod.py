# coding:utf-8

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""
对selenium 进行封装
"""
BY_DEFAULT = By.XPATH

class SeleniumMethod(object):
    def __init__(self, driver=None):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def _get_locator(self, value, by=BY_DEFAULT):
        return self.driver.find_element(by, value)

    def wait_element_exit(self, value, by=BY_DEFAULT):
        WebDriverWait(self.driver, 5).until(lambda driver: self._get_locator(value, by))

    def click_element(self, value, by=BY_DEFAULT):
        self.driver.wait_element_exit(value, self._get_locator(value, by))
        self._get_locator(by, value).click()
        time.sleep(1)



"""
更多页面元素操作方法待补充
"""