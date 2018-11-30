# coding:utf-8
import time
import pytest
from common.seleniumMethod import SeleniumMethod
from pageLocator import joinUs
from readConfig import ReadConfig


@pytest.fixture(scope='module')
def driver(browser):
    browser.get(ReadConfig().get_http('url'))
    time.sleep(1)
    driver=SeleniumMethod(browser)
    return driver

def test_login(driver):
    driver.wait_element_exit(joinUs.HomePage)
    assert driver.get_title == joinUs.HomePageAssert

def test_login1(driver):
    driver.wait_element_exit(joinUs.HomePage)
    assert driver.get_title != joinUs.HomePageAssert
