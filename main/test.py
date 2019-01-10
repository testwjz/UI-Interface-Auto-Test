from requests import request

"""

安装certifi、cryptography 、pyOpenSSL,则可以进行https请求，如果认证还是失败，再扩展代码支持自定义认证


"""


class myRequest(object):
    def __init__(self, request=request):
        self.request = request
        self.method = "post"
        self.url = None
        self.params = None
        self.headers = {"content-type": "application/json"}
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


my = myRequest()
my.set_method("post")
my.set_url("https://offical.xinchao.com/api/getCasesForBlm")
my.set_data('{"page":2, "pageSize":2}')
my.set_headers({"Content-Type": "application/json"})
re = my.my_request()
print(re.text)
