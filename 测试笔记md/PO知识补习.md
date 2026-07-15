# 1.2 安装Python

推荐版本：

```
Python 3.12.x
```

查看版本：

```
python --version
```

或者：

```
python -V
```

查看 pip：

```
pip --version
```

输出：

```
Python 3.12.3

pip 24.x
```

# 1.3 第一个Python程序

创建：

```
print("Hello World")
```

运行结果：

```
Hello World
```

变量：

```
name = "Tom"

age = 18

print(name)
print(age)
```

输出：

```
Tom

18
```

# 1.4 PyCharm安装

推荐：

Community版本（免费）

Professional版本（收费）

推荐插件：

### Chinese

中文支持

### Translation

翻译插件

### Rainbow Brackets

彩色括号

### CodeGlance

代码缩略图

### .ignore

生成 .gitignore

### GitToolBox

Git增强

### String Manipulation

字符串工具

### Key Promoter X

快捷键提示

### SonarLint

代码质量检查

# 1.5 创建项目

例如：

```
Python_Auto_Test

│
├── config
├── common
├── data
├── file
├── img
├── log
├── report
├── testcase
├── page
├── locator
└── run.py
```

这是企业常见结构。

# 1.6 pip包管理

安装：

```
pip install requests
```

指定版本：

```
pip install requests==2.32.0
```

升级：

```
pip install --upgrade requests
```

卸载：

```
pip uninstall requests
```

查看：

```
pip list
```

导出依赖：

```
pip freeze > requirements.txt
```

安装依赖：

```
pip install -r requirements.txt
```

# 1.7 镜像源配置

国内推荐：

清华源：

```
https://pypi.tuna.tsinghua.edu.cn/simple
```

临时使用：

```
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
```

永久配置：

Windows：

创建：

```
C:\Users\用户名\pip\pip.ini
```

内容：

```
[global]
index-url=https://pypi.tuna.tsinghua.edu.cn/simple
```

# 1.8 虚拟环境

为什么需要虚拟环境？

问题：

项目A：

```
requests==2.25
```

项目B：

```
requests==2.32
```

版本冲突。

解决：

每个项目使用独立环境。

创建：

```
python -m venv venv
```

目录：

```
venv

Scripts

Lib

Include
```

激活：

Windows：

```
venv\Scripts\activate
```

Linux：

```
source venv/bin/activate
```

退出：

```
deactivate
```

# 1.9 requirements.txt

生成：

```
pip freeze > requirements.txt
```

内容：

```
requests==2.32.0

selenium==4.25.0

openpyxl==3.1.5

pytest==8.3.4
```

安装：

```
pip install -r requirements.txt
```

企业项目交付必备。

# 1.10 Hello Python项目

创建：

```
print("学习Python自动化测试")
```

输入：

```
name = input("请输入姓名：")

print("你好", name)
```

计算：

```
a = 10

b = 20

print(a + b)
```

输出：

```
30
```

# 1.11 常见错误

### Python未加入环境变量

现象：

```
python 不是内部或外部命令
```

解决：

重新安装并勾选：

```
Add Python to PATH
```

### pip不可用

解决：

```
python -m pip install --upgrade pip
```

### 模块找不到

错误：

```
ModuleNotFoundError
```

解决：

```
pip install 模块名
```

# 1.12 企业开发环境推荐

Python：

```
3.12.x
```

IDE：

```
PyCharm Professional
```

浏览器：

```
Chrome
```

自动化：

```
Selenium

Playwright
```

接口：

```
Requests

Pytest
```

数据库：

```
MySQL

Redis
```

框架：

```
FastAPI
```

容器：

```
Docker
```

AI：

```
LangChain

OpenAI

MCP
```

# 2.1 Python数据类型概述

Python 常用数据类型：

```
数字类型
│
├── int
├── float
└── bool

序列类型
│
├── str
├── list
└── tuple

集合类型
│
└── set

映射类型
│
└── dict
```

其中：

自动化测试中使用最多的是：

```
str
list
dict
```

# 2.2 int（整数）

定义：

```
age = 18

num = -100
```

支持：

```
+
-
*
/
//
%
**
```

示例：

```
print(10 + 3)

print(10 - 3)

print(10 * 3)

print(10 / 3)

print(10 // 3)

print(10 % 3)

print(2 ** 5)
```

输出：

```
13
7
30
3.3333
3
1
32
```

企业应用：

统计：

```
success_count += 1
```

# 2.3 float（浮点数）

定义：

```
price = 99.9

score = 88.5
```

注意：

浮点数存在精度问题。

例如：

```
print(0.1 + 0.2)
```

结果：

```
0.30000000000000004
```

解决：

```
round(0.1 + 0.2, 2)
```

输出：

```
0.3
```

# 2.4 bool（布尔类型）

只有两个值：

```
True

False
```

示例：

```
is_login = True

is_success = False
```

判断：

```
if is_login:

    print("登录成功")
```

企业应用：

接口断言：

```
assert response.status_code == 200
```

结果：

返回 True 或 False。

# 2.5 str（字符串）

最重要的数据类型。

定义：

```
name = "Tom"

msg = 'hello'
```

多行：

```
content = """
第一行
第二行
"""
```

# 2.6 字符串索引

```
s = "abcdef"
```

位置：

```
a b c d e f
0 1 2 3 4 5
```

获取：

```
print(s[0])

print(s[3])
```

输出：

```
a

d
```

负索引：

```
print(s[-1])
```

输出：

```
f
```

# 2.7 字符串切片

语法：

```
字符串[start:end:step]
```

示例：

```
s = "abcdef"

print(s[0:3])

print(s[:3])

print(s[2:])

print(s[::2])

print(s[::-1])
```

输出：

```
abc

abc

cdef

ace

fedcba
```

企业应用：

字符串反转：

```
password[::-1]
```

# 2.8 常用字符串方法

### upper()

大写：

```
s.upper()
```

### lower()

小写：

```
s.lower()
```

### replace()

替换：

```
url = "http://baidu.com"

url.replace("http", "https")
```

### split()

切割：

```
s = "1,2,3"

s.split(",")
```

结果：

```
['1', '2', '3']
```

### join()

拼接：

```
",".join(["a", "b", "c"])
```

结果：

```
a,b,c
```

### strip()

去空格：

```
username = " admin "

username.strip()
```

### startswith()

判断开头：

```
url.startswith("https")
```

### endswith()

判断结尾：

```
file.endswith(".jpg")
```

### find()

查找：

```
s.find("abc")
```

找到：

返回索引。

找不到：

返回：

```
-1
```

## 企业应用

token：

```
token = "Bearer xxxxx"

token.startswith("Bearer")
```

文件：

```
img.endswith(".png")
```

URL：

```
url.replace("http", "https")
```

# 2.9 list（列表）

定义：

```
nums = [1, 2, 3]
```

支持：

```
混合类型
```

例如：

```
data = [1, "Tom", True]
```

# 2.10 添加元素

append：

```
nums.append(4)
```

insert：

```
nums.insert(0, 100)
```

extend：

```
nums.extend([5, 6])
```

# 2.11 删除元素

remove：

```
nums.remove(2)
```

pop：

```
nums.pop()
```

clear：

```
nums.clear()
```

# 2.12 排序

升序：

```
nums.sort()
```

降序：

```
nums.sort(reverse=True)
```

反转：

```
nums.reverse()
```

# 2.13 遍历

```
for num in nums:

    print(num)
```

索引：

```
for i, value in enumerate(nums):

    print(i, value)
```

## 企业应用

Selenium：

```
elements = driver.find_elements()

for ele in elements:

    print(ele.text)
```

# 2.14 tuple（元组）

定义：

```
t = (1, 2, 3)
```

特点：

```
不可修改
```

应用：

配置项：

```
host = ("127.0.0.1", 3306)
```

# 2.15 set（集合）

定义：

```
s = {1, 2, 3}
```

特点：

```
无序

不重复
```

去重：

```
nums = [1,1,2,3,3]

print(set(nums))
```

输出：

```
{1,2,3}
```

# 2.16 dict（字典）

自动化测试中使用最多。

定义：

```
user = {

    "name":"Tom",

    "age":18
}
```

获取：

```
user["name"]

user.get("name")
```

新增：

```
user["sex"] = "男"
```

修改：

```
user["age"] = 20
```

删除：

```
user.pop("age")
```

遍历：

```
for k,v in user.items():

    print(k,v)
```

## 企业应用

接口返回：

```
{
    "code":200,
    "msg":"success",
    "data":{
        "token":"xxxxx"
    }
}
```

提取：

```
token = res["data"]["token"]
```

# 2.17 可变对象与不可变对象

不可变：

```
int

float

bool

str

tuple
```

可变：

```
list

dict

set
```

示例：

```
a = [1,2]

b = a

b.append(3)

print(a)
```

输出：

```
[1,2,3]
```

因为：

```
a 和 b 指向同一个对象
```

# 2.18 浅拷贝

```
import copy

a = [[1,2],3]

b = copy.copy(a)
```

特点：

```
第一层复制

第二层共享
```

# 2.19 深拷贝

```
import copy

a = [[1,2],3]

b = copy.deepcopy(a)
```

特点：

```
完全独立
```

企业应用：

测试数据复制：

```
new_data = copy.deepcopy(data)
```

避免污染原始数据。

# 3.1 什么是流程控制

程序默认执行顺序：

```
第一行
↓
第二行
↓
第三行
↓
结束
```

通过流程控制可以实现：

- 条件判断
- 循环执行
- 跳过执行
- 提前结束

流程控制主要包括：

```
条件控制
│
└── if

循环控制
│
├── for
└── while

循环辅助
│
├── break
├── continue
└── pass
```

# 3.2 if语句

语法：

```
if 条件:
    代码块
```

示例：

```
score = 80

if score >= 60:
    print("及格")
```

输出：

```
及格
```

# 3.3 if else

```
score = 50

if score >= 60:
    print("及格")
else:
    print("不及格")
```

输出：

```
不及格
```

# 3.4 if elif else

```
score = 85

if score >= 90:
    print("优秀")

elif score >= 80:
    print("良好")

elif score >= 60:
    print("及格")

else:
    print("不及格")
```

输出：

```
良好
```

## 企业应用

接口断言：

```
if response.status_code == 200:
    print("成功")
else:
    print("失败")
```

登录判断：

```
if "登录成功" in page_source:
    print("通过")
```

# 3.5 for循环

语法：

```
for 变量 in 可迭代对象:
    代码块
```

示例：

```
for i in [1,2,3]:
    print(i)
```

输出：

```
1
2
3
```

# 3.6 range()

生成数字序列。

## range(5)

```
for i in range(5):
    print(i)
```

输出：

```
0
1
2
3
4
```

## range(start,end)

```
for i in range(1,6):
    print(i)
```

输出：

```
1
2
3
4
5
```

## range(start,end,step)

```
for i in range(0,10,2):
    print(i)
```

输出：

```
0
2
4
6
8
```

## 企业应用

执行10次：

```
for i in range(10):
    send_request()
```

# 3.7 enumerate()

获取索引和值。

普通遍历：

```
names = ["Tom","Jack","Lucy"]

for name in names:
    print(name)
```

使用 enumerate：

```
for index,name in enumerate(names):
    print(index,name)
```

输出：

```
0 Tom
1 Jack
2 Lucy
```

## 企业应用

遍历 Excel 数据：

```
for row,data in enumerate(datas):
    print(row,data)
```

# 3.8 while循环

语法：

```
while 条件:
    代码块
```

示例：

```
i = 1

while i <= 5:

    print(i)

    i += 1
```

输出：

```
1
2
3
4
5
```

## 无限循环

```
while True:

    pass
```

需要配合：

```
break
```

使用。

# 3.9 break

作用：

结束循环。

示例：

```
while True:

    num = input()

    if num == "q":

        break
```

输入：

```
q
```

循环结束。

## 企业应用

轮询订单状态：

```
while True:

    status = query_order()

    if status == "success":

        break
```

流程：

```
查询订单
↓
未支付
↓
继续查询
↓
已支付
↓
break
↓
结束
```

# 3.10 continue

作用：

跳过本次循环。

示例：

```
for i in range(5):

    if i == 3:

        continue

    print(i)
```

输出：

```
0
1
2
4
```

## 企业应用

跳过失败数据：

```
for case in cases:

    if case["run"] == False:

        continue

    execute(case)
```

# 3.11 pass

作用：

占位。

示例：

```
if True:

    pass
```

避免：

```
IndentationError
```

## 企业应用

框架开发：

```
class BasePage:

    def click(self):

        pass
```

后续实现。

# 3.12 嵌套循环

示例：

```
for i in range(3):

    for j in range(2):

        print(i,j)
```

输出：

```
0 0
0 1
1 0
1 1
2 0
2 1
```

## 企业应用

Excel：

```
sheet
↓
行
↓
列
```

代码：

```
for row in rows:

    for cell in row:

        print(cell.value)
```

# 3.13 列表推导式

传统：

```
nums = []

for i in range(5):

    nums.append(i)
```

推导式：

```
nums = [i for i in range(5)]
```

结果：

```
[0,1,2,3,4]
```

平方：

```
nums = [i*i for i in range(5)]
```

结果：

```
[0,1,4,9,16]
```

条件：

```
nums = [i for i in range(10) if i%2==0]
```

结果：

```
[0,2,4,6,8]
```

## 企业应用

提取用户名：

```
users = [

    {"name":"Tom"},

    {"name":"Jack"}

]

names = [

    user["name"]

    for user in users

]
```

结果：

```
['Tom','Jack']
```

# 3.14 字典推导式

示例：

```
dic = {

    i:i*i

    for i in range(5)

}
```

结果：

```
{
0:0,
1:1,
2:4,
3:9,
4:16
}
```

## 企业应用

生成测试数据：

```
params = {

    f"id{i}":i

    for i in range(10)

}
```

# 3.15 三元表达式

普通：

```
if age >=18:

    result = "成年"

else:

    result = "未成年"
```

简写：

```
result = "成年" if age >=18 else "未成年"
```

## 企业应用

断言：

```
msg = "成功" if code==200 else "失败"
```

# 3.16 综合案例

统计偶数：

```
count = 0

for i in range(1,101):

    if i % 2 == 0:

        count += 1

print(count)
```

输出：

```
50
```

## 企业应用案例

批量执行测试：

```
for case in cases:

    if case["is_run"] == False:

        continue

    result = execute(case)

    if result == False:

        break
```

流程：

```
读取用例
↓
是否执行
↓
continue
↓
执行
↓
失败
↓
break
```

# 4.1 什么是函数

函数：

就是将一段重复使用的代码封装起来。

例如：

传统写法：

```
print("登录")
print("输入账号")
print("输入密码")
print("点击登录")
```

如果多次使用：

```
print("登录")
print("输入账号")
print("输入密码")
print("点击登录")

print("登录")
print("输入账号")
print("输入密码")
print("点击登录")
```

代码重复。

封装：

```
def login():

    print("输入账号")

    print("输入密码")

    print("点击登录")
```

调用：

```
login()
```

优点：

```
代码复用

方便维护

降低耦合

提高可读性
```

# 4.2 定义函数

语法：

```
def 函数名():

    函数体
```

示例：

```
def hello():

    print("Hello Python")
```

调用：

```
hello()
```

输出：

```
Hello Python
```

# 4.3 带参数函数

参数：

用于接收外部数据。

定义：

```
def add(a,b):

    print(a+b)
```

调用：

```
add(10,20)
```

输出：

```
30
```

多个参数：

```
def login(username,password):

    print(username,password)
```

调用：

```
login("admin","123456")
```

输出：

```
admin 123456
```

## 企业应用

Selenium：

```
def input_text(locator,text):

    element.send_keys(text)
```

调用：

```
input_text(username_locator,"admin")
```

# 4.4 返回值

return：

返回结果。

示例：

```
def add(a,b):

    return a+b
```

调用：

```
result = add(10,20)

print(result)
```

输出：

```
30
```

多个返回值：

```
def info():

    return "Tom",18
```

接收：

```
name,age = info()
```

## 企业应用

获取 token：

```
def login():

    return token
```

调用：

```
token = login()
```

# 4.5 默认参数

定义：

```
def login(username,password="123456"):

    print(username,password)
```

调用：

```
login("admin")
```

输出：

```
admin 123456
```

覆盖：

```
login("admin","888888")
```

输出：

```
admin 888888
```

## 企业应用

浏览器：

```
def open_browser(browser="chrome"):

    pass
```

调用：

```
open_browser()
```

默认：

```
chrome
```

# 4.6 关键字参数

定义：

```
def info(name,age):

    print(name,age)
```

调用：

```
info(age=18,name="Tom")
```

输出：

```
Tom 18
```

优点：

提高代码可读性。

# 4.7 可变参数 *args

作用：

接收多个位置参数。

定义：

```
def add(*args):

    print(args)
```

调用：

```
add(1,2,3,4)
```

输出：

```
(1,2,3,4)
```

类型：

```
tuple
```

求和：

```
def add(*args):

    total = 0

    for i in args:

        total += i

    return total
```

调用：

```
print(add(1,2,3))
```

输出：

```
6
```

## 企业应用

日志：

```
logger.info(*args)
```

# 4.8 可变关键字参数 **kwargs

作用：

接收多个 key=value。

定义：

```
def info(**kwargs):

    print(kwargs)
```

调用：

```
info(name="Tom",age=18)
```

输出：

```
{
'name':'Tom',
'age':18
}
```

类型：

```
dict
```

## 企业应用

requests 二次封装：

```
def send_request(**kwargs):

    response = requests.request(**kwargs)

    return response
```

调用：

```
send_request(

    method="post",

    url=url,

    json=data

)
```

这是企业项目最经典的写法。

# 4.9 参数顺序

正确：

```
def test(

    a,

    b,

    c=10,

    *args,

    **kwargs

):

    pass
```

顺序：

```
普通参数

↓

默认参数

↓

*args

↓

**kwargs
```

# 4.10 lambda表达式

普通：

```
def add(a,b):

    return a+b
```

lambda：

```
add = lambda a,b:a+b
```

调用：

```
print(add(10,20))
```

输出：

```
30
```

适用于：

简单函数。

# 4.11 map()

作用：

映射。

示例：

```
nums = [1,2,3]

result = map(

    lambda x:x*2,

    nums

)

print(list(result))
```

输出：

```
[2,4,6]
```

## 企业应用

字符串转数字：

```
nums = list(

    map(

        int,

        ["1","2","3"]

    )

)
```

结果：

```
[1,2,3]
```

# 4.12 filter()

过滤。

示例：

```
nums = [1,2,3,4,5]

result = filter(

    lambda x:x%2==0,

    nums

)

print(list(result))
```

输出：

```
[2,4]
```

## 企业应用

过滤执行用例：

```
cases = [

{"run":True},

{"run":False}

]
```

筛选：

```
result = filter(

    lambda x:x["run"],

    cases

)
```

# 4.13 sorted()

排序。

示例：

```
nums = [3,1,2]

print(

    sorted(nums)

)
```

输出：

```
[1,2,3]
```

降序：

```
sorted(

    nums,

    reverse=True

)
```

字典排序：

```
users = [

{"age":20},

{"age":18}

]
```

排序：

```
sorted(

users,

key=lambda x:x["age"]

)
```

结果：

```
[
{'age':18},

{'age':20}

]
```

## 企业应用

订单金额排序：

```
orders = [

{"price":100},

{"price":50}

]
```

按金额排序。

# 4.14 递归函数

函数调用自己。

示例：

阶乘：

```
def factorial(n):

    if n==1:

        return 1

    return n*factorial(n-1)
```

调用：

```
factorial(5)
```

结果：

```
120
```

# 4.15 局部变量

定义：

函数内部变量。

```
def test():

    num = 10
```

作用域：

函数内部。

外部无法访问。

# 4.16 全局变量

定义：

函数外部变量。

```
count = 0
```

函数中使用：

```
global count
```

修改：

```
count += 1
```

## 企业应用

统计成功数量：

```
success_count += 1
```

# 4.17 函数嵌套

示例：

```
def outer():

    def inner():

        print("内部函数")

    inner()
```

# 5.1 为什么要学习面向对象

面向对象（Object Oriented Programming，OOP）是一种程序设计思想。

如果没有 OOP：

```
driver.find_element().click()

driver.find_element().send_keys()

driver.find_element().text
```

代码重复、维护困难。

使用 OOP：

```
login_page.login()

home_page.search()

news_page.collect()
```

更加清晰。

------

# 5.2 类（class）和对象（object）

现实世界：

```
类（模板）
↓
汽车

对象（实例）
↓
宝马
↓
奔驰
↓
奥迪
```

Python：

```
class Student:

    pass
```

创建对象：

```
stu = Student()
```

流程：

```
Student类
↓
实例化
↓
stu对象
```

------

# 5.3 属性

属性：

描述对象的特征。

例如：

学生：

```
姓名

年龄

成绩
```

代码：

```
class Student:

    pass

stu = Student()

stu.name = "Tom"

stu.age = 18
```

访问：

```
print(stu.name)
```

输出：

```
Tom
```

------

# 5.4 方法

方法：

对象拥有的行为。

```
class Student:

    def study(self):

        print("学习")
```

创建对象：

```
stu = Student()
```

调用：

```
stu.study()
```

输出：

```
学习
```

------

# 5.5 self

self：

代表当前对象。

例如：

```
class Student:

    def study(self):

        print(self)
```

调用：

```
stu = Student()

stu.study()
```

本质：

```
Student.study(stu)
```

所以：

```
self 就是对象自己
```

------

# 5.6 **init** 构造方法

作用：

初始化对象。

```
class Student:

    def __init__(self,name,age):

        self.name = name

        self.age = age
```

创建：

```
stu = Student("Tom",18)
```

访问：

```
print(stu.name)
```

输出：

```
Tom
```

------

## 企业应用

登录页面：

```
class LoginPage:

    def __init__(self,driver):

        self.driver = driver
```

调用：

```
login_page = LoginPage(driver)
```

这是 PO 模型最经典的写法。

------

# 5.7 实例变量

定义：

```
self.name
```

示例：

```
class Student:

    def __init__(self,name):

        self.name = name
```

每个对象互不影响。

```
s1 = Student("Tom")

s2 = Student("Jack")
```

结果：

```
s1.name

Tom

s2.name

Jack
```

------

# 5.8 类变量

所有对象共享。

```
class Student:

    school = "清华大学"
```

访问：

```
Student.school
```

对象：

```
stu.school
```

------

## 企业应用

配置：

```
class Config:

    BASE_URL = "https://www.baidu.com"
```

调用：

```
Config.BASE_URL
```

------

# 5.9 封装

目的：

隐藏内部实现。

例如：

```
class LoginPage:

    def login(self):

        self.input_username()

        self.input_password()

        self.click_login()
```

外部：

```
login_page.login()
```

不用关心内部过程。

流程：

```
login()
↓
输入账号
↓
输入密码
↓
点击登录
```

------

# 5.10 继承

父类：

```
class Animal:

    def eat(self):

        print("吃东西")
```

子类：

```
class Dog(Animal):

    pass
```

调用：

```
dog = Dog()

dog.eat()
```

输出：

```
吃东西
```

------

## 企业应用

BasePage：

```
class BasePage:

    def click(self):

        pass

    def input(self):

        pass
```

登录页：

```
class LoginPage(BasePage):

    pass
```

首页：

```
class HomePage(BasePage):

    pass
```

流程：

```
BasePage
↓
LoginPage

HomePage

NewsPage
```

这是企业自动化框架标准结构。

------

# 5.11 方法重写

父类：

```
class Animal:

    def speak(self):

        print("动物叫")
```

子类：

```
class Dog(Animal):

    def speak(self):

        print("汪汪")
```

调用：

```
Dog().speak()
```

输出：

```
汪汪
```

------

# 5.12 super()

调用父类方法。

父类：

```
class Animal:

    def __init__(self,name):

        self.name = name
```

子类：

```
class Dog(Animal):

    def __init__(self,name,age):

        super().__init__(name)

        self.age = age
```

创建：

```
dog = Dog("旺财",2)
```

------

## 企业应用

BasePage：

```
class BasePage:

    def __init__(self,driver):

        self.driver = driver
```

子类：

```
class LoginPage(BasePage):

    def __init__(self,driver):

        super().__init__(driver)
```

------

# 5.13 多态

相同方法，不同表现。

父类：

```
class Animal:

    def speak(self):

        pass
```

子类：

```
class Dog(Animal):

    def speak(self):

        print("汪汪")
class Cat(Animal):

    def speak(self):

        print("喵喵")
```

调用：

```
animals = [

    Dog(),

    Cat()

]

for animal in animals:

    animal.speak()
```

输出：

```
汪汪

喵喵
```

------

# 5.14 静态方法

使用：

```
@staticmethod
```

定义：

```
class Utils:

    @staticmethod

    def add(a,b):

        return a+b
```

调用：

```
Utils.add(1,2)
```

特点：

```
不依赖对象

不依赖类变量
```

------

## 企业应用

日期工具：

```
class DateUtil:

    @staticmethod

    def get_now():
        pass
```

------

# 5.15 类方法

使用：

```
@classmethod
```

定义：

```
class Student:

    count = 0

    @classmethod

    def show_count(cls):

        print(cls.count)
```

调用：

```
Student.show_count()
```

cls：

代表类。

------

# 5.16 魔术方法

## **str**

打印对象。

```
class Student:

    def __str__(self):

        return "学生对象"
```

输出：

```
print(stu)
```

结果：

```
学生对象
```

------

## **len**

长度。

```
class MyList:

    def __len__(self):

        return 10
```

调用：

```
len(obj)
```

结果：

```
10
```

------

## **call**

让对象像函数一样调用。

```
class Test:

    def __call__(self):

        print("hello")
```

调用：

```
obj()
```

输出：

```
hello
```

------

# 5.17 私有属性

定义：

```
__name
```

示例：

```
class Student:

    def __init__(self):

        self.__age = 18
```

外部：

```
stu.__age
```

报错。

访问：

```
stu._Student__age
```

一般不推荐。

------

## 企业应用（PO模型）

BasePage：

```
class BasePage:

    def click(self,locator):

        pass

    def input(self,locator,text):

        pass
```

登录页：

```
class LoginPage(BasePage):

    username = ("id","username")

    password = ("id","password")

    button = ("id","login")

    def login(self,user,pwd):

        self.input(self.username,user)

        self.input(self.password,pwd)

        self.click(self.button)
```

测试：

```
login_page = LoginPage(driver)

login_page.login(

    "admin",

    "123456"

)
```

流程：

```
TestCase
↓
LoginPage
↓
BasePage
↓
Selenium
↓
Chrome
```

# 6.1 为什么要学习文件操作

在自动化测试中，大量数据来自文件：

```
账号密码

测试用例

配置文件

接口参数

环境变量

测试报告

日志文件

Excel数据
```

例如：

```
username = "admin"

password = "123456"
```

硬编码方式：

```
修改困难

维护困难

无法数据驱动
```

企业项目：

```
Excel

JSON

YAML

Config

Database
```

统一管理。

------

# 6.2 文件基本操作

## 打开文件

语法：

```
open(
    file,
    mode,
    encoding
)
```

示例：

```
f = open(
    "test.txt",
    "r",
    encoding="utf-8"
)
```

------

## 文件模式

| 模式 | 说明       |
| ---- | ---------- |
| r    | 读取       |
| w    | 写入       |
| a    | 追加       |
| rb   | 二进制读取 |
| wb   | 二进制写入 |

------

# 6.3 读取文件

## read()

全部读取：

```
f = open(
    "test.txt",
    "r",
    encoding="utf-8"
)

content = f.read()

print(content)
```

------

## readline()

读取一行：

```
line = f.readline()
```

------

## readlines()

读取全部行：

```
lines = f.readlines()
```

结果：

```
[
    "第一行\n",
    "第二行\n"
]
```

------

# 6.4 写入文件

## write()

```
f = open(
    "test.txt",
    "w",
    encoding="utf-8"
)

f.write("Hello Python")
```

结果：

```
覆盖原文件
```

------

## 追加

```
f = open(
    "test.txt",
    "a",
    encoding="utf-8"
)

f.write("\n新增内容")
```

结果：

```
原内容保留
```

------

# 6.5 close()

传统：

```
f = open(
    "test.txt",
    "r",
    encoding="utf-8"
)

print(f.read())

f.close()
```

问题：

```
异常情况下可能无法关闭
```

------

# 6.6 with语句

推荐使用。

```
with open(
    "test.txt",
    "r",
    encoding="utf-8"
) as f:

    print(f.read())
```

流程：

```
打开文件
↓
执行代码
↓
自动关闭
```

企业项目全部采用这种方式。

------

# 6.7 JSON

自动化测试最重要的数据格式之一。

例如接口返回：

```
{
    "code":200,
    "msg":"success",
    "data":{
        "token":"abc123"
    }
}
```

------

# 6.8 json模块

导入：

```
import json
```

------

## dumps()

Python → JSON字符串

```
import json

data = {

    "name":"Tom",

    "age":18
}

result = json.dumps(data)

print(result)
```

结果：

```
'{"name":"Tom","age":18}'
```

------

## loads()

JSON字符串 → Python对象

```
res = '{"name":"Tom"}'

data = json.loads(res)

print(data)
```

结果：

```
{
    "name":"Tom"
}
```

类型：

```
dict
```

------

# 6.9 JSON文件读写

写入：

```
import json

data = {

    "username":"admin",

    "password":"123456"
}

with open(
    "user.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        data,
        f,
        ensure_ascii=False,
        indent=4
    )
```

------

读取：

```
with open(
    "user.json",
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)
```

------

## 企业应用

接口测试数据：

```
{
  "username":"admin",
  "password":"123456"
}
```

读取：

```
data = json.load(f)
```

发送：

```
requests.post(
    url,
    json=data
)
```

------

# 6.10 CSV文件

CSV：

```
逗号分隔文件
```

示例：

```
name,age
Tom,18
Jack,20
```

------

读取：

```
import csv

with open(
    "user.csv",
    "r",
    encoding="utf-8"
) as f:

    reader = csv.reader(f)

    for row in reader:

        print(row)
```

输出：

```
['name','age']

['Tom','18']
```

------

## 企业应用

批量账号测试：

```
username,password

admin,123456

test,888888
```

------

# 6.11 openpyxl

企业自动化测试最常用。

安装：

```
pip install openpyxl
```

------

# 6.12 创建Excel

```
from openpyxl import Workbook

wb = Workbook()

ws = wb.active

ws["A1"] = "用户名"

ws["B1"] = "密码"

wb.save("user.xlsx")
```

------

# 6.13 读取Excel

```
from openpyxl import load_workbook

wb = load_workbook(
    "user.xlsx"
)

sheet = wb.active

print(
    sheet["A1"].value
)
```

输出：

```
用户名
```

------

# 6.14 获取行列

最大行：

```
sheet.max_row
```

最大列：

```
sheet.max_column
```

------

遍历：

```
for row in sheet.iter_rows():

    for cell in row:

        print(cell.value)
```

------

## 企业应用

读取测试用例：

| id   | title    | username | password |
| ---- | -------- | -------- | -------- |
| 1    | 登录成功 | admin    | 123456   |
| 2    | 登录失败 | test     | 111111   |

读取：

```
for row in sheet.iter_rows(
    min_row=2,
    values_only=True
):
    print(row)
```

------

# 6.15 configparser

读取 ini 配置。

配置：

```
[mysql]

host=127.0.0.1

port=3306
```

读取：

```
import configparser

config = configparser.ConfigParser()

config.read(
    "config.ini",
    encoding="utf-8"
)

host = config.get(
    "mysql",
    "host"
)
```

------

## 企业应用

数据库配置：

```
[mysql]

host=127.0.0.1

user=root

password=123456
```

------

# 6.16 YAML

现代自动化测试首选配置格式。

安装：

```
pip install pyyaml
```

------

配置：

```
base_url: http://test.com

mysql:
  host: 127.0.0.1
  port: 3306
```

------

读取：

```
import yaml

with open(
    "config.yaml",
    "r",
    encoding="utf-8"
) as f:

    data = yaml.safe_load(f)

print(data)
```

结果：

```
{
    'base_url':'http://test.com'
}
```

------

### 为什么推荐 YAML

相比 JSON：

JSON：

```
{
  "host":"127.0.0.1"
}
```

YAML：

```
host: 127.0.0.1
```

更简洁。

------

## 企业应用

pytest：

```
base_url: https://test.com

username: admin

password: 123456
```

------

# 6.17 pickle

序列化对象。

保存：

```
import pickle

with open(
    "data.pkl",
    "wb"
) as f:

    pickle.dump(data,f)
```

读取：

```
pickle.load(f)
```

一般了解即可。

------

## 企业项目结构

```
AutoTest

config
│
├── config.yaml

data
│
├── login.xlsx
├── register.xlsx

file
│
├── upload.jpg

log
│
├── test.log

report
│
├── allure-report
```

------

## 实战：Excel数据驱动

Excel：

| username | password |
| -------- | -------- |
| admin    | 123456   |
| test     | 111111   |

读取：

```
from openpyxl import load_workbook

wb = load_workbook(
    "login.xlsx"
)

sheet = wb.active

for row in sheet.iter_rows(
    min_row=2,
    values_only=True
):

    username,password = row

    print(username,password)
```

输出：

```
admin 123456

test 111111
```

# 7.1 什么是异常

异常（Exception）：

程序运行过程中发生的错误。

例如：

```
print(10/0)
```

运行：

```
ZeroDivisionError:
division by zero
```

程序：

```
执行
↓
发生错误
↓
程序终止
```

问题：

```
后续代码无法执行
```

解决：

```
try
↓
except
↓
捕获异常
↓
程序继续运行
```

------

# 7.2 常见异常

### ZeroDivisionError

除零异常：

```
10/0
```

------

### NameError

变量不存在：

```
print(name)
```

------

### TypeError

类型错误：

```
"10" + 10
```

------

### ValueError

值错误：

```
int("abc")
```

------

### IndexError

索引越界：

```
nums = [1,2]

print(nums[10])
```

------

### KeyError

字典键不存在：

```
user = {
    "name":"Tom"
}

print(user["age"])
```

------

### FileNotFoundError

文件不存在：

```
open("abc.txt")
```

------

### ModuleNotFoundError

模块不存在：

```
import aaa
```

------

### AttributeError

属性不存在：

```
None.click()
```

------

# 7.3 try except

语法：

```
try:
    代码
except:
    异常处理
```

示例：

```
try:

    print(10/0)

except:

    print("发生异常")
```

输出：

```
发生异常
```

程序继续执行。

------

# 7.4 捕获指定异常

推荐写法：

```
try:

    num = int("abc")

except ValueError:

    print("转换失败")
```

输出：

```
转换失败
```

------

多个异常：

```
try:

    pass

except ValueError:

    pass

except TypeError:

    pass
```

------

# 7.5 Exception

捕获所有异常：

```
try:

    pass

except Exception:

    print("发生异常")
```

企业项目大量使用。

------

获取异常对象：

```
try:

    10/0

except Exception as e:

    print(e)
```

输出：

```
division by zero
```

------

# 7.6 else

没有异常时执行。

```
try:

    print("成功")

except Exception:

    print("失败")

else:

    print("没有异常")
```

输出：

```
成功

没有异常
```

------

流程：

```
try
↓
是否异常？
↓
否
↓
else
```

------

# 7.7 finally

无论是否异常都会执行。

```
try:

    10/0

except:

    print("异常")

finally:

    print("关闭资源")
```

输出：

```
异常

关闭资源
```

------

企业应用：

数据库：

```
conn.close()
```

浏览器：

```
driver.quit()
```

文件：

```
file.close()
```

------

# 7.8 raise

主动抛出异常。

示例：

```
age = -1

if age < 0:

    raise ValueError("年龄不能小于0")
```

结果：

```
ValueError:
年龄不能小于0
```

------

企业应用

接口断言：

```
if code != 200:

    raise Exception(
        "接口执行失败"
    )
```

------

# 7.9 自定义异常

定义：

```
class LoginError(Exception):

    pass
```

抛出：

```
raise LoginError(
    "登录失败"
)
```

捕获：

```
except LoginError:

    print("登录异常")
```

------

## 企业应用

```
class ElementNotFoundError(
    Exception
):

    pass
```

元素不存在：

```
raise ElementNotFoundError(
    "元素未找到"
)
```

------

# 7.10 traceback

查看详细异常信息。

导入：

```
import traceback
```

示例：

```
try:

    10/0

except Exception:

    traceback.print_exc()
```

输出：

```
完整错误堆栈
```

------

## 企业应用

保存日志：

```
logger.error(
    traceback.format_exc()
)
```

------

# 7.11 assert断言

语法：

```
assert 条件
```

示例：

```
assert 1 == 1
```

通过。

失败：

```
assert 1 == 2
```

结果：

```
AssertionError
```

------

自定义提示：

```
assert 1==2,"断言失败"
```

------

## 企业应用

接口：

```
assert response.status_code == 200
```

页面：

```
assert "登录成功" in text
```

------

# 7.12 Selenium异常

导入：

```
from selenium.common.exceptions import *
```

常见：

### NoSuchElementException

元素不存在。

```
driver.find_element()
```

------

### TimeoutException

等待超时。

```
WebDriverWait()
```

------

### ElementClickInterceptedException

元素被遮挡。

------

### StaleElementReferenceException

元素失效。

页面刷新后常见。

------

## 企业应用

```
try:

    element.click()

except Exception:

    logger.error(
        "点击失败"
    )
```

------

# 7.13 requests异常

导入：

```
import requests
```

超时：

```
requests.get(
    url,
    timeout=5
)
```

异常：

```
requests.exceptions.Timeout
```

------

连接异常：

```
requests.exceptions.ConnectionError
```

------

统一捕获：

```
try:

    requests.get(url)

except requests.exceptions.RequestException:

    print("请求失败")
```

------

# 7.14 企业级封装

```
def send_request(
        **kwargs
):

    try:

        response = requests.request(
            **kwargs
        )

        return response

    except Exception as e:

        logger.error(e)

        raise
```

流程：

```
请求
↓
成功
↓
返回response

失败
↓
记录日志
↓
继续抛出
```

------

# 7.15 retry机制

重试：

```
for i in range(3):

    try:

        response = requests.get(url)

        break

    except Exception:

        print("重试")
```

流程：

```
请求
↓
失败
↓
重试
↓
失败
↓
重试
↓
成功
```

------

# 7.16 企业异常体系

```
BaseError
│
├── LoginError
├── MysqlError
├── RequestError
├── ElementError
└── FileError
```

例如：

```
class RequestError(
    Exception
):

    pass
```

统一：

```
raise RequestError(
    "接口失败"
)
```

# 8.1 什么是正则表达式

正则表达式（Regular Expression）：

用于匹配字符串的一套规则。

例如：

字符串：

```
text = "手机号：13812345678"
```

提取手机号：

```
13812345678
```

如果不用正则：

```
切片

find()

split()
```

复杂且不灵活。

使用正则：

```
\d{11}
```

即可完成。

------

## 企业应用

自动化测试中：

```
token提取

验证码提取

手机号提取

订单号提取

日志分析

HTML解析

数据关联
```

------

# 8.2 re模块

导入：

```
import re
```

------

# 8.3 match()

从字符串开头匹配。

语法：

```
re.match(
    pattern,
    string
)
```

示例：

```
import re

res = re.match(
    "hello",
    "hello world"
)

print(res)
```

结果：

```
<re.Match object>
```

获取内容：

```
print(res.group())
```

输出：

```
hello
```

------

不匹配：

```
re.match(
    "world",
    "hello world"
)
```

结果：

```
None
```

因为：

```
match

只匹配开头
```

------

# 8.4 search()

搜索整个字符串。

```
res = re.search(
    "world",
    "hello world"
)

print(
    res.group()
)
```

输出：

```
world
```

------

区别：

| 方法   | 匹配范围 |
| ------ | -------- |
| match  | 开头     |
| search | 全字符串 |

------

## 企业应用

提取 token：

```
text = "token=abc123"

res = re.search(
    "token=(.*)",
    text
)

print(
    res.group(1)
)
```

结果：

```
abc123
```

------

# 8.5 findall()

查找全部。

```
text = "1 2 3 4"

res = re.findall(
    "\d",
    text
)

print(res)
```

输出：

```
['1','2','3','4']
```

------

手机号：

```
text = """

13812345678

18888888888

"""
re.findall(
    r"\d{11}",
    text
)
```

结果：

```
[
'13812345678',

'18888888888'
]
```

------

## 企业应用

日志分析：

```
error_codes = re.findall(
    r"\d+",
    log
)
```

------

# 8.6 元字符

### .

匹配任意字符

```
re.findall(
    "a.",
    "abc"
)
```

结果：

```
['ab']
```

------

### \d

数字：

```
0-9
```

示例：

```
re.findall(
    r"\d",
    "abc123"
)
```

结果：

```
['1','2','3']
```

------

### \D

非数字。

------

### \w

字母数字下划线。

```
a-z

A-Z

0-9

_
```

------

### \W

非：

```
\w
```

------

### \s

空白字符。

```
空格

换行

tab
```

------

### \S

非空白字符。

------

# 8.7 数量词

### *

0~无限次

```
ab*
```

匹配：

```
a

ab

abb
```

------

### +

1~无限次

```
ab+
```

匹配：

```
ab

abb
```

------

### ?

0或1次

```
ab?
```

------

### {n}

固定 n 次

```
\d{11}
```

手机号。

------

### {m,n}

范围

```
\d{6,8}
```

6~8 位数字。

------

## 企业应用

验证码：

```
\d{6}
```

------

# 8.8 字符集 []

示例：

```
[abc]
```

匹配：

```
a

b

c
```

------

范围：

```
[a-z]
```

------

数字：

```
[0-9]
```

------

大小写：

```
[A-Za-z]
```

------

# 8.9 开始和结束

### ^

开始：

```
^hello
```

------

### $

结束：

```
world$
```

------

手机号：

```
^1\d{10}$
```

表示：

```
以1开始

11位数字

必须结束
```

------

# 8.10 分组 ()

示例：

```
text = "138-8888"

res = re.search(

    r"(\d+)-(\d+)",

    text

)
```

获取：

```
res.group(0)
```

结果：

```
138-8888
```

第一组：

```
res.group(1)
```

结果：

```
138
```

第二组：

```
res.group(2)
```

结果：

```
8888
```

------

## 企业应用

Cookie：

```
Set-Cookie:
token=abc123;
```

提取：

```
re.search(

    r"token=(.*?);",

    text

).group(1)
```

结果：

```
abc123
```

------

# 8.11 贪婪匹配

默认：

贪婪。

示例：

```
text = "<a>123</a><a>456</a>"
re.findall(
    "<a>.*</a>",
    text
)
```

结果：

```
[
'<a>123</a><a>456</a>'
]
```

因为：

```
.*

尽可能多匹配
```

------

# 8.12 非贪婪匹配

使用：

```
.*?
```

示例：

```
re.findall(
    "<a>.*?</a>",
    text
)
```

结果：

```
[
'<a>123</a>',

'<a>456</a>'
]
```

------

## 企业应用

HTML 提取：

```
title = re.search(

    "<title>(.*?)</title>",

    html

)
```

------

# 8.13 split()

切割。

```
text = "1,2,3"

re.split(
    ",",
    text
)
```

结果：

```
['1','2','3']
```

------

多个分隔符：

```
re.split(
    ",|;",
    "1,2;3"
)
```

结果：

```
['1','2','3']
```

------

# 8.14 sub()

替换。

```
re.sub(

    r"\d",

    "*",

    "abc123"

)
```

结果：

```
abc***
```

------

企业应用：

日志脱敏：

```
13812345678
```

↓

```
138****5678
```

------

# 8.15 compile()

预编译。

普通：

```
re.search(
    pattern,
    text
)
```

大量匹配：

```
pattern = re.compile(
    r"\d+"
)
```

使用：

```
pattern.findall(
    text
)
```

效率更高。

------

## 企业应用

日志分析：

```
phone_pattern = re.compile(
    r"1\d{10}"
)
```

重复使用。

------

# 8.16 flags

忽略大小写：

```
re.I
```

示例：

```
re.findall(

    "python",

    "Python",

    re.I

)
```

结果：

```
['Python']
```

------

多行：

```
re.M
```

------

## 企业应用

HTML：

大小写不固定。

使用：

```
re.I
```

------

# 项目实战

### 提取 token

返回：

```
response = """

code=200

token=abc123

"""
```

代码：

```
token = re.search(

    r"token=(.*)",

    response

).group(1)
```

结果：

```
abc123
```

------

### 提取订单号

字符串：

```
orderNo=202506280001
```

代码：

```
re.search(

    r"orderNo=(\d+)",

    text

).group(1)
```

------

### 手机号校验

```
phone = "13812345678"
if re.match(

    r"^1\d{10}$",

    phone

):

    print("合法")
```

------

### HTML 提取标题

```
html = """

<title>百度一下</title>

"""
title = re.search(

    r"<title>(.*?)</title>",

    html

).group(1)
```

结果：

```
百度一下
```

# 9.1 为什么学习装饰器

企业项目中：

经常需要给函数增加：

```
日志

异常处理

耗时统计

登录验证

截图

重试机制

权限校验
```

例如：

原函数：

```
def login():

    print("登录")
```

增加日志：

```
print("开始执行")

login()

print("结束执行")
```

如果每个函数都写：

```
重复代码

维护困难
```

解决方案：

```
装饰器
```

------

# 9.2 函数也是对象

Python 中：

函数也是对象。

定义：

```
def test():

    print("hello")
```

赋值：

```
a = test
```

调用：

```
a()
```

输出：

```
hello
```

------

函数作为参数：

```
def func(f):

    f()
```

调用：

```
func(test)
```

------

函数作为返回值：

```
def outer():

    def inner():

        print("hello")

    return inner
```

调用：

```
f = outer()

f()
```

输出：

```
hello
```

这是装饰器的基础。

------

# 9.3 闭包（Closure）

定义：

函数内部返回函数。

示例：

```
def outer():

    num = 10

    def inner():

        print(num)

    return inner
```

调用：

```
f = outer()

f()
```

输出：

```
10
```

流程：

```
outer
↓
产生局部变量 num
↓
inner
↓
保存 num
↓
返回
```

特点：

```
内部函数

引用外部变量

外部函数返回内部函数
```

------

# 9.4 最简单装饰器

原函数：

```
def login():

    print("登录")
```

装饰器：

```
def wrapper(func):

    def inner():

        print("开始")

        func()

        print("结束")

    return inner
```

使用：

```
login = wrapper(login)

login()
```

输出：

```
开始

登录

结束
```

------

# 9.5 @语法糖

上面可以简化：

```
@wrapper
def login():

    print("登录")
```

等价于：

```
login = wrapper(login)
```

调用：

```
login()
```

输出：

```
开始

登录

结束
```

------

## 企业应用

日志：

```
@logger
```

截图：

```
@screenshot
```

重试：

```
@retry
```

权限：

```
@login_required
```

------

# 9.6 通用装饰器

问题：

```
def login():

    pass
```

有参数：

```
def add(a,b):

    pass
```

如何兼容？

使用：

```
*args

**kwargs
```

代码：

```
def wrapper(func):

    def inner(

            *args,

            **kwargs

    ):

        print("开始")

        result = func(

            *args,

            **kwargs

        )

        print("结束")

        return result

    return inner
```

------

示例：

```
@wrapper
def add(a,b):

    return a+b
```

调用：

```
print(

    add(1,2)

)
```

输出：

```
开始

结束

3
```

------

# 9.7 多层装饰器

定义：

```
@a

@b

def test():

    pass
```

执行顺序：

```
a(
    b(
      test
    )
)
```

调用顺序：

```
a开始

b开始

test

b结束

a结束
```

------

# 9.8 functools.wraps

问题：

装饰后：

```
print(
    test.__name__
)
```

结果：

```
inner
```

原函数名字丢失。

解决：

```
from functools import wraps
```

使用：

```
from functools import wraps

def wrapper(func):

    @wraps(func)

    def inner():

        func()

    return inner
```

结果：

```
test.__name__
```

仍然是：

```
test
```

企业项目必须使用。

------

# 9.9 带参数装饰器

示例：

```
@logger("info")
```

实现：

```
def logger(level):

    def outer(func):

        def inner():

            print(level)

            func()

        return inner

    return outer
```

使用：

```
@logger("debug")

def test():

    pass
```

------

# 9.10 时间统计装饰器

```
import time

def timer(func):

    def inner(

            *args,

            **kwargs

    ):

        start = time.time()

        result = func(

            *args,

            **kwargs

        )

        end = time.time()

        print(

            end-start

        )

        return result

    return inner
```

使用：

```
@timer
def search():

    time.sleep(2)
```

输出：

```
2.0
```

------

## 企业应用

统计：

```
接口耗时

页面加载时间

SQL执行时间
```

------

# 9.11 yield

普通函数：

```
def test():

    return 1
```

生成器：

```
def test():

    yield 1
```

调用：

```
g = test()
```

类型：

```
generator
```

取值：

```
next(g)
```

输出：

```
1
```

------

# 9.12 next()

示例：

```
def nums():

    yield 1

    yield 2

    yield 3
```

调用：

```
g = nums()

print(next(g))

print(next(g))

print(next(g))
```

输出：

```
1

2

3
```

第四次：

报错：

```
StopIteration
```

------

# 9.13 for循环生成器

推荐：

```
for i in nums():

    print(i)
```

输出：

```
1

2

3
```

------

# 9.14 yield 和 return 区别

return：

```
结束函数
```

yield：

```
暂停函数
```

流程：

```
yield
↓
暂停
↓
next()
↓
继续执行
```

------

# 9.15 send()

生成器通信。

示例：

```
def test():

    num = yield

    print(num)
```

创建：

```
g = test()
```

启动：

```
next(g)
```

发送：

```
g.send(100)
```

输出：

```
100
```

了解即可。

------

# 9.16 iterable 和 iterator

### iterable

可迭代对象：

```
list

tuple

dict

set

str
```

判断：

```
from collections.abc import Iterable

isinstance(
    [],
    Iterable
)
```

结果：

```
True
```

------

### iterator

迭代器：

```
generator

iter(list)
```

判断：

```
from collections.abc import Iterator
```

------

关系：

```
Iterable
↓
iter()
↓
Iterator
↓
next()
```

------

## 企业应用

读取大文件：

```
def read():

    with open(

        "a.txt"

    ) as f:

        for line in f:

            yield line
```

优点：

```
节省内存
```

------

# 9.17 企业日志装饰器

```
def log(func):

    def inner(

            *args,

            **kwargs

    ):

        logger.info(

            f"{func.__name__}开始"

        )

        result = func(

            *args,

            **kwargs

        )

        logger.info(

            f"{func.__name__}结束"

        )

        return result

    return inner
```

使用：

```
@log
def login():

    pass
```

------

# 9.18 retry装饰器

```
def retry(func):

    def inner(

            *args,

            **kwargs

    ):

        for i in range(3):

            try:

                return func(

                    *args,

                    **kwargs

                )

            except:

                print(

                    "重试"

                )

    return inner
```

使用：

```
@retry
def request():

    pass
```

# 10.1 什么是模块

模块（Module）：

一个 `.py` 文件就是一个模块。

例如：

```
login.py

register.py

mysql_util.py
```

都是模块。

作用：

```
代码复用

降低耦合

方便维护
```

------

# 10.2 import 导入模块

创建：

login.py

```
def login():

    print("登录成功")
```

main.py：

```
import login

login.login()
```

输出：

```
登录成功
```

------

# 10.3 from ... import ...

普通导入：

```
import math

print(
    math.sqrt(16)
)
```

简化：

```
from math import sqrt

print(
    sqrt(16)
)
```

输出：

```
4
```

------

导入多个：

```
from math import sqrt,pow
```

------

# 10.4 as 别名

模块别名：

```
import numpy as np
```

使用：

```
np.array()
```

------

函数别名：

```
from math import sqrt as s

print(
    s(16)
)
```

------

## 企业项目

```
import pandas as pd

import requests as rq

import numpy as np
```

非常常见。

------

# 10.5 import *

不推荐：

```
from math import *
```

问题：

```
命名冲突

不清晰

可读性差
```

企业开发禁止。

------

# 10.6 **name**

每个模块都有：

```
__name__
```

当前文件执行：

```
print(__name__)
```

直接运行：

```
__main__
```

被导入：

```
模块名
```

------

# 10.7 **main**

经典写法：

```
def login():

    print("登录")

if __name__ == "__main__":

    login()
```

作用：

```
直接运行执行

导入不执行
```

------

## 企业应用

工具类：

```
mysql_util.py

excel_util.py

yaml_util.py
```

都会这样写。

------

# 10.8 sys模块

导入：

```
import sys
```

------

Python路径：

```
print(sys.path)
```

------

获取参数：

```
print(sys.argv)
```

------

退出程序：

```
sys.exit()
```

------

企业应用

解决：

```
ModuleNotFoundError
```

添加路径：

```
sys.path.append(
    project_path
)
```

------

# 10.9 os模块

导入：

```
import os
```

------

获取当前目录：

```
os.getcwd()
```

------

获取文件列表：

```
os.listdir()
```

------

创建目录：

```
os.mkdir(
    "report"
)
```

------

递归创建：

```
os.makedirs(
    "log/img"
)
```

------

判断：

```
os.path.exists(
    "report"
)
```

------

拼接路径：

```
os.path.join(
    "data",
    "login.xlsx"
)
```

结果：

```
data/login.xlsx
```

------

## 企业应用

创建报告目录：

```
if not os.path.exists(

        "report"

):

    os.mkdir(

        "report"

    )
```

------

# 10.10 pathlib

现代推荐。

导入：

```
from pathlib import Path
```

当前路径：

```
Path.cwd()
```

文件：

```
Path("config.yaml")
```

拼接：

```
Path("data")/"login.xlsx"
```

结果：

```
data/login.xlsx
```

------

判断：

```
Path(
    "report"
).exists()
```

创建：

```
Path(
    "report"
).mkdir()
```

------

相比：

```
os.path
```

更优雅。

------

# 10.11 datetime

获取时间：

```
from datetime import datetime

print(

    datetime.now()

)
```

输出：

```
2026-06-28 12:30:00
```

------

格式化：

```
datetime.now().strftime(

    "%Y-%m-%d %H:%M:%S"

)
```

结果：

```
2026-06-28 12:30:00
```

------

字符串转时间：

```
datetime.strptime(

    "2026-06-28",

    "%Y-%m-%d"

)
```

------

## 企业应用

生成日志：

```
test_20260628.log
```

------

# 10.12 time

暂停：

```
import time

time.sleep(3)
```

------

时间戳：

```
time.time()
```

------

企业应用：

```
等待

统计耗时

生成唯一文件名
```

------

# 10.13 random

随机整数：

```
import random

random.randint(

    1,

    100

)
```

------

随机元素：

```
random.choice(
    ["Tom","Jack"]
)
```

------

随机字符串：

```
import string

''.join(

random.choices(

string.ascii_letters,

k=8

)

)
```

------

## 企业应用

随机手机号：

```
phone = "138" + ''.join(

random.choices(

"0123456789",

k=8

)

)
```

------

# 10.14 collections

Counter：

统计次数。

```
from collections import Counter

nums = [1,1,2]

print(

Counter(nums)

)
```

输出：

```
{
1:2,

2:1
}
```

------

defaultdict：

```
from collections import defaultdict

dic = defaultdict(int)

dic["a"] += 1
```

------

deque：

双端队列。

了解即可。

------

## 企业应用

日志分析：

```
Counter(error_codes)
```

统计错误数量。

------

# 10.15 hashlib

MD5加密。

```
import hashlib

md5 = hashlib.md5()

md5.update(

"123456".encode()

)

print(

md5.hexdigest()

)
```

结果：

```
e10adc3949ba59abbe56e057f20f883e
```

------

## 企业应用

接口签名：

```
sign
```

密码加密：

```
password_md5
```

------

# 10.16 requirements.txt

导出：

```
pip freeze > requirements.txt
```

安装：

```
pip install -r requirements.txt
```

示例：

```
requests==2.32.3

selenium==4.28.0

openpyxl==3.1.5

pytest==8.4.0
```

------

# 10.17 虚拟环境 venv

创建：

```
python -m venv venv
```

激活：

Windows：

```
venv\Scripts\activate
```

退出：

```
deactivate
```

------

作用：

```
隔离环境

避免依赖冲突
```

------

# 10.18 企业项目结构

```
AutoTest

Base
│
├── base_page.py

Common
│
├── log_util.py
├── excel_util.py
├── yaml_util.py

Config
│
├── config.yaml

Data
│
├── login.xlsx

Locator
│
├── login_locator.py

Page
│
├── login_page.py

TestCase
│
├── test_login.py

Report

Log

Img

requirements.txt

run.py
```

------

# 10.19 包（Package）

目录：

```
Common

├── __init__.py

├── excel_util.py

├── yaml_util.py
```

包含：

```
__init__.py
```

即可成为包。

导入：

```
from Common.excel_util import ExcelUtil
```

# 11.1 为什么需要日志

程序运行过程中：

```
执行测试
↓
发生错误
↓
程序退出
↓
不知道哪里错
```

如果有日志：

```
执行测试
↓
记录日志
↓
发生错误
↓
查看日志
↓
定位问题
```

日志是：

```
企业级项目的眼睛
```

------

# 11.2 print 和 logging 的区别

### print

```
print("登录成功")
```

缺点：

```
不能分级

不能保存文件

无法格式化

不适合项目
```

------

### logging

```
logger.info(
    "登录成功"
)
```

优点：

```
支持等级

支持文件

支持格式化

支持切割

支持多输出
```

企业项目全部使用 logging。

------

# 11.3 logging模块

导入：

```
import logging
```

最简单：

```
import logging

logging.warning(
    "warning"
)
```

输出：

```
WARNING:root:warning
```

------

# 11.4 日志等级

从低到高：

| 等级     | 数值 |
| -------- | ---- |
| DEBUG    | 10   |
| INFO     | 20   |
| WARNING  | 30   |
| ERROR    | 40   |
| CRITICAL | 50   |

------

### DEBUG

调试信息：

```
logger.debug(
    "变量值"
)
```

------

### INFO

正常流程：

```
logger.info(
    "登录成功"
)
```

------

### WARNING

警告：

```
logger.warning(
    "库存不足"
)
```

------

### ERROR

错误：

```
logger.error(
    "接口失败"
)
```

------

### CRITICAL

严重错误：

```
logger.critical(
    "系统崩溃"
)
```

------

## 企业规范

```
DEBUG

开发环境

INFO

正常运行

ERROR

异常信息
```

最常用：

```
INFO + ERROR
```

------

# 11.5 basicConfig()

快速配置：

```
import logging

logging.basicConfig(

    level=logging.INFO

)

logging.info(
    "hello"
)
```

------

输出格式：

```
logging.basicConfig(

    format="%(asctime)s %(levelname)s %(message)s"

)
```

结果：

```
2026-06-28 10:00:00 INFO hello
```

------

# 常用占位符

### 时间

```
%(asctime)s
```

------

### 等级

```
%(levelname)s
```

------

### 文件名

```
%(filename)s
```

------

### 行号

```
%(lineno)d
```

------

### 方法名

```
%(funcName)s
```

------

### 内容

```
%(message)s
```

------

企业常用：

```
"%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s"
```

------

# 11.6 Logger对象

创建：

```
logger = logging.getLogger()
```

指定名称：

```
logger = logging.getLogger(
    "autotest"
)
```

输出：

```
logger.info(
    "登录成功"
)
```

------

推荐：

```
logger = logging.getLogger(
    __name__
)
```

每个模块一个 logger。

------

# 11.7 Handler

作用：

```
日志输出到哪里
```

流程：

```
Logger
↓
Handler
↓
控制台
文件
数据库
邮件
```

------

# 11.8 StreamHandler

控制台输出。

```
import logging

logger = logging.getLogger()

handler = logging.StreamHandler()

logger.addHandler(
    handler
)
```

------

# 11.9 FileHandler

输出文件。

```
handler = logging.FileHandler(

    "test.log",

    encoding="utf-8"

)
```

添加：

```
logger.addHandler(
    handler
)
```

------

结果：

生成：

```
test.log
```

------

# 11.10 Formatter

格式化器。

创建：

```
formatter = logging.Formatter(

"%(asctime)s | %(levelname)s | %(message)s"

)
```

绑定：

```
handler.setFormatter(
    formatter
)
```

------

流程：

```
Logger
↓
Handler
↓
Formatter
↓
输出
```

------

# 11.11 完整日志系统

```
import logging

logger = logging.getLogger()

logger.setLevel(
    logging.INFO
)

handler = logging.FileHandler(

    "test.log",

    encoding="utf-8"

)

formatter = logging.Formatter(

"%(asctime)s | %(levelname)s | %(message)s"

)

handler.setFormatter(
    formatter
)

logger.addHandler(
    handler
)

logger.info(
    "登录成功"
)
```

------

# 11.12 同时输出控制台+文件

```
console_handler = logging.StreamHandler()

file_handler = logging.FileHandler(

    "test.log",

    encoding="utf-8"

)
```

两个 handler：

```
logger.addHandler(
    console_handler
)

logger.addHandler(
    file_handler
)
```

效果：

```
控制台有日志

文件也有日志
```

企业必备。

------

# 11.13 RotatingFileHandler

日志大小切割。

导入：

```
from logging.handlers import RotatingFileHandler
```

创建：

```
handler = RotatingFileHandler(

    "test.log",

    maxBytes=1024,

    backupCount=3,

    encoding="utf-8"

)
```

含义：

```
超过1KB切割

最多保留3份
```

生成：

```
test.log

test.log.1

test.log.2
```

------

## 企业应用

防止：

```
日志无限增长
```

------

# 11.14 TimedRotatingFileHandler

按时间切割。

导入：

```
from logging.handlers import TimedRotatingFileHandler
```

创建：

```
handler = TimedRotatingFileHandler(

    "test.log",

    when="D",

    interval=1,

    backupCount=7,

    encoding="utf-8"

)
```

含义：

```
每天一个日志

保留7天
```

------

企业项目常用：

```
每天切割

保留7天
```

------

# 11.15 exception()

记录异常堆栈。

错误：

```
try:

    10/0

except Exception:

    logger.exception(
        "发生异常"
    )
```

输出：

```
错误信息

完整堆栈
```

比：

```
logger.error()
```

更强。

------

# 11.16 logging + Selenium

点击：

```
logger.info(
    "点击登录按钮"
)
```

异常：

```
except Exception:

    logger.error(
        "点击失败"
    )
```

输出：

```
定位元素

点击元素

点击失败
```

方便排查。

------

# 11.17 logging + requests

发送：

```
logger.info(
    "发送请求"
)
```

参数：

```
logger.info(
    data
)
```

响应：

```
logger.info(
    response.text
)
```

异常：

```
logger.error(
    e
)
```

------

## 企业应用

接口日志：

```
url

method

headers

body

response
```

全部记录。

------

# 11.18 企业级日志工具

目录：

```
Common

└── log_util.py
```

封装：

```
class LogUtil:

    @staticmethod
    def create_logger():

        pass
```

返回：

```
logger
```

使用：

```
from Common.log_util import LogUtil

logger = LogUtil.create_logger()
```

------

## 企业目录

```
Log

├── 20260628.log

├── 20260629.log
```

------

# 11.19 避免重复日志

问题：

```
logger.addHandler()
```

重复调用。

结果：

```
日志输出两次
```

解决：

```
if not logger.handlers:

    logger.addHandler(
        handler
    )
```

# 12.1 为什么学习 OOP

前面：

都是面向过程：

```
driver.find_element().click()

driver.find_element().send_keys()
```

问题：

```
代码重复

维护困难

耦合严重
```

企业项目：

```
BasePage

LoginPage

HomePage

MysqlUtil

ExcelUtil

LogUtil
```

全部采用：

```
面向对象
```

------

# 12.2 类和对象

现实世界：

```
人
↓
类

张三
↓
对象
```

汽车：

```
Car
↓
类

宝马
奔驰
奥迪
↓
对象
```

Python：

```
class Dog:

    pass
```

创建对象：

```
dog = Dog()
```

流程：

```
Class
↓
实例化
↓
Object
```

------

# 12.3 属性

定义：

```
class Dog:

    name = "旺财"

    age = 3
```

访问：

```
dog = Dog()

print(dog.name)
```

输出：

```
旺财
```

------

# 12.4 方法

定义：

```
class Dog:

    def run(self):

        print("奔跑")
```

调用：

```
dog = Dog()

dog.run()
```

输出：

```
奔跑
```

------

# 12.5 self

示例：

```
class Dog:

    def run(self):

        print(self)
```

调用：

```
dog = Dog()

dog.run()
```

实际：

```
Dog.run(dog)
```

self：

```
当前对象
```

------

# 12.6 构造函数 **init**()

创建对象自动执行。

```
class Dog:

    def __init__(self):

        print("初始化")
```

实例化：

```
dog = Dog()
```

输出：

```
初始化
```

------

带参数：

```
class Dog:

    def __init__(

            self,

            name,

            age

    ):

        self.name = name

        self.age = age
```

调用：

```
dog = Dog(

    "旺财",

    3
)
```

访问：

```
print(dog.name)
```

结果：

```
旺财
```

------

# 12.7 实例属性

属于对象。

```
class Dog:

    def __init__(

            self,

            name

    ):

        self.name = name
```

创建：

```
dog1 = Dog("Tom")

dog2 = Dog("Jack")
```

结果：

```
dog1.name

Tom

dog2.name

Jack
```

互不影响。

------

# 12.8 类属性

属于类。

```
class Dog:

    count = 0
```

访问：

```
Dog.count
```

或者：

```
dog.count
```

所有对象共享。

------

## 企业应用

统计：

```
浏览器数量

数据库连接数

请求次数
```

------

# 12.9 封装

隐藏内部实现。

提供接口。

例子：

银行卡：

```
密码
↓
隐藏

取钱
↓
公开
```

代码：

```
class User:

    def __init__(self):

        self.__password = "123456"
```

访问：

```
user.__password
```

报错。

------

提供方法：

```
def get_password(

        self

):

    return self.__password
```

调用：

```
user.get_password()
```

------

## 企业应用

隐藏：

```
数据库密码

token

driver
```

------

# 12.10 继承

父类：

```
class Animal:

    def eat(self):

        print("吃")
```

子类：

```
class Dog(

    Animal

):

    pass
```

调用：

```
dog = Dog()

dog.eat()
```

输出：

```
吃
```

流程：

```
Animal
↓
Dog
```

------

## 企业应用

```
BasePage
↓
LoginPage

HomePage

OrderPage
```

------

# 12.11 方法重写

父类：

```
class Animal:

    def run(self):

        print("动物跑")
```

子类：

```
class Dog(

    Animal

):

    def run(self):

        print("狗跑")
```

调用：

```
dog.run()
```

输出：

```
狗跑
```

------

# 12.12 super()

调用父类。

父类：

```
class Animal:

    def __init__(

            self,

            name

    ):

        self.name = name
```

子类：

```
class Dog(

    Animal

):

    def __init__(

            self,

            name,

            age

    ):

        super().__init__(

            name

        )

        self.age = age
```

调用：

```
dog = Dog(

    "Tom",

    3
)
```

结果：

```
dog.name
```

输出：

```
Tom
```

------

## 企业应用

```
class LoginPage(

    BasePage

):

    def __init__(

            self,

            driver

    ):

        super().__init__(

            driver

        )
```

非常常见。

------

# 12.13 多态

统一接口。

父类：

```
class Animal:

    def speak(self):

        pass
```

子类：

```
class Dog(

    Animal

):

    def speak(self):

        print("汪")
class Cat(

    Animal

):

    def speak(self):

        print("喵")
```

统一：

```
def test(animal):

    animal.speak()
```

调用：

```
test(Dog())

test(Cat())
```

------

## 企业应用

浏览器：

```
ChromeDriver

EdgeDriver

FirefoxDriver
```

统一：

```
driver.get()
```

------

# 12.14 静态方法

不需要：

```
self

cls
```

定义：

```
@staticmethod
def add(a,b):

    return a+b
```

调用：

```
MathUtil.add(
    1,
    2
)
```

------

企业应用

工具类：

```
ExcelUtil

YamlUtil

DateUtil
```

------

# 12.15 类方法

使用：

```
@classmethod
```

参数：

```
cls
```

示例：

```
class Dog:

    count = 0

    @classmethod
    def show_count(

            cls

    ):

        print(

            cls.count

        )
```

调用：

```
Dog.show_count()
```

------

# 12.16 魔术方法

### **str**()

对象打印。

默认：

```
print(obj)
```

输出：

```
<Dog object>
```

重写：

```
class Dog:

    def __str__(self):

        return "Dog对象"
```

输出：

```
Dog对象
```

------

### **len**()

```
class Dog:

    def __len__(self):

        return 100
```

调用：

```
len(obj)
```

结果：

```
100
```

------

### **call**()

对象像函数一样调用。

```
class Dog:

    def __call__(self):

        print("hello")
```

调用：

```
dog()
```

输出：

```
hello
```

------

# 12.17 isinstance()

判断类型：

```
isinstance(
    dog,
    Dog
)
```

结果：

```
True
```

继承：

```
isinstance(
    dog,
    Animal
)
```

也是：

```
True
```

------

# 12.18 单例模式

作用：

整个项目只有一个对象。

企业应用：

```
Logger

Mysql

Redis

Driver
```

------

实现：

```
class Singleton:

    _instance = None

    def __new__(

            cls,

            *args,

            **kwargs

    ):

        if not cls._instance:

            cls._instance = super().__new__(

                cls

            )

        return cls._instance
```

测试：

```
a = Singleton()

b = Singleton()

print(a is b)
```

输出：

```
True
```

------

# 12.19 Page Object思想

核心：

页面 = 类

例如：

登录页：

```
LoginPage
```

首页：

```
HomePage
```

订单页：

```
OrderPage
```

关系：

```
BasePage
↓
LoginPage

HomePage

OrderPage
```

------

# BasePage

```
class BasePage:

    def click(

            self,

            locator

    ):

        pass

    def input(

            self,

            locator,

            value

    ):

        pass
```

------

LoginPage：

```
class LoginPage(

    BasePage

):

    def login(

            self,

            username,

            password

    ):

        pass
```

------

TestCase：

```
login_page.login()
```

流程：

```
TestCase
↓
Page
↓
BasePage
↓
Selenium
```

这是企业标准架构。

# 13.1 为什么测试工程师必须会数据库？

企业项目中：

需要验证：

```
注册成功
↓
数据库是否新增用户？

下单成功
↓
订单表是否新增？

支付成功
↓
状态是否更新？

分佣成功
↓
佣金表是否生成记录？
```

所以：

```
接口断言 = 页面断言 + 数据库断言
```

数据库能力是自动化测试工程师必备技能。

------

# 13.2 安装 PyMySQL

安装：

```
pip install pymysql
```

导入：

```
import pymysql
```

------

# 13.3 建立数据库连接

```
import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="123456",
    database="test",
    charset="utf8mb4"
)
```

参数：

| 参数     | 含义   |
| -------- | ------ |
| host     | IP地址 |
| port     | 端口   |
| user     | 用户名 |
| password | 密码   |
| database | 数据库 |
| charset  | 编码   |

------

# 13.4 cursor 游标

创建：

```
cursor = conn.cursor()
```

作用：

```
数据库
↓
连接(conn)
↓
游标(cursor)
↓
执行SQL
```

可以理解为：

```
cursor = SQL执行器
```

------

# 13.5 execute()

执行 SQL：

```
sql = "select * from user"

cursor.execute(sql)
```

返回：

```
rows = cursor.execute(sql)

print(rows)
```

结果：

```
3
```

表示：

```
查询到3条记录
```

------

# 13.6 fetchone()

获取一条记录：

```
cursor.execute(
    "select * from user"
)

result = cursor.fetchone()

print(result)
```

结果：

```
(1, 'Tom')
```

类型：

```
tuple
```

------

# 13.7 fetchall()

获取所有记录：

```
cursor.execute(
    "select * from user"
)

result = cursor.fetchall()

print(result)
```

结果：

```
(
(1,'Tom'),
(2,'Jack')
)
```

类型：

```
tuple
```

------

# 13.8 fetchmany()

获取指定数量：

```
cursor.fetchmany(2)
```

获取：

```
前两条记录
```

------

# 13.9 DictCursor

默认：

```
(1,'Tom')
```

不方便。

推荐：

```
cursor = conn.cursor(

    pymysql.cursors.DictCursor

)
```

结果：

```
{
"id":1,
"name":"Tom"
}
```

企业必用。

------

# 13.10 插入数据

SQL：

```
sql = """

insert into user(

name

)

values(

'Tom'

)

"""
```

执行：

```
cursor.execute(sql)

conn.commit()
```

------

注意：

必须：

```
commit()
```

否则不会保存。

------

# 13.11 更新数据

```
sql = """

update user

set name='Jack'

where id=1

"""
```

执行：

```
cursor.execute(sql)

conn.commit()
```

------

# 13.12 删除数据

```
sql = """

delete from user

where id=1

"""
```

执行：

```
cursor.execute(sql)

conn.commit()
```

------

# 13.13 事务

流程：

```
execute
↓
commit
↓
永久保存
```

如果：

```
execute
↓
rollback
↓
撤销
```

------

示例：

```
try:

    cursor.execute(sql)

    conn.commit()

except Exception:

    conn.rollback()
```

------

企业项目：

```
下单

扣库存

生成订单

支付

分佣
```

都属于事务。

------

# 13.14 参数化查询

错误写法：

```
username = "Tom"

sql = f"""

select *

from user

where name='{username}'

"""
```

存在：

```
SQL注入
```

------

正确：

```
sql = """

select *

from user

where name=%s

"""

cursor.execute(

    sql,

    ("Tom",)

)
```

------

多个参数：

```
sql = """

select *

from user

where name=%s

and age=%s

"""

cursor.execute(

    sql,

    (

        "Tom",

        20

    )

)
```

企业必须使用参数化。

------

# 13.15 SQL注入

危险：

用户输入：

```
' or 1=1 #
```

SQL：

```
select *

from user

where name=''

or 1=1
```

结果：

```
所有数据泄露
```

解决：

```
参数化查询
```

------

# 13.16 executemany()

批量插入：

```
sql = """

insert into user(

name

)

values(

%s

)

"""
```

数据：

```
data = [

("Tom",),

("Jack",),

("Rose",)

]
```

执行：

```
cursor.executemany(

    sql,

    data

)

conn.commit()
```

效率更高。

------

# 13.17 获取自增ID

插入：

```
cursor.execute(sql)

conn.commit()
```

获取：

```
print(

cursor.lastrowid

)
```

结果：

```
10
```

企业常用：

```
生成订单后

获取订单ID
```

------

# 13.18 with 上下文

传统：

```
conn = pymysql.connect()

cursor = conn.cursor()

...

cursor.close()

conn.close()
```

容易忘记关闭。

------

推荐：

```
with pymysql.connect(

    host="127.0.0.1",

    user="root",

    password="123456",

    database="test"

) as conn:

    with conn.cursor() as cursor:

        cursor.execute(

            "select * from user"

        )
```

自动关闭资源。

------

# 13.19 ORM思想

SQL：

```
select *

from user
```

ORM：

```
user.name
```

思想：

```
表
↓
类

记录
↓
对象
```

代表：

```
SQLAlchemy

Django ORM
```

测试开发了解即可。

------

# 13.20 数据库连接池

问题：

每次：

```
connect()
```

代价很大。

企业：

```
程序启动
↓
创建连接池
↓
复用连接
```

优点：

```
性能高

资源利用率高
```

常见：

```
DBUtils
```

------

# 13.21 企业级 MysqlUtil

目录：

```
Common

└── mysql_util.py
```

结构：

```
class MysqlUtil:

    def connect(self):
        pass

    def select_one(self):
        pass

    def select_all(self):
        pass

    def update(self):
        pass

    def insert(self):
        pass
```

------

# 13.22 单例模式 + MysqlUtil

整个项目：

只需要一个连接。

```
MysqlUtil()
```

配合：

```
__new__()
```

实现单例。

------

## 企业目录

```
Common
│
├── mysql_util.py

Config
│
├── config.yaml

TestCase

Page

Data
```

# 14.1 为什么要学习 Excel 和 YAML

企业项目：

测试数据：

```
账号密码

手机号

验证码

订单号

搜索关键字
```

配置数据：

```
URL

数据库

Redis

日志等级

浏览器类型
```

存放位置：

```
Excel
↓
测试数据

YAML
↓
配置文件
```

所以：

```
Excel + YAML

=

自动化框架的数据中心
```

------

# 14.2 安装 openpyxl

安装：

```
pip install openpyxl
```

导入：

```
import openpyxl
```

------

# 14.3 Workbook

创建 Excel：

```
from openpyxl import Workbook

wb = Workbook()
```

保存：

```
wb.save(
    "login.xlsx"
)
```

生成：

```
login.xlsx
```

------

# 14.4 load_workbook

读取文件：

```
from openpyxl import load_workbook

wb = load_workbook(
    "login.xlsx"
)
```

------

# 14.5 Worksheet

获取 sheet：

```
sheet = wb.active
```

指定：

```
sheet = wb["Sheet1"]
```

查看名称：

```
print(
    sheet.title
)
```

------

# 14.6 Cell

写入：

```
sheet["A1"] = "用户名"

sheet["B1"] = "密码"
```

保存：

```
wb.save(
    "login.xlsx"
)
```

------

读取：

```
print(
    sheet["A1"].value
)
```

结果：

```
用户名
```

------

# 14.7 row column

写：

```
sheet.cell(
    row=1,
    column=1
).value = "用户名"
```

读：

```
value = sheet.cell(
    row=2,
    column=2
).value
```

------

企业推荐：

```
cell()
```

比：

```
A1
```

更灵活。

------

# 14.8 max_row max_column

获取最大行：

```
sheet.max_row
```

最大列：

```
sheet.max_column
```

示例：

```
rows = sheet.max_row

for i in range(
        2,
        rows+1
):
    pass
```

------

# 14.9 遍历 Excel

示例：

```
for row in sheet.iter_rows():

    for cell in row:

        print(
            cell.value
        )
```

------

获取 values：

```
for row in sheet.values:

    print(row)
```

输出：

```
(
'admin',
'123456'
)
```

------

# 14.10 append()

追加：

```
sheet.append(

[
"admin",
"123456"
]

)
```

保存：

```
wb.save(
    "login.xlsx"
)
```

------

# 14.11 删除行

```
sheet.delete_rows(
    2
)
```

删除：

```
第2行
```

------

插入：

```
sheet.insert_rows(
    2
)
```

------

# 14.12 修改数据

```
sheet.cell(
    2,
    1
).value = "Tom"
```

保存：

```
wb.save(
    "login.xlsx"
)
```

------

## 企业应用

回写结果：

```
PASS

FAIL
```

------

# 14.13 ExcelUtil封装

目录：

```
Common

└── excel_util.py
```

结构：

```
class ExcelUtil:

    def read_data(self):
        pass

    def write_data(self):
        pass
```

返回：

```
[
{
"username":"admin",
"password":"123456"
}
]
```

企业必写。

------

# 14.14 安装 PyYAML

安装：

```
pip install pyyaml
```

导入：

```
import yaml
```

------

# 14.15 YAML格式

示例：

config.yaml

```
url: http://test.com

browser: chrome

timeout: 10
```

读取：

```
with open(

        "config.yaml",

        encoding="utf8"

) as f:

    data = yaml.safe_load(f)
```

结果：

```
{
"url":"http://test.com",
"browser":"chrome"
}
```

------

# 14.16 多层 YAML

配置：

```
mysql:

  host: 127.0.0.1

  user: root

  password: 123456
```

读取：

```
data["mysql"]["host"]
```

结果：

```
127.0.0.1
```

------

## 企业配置中心

```
url:

  dev: xxx

  test: xxx

  prod: xxx
```

------

# 14.17 safe_load()

推荐：

```
yaml.safe_load()
```

不要：

```
yaml.load()
```

原因：

```
安全问题
```

------

# 14.18 写 YAML

```
dic = {

"url":"xxx",

"timeout":10

}
```

保存：

```
with open(

"config.yaml",

"w",

encoding="utf8"

) as f:

    yaml.dump(

        dic,

        f,

        allow_unicode=True

    )
```

------

# 14.19 Data Driven

思想：

```
代码

+

数据

分离
```

例如：

Excel：

```
admin 123456

Tom 111111

Jack 222222
```

代码：

```
def test_login():

    login()
```

执行：

```
循环读取数据

执行测试
```

优点：

```
复用性高

维护方便
```

------

# 14.20 ddt

安装：

```
pip install ddt
```

导入：

```
from ddt import ddt,data
```

------

使用：

```
@ddt
class TestLogin:

    @data(

        ("admin","123456"),

        ("Tom","111")

    )

    def test_login(

            self,

            value

    ):

        pass
```

------

# 14.21 unpack

拆包：

```
from ddt import unpack
```

使用：

```
@data(

("admin","123456")

)

@unpack
```

函数：

```
def test_login(

        self,

        username,

        password

):
```

------

# 14.22 pytest 参数化

推荐：

```
@pytest.mark.parametrize(

"username,password",

[
("admin","123456"),

("Tom","111")

]

)
```

函数：

```
def test_login(

username,

password

):
```

------

企业：

优先：

```
pytest

>

ddt
```

------

# 14.23 config.yaml

目录：

```
Config

├── config.yaml
```

示例：

```
url:

  https://xxx.com

mysql:

  host: 127.0.0.1

  user: root

browser:

  chrome
```

------

## 企业目录

```
Config

Data

Common

TestCase
```

------

# 14.24 ConfigUtil

封装：

```
class ConfigUtil:

    def get_url():
        pass

    def get_mysql():
        pass
```

调用：

```
ConfigUtil.get_url()
```

而不是：

```
yaml.safe_load()
```

到处写。

# 15.1 为什么学习 Redis？

MySQL：

```
磁盘存储
↓
速度较慢
```

Redis：

```
内存存储
↓
速度极快
```

速度：

```
Redis

微秒级

↓

MySQL

毫秒级
```

------

## 企业应用

### Token

```
登录
↓
生成 token
↓
Redis 保存
↓
接口校验
```

------

### Session

```
用户状态

购物车

验证码
```

------

### 秒杀系统

```
库存

订单队列

分布式锁
```

------

### 排行榜

```
积分榜

热搜榜

销售榜
```

------

# 15.2 Redis 安装

默认端口：

```
6379
```

连接：

```
host

port

password
```

------

# 15.3 安装 redis-py

安装：

```
pip install redis
```

导入：

```
import redis
```

------

# 15.4 建立连接

```
import redis

r = redis.Redis(

    host="127.0.0.1",

    port=6379,

    password="123456",

    decode_responses=True

)
```

推荐：

```
decode_responses=True
```

否则：

```
b'admin'
```

会返回 bytes。

------

# 15.5 set()

保存数据：

```
r.set(
    "name",
    "Tom"
)
```

查看：

```
r.get(
    "name"
)
```

结果：

```
Tom
```

------

流程：

```
key
↓

name

value
↓

Tom
```

------

# 15.6 get()

获取：

```
value = r.get(
    "name"
)

print(value)
```

结果：

```
Tom
```

------

# 15.7 delete()

删除：

```
r.delete(
    "name"
)
```

------

# 15.8 exists()

判断：

```
r.exists(
    "name"
)
```

结果：

```
1
```

存在：

```
True
```

------

# 15.9 expire()

设置过期时间：

```
r.expire(

    "token",

    3600

)
```

含义：

```
1小时后失效
```

------

直接：

```
r.set(

    "token",

    "abc",

    ex=3600

)
```

推荐。

------

## 企业应用

登录：

```
token

↓

Redis

↓

2小时过期
```

------

# 15.10 ttl()

查看剩余时间：

```
r.ttl(
    "token"
)
```

结果：

```
3550
```

单位：

```
秒
```

------

# 15.11 String 类型

最常见。

保存：

```
r.set(
    "username",
    "admin"
)
```

获取：

```
r.get(
    "username"
)
```

------

应用：

```
token

验证码

配置

缓存
```

------

# 15.12 List 类型

类似：

```
[]
```

左插：

```
r.lpush(

    "names",

    "Tom"

)
```

右插：

```
r.rpush(

    "names",

    "Jack"

)
```

获取：

```
r.lrange(

    "names",

    0,

    -1

)
```

结果：

```
['Tom','Jack']
```

------

应用：

```
消息队列

任务队列
```

------

# 15.13 Set 类型

特点：

```
去重

无序
```

添加：

```
r.sadd(

    "user",

    "Tom"

)
```

获取：

```
r.smembers(
    "user"
)
```

------

应用：

```
用户标签

共同好友

去重
```

------

# 15.14 Hash 类型（★★★★★）

类似：

```
dict
```

保存：

```
r.hset(

    "user:1",

    "name",

    "Tom"

)
```

增加：

```
r.hset(

    "user:1",

    "age",

    20

)
```

获取：

```
r.hget(

    "user:1",

    "name"

)
```

结果：

```
Tom
```

全部：

```
r.hgetall(
    "user:1"
)
```

结果：

```
{
'name':'Tom',

'age':'20'
}
```

------

企业应用：

### 用户信息

```
user:1001
```

↓

```
{
name

phone

age
}
```

------

### Session

### 购物车

### Token

Hash 使用最多。

------

# 15.15 ZSet（有序集合）

特点：

```
自动排序
```

添加：

```
r.zadd(

    "rank",

    {

        "Tom":100,

        "Jack":90

    }

)
```

查看：

```
r.zrange(

    "rank",

    0,

    -1

)
```

结果：

```
[
'Jack',

'Tom'
]
```

------

应用：

```
积分榜

热搜榜

排行榜
```

------

# 五种数据类型总结

| 类型   | Python对应 | 应用     |
| ------ | ---------- | -------- |
| String | str        | token    |
| List   | list       | 队列     |
| Set    | set        | 去重     |
| Hash   | dict       | 用户信息 |
| ZSet   | 排序集合   | 排行榜   |

------

# 15.16 incr()

自增：

```
r.set(
    "count",
    1
)

r.incr(
    "count"
)
```

结果：

```
2
```

------

企业应用：

```
访问量

点赞数

库存
```

------

# 15.17 Pipeline

问题：

连续：

```
r.set()

r.get()

r.delete()
```

网络请求太多。

------

解决：

```
pipe = r.pipeline()

pipe.set(
    "name",
    "Tom"
)

pipe.get(
    "name"
)

pipe.execute()
```

作用：

```
批量执行

提高性能
```

------

# 15.18 发布订阅

发布：

```
r.publish(

    "news",

    "hello"

)
```

订阅：

```
sub = r.pubsub()

sub.subscribe(
    "news"
)
```

了解即可。

------

# 15.19 分布式锁

加锁：

```
r.set(

    "lock",

    "1",

    nx=True,

    ex=10

)
```

含义：

```
不存在才创建

10秒后自动释放
```

------

应用：

```
秒杀

订单

库存
```

------

# 15.20 RedisUtil 封装

目录：

```
Common

└── redis_util.py
```

结构：

```
class RedisUtil:

    def set(self):
        pass

    def get(self):
        pass

    def delete(self):
        pass
```

------

## 单例模式

整个项目：

只有一个：

```
Redis()
```

对象。

推荐：

```
Singleton
```

实现。

------

# 15.21 Token缓存

登录：

```
用户登录
↓
生成token
↓
Redis
↓
2小时过期
```

代码：

```
r.set(

    token,

    user_id,

    ex=7200

)
```

------

接口：

```
token
↓

Redis查询

↓

用户
```

------

# 15.22 Session缓存

保存：

```
session_id
```

↓

```
Hash
```

↓

```
用户信息
```

------

# 15.23 验证码缓存

发送：

```
123456
```

保存：

```
r.set(

    phone,

    code,

    ex=300

)
```

5分钟失效。

------

# 15.24 秒杀库存

库存：

```
r.set(
    "goods",
    100
)
```

下单：

```
r.decr(
    "goods"
)
```

避免：

```
超卖
```

# 16.1 为什么学习 Requests？

自动化测试：

本质上是在模拟：

```
浏览器
↓
发送 HTTP 请求
↓
服务器
↓
返回响应
```

例如：

登录：

```
POST

/login
```

查询：

```
GET

/user
```

下单：

```
POST

/order
```

支付：

```
POST

/pay
```

所以：

```
Requests

=

接口自动化核心
```

------

# 16.2 安装 Requests

安装：

```
pip install requests
```

导入：

```
import requests
```

------

# 16.3 GET 请求

访问：

```
import requests

response = requests.get(

    "https://httpbin.org/get"

)
```

查看状态码：

```
print(
    response.status_code
)
```

结果：

```
200
```

------

查看文本：

```
print(
    response.text
)
```

返回：

```
HTML

JSON

字符串
```

------

# 16.4 JSON()

接口返回：

```
{
  "name":"Tom"
}
```

解析：

```
data = response.json()

print(
    data
)
```

结果：

```
{
"name":"Tom"
}
```

类型：

```
dict
```

------

企业中：

最常见：

```
response.json()
```

------

# 16.5 POST 请求

发送：

```
response = requests.post(

    url,

    json={

        "username":"admin",

        "password":"123456"

    }

)
```

------

查看：

```
response.json()
```

------

# 16.6 params

GET 参数：

URL：

```
/user?id=1
```

代码：

```
requests.get(

    url,

    params={

        "id":1

    }

)
```

生成：

```
?id=1
```

------

多个参数：

```
params={

"id":1,

"name":"Tom"

}
```

------

# 16.7 data 和 json 区别（★★★★★）

### form 表单

```
requests.post(

url,

data={

"username":"admin"

}

)
```

请求体：

```
application/x-www-form-urlencoded
```

------

### JSON

```
requests.post(

url,

json={

"username":"admin"

}

)
```

请求头自动：

```
application/json
```

------

企业接口：

95%

使用：

```
json=
```

------

# 16.8 Header

添加：

```
headers = {

"token":"abc"

}
```

发送：

```
requests.get(

url,

headers=headers

)
```

------

常见：

```
Authorization

token

User-Agent
```

------

# 16.9 Cookie

获取：

```
response.cookies
```

转换：

```
dict(

response.cookies

)
```

------

发送：

```
requests.get(

url,

cookies={

"sid":"123"

}

)
```

------

# 16.10 Session（★★★★★）

问题：

登录：

```
login
↓

token
↓

查询用户
```

每次传 Cookie：

麻烦。

------

解决：

```
session = requests.Session()
```

登录：

```
session.post(
    login_url
)
```

查询：

```
session.get(
    user_url
)
```

自动：

```
Cookie保持
```

------

企业：

接口自动化：

大量使用：

```
Session()
```

------

# 16.11 PUT 请求

修改：

```
requests.put(

url,

json=data

)
```

------

# 16.12 DELETE 请求

删除：

```
requests.delete(

url
)
```

------

# 16.13 Response对象

返回：

```
response
```

属性：

### status_code

```
response.status_code
```

------

### text

```
response.text
```

------

### json()

```
response.json()
```

------

### headers

```
response.headers
```

------

### cookies

```
response.cookies
```

------

### elapsed

响应时间：

```
response.elapsed
```

------

# 16.14 状态码

常见：

| 状态码 | 含义       |
| ------ | ---------- |
| 200    | 成功       |
| 201    | 创建成功   |
| 301    | 重定向     |
| 400    | 参数错误   |
| 401    | 未登录     |
| 403    | 无权限     |
| 404    | 不存在     |
| 500    | 服务器异常 |

------

断言：

```
assert response.status_code == 200
```

------

# 16.15 timeout

防止：

接口卡死。

设置：

```
requests.get(

url,

timeout=5

)
```

含义：

```
5秒超时
```

企业必须设置。

------

# 16.16 verify=False

关闭证书验证：

```
requests.get(

url,

verify=False

)
```

一般：

测试环境。

------

生产环境：

不推荐。

------

# 16.17 上传文件

接口：

```
/upload
```

代码：

```
files = {

"file":

open(

"a.jpg",

"rb"

)

}
```

发送：

```
requests.post(

url,

files=files

)
```

------

# 16.18 下载文件

获取：

```
response = requests.get(
    url
)
```

保存：

```
with open(

"a.jpg",

"wb"

) as f:

    f.write(

        response.content

    )
```

------

# 16.19 Retry重试

安装：

```
pip install urllib3
```

示例：

```
from requests.adapters import HTTPAdapter

from urllib3.util.retry import Retry
```

创建：

```
retry = Retry(

total=3

)
```

挂载：

```
session.mount(

"https://",

HTTPAdapter(

max_retries=retry

)

)
```

作用：

```
失败自动重试
```

------

# 16.20 Token管理

登录：

```
token = response.json()["token"]
```

Header：

```
headers = {

"token":token

}
```

后续：

```
requests.get(

url,

headers=headers

)
```

------

## 企业：

封装：

```
get_token()
```

统一管理。

------

# 16.21 接口关联

登录：

返回：

```
user_id
```

查询：

```
/user/{id}
```

代码：

```
user_id = login_res["id"]

requests.get(

f"/user/{user_id}"

)
```

这就是：

```
接口关联
```

------

# 16.22 RequestUtil

目录：

```
Common

└── request_util.py
```

结构：

```
class RequestUtil:

    def get():
        pass

    def post():
        pass

    def put():
        pass

    def delete():
        pass
```

统一：

```
日志

header

token

异常处理
```

# 17.1 为什么需要接口自动化框架

简单脚本：

```
requests.post()

requests.get()

requests.put()
```

问题：

```
代码重复

无法维护

没有日志

没有报告

没有数据驱动

没有数据库断言
```

企业项目：

需要：

```
高复用

低耦合

易维护

易扩展
```

因此：

```
需要接口自动化框架
```

------

# 17.2 企业框架目录

标准目录：

```
Api
│
├── login_api.py
├── user_api.py
├── order_api.py

Common
│
├── request_util.py
├── mysql_util.py
├── redis_util.py
├── yaml_util.py
├── log_util.py

Config
│
├── config.yaml

Data
│
├── login.yaml

TestCase
│
├── test_login.py
├── test_order.py

Report
│
├── allure-report

Log
│
├── log.txt
```

------

# 17.3 BaseApi思想

每个接口：

都是一个类。

例如：

登录：

```
LoginApi
```

用户：

```
UserApi
```

订单：

```
OrderApi
```

继承：

```
BaseApi
```

流程：

```
BaseApi
↓

LoginApi

UserApi

OrderApi
```

------

# 17.4 RequestUtil 封装

传统：

```
requests.post()

requests.get()
```

企业：

```
RequestUtil().send_request()
```

统一：

```
日志

header

token

session

异常处理
```

------

结构：

```
class RequestUtil:

    def send_request(
            self,
            method,
            url,
            **kwargs
    ):
        pass
```

------

# 17.5 Session管理

创建：

```
session = requests.Session()
```

整个项目：

共享：

```
session
```

优点：

```
自动Cookie保持

减少连接开销
```

------

企业：

单例模式：

```
Session()
```

------

# 17.6 Token管理（★★★★★）

登录：

```
token = login()
```

保存：

```
headers = {

"token":token

}
```

问题：

每个接口都传：

麻烦。

------

企业：

封装：

```
TokenUtil.get_token()
```

自动：

```
登录

获取token

缓存token
```

------

调用：

```
RequestUtil()

↓

自动添加header
```

------

# 17.7 YAML数据驱动

目录：

```
Data

login.yaml
```

数据：

```
username: admin

password: 123456
```

读取：

```
YamlUtil.read_yaml()
```

作用：

```
代码

数据

分离
```

------

# 17.8 BaseApi

统一：

```
class BaseApi:

    def get():

        pass

    def post():

        pass
```

内部：

调用：

```
RequestUtil
```

------

LoginApi：

```
class LoginApi(

        BaseApi

):

    def login():

        pass
```

------

OrderApi：

```
class OrderApi(

        BaseApi

):

    def create_order():

        pass
```

------

# 17.9 日志系统

目录：

```
Log

log.txt
```

记录：

```
请求URL

请求参数

响应结果

异常信息
```

调用：

```
logger.info()
```

------

企业：

统一：

```
LogUtil
```

------

# 17.10 响应断言

状态码：

```
assert response.status_code == 200
```

业务码：

```
assert response.json()["code"] == 0
```

消息：

```
assert response.json()["msg"] == "成功"
```

------

# 17.11 数据库断言（★★★★★）

接口：

```
注册成功
```

页面：

显示成功。

不够。

还需要：

```
select *

from user
```

验证：

```
数据库是否新增记录
```

------

调用：

```
MysqlUtil.select_one()
```

断言：

```
assert result
```

------

企业：

```
接口断言

+

数据库断言
```

------

# 17.12 Redis断言

例如：

登录：

生成：

```
token
```

验证：

Redis：

```
RedisUtil.get(token)
```

断言：

```
assert token
```

------

# 17.13 接口关联（★★★★★）

登录：

返回：

```
user_id
```

查询：

需要：

```
user_id
```

流程：

```
登录接口

↓

user_id

↓

用户接口
```

代码：

```
user_id = login_res["id"]

user_api.get_user(
    user_id
)
```

------

订单：

```
创建订单

↓

order_id

↓

支付订单
```

------

这是企业最常见场景。

------

# 17.14 Extract机制

提取：

```
$.data.id
```

保存：

```
order_id
```

后续：

引用：

```
${order_id}
```

思想：

```
提取

↓

保存

↓

引用
```

类似：

JMeter。

------

# 17.15 参数化

Pytest：

```
@pytest.mark.parametrize()
```

读取：

Excel：

```
ExcelUtil()
```

或者：

YAML：

```
YamlUtil()
```

作用：

```
一套代码

多组数据
```

------

# 17.16 Allure集成

添加：

```
@allure.title()
```

步骤：

```
with allure.step():
```

截图：

```
allure.attach()
```

生成：

```
HTML报告
```

------

# 17.17 BaseUrl管理

config.yaml：

```
host:

  test:

    http://test.com
```

获取：

```
ConfigUtil.get_host()
```

拼接：

```
host + api
```

避免：

硬编码。

------

# 17.18 环境切换

支持：

```
dev

test

pre

prod
```

配置：

```
env:

  test
```

自动：

切换：

```
ConfigUtil()
```

------

# 17.19 异常处理

捕获：

```
try:
```

记录：

```
logger.exception()
```

返回：

```
False
```

避免：

程序崩溃。

------

# 17.20 Retry机制

网络异常：

自动：

重试：

```
Retry(
    total=3
)
```

作用：

提高稳定性。

------

# 17.21 企业框架执行流程

```
pytest

↓

test_login

↓

LoginApi

↓

BaseApi

↓

RequestUtil

↓

Session

↓

Response

↓

数据库断言

↓

Allure报告
```

# 18.1 为什么学习 Pytest？

企业自动化：

几乎都是：

```
Pytest
```

已经逐渐替代：

```
unittest
```

原因：

```
简单

灵活

插件丰富

支持参数化

支持 Fixture

支持 Allure

支持并发
```

------

# 18.2 安装 Pytest

安装：

```
pip install pytest
```

查看版本：

```
pytest --version
```

------

# 18.3 编写第一个测试

文件：

```
test_demo.py
```

代码：

```
def test_add():

    assert 1 + 1 == 2
```

运行：

```
pytest
```

结果：

```
1 passed
```

------

# 18.4 Pytest命名规则

### 文件

必须：

```
test_xxx.py
```

或者：

```
*_test.py
```

------

### 类

推荐：

```
class TestLogin:
```

------

### 方法

必须：

```
def test_login():
```

------

否则：

不会执行。

------

# 18.5 assert断言（★★★★★）

判断：

```
assert 1 == 1
```

字符串：

```
assert "成功" == "成功"
```

列表：

```
assert len([1,2]) == 2
```

接口：

```
assert response.status_code == 200
```

JSON：

```
assert response.json()["code"] == 0
```

数据库：

```
assert result
```

------

企业：

95%

都是：

```
assert
```

------

# 18.6 执行指定文件

运行：

```
pytest test_login.py
```

指定类：

```
pytest test_login.py::TestLogin
```

指定方法：

```
pytest test_login.py::TestLogin::test_login
```

------

# 18.7 -v详细模式

运行：

```
pytest -v
```

输出：

```
PASSED

FAILED
```

更加清晰。

------

# 18.8 -s显示print

默认：

```
print()
```

不显示。

运行：

```
pytest -s
```

即可显示。

------

组合：

```
pytest -vs
```

企业最常用。

------

# 18.9 skip（跳过）

导入：

```
import pytest
```

跳过：

```
@pytest.mark.skip
def test_login():
    pass
```

结果：

```
SKIPPED
```

------

指定原因：

```
@pytest.mark.skip(

    reason="功能未完成"

)
```

------

# 18.10 skipif

条件跳过：

```
@pytest.mark.skipif(

    1 == 1,

    reason="跳过"

)
```

满足条件：

跳过。

------

企业应用：

```
Windows

Linux

不同环境
```

------

# 18.11 xfail（预期失败）

代码：

```
@pytest.mark.xfail
def test_demo():

    assert 1 == 2
```

结果：

```
XFAIL
```

不会影响整体结果。

------

应用：

```
已知Bug

等待开发修复
```

------

# 18.12 marker（★★★★★）

标签：

```
@pytest.mark.smoke
```

示例：

```
@pytest.mark.smoke
def test_login():
    pass
```

运行：

```
pytest -m smoke
```

执行：

```
冒烟测试
```

------

企业常用：

```
@pytest.mark.smoke

@pytest.mark.regression

@pytest.mark.api

@pytest.mark.ui
```

------

# 18.13 parametrize（★★★★★）

参数化：

```
@pytest.mark.parametrize(

"username,password",

[
("admin","123456"),

("Tom","111111")

]

)
```

函数：

```
def test_login(

username,

password

):

    pass
```

执行：

2次。

------

企业：

大量使用。

------

# 18.14 ids

美化名称：

```
@pytest.mark.parametrize(

"username,password",

[

("admin","123456"),

("Tom","111")

],

ids=[

"管理员",

"普通用户"

]

)
```

报告：

更加友好。

------

# 18.15 setup_method

每个方法执行前：

```
def setup_method(

self

):

    print("开始")
```

执行后：

```
def teardown_method(

self

):

    print("结束")
```

------

流程：

```
setup

↓

test

↓

teardown
```

------

# 18.16 setup_class

类开始：

```
setup_class()
```

类结束：

```
teardown_class()
```

执行一次。

------

# 18.17 pytest.main()

代码执行：

```
pytest.main(

["-vs"]

)
```

代替：

cmd。

------

# 18.18 conftest.py（★★★★★）

作用：

共享：

```
fixture

hook

配置
```

文件：

```
conftest.py
```

特点：

```
自动发现

无需import
```

------

企业：

必备。

------

# 18.19 pytest.ini

配置：

```
[pytest]

addopts=-vs
```

作用：

默认：

```
-vs
```

------

marker：

注册：

```
markers=

    smoke

    regression
```

避免：

警告。

------

# 18.20 pytest-html

安装：

```
pip install pytest-html
```

生成：

```
pytest

--html=report.html
```

生成：

```
HTML报告
```

------

企业：

更多：

```
Allure
```

------

# 18.21 执行失败重跑

安装：

```
pip install pytest-rerunfailures
```

执行：

```
pytest

--reruns 3
```

失败：

自动重跑。

------

# 18.22 并发执行

安装：

```
pip install pytest-xdist
```

执行：

```
pytest -n 4
```

4线程。

------

企业：

常用。

------

# 企业项目目录

```
TestCase

├── test_login.py

├── test_order.py

conftest.py

pytest.ini
```

------

# 19.1 为什么需要 Fixture？

以前（unittest）：

```
setUp()

tearDown()
```

存在问题：

```
耦合严重

复用性差

无法跨文件共享
```

------

Pytest：

使用：

```
fixture
```

实现：

```
资源管理

数据共享

前后置

依赖注入
```

------

企业：

```
95%

都在使用 Fixture
```

------

# 19.2 第一个 Fixture

导入：

```
import pytest
```

定义：

```
@pytest.fixture()
def login():

    print("登录")
```

使用：

```
def test_order(

        login

):

    print("下单")
```

输出：

```
登录

下单
```

------

思想：

```
依赖注入
```

不是：

主动调用。

------

# 19.3 返回数据

fixture：

```
@pytest.fixture()
def token():

    return "abcdef"
```

测试：

```
def test_user(

        token

):

    print(token)
```

输出：

```
abcdef
```

------

应用：

```
token

driver

数据库连接

session
```

------

# 19.4 多个 Fixture

```
@pytest.fixture()
def login():
    pass


@pytest.fixture()
def token():
    pass
```

使用：

```
def test_order(

login,

token

):
    pass
```

执行：

```
login

↓

token

↓

test
```

------

# 19.5 Scope（★★★★★）

作用：

控制：

```
生命周期
```

参数：

```
scope=
```

支持：

```
function

class

module

package

session
```

------

# function

默认：

每个方法执行一次。

```
@pytest.fixture(

scope="function"

)
```

------

# class

每个类执行一次。

```
scope="class"
```

------

# module

一个文件一次。

```
scope="module"
```

------

# session（★★★★★）

整个项目：

执行一次。

```
scope="session"
```

应用：

```
浏览器

数据库

token

session
```

企业最常用。

------

# 19.6 yield（★★★★★）

以前：

```
return
```

只能返回。

------

推荐：

```
@pytest.fixture()
def login():

    print("开始")

    yield

    print("结束")
```

执行：

```
开始

↓

test

↓

结束
```

------

作用：

实现：

```
前置

+

后置
```

------

# Selenium应用

```
@pytest.fixture()
def driver():

    driver = Chrome()

    yield driver

    driver.quit()
```

------

# 19.7 conftest.py（★★★★★）

作用：

共享 Fixture。

目录：

```
Project

│

conftest.py
```

定义：

```
@pytest.fixture()
def driver():
    pass
```

测试：

```
def test_login(

driver

):
    pass
```

无需：

```
import
```

------

企业：

所有 fixture：

都放：

```
conftest.py
```

------

# 19.8 autouse

自动执行：

```
@pytest.fixture(

autouse=True

)
```

示例：

```
@pytest.fixture(

autouse=True

)

def init():

    print("开始")
```

每个用例：

自动执行。

------

应用：

```
日志

截图

初始化
```

------

# 19.9 request对象

获取：

测试方法。

```
@pytest.fixture()
def demo(

request

):

    print(

request.node.name

)
```

结果：

```
test_login
```

------

用途：

```
动态数据

方法名

参数
```

------

# 19.10 Fixture依赖

fixture：

调用 fixture。

```
@pytest.fixture()
def token():
    return "abc"


@pytest.fixture()
def login(

token

):

    return token
```

关系：

```
token

↓

login

↓

test
```

------

企业大量使用。

------

# 19.11 Fixture缓存

同一个方法：

```
login
```

只执行：

一次。

例如：

```
def test_demo(

login,

login

)
```

实际：

执行：

一次。

------

提高效率。

------

# 19.12 params参数化

fixture：

支持：

```
@pytest.fixture(

params=[

"admin",

"Tom"

]

)
```

使用：

```
def test_login(

request

):

    print(

request.param

)
```

执行：

两次。

------

# 19.13 request.param

获取：

参数。

```
@pytest.fixture(

params=[1,2]

)

def data(

request

):

    return request.param
```

------

测试：

```
def test_demo(

data

):

    print(data)
```

输出：

```
1

2
```

------

# 19.14 Fixture工厂

返回：

函数。

```
@pytest.fixture()
def login():

    def inner(

username,

password

):
        pass

    return inner
```

调用：

```
def test_demo(

login

):

    login(

        "admin",

        "123456"

    )
```

------

应用：

动态数据。

------

# 19.15 浏览器管理（★★★★★）

企业：

```
@pytest.fixture(

scope="session"

)

def driver():

    driver = Chrome()

    yield driver

    driver.quit()
```

整个项目：

一个浏览器。

------

流程：

```
Chrome

↓

yield

↓

TestCase

↓

quit()
```

------

# 19.16 Session管理

接口：

```
@pytest.fixture(

scope="session"

)

def session():

    s = requests.Session()

    yield s

    s.close()
```

整个项目：

共享：

```
Session()
```

------

# 19.17 数据库连接管理

```
@pytest.fixture(

scope="session"

)

def mysql():

    conn = pymysql.connect()

    yield conn

    conn.close()
```

------

企业：

推荐：

session。

------

# 19.18 Redis连接管理

```
@pytest.fixture(

scope="session"

)

def redis_conn():

    yield Redis()
```

整个项目：

一个连接。

------

# 19.19 Fixture + Selenium

```
driver
```

↓

页面对象：

```
LoginPage
```

↓

TestCase

结构：

```
fixture

↓

driver

↓

page

↓

test
```

------

# 19.20 Fixture + BasePage

```
@pytest.fixture()
def login_page(

driver

):

    return LoginPage(

        driver

    )
```

测试：

```
def test_login(

login_page

):
    pass
```

实现：

依赖注入。

------

## 企业目录（★★★★★）

```
Project

│

conftest.py

│

Page

│

Locator

│

Common

│

TestCase
```

# 20.1 为什么使用 Allure？

很多初学者使用：

```
HTMLTestRunner
pytest-html
```

这些报告只能展示：

```
测试结果

PASS

FAIL
```

企业更关注：

```
测试步骤

请求参数

响应结果

失败原因

截图

日志

环境信息

历史趋势
```

所以：

```
企业自动化

↓

Pytest

+

Allure
```

几乎已经成为标准配置。

------

# 20.2 安装 Allure

安装 Python 插件：

```
pip install allure-pytest
```

安装 Allure Commandline（需单独安装）。

检查版本：

```
allure --version
```

------

# 20.3 生成 Allure 数据

执行：

```
pytest

--alluredir=./report/xml
```

生成：

```
report

└── xml

    *.json

    *.txt

    *.attachment
```

注意：

这里生成的是：

```
原始数据
```

不是 HTML。

------

# 20.4 生成 HTML 报告

执行：

```
allure generate

./report/xml

-o

./report/html

--clean
```

生成：

```
report

├── html
```

打开：

```
allure open

./report/html
```

浏览器即可查看。

------

# 20.5 title（★★★★★）

默认：

```
test_login
```

不好看。

使用：

```
import allure


@allure.title(

    "用户登录"

)
def test_login():
    pass
```

报告：

显示：

```
用户登录
```

------

# 20.6 description

添加说明：

```
@allure.description(

    "验证用户名密码登录"

)
```

报告：

可以看到：

```
详细描述
```

------

# 20.7 feature（★★★★★）

表示：

```
模块
```

例如：

```
@allure.feature(

    "登录模块"

)
```

企业：

```
登录

订单

支付

购物车

用户中心
```

------

# 20.8 story

表示：

```
功能点
```

例如：

```
@allure.story(

    "账号密码登录"

)
```

关系：

```
登录模块

↓

账号密码登录
```

------

# 20.9 severity（★★★★★）

表示：

```
Bug等级
```

例如：

```
@allure.severity(

allure.severity_level.CRITICAL

)
```

支持：

```
BLOCKER

CRITICAL

NORMAL

MINOR

TRIVIAL
```

企业：

用于：

```
缺陷优先级
```

------

# 20.10 tag

标签：

```
@allure.tag(

"api"

)
```

多个：

```
@allure.tag(

"smoke",

"login"

)
```

报告：

支持：

```
筛选
```

------

# 20.11 step（★★★★★）

以前：

日志：

```
登录

查询

退出
```

不直观。

使用：

```
with allure.step(

"输入账号"

):
    pass
```

多个：

```
with allure.step(

"输入密码"

):
    pass
with allure.step(

"点击登录"

):
    pass
```

报告：

形成：

```
输入账号

↓

输入密码

↓

点击登录
```

企业：

大量使用。

------

# 20.12 attach 文本

添加：

```
allure.attach(

"登录成功",

"响应结果"

)
```

报告：

点击：

即可查看。

------

# 20.13 attach JSON（★★★★★）

接口：

返回：

```
res = {

"code":0,

"msg":"成功"

}
```

添加：

```
import json

allure.attach(

json.dumps(

res,

indent=4,

ensure_ascii=False

),

"响应JSON"

)
```

报告：

可直接查看：

JSON。

------

# 20.14 attach 图片

例如：

```
driver.save_screenshot(

"a.png"

)
```

添加：

```
allure.attach.file(

"a.png",

attachment_type=

allure.attachment_type.PNG

)
```

报告：

显示：

截图。

------

# 20.15 attach 日志

日志：

```
logger.info(

"登录成功"

)
```

添加：

```
allure.attach.file(

"log.txt"
)
```

企业：

常见。

------

# 20.16 Selenium失败截图（★★★★★）

失败：

自动：

截图。

```
try:

    assert False

except:

    driver.save_screenshot(

        "fail.png"

    )

    raise
```

报告：

自动：

查看：

失败页面。

------

# 20.17 environment.properties

目录：

```
report

└── environment.properties
```

内容：

```
Browser=Chrome

OS=Windows11

Python=3.12

Env=Test
```

报告：

显示：

```
环境信息
```

------

# 20.18 executor.json

记录：

```
Jenkins

Git

Build

Branch
```

例如：

```
{
"buildName":"Build001",

"buildUrl":"http://jenkins"

}
```

企业：

CI/CD：

使用。

------

# 20.19 categories.json

自定义：

Bug分类。

例如：

```
AssertionError

↓

断言失败
TimeoutException

↓

超时
```

报告：

自动：

统计：

Bug类型。

------

# 20.20 History Trend（★★★★★）

保存：

```
history
```

目录：

下次：

复制：

即可。

效果：

```
历史趋势

通过率

失败率
```

企业：

持续集成：

必须。

------

# 20.21 Jenkins集成

流程：

```
Git

↓

Jenkins

↓

Pytest

↓

Allure

↓

HTML报告
```

最终：

自动：

发送：

```
邮件

企业微信

钉钉
```

------

# 20.22 Allure + Selenium

步骤：

```
打开浏览器

↓

登录

↓

搜索

↓

截图

↓

关闭浏览器
```

全部：

记录：

报告。

------

# 20.23 Allure + 接口自动化

请求：

```
URL
```

↓

Header

↓

Body

↓

Response

↓

数据库断言

↓

Redis断言

全部：

attach。

# 21.1 为什么学习 Docker？

传统开发：

```
开发电脑
↓

可以运行

↓

测试电脑

↓

不能运行

↓

生产环境

↓

又不能运行
```

原因：

```
环境不同
```

例如：

```
Python版本不同

Chrome版本不同

驱动版本不同

依赖库不同
```

Docker：

```
应用

+

运行环境

+

依赖

↓

打包

↓

任何电脑都能运行
```

一句话：

> Docker = 一次构建，到处运行（Build Once, Run Anywhere）

------

# 21.2 Docker 核心概念（★★★★★）

Docker 有四个核心概念：

```
Image（镜像）

↓

Container（容器）

↓

Volume（数据卷）

↓

Network（网络）
```

关系：

```
Image

↓

启动

↓

Container
```

类似：

```
Image

≈

Python 类（Class）

Container

≈

对象（Object）
```

------

# 21.3 安装 Docker

Windows：

安装：

```
Docker Desktop
```

Linux：

```
sudo apt install docker.io
```

查看版本：

```
docker --version
```

查看是否运行：

```
docker info
```

------

# 21.4 Image（镜像）

查看：

```
docker images
```

例如：

```
REPOSITORY     TAG

python         3.12

mysql          8.0

redis          latest

nginx          latest
```

下载：

```
docker pull python:3.12
```

下载最新版：

```
docker pull redis
```

------

# 21.5 Container（容器）

启动：

```
docker run hello-world
```

查看：

```
docker ps
```

查看全部：

```
docker ps -a
```

停止：

```
docker stop 容器ID
```

启动：

```
docker start 容器ID
```

删除：

```
docker rm 容器ID
```

------

# 21.6 常用 docker run 参数（★★★★★）

后台运行：

```
docker run -d nginx
```

映射端口：

```
docker run -p 8080:80 nginx
```

命名：

```
docker run --name redis redis
```

挂载目录：

```
docker run -v D:\Project:/app python
```

进入容器：

```
docker exec -it 容器ID bash
```

------

# 21.7 Volume（数据卷）

为什么需要？

容器删除：

```
数据库

↓

数据丢失
```

解决：

Volume。

创建：

```
docker volume create mysql-data
```

挂载：

```
docker run

-v mysql-data:/var/lib/mysql
```

企业：

```
MySQL

Redis

Jenkins
```

都必须使用数据卷。

------

# 21.8 Network（网络）

查看：

```
docker network ls
```

创建：

```
docker network create auto-test
```

运行：

```
docker run

--network auto-test
```

作用：

多个容器：

可以互相通信。

------

# 21.9 Dockerfile（★★★★★）

作用：

自动构建镜像。

例如：

```
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["pytest"]
```

构建：

```
docker build

-t auto-test .
```

启动：

```
docker run auto-test
```

------

# 21.10 COPY 与 ADD

COPY：

```
COPY . .
```

复制文件。

------

ADD：

```
ADD test.zip .
```

支持：

```
解压

URL
```

企业：

推荐：

```
COPY
```

------

# 21.11 CMD 与 ENTRYPOINT

CMD：

```
CMD ["pytest"]
```

运行：

```
docker run image
```

执行：

```
pytest
```

------

ENTRYPOINT：

固定执行。

企业：

更多：

```
CMD
```

------

# 21.12 ENV

设置环境变量：

```
ENV ENV=test
```

Python：

```
import os

os.getenv("ENV")
```

企业：

用于：

```
dev

test

pre

prod
```

环境切换。

------

# 21.13 Docker Compose（★★★★★）

为什么需要？

以前：

启动：

```
MySQL

Redis

Python

Jenkins
```

需要：

四个命令。

Compose：

一个命令。

------

安装：

```
docker compose version
```

------

# 21.14 docker-compose.yml

示例：

```
version: "3"

services:

  mysql:

    image: mysql:8

  redis:

    image: redis

  test:

    build: .
```

启动：

```
docker compose up
```

后台：

```
docker compose up -d
```

关闭：

```
docker compose down
```

------

# 21.15 部署 Python 自动化项目

目录：

```
Project

Dockerfile

docker-compose.yml

requirements.txt
```

Dockerfile：

```
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["pytest","-vs"]
```

启动：

```
docker compose up
```

自动：

执行：

Pytest。

------

# 21.16 Selenium Grid（★★★★★）

企业：

UI自动化：

不用：

本地浏览器。

流程：

```
Pytest

↓

RemoteDriver

↓

Selenium Grid

↓

Chrome

↓

Firefox

↓

Edge
```

优点：

```
远程执行

并发执行

跨浏览器
```

------

# 21.17 Jenkins + Docker

流程：

```
Git Pull

↓

Docker Build

↓

Docker Run

↓

Pytest

↓

Allure

↓

邮件通知
```

企业：

CI/CD：

标准流程。

------

# 21.18 查看日志

查看：

```
docker logs 容器ID
```

实时：

```
docker logs -f 容器ID
```

企业：

排查：

Bug。

------

# 21.19 进入容器

进入：

```
docker exec

-it

容器ID

bash
```

Ubuntu：

进入：

Shell。

------

# 21.20 删除资源

删除容器：

```
docker rm 容器ID
```

删除镜像：

```
docker rmi image
```

删除未使用：

```
docker system prune
```

注意：

生产环境：

谨慎执行。

# 22.1 为什么测试工程师要学习 FastAPI？

很多人认为：

```
测试工程师

↓

只会调用接口
```

实际上企业更希望：

```
测试工程师

↓

自己开发接口

↓

自己搭建Mock服务

↓

自己构造测试数据

↓

自己开发测试工具
```

FastAPI 是目前 Python 最流行的 Web 框架之一：

```
Flask

↓

Django

↓

FastAPI（推荐）
```

优点：

```
性能高

开发快

自动生成接口文档

类型提示完善

易于测试
```

------

# 22.2 安装 FastAPI

安装：

```
pip install fastapi
```

安装 Web 服务：

```
pip install uvicorn
```

启动：

```
uvicorn main:app --reload
```

参数说明：

- `main`：Python 文件名
- `app`：FastAPI 实例
- `--reload`：代码修改后自动重启

------

# 22.3 第一个 FastAPI 项目

创建：

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "Hello FastAPI"}
```

启动后访问：

```
http://127.0.0.1:8000/
```

返回：

```
{
    "msg": "Hello FastAPI"
}
```

------

# 22.4 自动接口文档（★★★★★）

FastAPI 自动生成 Swagger 文档。

访问：

```
http://127.0.0.1:8000/docs
```

还支持：

```
/redoc
```

企业价值：

```
前后端联调

测试调试

接口验证
```

无需手写接口文档。

------

# 22.5 GET 请求

示例：

```
@app.get("/user")
def get_user():
    return {"name": "Tom"}
```

浏览器：

```
GET /user
```

返回：

```
{
    "name":"Tom"
}
```

------

# 22.6 Query 参数

例如：

```
/user?id=1
```

代码：

```
@app.get("/user")
def get_user(id: int):
    return {"id": id}
```

访问：

```
/user?id=100
```

返回：

```
{
    "id":100
}
```

------

# 22.7 Path 参数

URL：

```
/user/100
```

代码：

```
@app.get("/user/{id}")
def get_user(id: int):
    return {"id": id}
```

返回：

```
{
    "id":100
}
```

------

# 22.8 POST 请求（★★★★★）

提交 JSON：

```
{
    "username":"admin",
    "password":"123456"
}
```

创建模型：

```
from pydantic import BaseModel

class Login(BaseModel):
    username: str
    password: str
```

接口：

```
@app.post("/login")
def login(data: Login):
    return data
```

------

# 22.9 Pydantic 数据模型（★★★★★）

作用：

```
自动校验

自动转换

自动生成文档
```

示例：

```
class User(BaseModel):

    id: int

    name: str

    age: int
```

如果：

```
age="abc"
```

FastAPI：

自动返回：

```
422 Validation Error
```

------

# 22.10 Body 参数

读取请求体：

```
from fastapi import Body

@app.post("/login")
def login(
    username: str = Body(),
    password: str = Body()
):
    return username
```

企业：

更多使用：

```
Pydantic
```

------

# 22.11 PUT 请求

更新：

```
@app.put("/user/{id}")
def update_user(id: int):
    return {"id": id}
```

RESTful：

```
PUT

更新资源
```

------

# 22.12 DELETE 请求

删除：

```
@app.delete("/user/{id}")
def delete_user(id: int):
    return {"msg": "删除成功"}
```

------

# 22.13 Response Model（★★★★★）

返回模型：

```
class User(BaseModel):

    id:int

    name:str
```

接口：

```
@app.get(
"/user",
response_model=User
)
```

优点：

```
统一返回格式

自动过滤字段
```

------

# 22.14 文件上传

安装：

```
pip install python-multipart
```

接口：

```
from fastapi import UploadFile

@app.post("/upload")
async def upload(file: UploadFile):
    return {"filename": file.filename}
```

企业：

用于：

```
Excel

图片

附件
```

------

# 22.15 文件下载

返回：

```
FileResponse()
```

企业：

下载：

```
Excel

PDF

报告
```

------

# 22.16 JWT 登录认证（★★★★★）

登录：

成功：

生成：

```
JWT Token
```

请求：

Header：

```
Authorization

Bearer Token
```

验证：

Token。

企业：

接口：

基本都使用：

```
JWT
```

------

# 22.17 SQLAlchemy 数据库

安装：

```
pip install sqlalchemy
```

连接：

```
engine=create_engine(...)
```

操作：

```
CRUD
```

企业：

ORM：

标准方案。

------

# 22.18 FastAPI + MySQL

流程：

```
FastAPI

↓

SQLAlchemy

↓

MySQL
```

接口：

直接：

查询数据库。

------

# 22.19 Pytest 测试 FastAPI（★★★★★）

官方：

提供：

```
TestClient
```

示例：

```
from fastapi.testclient import TestClient

client=TestClient(app)

def test_login():

    res=client.get("/")

    assert res.status_code==200
```

无需：

启动：

浏览器。

------

# 22.20 Mock 服务（★★★★★）

企业：

经常：

前端：

未完成。

接口：

不存在。

解决：

FastAPI：

快速：

开发：

Mock。

例如：

```
@app.get("/order")
```

返回：

模拟数据。

# 23.1 为什么学习 Playwright？（★★★★★）

近几年企业 UI 自动化发生了很大的变化：

```
Selenium
      ↓
Playwright
```

越来越多的大厂开始使用：

- Microsoft（Playwright 官方）
- 字节跳动
- 美团
- 腾讯部分业务
- 小米
- Shopee
- Lazada

原因：

```
稳定

速度快

自动等待

支持多浏览器

支持录制

支持Trace调试

支持API测试
```

------

# 23.2 Selenium 与 Playwright 对比（★★★★★）

| 对比项      | Selenium    | Playwright  |
| ----------- | ----------- | ----------- |
| 浏览器驱动  | 需要 Driver | 无需 Driver |
| 自动等待    | ❌ 基本没有  | ✅ 内置      |
| 执行速度    | 一般        | 很快        |
| 定位方式    | WebElement  | Locator     |
| 多标签      | 较复杂      | 简单        |
| Network监听 | 较弱        | 很强        |
| Trace调试   | 无          | 支持        |
| 稳定性      | 一般        | 很高        |

企业趋势：

```
老项目：

Selenium

新项目：

Playwright
```

------

# 23.3 安装 Playwright

安装：

```
pip install playwright
```

安装浏览器：

```
playwright install
```

查看版本：

```
playwright --version
```

------

# 23.4 第一个 Playwright 程序

```
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.baidu.com")

    browser.close()
```

运行后：

浏览器自动打开。

------

# 23.5 三大核心对象（★★★★★）

Playwright：

最重要三个对象：

```
Browser

↓

BrowserContext

↓

Page
```

关系：

```
Browser

↓

多个Context

↓

多个Page
```

------

Browser：

浏览器。

例如：

```
browser = p.chromium.launch()
```

------

Context：

浏览器环境。

类似：

```
无痕模式
```

多个用户：

互不影响。

------

Page：

网页。

例如：

```
page.goto(...)
```

------

# 23.6 Locator（★★★★★）

Selenium：

```
find_element()
```

Playwright：

```
locator()
```

例如：

```
page.locator("#username")
```

支持：

```
CSS

XPath

Text

Role

Placeholder

Label
```

推荐：

```
Locator
```

------

# 23.7 元素操作

输入：

```
page.locator("#user").fill("admin")
```

点击：

```
page.locator("#login").click()
```

获取文本：

```
text = page.locator(".title").text_content()
```

清空：

```
.fill("")
```

------

# 23.8 自动等待（★★★★★）

这是 Playwright 最大优势。

Selenium：

```
time.sleep(3)
```

或者：

```
WebDriverWait()
```

Playwright：

```
page.locator("#login").click()
```

自动等待：

```
元素出现

元素可点击

动画结束
```

无需：

```
sleep()
```

------

# 23.9 页面等待

等待URL：

```
page.wait_for_url()
```

等待元素：

```
page.wait_for_selector()
```

等待加载完成：

```
page.wait_for_load_state()
```

企业：

大量使用。

------

# 23.10 鼠标操作

双击：

```
locator.dblclick()
```

右键：

```
locator.click(button="right")
```

悬停：

```
locator.hover()
```

拖拽：

```
locator.drag_to()
```

------

# 23.11 键盘操作

回车：

```
page.keyboard.press("Enter")
```

组合键：

```
page.keyboard.press("Control+A")
```

复制：

```
page.keyboard.press("Control+C")
```

------

# 23.12 多标签页（★★★★★）

打开：

```
new_page = context.new_page()
```

监听：

```
with context.expect_page():
```

切换：

```
new_page.bring_to_front()
```

企业：

支付：

广告：

OAuth登录：

大量使用。

------

# 23.13 文件上传

```
page.set_input_files(
    "#upload",
    "a.png"
)
```

无需：

操作：

Windows文件框。

------

# 23.14 文件下载

监听：

```
with page.expect_download():
```

保存：

```
download.save_as()
```

------

# 23.15 浏览器截图

整个页面：

```
page.screenshot(
    path="page.png"
)
```

元素：

```
locator.screenshot()
```

企业：

失败：

自动截图。

------

# 23.16 视频录制

Context：

开启：

```
record_video_dir
```

自动：

保存：

视频。

企业：

Bug复现。

------

# 23.17 Network监听（★★★★★）

监听：

接口：

```
page.on("request")
```

监听：

响应：

```
page.on("response")
```

企业：

验证：

```
请求

Header

Body

Response
```

------

# 23.18 Route Mock

拦截：

接口：

```
page.route()
```

返回：

模拟数据。

企业：

Mock：

测试。

------

# 23.19 Trace Viewer（★★★★★）

开启：

```
context.tracing.start()
```

结束：

```
context.tracing.stop()
```

生成：

```
trace.zip
```

查看：

```
playwright show-trace trace.zip
```

包含：

```
页面

请求

DOM

Console

截图
```

企业：

定位Bug：

神器。

------

# 23.20 Pytest + Playwright

安装：

```
pip install pytest-playwright
```

Fixture：

```
def test_login(page):
```

直接：

使用：

```
page.goto(...)
```

企业：

推荐。

------

# 23.21 Page Object Model（★★★★★）

目录：

```
Page

LoginPage.py

OrderPage.py
```

BasePage：

统一：

封装。

测试：

```
login.login()
```

与 Selenium：

思想：

一致。

# 24.1 什么是 CI/CD？（★★★★★）

CI：

```
Continuous Integration

持续集成
```

CD：

```
Continuous Delivery

持续交付

或

Continuous Deployment

持续部署
```

企业流程：

```
开发提交代码
        │
        ▼
Git / GitLab
        │
        ▼
Jenkins 自动拉取代码
        │
        ▼
自动安装依赖
        │
        ▼
执行 Pytest
        │
        ▼
生成 Allure 报告
        │
        ▼
发送通知
```

优点：

```
减少人工操作

快速反馈

持续验证质量

自动发布
```

------

# 24.2 为什么自动化测试需要 Jenkins？

没有 Jenkins：

```
人工打开项目

↓

执行 pytest

↓

生成报告

↓

发送报告
```

有 Jenkins：

```
代码提交

↓

自动执行

↓

自动报告

↓

自动通知
```

真正做到：

```
无人值守
```

------

# 24.3 安装 Jenkins

Docker 推荐方式：

```
docker run -d \
-p 8080:8080 \
-p 50000:50000 \
--name jenkins \
jenkins/jenkins:lts
```

访问：

```
http://localhost:8080
```

首次启动：

需要：

```
Admin Password
```

------

# 24.4 Jenkins 插件（★★★★★）

企业常用插件：

```
Git

GitLab

Pipeline

Allure

Docker

Email Extension

Workspace Cleanup

Parameterized Trigger
```

建议：

安装：

```
Suggested Plugins
```

------

# 24.5 创建第一个 Job

创建：

```
New Item

↓

Freestyle Project
```

配置：

```
源码

↓

构建

↓

构建后操作
```

点击：

```
Build Now
```

------

# 24.6 Git 集成（★★★★★）

源码管理：

选择：

```
Git
```

填写：

```
Repository URL
```

例如：

```
https://github.com/xxx/project.git
```

配置：

```
Branch

main

master

develop
```

企业：

一般：

```
GitLab
```

------

# 24.7 执行 Pytest

构建步骤：

```
Execute Shell

或

Execute Windows Batch
```

例如：

```
pytest -vs
```

生成：

自动：

测试结果。

------

# 24.8 Allure 集成（★★★★★）

Pytest：

```
pytest

--alluredir=Report/allure-result
```

构建后：

选择：

```
Allure Report
```

目录：

```
Report/allure-result
```

构建完成：

即可查看：

HTML 报告。

------

# 24.9 参数化构建

开启：

```
This project is parameterized
```

添加：

```
ENV

DEV

TEST

PRE

PROD
```

Python：

读取：

```
os.getenv("ENV")
```

企业：

非常常见。

------

# 24.10 定时执行（★★★★★）

Build periodically：

Cron：

```
H 2 * * *
```

表示：

```
每天凌晨2点
```

例如：

每天：

执行：

回归测试。

------

# 24.11 Pipeline（★★★★★）

企业：

越来越多：

使用：

```
Pipeline
```

代替：

Freestyle。

原因：

```
代码化

版本管理

易维护
```

------

# 24.12 Jenkinsfile

示例：

```
pipeline {

    agent any

    stages {

        stage('Install') {

            steps {

                sh 'pip install -r requirements.txt'

            }

        }

        stage('Test') {

            steps {

                sh 'pytest -vs'

            }

        }

    }

}
```

放入：

```
项目根目录
```

------

# 24.13 多阶段流水线

流程：

```
Checkout

↓

Install

↓

Pytest

↓

Allure

↓

Archive

↓

Notify
```

每一步：

都是：

一个 Stage。

------

# 24.14 Docker 集成（★★★★★）

流程：

```
Git Pull

↓

Docker Build

↓

Docker Run

↓

Pytest

↓

Allure
```

示例：

```
sh 'docker compose up --build'
```

企业：

推荐。

------

# 24.15 多环境执行

例如：

```
DEV

↓

TEST

↓

PRE

↓

PROD
```

Pipeline：

读取：

环境变量。

自动：

切换：

配置。

------

# 24.16 邮件通知

插件：

```
Email Extension
```

配置：

SMTP。

执行完成：

自动：

发送：

```
Allure 报告

日志

附件
```

------

# 24.17 企业微信 / 钉钉通知

构建完成：

发送：

```
构建结果

执行时间

通过率

报告地址
```

企业：

普遍使用。

------

# 24.18 自动清理工作区

插件：

```
Workspace Cleanup
```

作用：

```
删除缓存

删除历史文件
```

避免：

磁盘：

越来越大。

------

# 24.19 Jenkins 权限管理

企业：

角色：

```
管理员

开发

测试

产品
```

配置：

不同：

权限。

------

# 24.20 企业自动化平台架构（★★★★★）

整体流程：

```
Git / GitLab
        │
        ▼
Jenkins
        │
        ▼
Docker
        │
        ▼
Pytest
        │
        ▼
Allure
        │
        ▼
邮件/企业微信/钉钉
```

这是目前互联网企业最常见的自动化测试平台架构。

# 25.1 企业自动化框架为什么要分层？（★★★★★）

很多初学者的自动化脚本是这样的：

```
driver.find_element(...).send_keys(...)
driver.find_element(...).click()
assert ...
```

问题：

- 定位重复
- 代码冗余
- 页面改版需要修改大量脚本
- 不利于多人协作
- 难以维护

企业采用分层架构：

```
TestCase（测试用例）
        │
        ▼
Page（页面对象）
        │
        ▼
Base（基础封装）
        │
        ▼
Driver（浏览器驱动）
```

接口自动化同样如此：

```
TestCase
      │
      ▼
Api
      │
      ▼
RequestUtil
      │
      ▼
Requests
```

------

# 25.2 企业级项目目录（★★★★★）

建议目录如下：

```
AutoTestProject
│
├── Config                 # 配置文件
│   ├── config.yaml
│   └── env.py
│
├── Common                 # 公共工具
│   ├── logger.py
│   ├── yaml_util.py
│   ├── mysql_util.py
│   ├── redis_util.py
│   ├── request_util.py
│   └── screenshot.py
│
├── Base                   # 基础封装
│   ├── base_page.py
│   ├── base_api.py
│   └── driver.py
│
├── Page                   # 页面对象
│
├── Api                    # 接口对象
│
├── Locator                # 页面元素
│
├── Data                   # 测试数据
│
├── TestCase               # 测试用例
│   ├── UI
│   └── API
│
├── Report
│   ├── allure-result
│   └── allure-report
│
├── Log
│
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── pytest.ini
├── conftest.py
└── requirements.txt
```

------

# 25.3 BasePage 设计（★★★★★）

所有页面继承 `BasePage`。

负责封装：

```
打开页面
定位元素
点击
输入
获取文本
等待
截图
执行 JavaScript
```

示例：

```
class BasePage:

    def click(self, locator):
        ...

    def input(self, locator, text):
        ...

    def get_text(self, locator):
        ...

    def screenshot(self):
        ...
```

原则：

> 页面只负责业务，不负责底层实现。

------

# 25.4 Page Object（PO）模式（★★★★★）

例如登录页面：

```
LoginPage
```

只提供业务方法：

```
login(username, password)
```

而不是：

```
find_element(...)
click(...)
```

测试代码：

```
login_page.login("admin", "123456")
```

优点：

- 可读性高
- 页面改版影响小
- 易维护

------

# 25.5 BaseApi 设计

接口自动化也需要封装：

```
class BaseApi:

    def get(self):
        ...

    def post(self):
        ...

    def put(self):
        ...

    def delete(self):
        ...
```

业务接口：

```
class LoginApi(BaseApi):
    pass
```

测试代码：

```
login_api.login()
```

------

# 25.6 配置管理（★★★★★）

企业不会把配置写死。

推荐：

```
test:
  base_url: http://test.xxx.com

pre:
  base_url: http://pre.xxx.com

prod:
  base_url: http://xxx.com
```

通过环境变量切换：

```
ENV=test
```

Python：

```
os.getenv("ENV")
```

------

# 25.7 日志管理

统一封装：

```
logger.py
```

支持：

- INFO
- WARNING
- ERROR
- DEBUG

日志格式：

```
时间

模块

线程

日志等级

内容
```

不要：

```
print()
```

------

# 25.8 数据驱动（★★★★★）

推荐：

```
YAML

Excel

JSON
```

例如：

```
login_success:

 username: admin

 password: 123456
```

Pytest：

```
@pytest.mark.parametrize(...)
```

------

# 25.9 Fixture 统一管理

所有 Fixture：

统一放：

```
conftest.py
```

例如：

```
browser()

login()

db()

redis()

token()
```

避免：

重复代码。

------

# 25.10 MySQL 数据断言（★★★★★）

不仅验证接口返回：

还验证数据库：

```
接口返回成功

↓

数据库是否新增数据
```

例如：

```
select * from user
where id=1;
```

自动：

断言。

------

# 25.11 Redis 数据断言

例如：

登录：

接口：

成功。

验证：

Redis：

```
Token

Session

验证码

缓存
```

是否正确。

------

# 25.12 Allure 集成

失败：

自动：

```
截图

日志

请求

响应

SQL

Redis
```

全部：

Attach。

------

# 25.13 Docker 部署

整个项目：

```
docker compose up
```

即可：

启动：

```
MySQL

Redis

自动化测试
```

------

# 25.14 Jenkins 集成

流程：

```
Git Push
      │
      ▼
Jenkins
      │
      ▼
Docker
      │
      ▼
Pytest
      │
      ▼
Allure
      │
      ▼
邮件通知
```

无人值守。

------

# 25.15 企业自动化执行流程（★★★★★）

完整流程：

```
开发提交代码
        │
        ▼
GitLab
        │
        ▼
Jenkins
        │
        ▼
Docker Compose
        │
        ▼
启动测试环境
        │
        ▼
执行 UI 自动化
        │
        ▼
执行接口自动化
        │
        ▼
数据库断言
        │
        ▼
Redis 断言
        │
        ▼
生成 Allure 报告
        │
        ▼
发送邮件 / 企业微信
```

------

# 25.16 企业综合项目（★★★★★）

项目：

**电商平台自动化测试**

模块：

```
登录

用户中心

商品

购物车

订单

支付

优惠券

退款

售后

积分

会员
```

覆盖：

- UI 自动化
- 接口自动化
- 数据库验证
- Redis 验证
- Allure 报告
- Jenkins 持续集成

------

# 25.17 企业开发规范

统一遵循：

- PEP8 编码规范
- Git Flow 分支管理
- Code Review
- 日志规范
- 配置分离
- 数据与代码分离
- 公共方法统一封装

------

# 25.18 性能优化

提升执行效率：

- 使用 Fixture 复用浏览器
- Pytest 并行执行（xdist）
- Headless 模式
- Selenium Grid / Playwright 多浏览器
- Docker 隔离环境

------

# 25.19 简历项目描述（★★★★★）

项目名称：

> 企业级电商自动化测试平台

项目职责：

- 基于 Python + Pytest + Selenium 搭建 UI 自动化框架
- 基于 Requests + Pytest 搭建接口自动化框架
- 封装 BasePage、BaseApi、RequestUtil
- 集成 MySQL、Redis 数据断言
- 使用 YAML 实现数据驱动
- 使用 Allure 生成测试报告
- 使用 Docker 容器化部署
- 使用 Jenkins 搭建 CI/CD 流水线
- 支持 DEV/TEST/PRE 多环境切换

这类项目经历非常适合写入简历，并且面试官通常会围绕这些内容深入提问。

# 26.1 AI 会取代测试工程师吗？

答案：

```
不会
```

AI 擅长：

- 重复性工作
- 文本生成
- 代码补全
- 数据分析
- 文档整理

AI 不擅长：

- 理解复杂业务
- 制定测试策略
- 风险评估
- 产品体验判断
- 跨部门沟通

未来企业更需要的是：

```
测试工程师
        +
AI
```

而不是：

```
AI
```

------

# 26.2 AI 在测试中的应用场景（★★★★★）

目前企业中最常见的 AI 应用包括：

```
需求分析
↓

测试点提取
↓

测试用例生成
↓

自动化脚本生成
↓

SQL 编写
↓

日志分析
↓

Bug 定位
↓

报告总结
```

AI 覆盖了测试生命周期的大部分重复性工作。

------

# 26.3 Prompt 工程基础（★★★★★）

Prompt（提示词）决定了 AI 输出的质量。

一个好的 Prompt 应包括：

```
角色

任务

背景

限制条件

输出格式
```

例如：

```
你是一名拥有 10 年经验的软件测试开发工程师。

请根据以下登录需求，生成完整的测试用例。

要求：

1. 使用 Excel 表格格式

2. 包括正常场景和异常场景

3. 包括边界值测试

4. 包括安全性测试
```

比：

```
帮我写测试用例
```

效果好得多。

------

# 26.4 使用 ChatGPT 编写测试用例

输入需求：

```
用户登录：

手机号 + 验证码登录。
```

AI 可以生成：

- 功能测试
- 异常测试
- 边界值测试
- 安全测试
- 性能建议

但工程师仍需：

- 校验业务逻辑
- 补充特殊场景
- 删除不符合实际的用例

------

# 26.5 使用 AI 编写 Selenium / Playwright 脚本（★★★★★）

例如：

输入：

```
使用 Playwright 编写登录自动化脚本。

要求：

使用 Page Object。

使用 Pytest。

生成 Allure 报告。
```

AI 可直接生成：

- 页面对象
- 测试用例
- Fixture
- Allure 注解

开发效率大幅提升。

------

# 26.6 使用 AI 编写接口自动化

例如：

输入：

```
根据以下接口文档，

使用 Requests + Pytest 编写接口自动化测试。
```

AI 可以生成：

- 请求代码
- 参数化
- Header
- Token
- 断言

但要检查：

- 是否符合团队框架
- 是否处理异常情况

------

# 26.7 使用 AI 编写 SQL

例如：

输入：

```
根据以下表结构，

统计每个机构的订单金额，

按月份分组，

金额倒序。
```

AI 可快速生成 SQL。

你的职责：

- 验证 SQL 是否正确
- 检查索引是否命中
- 优化性能

------

# 26.8 使用 AI 分析日志（★★★★★）

将日志提供给 AI：

```
TimeoutException

ElementClickInterceptedException

500 Internal Server Error
```

AI 可以帮助：

- 分析异常原因
- 推测可能问题
- 提供排查思路

注意：

不要上传生产环境敏感数据。

------

# 26.9 使用 AI 定位 Bug

提供：

```
需求

测试步骤

日志

截图

接口返回

数据库数据
```

AI 可以：

- 总结问题
- 提供排查方向
- 推荐验证方法

但最终结论仍需人工确认。

------

# 26.10 Cursor 在测试开发中的应用（★★★★★）

Cursor 非常适合：

```
自动补全代码

理解项目

修改函数

生成单元测试

重构代码
```

例如：

你可以直接输入：

```
请将当前 Selenium 页面对象改造成 Playwright Page Object。
```

Cursor 会基于整个项目上下文进行修改。

------

# 26.11 GitHub Copilot

适合：

- 自动补全代码
- 生成循环
- 生成 CRUD
- 编写注释

相比 Cursor：

Copilot 更偏：

```
代码补全
```

------

# 26.12 AI 编写 Python 工具

例如：

生成：

- Excel 工具
- YAML 工具
- Redis 工具
- 日志工具
- SQL 工具

可以快速完成基础代码，再由工程师优化。

------

# 26.13 AI 分析接口文档

输入：

Swagger 或 OpenAPI 文档。

AI 可以：

- 总结接口
- 生成测试点
- 编写自动化代码
- 生成 Mock 数据

------

# 26.14 AI 生成测试数据

例如：

生成：

```
身份证号

手机号

邮箱

订单

优惠券

地址
```

比手工编写更高效。

------

# 26.15 AI 编写正则表达式

例如：

输入：

```
匹配中国手机号。
```

AI 可生成：

```
^1[3-9]\d{9}$
```

减少查阅资料时间。

------

# 26.16 AI 的局限性（★★★★★）

AI 常见问题：

- 幻觉（编造不存在的内容）
- API 使用过时
- 代码不能直接运行
- 不理解企业业务
- 忽略边界场景

因此：

```
AI 负责生成

工程师负责验证
```

------

# 26.17 企业 AI 工作流（★★★★★）

推荐工作流：

```
需求
    │
    ▼
AI 提取测试点
    │
    ▼
人工补充
    │
    ▼
AI 生成测试用例
    │
    ▼
人工审核
    │
    ▼
AI 生成自动化脚本
    │
    ▼
人工调试
    │
    ▼
执行测试
    │
    ▼
AI 分析日志
    │
    ▼
人工确认 Bug
```

AI 是助手，不是最终决策者。

------

# 26.18 企业最佳实践

建议：

- 用 AI 生成初稿
- 不直接复制运行
- 保持代码规范
- 保护公司数据
- 建立团队 Prompt 模板库

------

# 企业项目实战

结合本课程项目：

```
需求文档
      │
      ▼
AI 提取测试点
      │
      ▼
生成 Excel 测试用例
      │
      ▼
生成 Pytest 用例
      │
      ▼
生成 Selenium / Playwright 页面对象
      │
      ▼
生成 Requests 接口代码
      │
      ▼
生成 SQL 验证
      │
      ▼
生成 Allure 报告总结
```

整个测试流程效率显著提升。

# 27.1 什么是 LLM？（★★★★★）

LLM（Large Language Model）：

```
大语言模型
```

例如：

- ChatGPT
- DeepSeek
- Claude
- Gemini
- Qwen（通义千问）
- Kimi

它们都属于：

```
生成式 AI（Generative AI）
```

传统接口：

```
输入
↓

固定输出
```

LLM：

```
输入 Prompt
↓

概率生成输出
```

因此：

> AI 测试与传统接口测试最大的区别就是：**输出不是唯一答案。**

------

# 27.2 AI 系统架构

企业中的 AI 应用通常如下：

```
用户
    │
    ▼
Web / App
    │
    ▼
FastAPI
    │
    ▼
Prompt
    │
    ▼
LLM API
    │
    ▼
Function Calling
    │
    ▼
数据库
Redis
知识库
第三方接口
```

测试对象不仅是模型，还包括整个 AI 应用链路。

------

# 27.3 调用 LLM API（★★★★★）

典型流程：

```
Python
    │
    ▼
HTTP Request
    │
    ▼
LLM API
    │
    ▼
JSON Response
```

返回内容通常包括：

- 输出文本
- Token 消耗
- 模型名称
- Finish Reason
- 调用耗时

测试时不仅要验证内容，还要验证这些元数据。

------

# 27.4 Prompt 工程

Prompt 是 AI 的"测试输入"。

好的 Prompt 包括：

```
角色

任务

上下文

限制条件

输出格式
```

例如：

```
角色：

高级软件测试工程师

任务：

生成登录模块测试用例

要求：

Markdown 表格

包含正常、异常、边界、安全测试
```

企业通常会维护统一的 Prompt 模板。

------

# 27.5 Function Calling（★★★★★）

传统 AI：

```
用户

↓

AI回答
```

Function Calling：

```
用户

↓

AI

↓

调用工具

↓

返回结果

↓

AI组织答案
```

例如：

AI 可以调用：

- 查询订单
- 查询天气
- 查询数据库
- 调用 FastAPI
- 调用 Redis

测试重点：

- 是否调用了正确工具
- 参数是否正确
- 调用失败是否降级处理

------

# 27.6 MCP（Model Context Protocol）（★★★★★）

MCP 是 AI 与外部工具交互的一种协议。

可以理解为：

```
AI

↓

MCP Server

↓

数据库

Git

浏览器

Redis

文件系统
```

测试关注：

- MCP Server 是否正常注册
- 工具是否可发现
- 调用参数是否合法
- 超时处理
- 权限控制

------

# 27.7 RAG（检索增强生成）

很多企业 AI 并不是直接回答，而是：

```
用户问题

↓

知识库检索

↓

返回相关文档

↓

LLM 总结

↓

最终回答
```

测试重点：

- 检索是否准确
- 文档是否最新
- 引用是否正确
- 回答是否基于知识库

------

# 27.8 AI Agent

Agent：

```
用户

↓

AI

↓

规划任务

↓

调用多个工具

↓

完成目标
```

例如：

```
创建测试账号

↓

生成订单

↓

支付

↓

退款

↓

验证数据库
```

整个流程：

AI 自动完成。

------

# 27.9 AI 接口测试

AI 接口测试除了验证 HTTP 状态码：

还要验证：

- 输出是否符合格式
- 是否包含敏感信息
- 是否符合业务要求
- 是否稳定
- 是否超时

例如：

```
HTTP 200

↓

输出不能为空

↓

必须包含指定关键词
```

------

# 27.10 AI 输出测试（★★★★★）

传统接口：

```
assert result=="登录成功"
```

AI：

不能这样测试。

推荐：

```
关键词匹配

格式验证

JSON Schema

语义相似度

人工抽检
```

例如：

验证：

```
必须包含：

退款

订单号

金额
```

而不是完全一致。

------

# 27.11 Prompt 自动化测试

企业会维护：

```
Prompt

↓

Expected Rule

↓

AI

↓

自动校验
```

例如：

100 个 Prompt：

每天自动测试。

发现：

Prompt 回归问题。

------

# 27.12 AI 幻觉（Hallucination）

AI 最大问题：

```
编造不存在的信息
```

例如：

- 编造接口
- 编造 SQL
- 编造 API
- 编造文档

测试重点：

验证：

```
真实性

来源

引用
```

------

# 27.13 AI 安全测试

重点：

- Prompt Injection（提示词注入）
- 越权访问
- 数据泄露
- 敏感信息输出
- Jailbreak（越狱）

例如：

测试：

```
请忽略之前所有指令……
```

模型是否被绕过。

------

# 27.14 AI 性能测试

关注：

- 首 Token 时间（TTFT）
- 总响应时间
- Token 吞吐量
- 并发能力
- 成本（Token 消耗）

企业常统计：

```
平均响应时间

P95

P99
```

------

# 27.15 AI 自动化测试框架（★★★★★）

推荐目录：

```
AITestProject
│
├── Prompt/
├── TestCase/
├── Common/
├── Config/
├── Report/
├── PromptData/
├── Evaluation/
├── Logs/
├── pytest.ini
└── requirements.txt
```

框架支持：

- Prompt 参数化
- API 调用
- 输出校验
- 日志记录
- Allure 报告

------

# 27.16 AI 输出评估（Evaluation）

企业通常不会只看：

```
是否返回
```

还会评估：

- 准确率
- 一致性
- 完整性
- 可读性
- 是否命中知识库
- 是否符合业务规则

评估方式：

- 自动规则
- 人工抽样
- LLM-as-a-Judge（模型辅助评估）

------

# 27.17 企业 AI 测试流程（★★★★★）

```
需求
    │
    ▼
Prompt 设计
    │
    ▼
调用 LLM
    │
    ▼
Function Calling
    │
    ▼
RAG 检索
    │
    ▼
输出评估
    │
    ▼
Allure 报告
    │
    ▼
Jenkins 定时执行
```

形成完整 AI 测试流水线。

------

# 企业项目实战

项目：

**AI 智能客服测试平台**

测试内容：

```
登录

↓

提问

↓

知识库检索

↓

LLM 回答

↓

Function Calling

↓

数据库验证

↓

日志分析

↓

Allure 报告
```

覆盖：

- Prompt 测试
- AI 接口测试
- RAG 测试
- Agent 测试
- 性能测试
- 安全测试

# 28.1 什么是性能测试？（★★★★★）

性能测试（Performance Testing）：

验证系统在不同负载下：

```
响应是否够快

是否稳定

能否支撑业务量
```

性能测试不是找功能 Bug，而是评估：

- 系统容量
- 响应速度
- 资源消耗
- 极限能力

------

# 28.2 常见性能测试类型（★★★★★）

## 1）负载测试（Load Test）

验证：

```
系统在预期用户量下是否稳定。
```

例如：

1000 用户同时下单。

------

## 2）压力测试（Stress Test）

持续增加压力：

```
1000

↓

3000

↓

5000

↓

10000
```

直到：

系统崩溃。

目的：

找到：

```
系统极限
```

------

## 3）稳定性测试（Soak Test）

例如：

```
持续运行：

24小时

48小时

72小时
```

观察：

- 内存泄漏
- CPU
- 数据库连接

------

## 4）容量测试

评估：

服务器：

还能支持：

多少用户。

------

## 5）峰值测试（Spike Test）

例如：

双十一：

```
突然：

100

↓

10000
```

观察：

系统：

恢复能力。

------

# 28.3 性能指标（★★★★★）

企业最关注：

| 指标       | 含义         |
| ---------- | ------------ |
| TPS        | 每秒事务数   |
| QPS        | 每秒查询数   |
| RT         | 响应时间     |
| Throughput | 吞吐量       |
| 并发用户   | 同时在线人数 |
| CPU        | CPU 使用率   |
| Memory     | 内存占用     |
| Disk IO    | 磁盘 IO      |
| Network    | 网络带宽     |

------

# 28.4 TPS 与 QPS 区别（★★★★★）

TPS：

```
Transaction Per Second
```

例如：

一个下单：

包括：

```
登录

↓

购物车

↓

支付

↓

订单
```

整体：

算：

一个事务。

------

QPS：

```
Query Per Second
```

更多用于：

```
数据库

搜索

接口
```

------

# 28.5 响应时间（RT）

组成：

```
客户端

↓

网络

↓

服务器

↓

数据库

↓

返回
```

企业：

关注：

```
P50

P90

P95

P99
```

例如：

P95：

表示：

95% 请求：

响应时间：

小于：

500ms。

------

# 28.6 JMeter（★★★★★）

Apache：

开源：

性能测试工具。

支持：

```
HTTP

HTTPS

TCP

JDBC

MQ

FTP
```

企业：

仍然：

大量使用。

------

# 28.7 JMeter 基本组件

```
Test Plan

↓

Thread Group

↓

Sampler

↓

Listener
```

最重要：

```
Thread Group
```

控制：

```
用户数

Ramp-up

Loop
```

------

# 28.8 JMeter 实战

例如：

登录接口：

```
POST

/login
```

设置：

```
100 用户

Ramp-up：

20 秒

Loop：

10 次
```

运行：

查看：

```
TPS

RT

Error
```

------

# 28.9 参数化

企业：

必须：

参数化。

例如：

CSV：

```
user1

user2

user3
```

避免：

所有用户：

同一个账号。

------

# 28.10 关联（★★★★★）

例如：

登录：

返回：

```
{
"token":"xxxxx"
}
```

后续：

请求：

自动：

引用：

Token。

JMeter：

使用：

```
JSON Extractor
```

------

# 28.11 Locust（★★★★★）

越来越多 Python 团队：

使用：

```
Locust
```

原因：

全部：

Python。

安装：

```
pip install locust
```

------

# 28.12 第一个 Locust 脚本

```
from locust import HttpUser, task

class User(HttpUser):

    @task
    def login(self):

        self.client.get("/")
```

运行：

```
locust
```

浏览器：

打开：

```
http://localhost:8089
```

------

# 28.13 Locust 用户行为

例如：

```
@task(5)
def home():
```

表示：

权重：

5。

企业：

模拟：

真实：

用户行为。

------

# 28.14 Python 编写性能测试

例如：

```
requests

↓

统计时间

↓

输出 TPS
```

适合：

小规模：

接口压测。

------

# 28.15 数据库性能分析

关注：

```
慢 SQL

索引

锁

连接数

执行计划
```

工具：

```
EXPLAIN
```

------

# 28.16 Redis 性能分析

关注：

```
Hit Rate

Memory

Key 数量

慢查询
```

企业：

大量：

使用。

------

# 28.17 AI 接口性能测试（★★★★★）

AI 接口：

新增指标：

```
首 Token 时间（TTFT）

总 Token 数

生成速度

Token/s
```

不仅：

关注：

HTTP。

还关注：

模型：

响应速度。

------

# 28.18 性能监控

企业：

监控：

```
CPU

Memory

Redis

MySQL

Docker

Network
```

常见工具：

- Prometheus
- Grafana

------

# 28.19 Jenkins 集成

Pipeline：

自动：

执行：

```
Locust

↓

生成报告

↓

发送邮件
```

实现：

持续性能测试。

------

# 28.20 企业性能测试流程（★★★★★）

```
需求

↓

性能目标

↓

设计场景

↓

准备数据

↓

执行压测

↓

监控资源

↓

分析瓶颈

↓

优化

↓

回归验证
```

形成：

闭环。

# 29.1 项目介绍

项目名称：

> **企业级电商自动化测试平台**

业务：

```
商城首页
↓

登录

↓

商品浏览

↓

购物车

↓

下单

↓

支付

↓

退款

↓

售后

↓

会员

↓

积分

↓

优惠券
```

------

# 29.2 系统架构

```
                    GitLab
                      │
                      ▼
                 Jenkins CI
                      │
                      ▼
              Docker Compose
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
 Selenium/Playwright  Requests API    FastAPI Mock
      │               │
      └───────┬───────┘
              ▼
          MySQL / Redis
              │
              ▼
        Allure Report
```

------

# 29.3 技术栈

包括：

```
Python

Pytest

Selenium

Playwright

Requests

FastAPI

MySQL

Redis

Docker

Jenkins

Allure

Git
```

------

# 29.4 UI 自动化

实现：

- 登录
- 商品搜索
- 加购物车
- 提交订单
- 退款

采用：

```
Page Object

BasePage

Locator

Pytest
```

------

# 29.5 后台管理系统

自动化：

后台：

```
登录

商品管理

订单管理

会员管理

退款审核

数据统计
```

涉及：

权限控制。

------

# 29.6 小程序自动化

例如：

微信小程序：

自动化：

```
登录

浏览商品

下单

支付
```

介绍：

常见方案：

- Appium
- minium
- Playwright（WebView 场景）

并说明各自适用场景。

------

# 29.7 App 接口自动化

例如：

```
APP

↓

登录

↓

Token

↓

首页

↓

商品

↓

订单
```

采用：

Requests。

------

# 29.8 支付流程自动化（★★★★★）

整个支付：

```
提交订单
      │
      ▼
生成订单
      │
      ▼
调用支付
      │
      ▼
支付回调
      │
      ▼
修改订单状态
      │
      ▼
积分增加
      │
      ▼
优惠券失效
```

验证：

UI

- 

接口

- 

数据库。

------

# 29.9 MySQL 数据验证

自动：

验证：

```
订单

库存

余额

积分

退款
```

SQL：

断言。

------

# 29.10 Redis 验证

例如：

```
Token

Session

购物车缓存

验证码

排行榜
```

自动：

验证。

------

# 29.11 Docker 部署

整个平台：

```
docker compose up
```

启动：

```
MySQL

Redis

FastAPI

Jenkins

自动化测试
```

------

# 29.12 Jenkins 持续集成

流程：

```
Git Push

↓

Jenkins

↓

Docker

↓

Pytest

↓

Allure

↓

企业微信
```

实现：

无人值守。

------

# 29.13 Allure 报告

展示：

- 用例数量
- 成功率
- 失败原因
- 执行时间
- 截图
- 日志

------

# 29.14 企业自动化平台目录

```
AutoTestPlatform
│
├── Base
├── Common
├── Config
├── Page
├── Api
├── Locator
├── Data
├── TestCase
│   ├── UI
│   └── API
├── Report
├── Docker
├── Jenkins
├── Logs
├── requirements.txt
└── README.md
```

------

# 29.15 简历包装（★★★★★）

如何写项目：

项目名称：

企业级电商自动化测试平台

职责：

- 负责 UI 自动化框架设计
- 搭建接口自动化框架
- MySQL 数据断言
- Redis 数据验证
- Jenkins 持续集成
- Docker 部署
- Allure 报告
- Page Object 设计

------

# 29.16 企业项目答辩

面试官：

> 这个项目为什么这样设计？

你能够回答：

- 为什么使用 PO？
- 为什么使用 Fixture？
- 为什么封装 BaseApi？
- 为什么使用 YAML？
- 为什么用 Docker？
- 为什么接 Jenkins？