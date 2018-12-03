# coding:utf-8

import time
from selenium.webdriver.support.wait import WebDriverWait

"""
对selenium 进行封装
定位直接调用element_locator，使用page-object
"""

class CustomDriver(object):
    def __init__(self):
        pass

    def get_title(self, driver):
        return driver.title

    def wait_element_exit(self, driver, element_locator):
        WebDriverWait(driver, 5).until(lambda driver: element_locator)

    def click_element(self, driver, element_locator):
        driver.wait_element_exit(driver, element_locator)
        element_locator.click()
        time.sleep(1)


"""
更多页面元素操作方法待补充
"""
