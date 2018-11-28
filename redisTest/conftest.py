#usr/bin/env python
#coding:utf-8
import os
import uuid
import pytest
from selenium import webdriver

path = os.path.split(os.path.realpath(__file__))[0]+'\\test\\'
screenshot_name = path + str(uuid.uuid4()) + ".png"
driver=None

#UI测试失败用例截图
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item,call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if not os.path.exists(path):
            os.mkdir(path)
        #增加额外日志文件到报告中
        #extra.append(pytest_html.extras.url(path, name='Driver log'))
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver.get_screenshot_as_file(screenshot_name)
            extra.append(pytest_html.extras.image(screenshot_name))
        report.extra = extra

@pytest.fixture(scope='session')
def browser(request):
    global driver
    if driver==None:
        driver = webdriver.Chrome()
    def _close():
        driver.close()
    request.addfinalizer(_close)
    return driver