import pytest

#成功的用例删除报告里面的信息
@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]