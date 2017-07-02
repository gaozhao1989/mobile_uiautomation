#mobile_uiautomation
Python based mobile uiautomation
使用python+appium+pytest+allure实现对移动端进行测试

**所需安装第三方包**
1. pyyaml
安装方式: pip install pyyaml
http://pyyaml.org/
2. pytest
安装方式: pip install pytest
http://pytest.org/
3. pytest-allure-adaptor
安装方式: pip install pytest-allure-adaptor
https://github.com/allure-framework/allure-python
4. pytest-timeout
安装方式: pip install pytest-timeout
https://bitbucket.org/pytest-dev/pytest-timeout/
5. pytest-ordering
安装方式: pip install pytest-ordering
https://github.com/ftobia/pytest-ordering
6. allure-command-line
mac安装方式: brew install allure
7. appium-python-client
安装方式: pip install appium-python-client


**执行入口**
执行入口文件为根目录下runner文件，或直接使用test文件


**test设置规则**
1. 测试类文件名命名规则为“test_xxxx”或者“xxxx_test”，否则将无法识别
2. 测试类文件内类名以“Testxxxx”开头，否则将无法识别
3. 测试类文件内测试方法以"test_xxxx"开头，狗则将无法识别