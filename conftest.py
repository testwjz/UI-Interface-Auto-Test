# usr/bin/env python
# coding:utf-8
import time
import pytest
from selenium import webdriver

from readConfig import ReadConfig


@pytest.fixture(scope='module')
def browser(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(ReadConfig().get_http('timeout'))
    driver.maximize_window()

    def _close():
        driver.close()

    request.addfinalizer(_close)
    return driver

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    summary = []
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    driver = item.funcargs['browser']
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if driver is not None:
            if (report.skipped and xfail) or (report.failed and not xfail):
                time.sleep(1)
                _gather_screenshot(driver, summary, extra, pytest_html)
        if summary:
            report.sections.append(('pytest-selenium-error-message', '\n'.join(summary)))
        report.extra = extra

def _gather_screenshot(driver, summary, extra, pytest_html):
    try:
        screenshot = driver.get_screenshot_as_base64()
    except Exception as e:
        summary.append('WARNING: Failed to gather screenshot: {0}'.format(e))
        return
    if pytest_html is not None:
        extra.append(pytest_html.extras.image(screenshot, 'Screenshot'))

@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
