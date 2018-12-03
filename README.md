# UI TEST PYTEST+SELENIUM

* common 公共方法
> CustomDriver类，自定义封装selenium方法

* config
> 存放一些配置文件

* pageLocator
> 使用page_objects包对界面元素进行封装


* report
> 执行结束后自动生成报告，使用pytest-html <br>
> 自动对失败的用例进行界面截图

* testCase    
> 测试用例存放地方

* 其他文件
> conftest.py 自定义全局fixture <br>
> pytest.ini pytest执行前初始化文件 <br>
> readConfig.py 为读取自定义配置文件而封装的类
