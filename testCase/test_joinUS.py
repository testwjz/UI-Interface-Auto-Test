# coding:utf-8
import time
import pytest

import common.CustomDriver as seleniumMethod
from pageLocator.joinUs import HomePage
from readConfig import ReadConfig

customdriver=seleniumMethod.CustomDriver()

@pytest.fixture(scope='function')
def homePage(selenium):
    homePage = HomePage(selenium, root_uri=ReadConfig().get_http('url'))
    homePage.get('/')
    time.sleep(1)
    return homePage

def test_login(homePage):
    customdriver.wait_element_exit(homePage, homePage.JOIN_HOME)
    assert customdriver.get_title(homePage.w) == homePage.HomePageAssert

def test_login1(homePage):
    customdriver.wait_element_exit(homePage, homePage.JOIN_HOME)
    assert customdriver.get_title(homePage.w) != homePage.HomePageAssert
