# coding:utf-8

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""
driver common function
"""
BY_DEFAULT=By.XPATH

# 获取元素位置，默认以xpath定位，可以自己制定
def _get_locator(driver, by=BY_DEFAULT, value=None):
    return driver.find_element(by, value)

def wait_element_exit(driver, by=BY_DEFAULT, value=None):
    WebDriverWait(driver, 5).until(lambda driver: _get_locator(driver, by, value))

def click_element(driver, by=BY_DEFAULT, value=None):
    wait_element_exit(driver, _get_locator(driver, by, value))
    _get_locator(driver, by, value).click()
    time.sleep(1)
