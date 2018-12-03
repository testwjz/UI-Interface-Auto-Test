# usr/bin/env python
# coding:utf-8
import pytest

@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]