import pytest
from interface.getCaseData import get_case_data, myRequest


@pytest.mark.parametrize("data,assertData,url,header,method", get_case_data())
def test_getCases(data,assertData,url,header,method):
    request=myRequest()
    request.set_method(method)
    request.set_url(url)
    request.set_headers(eval(header))
    request.set_data(data.encode('utf-8'))
    response=request.my_request()
    assert assertData in str(response.json())