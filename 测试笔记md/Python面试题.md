# Python面试题



### break 和 continue 的区别？

答：

```
break

结束整个循环。

continue

跳过本次循环。
```

### while True 如何退出？

答：

使用：

```
break
```

### range(5) 的结果？

答：

```
0 1 2 3 4
```

### enumerate 的作用？

答：

同时获取：

- 索引
- 元素

### 列表推导式的优点？

答：

代码更简洁。

执行效率更高。

### return 和 print 的区别？

答：

```
print

输出结果。

return

返回结果。
```

### *args 类型是什么？

答：

```
tuple
```

### **kwargs 类型是什么？

答：

```
dict
```

### lambda 的优点？

答：

代码简洁。

适合简单函数。

### sorted 和 sort 的区别？

答：

```
sort

修改原列表。

sorted

返回新列表。
```

### 为什么 requests 封装大量使用 **kwargs？

答：

参数灵活。

支持：

method

url

headers

json

params

cookies

timeout

等所有参数。

### self 是什么？

答：

当前对象。

------

### **init** 什么时候执行？

答：

创建对象时自动执行。

------

### 实例变量和类变量区别？

实例变量：

对象独有。

类变量：

所有对象共享。

------

### super() 有什么作用？

调用父类方法。

------

### 封装、继承、多态是什么？

封装：

隐藏实现。

继承：

代码复用。

多态：

统一接口。

------

### staticmethod 和 classmethod 区别？

静态方法：

没有 cls。

类方法：

有 cls。

------

### 为什么 PO 模型要使用继承？

因为：

```
公共方法

↓

BasePage

↓

LoginPage

HomePage

NewsPage
```

避免重复代码。

### read() 和 readline() 区别？

答：

```
read

读取全部内容

readline

读取一行
```

------

### 为什么推荐 with？

答：

自动关闭资源。

避免内存泄漏。

------

### JSON 和 dict 的关系？

答：

```
JSON

字符串格式

dict

Python对象
```

转换：

```
json.dumps()

json.loads()
```

------

### openpyxl 用来做什么？

答：

操作 Excel。

自动化测试数据驱动。

------

### YAML 比 JSON 有什么优势？

答：

更简洁。

更适合配置文件。

### try except finally 执行顺序？

```
try
↓
except
↓
finally
```

finally 一定执行。

------

### Exception 和 BaseException 区别？

```
BaseException

所有异常父类

Exception

普通异常父类
```

开发中：

使用：

```
except Exception
```

即可。

------

### raise 有什么作用？

主动抛出异常。

------

### assert 的作用？

断言。

判断结果是否符合预期。

------

### finally 为什么重要？

释放资源。

例如：

```
文件

数据库

浏览器
```

------

### Selenium 常见异常？

```
NoSuchElementException

TimeoutException

StaleElementReferenceException
```

------

### requests 常见异常？

```
Timeout

ConnectionError

RequestException
```

### 什么是闭包？

答：

```
函数内部定义函数

内部函数引用外部变量

返回内部函数
```

------

### 装饰器本质是什么？

答：

```
闭包 + 函数对象
```

------

### @xxx 等价于什么？

```
test = xxx(test)
```

------

### 为什么要用 wraps？

保持：

```
__name__

__doc__
```

不丢失。

------

### yield 和 return 区别？

```
return

结束函数

yield

暂停函数
```

------

### next() 的作用？

获取生成器下一个值。

------

### 生成器优点？

```
节省内存

惰性加载
```

### import 和 from import 区别？

答：

```
import math

math.sqrt()
from math import sqrt

sqrt()
```

------

### 为什么使用 if **name** == "**main**"？

防止：

导入模块时自动执行。

------

### os.path.join 为什么重要？

兼容：

```
Windows

Linux

Mac
```

路径分隔符。

------

### pathlib 和 os.path 哪个推荐？

答：

```
Python3 推荐：

pathlib
```

------

### requirements.txt 的作用？

记录项目依赖。

方便部署。

------

### 为什么要使用虚拟环境？

隔离依赖。

避免版本冲突。

------

### hashlib 常用在哪？

```
密码加密

接口签名

token生成
```

### logging 五个等级？

```
DEBUG

INFO

WARNING

ERROR

CRITICAL
```

------

### Logger、Handler、Formatter关系？

```
Logger

产生日志

↓

Handler

输出位置

↓

Formatter

格式化
```

------

### logger.exception 和 error 区别？

```
exception

记录完整堆栈

error

只有错误信息
```

------

### 为什么使用 RotatingFileHandler？

防止：

日志文件过大。

------

### 如何同时输出控制台和文件？

两个 handler。

------

### 为什么日志重复？

重复：

```
addHandler()
```

导致。
