import os
import time
import pytest

import common.CustomDriver as seleniumMethod
from pageLocator.joinUs import HomePage
from config.readConfig import ReadConfig, dirpath

customdriver = seleniumMethod.CustomDriver()


@pytest.fixture(scope='function')
def homePage(selenium):
    homePage = HomePage(selenium, root_uri=ReadConfig().get_http('url'))
    homePage.get('/')
    time.sleep(1)
    return homePage


def test_login(homePage):
    customdriver.wait_element_exit(homePage, homePage.JOIN_HOME)
    assert customdriver.get_title(homePage.w) == homePage.HomePageAssert
