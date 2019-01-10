import pytest
import requests

from interface.getCaseData import get_case_data


@pytest.mark.parametrize("data,assertData,url,header", get_case_data())
def test_getCases(data,assertData,url,header):
    re = requests.post(url=url, data=data, headers=eval(header))
    assert assertData in str(re.json())
