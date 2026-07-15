# unittest框架

# 测试框架基础

作用：

1.  提高测试效率，降低维护成本

2.  提高测试的准确性，增加代码的重用性

3.  核心思想是让不懂代码的人也能够通过这个框架去实现自动化测试

企业级自动化测试特点：

1.  一定是基于框架来实现

    目的是便于维护和升级，提升效率和可移植性

2.  结构科学：

    1.  工程结构明确清晰

    2.  代码规范：代码与数据分离；逻辑代码与测试代码分离

3.  遵循设计模式来实现

    1.  关键字驱动：常用基于行为，也可以基于流程，主要用于接口自动化

    2.  POM（页面对象模型），只能用于UI自动化，被称为业内最佳设计模式

单元测试框架对比

Python（80%）：unittest，pytest

java（20%）：junit，testng

|      | unittest                                                                                                         | pytest                                                                                                                                              |
| ---- | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 规则   | 1.测试文件必须导包：import unittest&#xA;2.测试类必须继承unittest.Testcase&#xA;3.测试方法必须以test\_开头                                  | 1.测试文件必须以test\_开头或\_test结尾&#xA;2.测试类名必须以Test开头&#xA;3.测试方法必须以test\_开头                                                                                |
| 固件   | setUp/tearDown 在测试用例之前/之后执行&#xA;setUpClass/tearDownClass 在测试类之前/之后执行&#xA;setUpModule/tearDownModule 在测试模块之前/之后执行 | setup/teardown 在测试用例之前/之后执行&#xA;setup\_class/teardown\_class 在测试类之前/之后执行&#xA;setup\_module/teardown\_module 在测试模块之前/之后执行&#xA;其它夹具：@pytest.fixtrue() |
| 断言   | self.assertEqual()&#xA;self.assertIn()等                                                                          | python自带的assert                                                                                                                                     |
| 报告   | HtmlTestrunner.py                                                                                                | pytest-html，allure插件                                                                                                                                |
| 失败重跑 | 没有                                                                                                               | pytest-rerunfaillures插件                                                                                                                             |
| 参数化  | @parameterized.expand()                                                                                          | @pytest.mark.parametrize()                                                                                                                          |

所有的测试框架都是做以下四件事：

1.  发现测试用例：按照设定的规则找到测试用例

2.  执行测试用例

3.  判断测试结果：通过或不通过

4.  生成测试报告

## 自动化测试用例

参考手工测试用例，并增加断言（必须要有）和后置条件（方便后续测试）

用例之间一般不能关联，这样可以使每个用例都单独执行，因此原则上一个用例打开一次浏览器

# unittest使用

*   &#x20;UnitTest是一个测试用例框架

*   Python安装时默认会有一个buildtin模块，UnitTest框架是默认集成在Python中的。意味着只要安装了Python就有UnitTest&#x20;

*   只需要通过 `import UnitTest` 就可以使用

unittest运行方式：

1.  命令行

    1.  python -m unittest 模块名.py

    2.  python -m unittest 模块名.类名.方法名

        可加-v参数，使执行信息更详细，-k通过通配符匹配方法名

2.  main

    ```python
    if __name__ == '__main__':
        unittest.main()
    ```

## 用例执行结果

| 符号 | 含义                        |
| -- | ------------------------- |
| .  | 用例执行成功，且断言通过              |
| F  | 用例执行成功，但断言不通过             |
| E  | 错误，一般是代码编写的有问题，导致元素未找到等问题 |
| S  | 跳过，没有执行此用例                |

## 用例执行顺序

此处的用例指的是通过unittest.defaultTestLoader.discover发现的.py文件

按ASCII码排序顺序执行：【0-9 A-Z a-z】A=65 a=97

## main参数详解

按住Ctrl点击unittest.main()中的main会发现其中的参数有：

```python
def __init__(self, module='__main__', defaultTest=None, argv=None,
                    testRunner=None, testLoader=loader.defaultTestLoader,
                    exit=True, verbosity=1, failfast=None, catchbreak=None,
                    buffer=None, warnings=None, *, tb_locals=False):
```

| 参数          | 含义                              |
| ----------- | ------------------------------- |
| module      | 测试用例所在路径，默认为\_\_main\_\_，表示当前模块 |
| defaultTest | 测试用例名称，默认是所有                    |
| argv        | 接收外部的参数                         |
| testRunner  | 测试运行期，TextTestRunner            |
| testLoader  | 指定使用的测试用例加载器                    |
| exit        | 是否在测试完成后结束Python程序              |
| verbosity   | 测试信息的详细程度，取0,1,2，数值越大越详细        |

## 断言

| 常用断言                | 作用           |
| ------------------- | ------------ |
| assertEqual(a,b)    | 断言a==b       |
| assertNotEqual(a,b) | 断言a !=b      |
| assertIn(a,b)       | 断言a在b中       |
| assertNotIn(a,b)    | 断言a不在b中      |
| assertTrue(条件表达式)   | 条件表达式为真时断言通过 |
| assertFalse(条件表达式)  | 条件表达式为假时断言通过 |

一个用例如果有多个步骤（如场景法设计的用例），一般会有多个断言

## 跳过执行

某个用例不想执行时，可用装饰器跳过执行，语法为：

```python
# 无条件跳过
@unittest.skip('说明文字')
def test_001(self):
  pass

# 条件为真时跳过
@unittest.skipIf(条件表达式,'说明文字')
def test_002(self):
  pass

```

# 参数化

参数化又叫数据驱动，将代码和数据分离，解耦合

## DDT

(data driver test )数据驱动测试，通过装饰器形式调用，可以完美应用于unittest框架实现数据驱动。

使用方法：

1.  安装ddt包

    ```python
    pip install ddt
    ```

ddt中的装饰器：

| 装饰器         | 作用                     |
| ----------- | ---------------------- |
| @ddt        | 类装饰器，声明当前类使用ddt        |
| @data       | 函数装饰器，用于给测试用例传递数据      |
| @unpack     | 函数装饰器，将传输的数据解包         |
| @file\_data | 函数装饰器，可直接读取yaml/json文件 |

@unpack使用的注意事项：

1.  数字、字符串和无序数据序列（如集合）不能解包

2.  字典解包时，键的名称和个数必须和用例中的参数保持一致

# 二次封装

为什么要二次封装（好处）：极大降低代码维护的工作量；利于团队协作

1.  POM层

    *   Base基础模块

        *   封装方法，包括内置方法和selenium中的方法

    *   PageObject页面对象模块（继承Base）

        *   页面的url、页面的核心元素、页面的业务流程操作（如登录、注册）

    *   TestCase测试用例模块（集成unittest.TestCase）

        *   测试用例

2.  方法层

    *   自定义模块（关键字驱动）

    *   调用第三方库

    *   数据驱动DDT

    *   全局ini配置文件

    *   yaml配置文件

    *   日志操作方法

3.  数据层

    *   csv、Excel、yaml、MySQL数据库

4.  输出层

    *   HTML测试报告

    *   日志文件

    *   截图附件

测试数据、测试代码（TestCase）、逻辑代码（Base、PageObject）分离

## 关键字驱动

提取最为常用的操作行为进行二次封装，实质就是面向对象思维里的对象与封装

## POM

POM是针对于系统进行的量身定制的测试模式，无法实现单个POM框架应对多个项目

# 代码的维护

影响UI自动化测试运行稳定性的因素：

1.  界面上无法预测的弹框和第三方弹出页面，如消息通知、浏览器版本的更新等，会导致元素无法定位

    解决方案

    *   关闭系统更新、浏览器更新

    *   尽量不要安装非必要的第三方软件，目前第三方软件常用推送广告

    *   保证测试机器干净，减少非必要的异常出现

2.  需求变化导致的前端界面变化；页面可能会根据用户的等级和状态呈现不同的效果

3.  数据的变化，这一次访问的数据和上一次并不相同

4.  网络或服务器性能导致的页面延迟造成的控件加载失败

    *   增加智能等待

    *   增加失败重跑（pytest的reruns参数）

5.  测试数据变更
