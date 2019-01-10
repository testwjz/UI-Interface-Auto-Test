import os

from config.readConfig import ReadConfig, dirpath
from requests import request


class myRequest(object):
    # 安装certifi、cryptography 、pyOpenSSL,则可以进行https请求，如果认证还是失败，再扩展代码支持自定义认证
    def __init__(self, request=request):
        self.request = request
        self.method = "post"
        self.url = None
        self.params = None
        self.headers = None
        self.allow_redirects = True
        self.data = None
        self.cookies = None
        self.files = None

    def set_method(self, method):
        self.method = method

    def set_url(self, url):
        self.url = url

    def set_params(self, params):
        self.params = params

    def set_headers(self, headers):
        self.headers = headers

    def set_allow_redirects(self, allow_redirects):
        self.allow_redirects = allow_redirects

    def set_data(self, data):
        self.data = data

    def set_cookies(self, cookies):
        self.cookies = cookies

    def set_files(self, files):
        self.files = files

    def my_request(self):
        return self.request(method=self.method, url=self.url, headers=self.headers, params=self.params, data=self.data,
                            cookies=self.cookies, files=self.files,
                            allow_redirects=self.allow_redirects)


def get_case_data():
    params = []
    for i in __get_listfile():
        params.extend(__get_datalist(i))
    return params


def __get_datalist(fileName):
    readconfig = ReadConfig(os.path.join(dirpath, "interface", fileName))
    datalist = [(readconfig.get('DATA', 'Data' + str(i)), readconfig.get('ASSERT', 'assert' + str(i)),
                readconfig.get('HTTP', 'url'), readconfig.get('HTTP', 'header'), readconfig.get('HTTP', 'method')) for
                i in range(1, (1 + int(readconfig.get('HTTP', 'dataNum'))))]
    return datalist


def __get_listfile():
    path = os.listdir(os.path.join(dirpath, "interface"))
    listfile = [i for i in path if '.ini' in i]
    return listfile
