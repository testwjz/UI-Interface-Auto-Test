import time

from selenium import webdriver

from common import seleniumMethod
from pageLocator import joinUs
from readConfig import ReadConfig

if __name__ == '__main__':
    selenium=webdriver.Chrome()
    selenium.get(ReadConfig().get_http('url'))
    time.sleep(1)
    seleniumMethod.wait_element_exit(selenium,value=joinUs.HomePage)
    assert selenium.title == joinUs.HomePageAssert