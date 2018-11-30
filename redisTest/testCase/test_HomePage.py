# coding:utf-8
import time
import pytest
from common import seleniumMethod
from pageLocator import joinUs
from readConfig import ReadConfig


@pytest.fixture(scope='module')
def open_url(browser):
    browser.get(ReadConfig().get_http('url'))
    time.sleep(1)
    return browser


def test_login(open_url):
    seleniumMethod.wait_element_exit(open_url, value=joinUs.HomePage)
    assert open_url.title == joinUs.HomePageAssert


def test_login1(open_url):
    seleniumMethod.wait_element_exit(open_url, value=joinUs.HomePage)
    assert open_url.title != joinUs.HomePageAssert
