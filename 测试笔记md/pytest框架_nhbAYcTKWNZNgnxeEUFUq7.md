# 基础

官方文档网址[https://docs.pytest.org/en/latest/contents.html](https://docs.pytest.org/en/latest/contents.html "https://docs.pytest.org/en/latest/contents.html")

**安装**

```powershell
pip install pytest
```

**默认的测试用例规则**

1.  在当前目录及其子目录中运行所有格式为test\_\*.py或者\*\_test.py的文件

2.  以Test开头，并且没有init方法的类

3.  测试方法必须以test开头

## 运行

两种运行方法：pytest.main()命令行，两者都可以指定运行参数，一般调试时候用，常用运行参数：

| 参数          | 效果                     |
| ----------- | ---------------------- |
| -s          | 输出打印信息，默认不会输出用例中的print |
| -v          | 显示详细信息                 |
| -k          | 运行名称中包含某个字符的测试用例       |
| -q          | 简化输出信息                 |
| -x          | 如果出现一条测试用例失败，退出测试      |
| --maxfail=n | 出现n个失败用例就终止测试          |

示例：

```python
# 输出打印信息，显示详细信息，只运行指定目录或文件中的用例
if __name__ == '__main__':
    pytest.main(['-vs','文件路径'])
    
# 输出打印信息，只运行指定目录或文件中的指定用例，用双冒号隔开
if __name__ == '__main__':
    pytest.main(['-s','文件路径::函数用例名'])
    # 或
    pytest.main(['-s','文件路径::类名::方法用例名'])
```

**cmd常用相关命令**

```powershell
# 查看pytest版本
pytest --version

# 显示可用的内置函数参数
pytest --fixtures

# 查看帮助
pytest --help
```

## 组件

注意：只有在类中，以下函数才会生效

```python
class TestLogin:
    # 在每个用例之前执行一次
    def setup(self):
        print('setup')
        
    # 在每个用例结束时执行一次
    def teardown(self):
        print('teardown')
        
    # 在所有用例之前执行一次，常用于创建日志对象，创建数据库连接
    def setup_class(self):
        print('setup_class')

    # 在所有用例之后执行一次，关闭数据库连接，销毁日志对象
    def teardown_class(self):
        print('teardown_class')
        
    def test01(self):
        print('test01')

    def test02(self):
        print('test02')

```

部分前后置，使用fixture装饰器

```python
@pytest.fixture(scope='作用域',params='数据驱动',autouse='自动执行',ids='数据驱动参数名',name='给fixture作用的函数重命名')
```

scope：function、class、module、package\session

autouse：Ture或False

例子：

1.  在指定函数前后调用一次

    ```python
    @pytest.fixture(scope='function')
    def exe():
        print('在调用的函数之前执行一次')
        yield
        print('在调用的函数之后执行一次')
        
    @pytest.mark.usefixture('exe')
    def test01():
        print('test01')

    ```

2.  在所有函数和类前后执行一次

    ```python
    @pytest.fixture(scope='session',autouse=Ture)
    def exe():
        print('在所有函数之前执行一次')
        yield
        print('在所有函数之后执行一次')
        
    def test02():
        print('test01')
    ```

会话和前后置，一般会结合cinftest.py文件一起使用

1.  conftest.py单独用于存放fixture固件的配置文件

2.  在conftest.py中固件在使用时不需要导包

3.  可以有多个conftest.py文件

# 插件

pytest有众多插件，如pytest-html（生成html格式的测试报告）；pytest-xdist（多线程执行用例）；pytest-ordering（改变用例执行顺序）；pytest-rerunfailures（失败后重跑）；allure-pytest（生成美观的测试报告）

pytest-html用法：使用参数--html=报告路径/报告名.html

## 多进程运行用例

多线程又叫分布式执行，多CPU分发，会减少很多运行时间，提高效率

安装pytest-xdist

```powershell
pip install pytest-xdist
```

将测试发送到多个CPU

```python
if __name__ == '__main__':
    pytest.main(['-n', '2']) # 2表示CPU数量
    # 或
    pytest.main(['-n=2'])
```

## 失败重跑

安装pytest-rerunfailures

```python
if __name__ == '__main__':
    pytest.main(['--returns=2']) # 2表示重跑次数，包括最开始执行的次数，一共会跑3次

```

## 改变用例执行顺序

用例执行顺序：默认从上到下

pytest-ordering

用法：用装饰器@pytest.mark.run(order=数字)来指定顺序，按数字升序执行，没有装饰器的在装饰器之后，按从上到下的顺序执行

```python
def test_01():
    print('test_01')


def test_02():
    print('test_02')


@pytest.mark.run(order=2)
def test_03():
    print('test_03')


@pytest.mark.run(order=1)
def test_04():
    print('test_04')
```

执行顺序为：test\_04，test\_03，test\_01，test\_02

# 配置文件

**真正企业自动化都会有：**pytest.ini配置文件

pytest.ini是pytest测试框架的核心配置文件

1.  位置：一般放在项目的根目录

2.  编码：必须是ANSI（GB2312或GBK）

3.  作用：改变pytest默认行为

4.  运行规则：不管是main运行，命令行运行，都会去读取这个配置文件

```ini
[pytest]
# 命令行参数，用空格分隔
addopts = -vs --reruns 2 --html=./report.html
# 测试用例的路径
testpaths = ./testcase
# 模块名的规则
python_files = test_*.py
# 类名的规则
python_classes = Test*
# 方法名的规则
python_functions = test
# 自定义标记，要与-m参数配合使用
markers = 
  smoke:冒烟测试
  users:用例管理模块
```

# 数据驱动

@pytest.mark.parametrize(args\_name,args\_value)

args\_name：参数名，字符串

args\_value：参数值，（list，tuple，字典

# allure报告

下载allure：[https://github.com/allure-framework/allure2/releases](https://github.com/allure-framework/allure2/releases "https://github.com/allure-framework/allure2/releases")

将allure下的bin加入环境变量path中，在cmd中使用`allure --version`如果出现版本号，则设置成功

生成报告的步骤

1.  生成临时json报告

    \--alluredir ./temps --clean-alluredir

2.  生成html报告

    ```python
    os.system('allure generate ./temps -o ./report --clean')
    ```
