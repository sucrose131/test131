



# **字符串可以用+号连接，注意+号作为连接符时只能连接字符串，其它类型的数据与字符串连接时要先转换为字符类型**

```
a = 1
b = "Hello"
c = str(a)+ b 
print(c)

1Hello
```

**print(type()):查看字符类型**

**python通过（）调用**

**shift+tab代码往前**

# 格式化输出字符串

```
 name = "严公公"
 age = 101
 sex = "不明"
 address = "深圳市-宝安区-坪洲"

print(f"名字是：{name} , 年龄是{age} ,性别是{sex}, 地址在{address}")  # 在括号最前面加f，然后变量用花括号扩起

名字是：严公公 , 年龄是101 ,性别是不明, 地址在深圳市-宝安区-坪洲
```



# 所有代码逻辑都是判定和循环

## 判定（等于需要用==，不等于需要用!=  判定可嵌套，注意层级关系）

```
if 条件1:（取反则为 if not 条件1：）
    满足条件1执行这里
elif 条件2:
    满足条件2执行这里
else:
    条件1和条件2都不满足执行这里
    
 
lambda结合if判断

语法：lambda 参数: 表达式1 if 条件 else 表达式2

# 判断一个数是否为正数
is_positive = lambda x: "正数" if x > 0 else "非正数"

print(is_positive(5))   # 输出: 正数
print(is_positive(0))   # 输出: 非正数
print(is_positive(-3))  # 输出: 非正数
```

![image-20250901151413679](D:\131\测试笔记md\image\image-20250901151413679.png)

![image-20250901151739066](D:\131\测试笔记md\image\image-20250901151739066.png)

## 打完断点后再进行debug

## 可在判定里加循环，也可在循环里加判定

## for循环（需要固定的容器或集合，循环的次数就是容器的大小）

for 变量 in 容器:
    循环主体
else:
    循环结束后执行的代码

### 如果需要遍历数字序列，可以使用内置 range() 函数。它相对于一个计数器

##### **break** 语句可以中途退出结束循环。如果从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。（一般搭配if，else使用）

##### **continue** 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。（一般搭配if，else使用）

**break和continue只能放在循环内**

![image-20250901171500910](D:\131\测试笔记md\image\image-20250901171500910.png)

```
l = [2, 7, 3, 4, 9, 1]
for i in l:
    print("hello", i)  # 遍历列表l，循环6次并打印每个元素前的"hello"
    
# 尝试修改列表中的元素，但使用了不必要的计数器
count = 0
for i in l:
    l[count] = (i + 15) * 2  # 修改列表中的元素
    count = count + 1  # 更新计数器
    print(count)  # 打印计数器的值
    print((i + 15) * 2)  # 打印修改后的值，但注意这里的i是原列表的值
print(l)  # 打印修改后的列表

# 另一种方式修改列表并存储结果到另一个列表
l2 = []
for i in l:
    print((i + 15) * 2)  # 打印修改后的值
    l2.append((i + 15) * 2)  # 将修改后的值添加到新列表l2
print(l, l2)  # 打印原列表l和新列表l2

# 使用range()函数进行循环
for i in range(100):
    print(i)  # 从0打印到99

for i in range(1, 101):
    print(i)  # 从1打印到100

for i in range(1, 101, 2):
    print(i)  # 从1开始，到100结束，步长为2（打印奇数）
```

## while循环（无限循环）

while 判断条件：
    执行语句

```
a = 10 #定义一个初始值
while a > 0:  # 当a大于0时，执行循环体
    a = a - 1  # 每次循环，a的值减1
    if a == 4:  # 检查a是否等于4
        break  # 如果是，跳出循环（这里之后的代码，包括continue，都不会被执行）
        #continue  #如果a等于4，跳过本次循环的剩余部分，直接开始下一次循环
    print(a)  # 打印a的值，但不会在a等于4时打印
```

while 判断条件:
    执行语句
else:
    不满足判断条件则执行此语句

```
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
```



# 函数

def 函数名（参数列表）:
    函数体

- **return [表达式]** 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。**使用return后，函数后面的代码就不会执行了。**

- 参数不能前面给，后面不给

  

![img](D:\131\测试笔记md\image\py-tup-10-26-1.png)

```
def max(a, b):#若def max(a==1, b==2)则1，2为默认值，若def max(a：str, b：int)a只能传字符串，b只能传整数
    if a > b:
        return a
    else:
        return b


print(max(4, 5))

#输出5
```

### 在函数内部修改全局变量的值，可以使用global关键字，也可以将局部变量声明为全局变量

语法格式：global 变量名

```
global关键字可以对全局变量进行修改：也可以在局部作用域中声明一个全局变量
# 定义一个全局变量
count = 0

def increase_count():
    # 声明要修改的全局变量
    global count
    # 在函数内部修改全局变量的值
    count += 1
    print(f"函数内修改后: count = {count}")

# 调用函数前的全局变量值
print(f"调用函数前: count = {count}")  # 输出: 调用函数前: count = 0

# 调用函数修改全局变量
increase_count()  # 输出: 函数内修改后: count = 1

# 调用函数后的全局变量值
print(f"调用函数后: count = {count}")  # 输出: 调用函数后: count = 1




#将局部变量声明为全局变量
def study():
    global name,age  # 声明要操作全局变量 name
    age = 18
    name = "python基础"  # 此时是对全局变量 name 进行赋值
    print(f"我们在学习{name}")

study()
print(name,age)

def work():
    print(name)

work()
    
```

# 拆包

### 对于函数中的多个返回数据，去掉元组，列表或者字典直接获取里面数据的过程叫做拆包

### **加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。**

### **加了两个星号 *\* 的参数会以字典的形式导入。**

```
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)

# 调用printinfo 函数
printinfo(70, 60, 50)

def test(*a):
    print(a)
test(1)
输出(1,)
```

### 同样**加了星号 * 的调用会解析元组。**

### **加了两个星号 *\* 的调用会解析字典。**

```
    def login(self,username,pwd):

        self.find_element_sendkeys(*self.UNSERNAME_BOX, text=username)  # 输入用户名
        print(*self.UNSERNAME_BOX)
        print(self.UNSERNAME_BOX)
        
      第一个print输出class name el-input__inner
      第二个print输出('class name', 'el-input__inner')
```



## 函数定义时使用 `*args`

#### 在函数定义语句 `def function_name(*args):` 中，`*args` 代表可变位置参数。其中，`*` 具备以下功能：

1. **参数收集**：允许函数接受任意数量的位置参数，并将这些参数收集到一个元组 `args` 中。例如，当函数被调用为 `function_name(1, 'two', 3.0)` 时，在函数内部，`args` 呈现为 `(1, 'two', 3.0)`。
2. **增强灵活性**：适用于不确定函数调用时会传入多少个位置参数的场景。以自动化测试中元素定位函数为例，由于不同元素的定位方式可能各不相同，使用 `*args` 能够灵活接收各种定位参数组合，如 `(By.ID, "element_id")` 或 `(By.CLASS_NAME, "element_class")` 等，从而满足多样化的定位需求。
3. 与之相对，如果函数定义为 `def function_name(args):`（未使用 `*`），函数仅能接受一个位置参数，该参数会被视为一个整体传入，而不会将多个值解析为独立参数。例如，调用 `function_name((1, 2, 3))`，此时 `args` 就是 `(1, 2, 3)` 这个元组，并非将 `1`、`2`、`3` 当作单独参数处理。

## 函数调用时使用 `*`

#### 在函数调用语句 `function_name(*iterable)` 中，`*` 用于解包参数。假设 `iterable` 是一个可迭代对象（如元组或列表），`*` 会将其中的元素作为独立参数传递给 `function_name` 函数。

1. 例如，若 `args = (By.ID, "element_id")`，那么 `function_name(*args)` 会将 `By.ID` 和 `"element_id"` 作为两个独立参数传递给 `function_name` 函数，效果等同于直接书写 `function_name(By.ID, "element_id")`。
2. 若调用时不使用 `*`，即 `function_name(args)`，则整个 `args` 对象（如上述元组 `(By.ID, "element_id")`）会被作为单个参数传递给 `function_name` 函数。这往往会使函数无法按预期处理参数，因为函数可能预期接收多个独立参数以执行特定操作，如元素定位等功能。

```
def find_element_sendkeys(self,*args,**kwargs):

    try:
        self.find_element(*args).send_keys(kwargs['text'])#
    except:
        self.save_screenshot()
        self.logger.error("填写数据失败:" + str(args)+" 数据是："+kwargs['text'])
        self.logger.error(traceback.print_exc())
        
在这段代码的上下文中，kwargs 是一个包含关键字参数的字典 。kwargs['text'] 是从 kwargs 字典中获取键为 'text' 对应的值。
例如，当你调用 find_element_sendkeys(*args, text="some input") 时，kwargs 字典会是 {"text": "some input"}，kwargs['text'] 就会取出字符串 "some input"。
```

# 类class 类名(self)（类是函数的集合，类中的函数叫方法）

- **类:** **class 类名(self)** 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。**self代表类本身**
- **方法：**类中定义的函数。
- **类变量：**类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
- **数据成员：**类变量或者实例变量用于处理类及其实例对象的相关的数据。
- **方法重写：**如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
- **局部变量：**定义在方法中的变量，只作用于当前实例的类。
- **实例变量：**在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
- **继承：**即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
- **实例化：**创建一个类的实例，类的具体对象。（类只是一个模板，我们不能直接使用模板，需要实例化确定类的具体对象。相当于一个确认按钮，确认模板生成的产品的名字。例：**产品名=类名()**）
- **对象：**通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
- **类属性**：对象和类都可以调用
- **实例属性（函数属性）：**只有对象能调用

#### 调用类的函数或方法：要先实例化再使用实例化名.函数名调用

```
class Test():
    d = 100  # 定义类变量d，初始值为100

    def __init__(self, a):   #当类进行实例化时给类的变量进行初始化。正常来说使用类的变量需要：实例化名.函数名。现在可直接调用
    
        self.e = a  # 定义实例变量e，并将其值设置为传递给构造函数的参数a

    def test1(self):
        a = 1  
        b = 2  
        c = a + b  
        print("test1:", c)  

    def test2(self, a, b=1):
        c = a + b  
        print("test2", c)  

    def test3(self):
    	self.d         #调用类的变量
        print(d * 100)  # 打印实例变量d的100倍
        self.test1()  # 调用test1方法

    def test4(self):
        self.d = 7  # 修改实例变量d的值为7

    def test5(self):
        self.e = 100  # 修改实例变量e的值为100
        
   
  
t = Test(10)  #对Test这个类进行实例化，并传递变量a为10        
print(t.e)  # 打印实例变量e的值，即10      
        
t.test1()  # 调用实例t的test1函数，输出 test1: 3        
        
print(t.d)  # 打印实例变量d的原始值，因为test4方法还未被调用，所以仍为100        
        
t.test4()  # 调用实例t的test4方法，修改d的值为7
print(t.d)  # 打印修改后的d的值，即7   
t.test3()  # 再次调用test3方法，此时d的值为7，所以打印的是700
     
        
```

### **类的继承**

```
class Father():
    def __init__(self, name):  # 初始化Father类，接收一个名字作为参数
        self.name = name  # 设置实例的name属性
    def eat(self):  # 定义一个方法，表示吃饭的行为
        print(f"{self.name}正在吃饭！")  # 打印出当前实例的名字和正在吃饭的信息
    def play(self):  # 定义一个方法，表示打麻将的行为
        print(f"{self.name}正在打麻将！")  # 打印出当前实例的名字和正在打麻将的信息
# 定义Mother类
class Mother():
    def __init__(self, sex):  # 初始化Mother类，接收一个性别作为参数
        self.sex = sex  # 设置实例的sex属性
    def dance(self):  # 定义一个方法，表示跳舞的行为
        print(f"性别是{self.sex}")  # 打印出当前实例的性别
# 定义Son类，继承自Father和Mother类
class Son(Father, Mother):
    def __init__(self, school, name, sex):  # 初始化Son类，接收学校、名字和性别作为参数
        self.school = school  # 设置实例的school属性
        self.name = name  # 设置实例的name属性，注意这里会覆盖从Father继承的name
        self.sex = sex  # 设置实例的sex属性，注意这里会覆盖从Mother继承的sex

    def study(self):  # 定义一个方法，表示学习的行为
        print(f"{self.name}正在学习")  # 打印出当前实例的名字和正在学习的信息

    def play(self):  # 重写Father类中的play方法
        print(f"{self.name}正在打游戏！")  # 打印出当前实例的名字和正在打游戏的信息

    def __str__(self):  # 定义一个特殊方法，用于返回实例的字符串表示
        return self.name  # 返回实例的name属性作为字符串

# 创建Father类的实例并调用方法
f = Father("老王")    
f.eat()  # 调用实例的eat方法
f.play()  # 调用实例的play方法

# 创建Son类的实例并调用方法
s = Son("老王") #能继承父类的形参，但只能继承第一个
s = Son("一中", "小王", "男") #多的只能自己设置形参
s.study()  # 调用实例的study方法
s.eat()  # 调用继承自Father的eat方法
s.play()  # 调用重写后的play方法
s.dance()  # 调用继承自Mother的dance方法

print(str(s))  # 调用__str__方法获取实例的字符串表示并打印
```

## 类继承与实例化概念区分

- 在 Python 中，当你定义一个类如 `class DataStatistics(RetrieveLocator, Newslistpage, HomeLocator, DataStatisticsLocator, Channelmanagementlocator):`，这仅仅表示 `DataStatistics` 类继承自 `RetrieveLocator`、`Newslistpage`、`HomeLocator`、`DataStatisticsLocator` 和 `Channelmanagementlocator` 这些类。继承意味着 `DataStatistics` 类可以获取这些父类的属性和方法，但并没有实例化这些类。
- 实例化是指创建类的对象，例如 `obj = SomeClass()`，这里 `obj` 就是 `SomeClass` 的一个实例。

## `setUp` 方法中的实例化分析

- 在 `setUp` 方法中，`self.page = DataStatistics()` 这行代码确实实例化了 `DataStatistics` 类，创建了一个 `DataStatistics` 类的对象并赋值给 `self.page`。
- 然而，并没有对 `RetrieveLocator`、`Newslistpage`、`HomeLocator`、`DataStatisticsLocator` 和 `Channelmanagementlocator` 进行单独实例化。当 `DataStatistics` 类被实例化时，它会继承父类的属性和方法，在运行时根据需要调用这些继承的特性，但父类本身并没有被单独实例化。

```
class  DataStatistics(RetrieveLocator,Newslistpage,HomeLocator,DataStatisticsLocator,Channelmanagementlocator):


@ddt
class TestRetrieve(unittest.TestCase,RetrieveLocator,Channelmanagementlocator):

    @classmethod
    def setUpClass(cls) -> None:
        pass
    def setUp(self) -> None:
        self.page = DataStatistics()  # 实例化DataStatistics只要实例化了就可以使用父类继承的方法
        self.page.lopen()  # 打开登录页面                      -page
        self.testlog = Logger.getLogger()  # 实例化日志对象    -testlog  这两个只是一个自定义的属性名，可命名为其他名称
        self.page.login2()  # 登录
        download_helper.clear_download_dir()
        time.sleep(2)
```

# 类有一个名为 __init__() 的特殊方法（**构造方法**），该方法在类实例化时会自动调用

```
class LoginPage(BasePage, LoginLocator):
	def __init__(self):
    	print(实例化类时自动打印这段话)

```

# 静态方法和类方法

#### 静态方法：

- 在 Python 中，静态方法是属于类而不属于实例的方法。它不依赖于实例状态，即不访问实例属性（`self`），也不访问类属性（`cls`），通常用于执行一些与类相关但不依赖于类的具体实例的操作。
- 定义静态方法需要使用 `@staticmethod` 装饰器。
- 静态方法不需要对类进行实例化就可以调用，也不依赖于实例的初始化状态。这是因为静态方法既不访问实例属性（通过 self 访问），也不访问类属性

```
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# 调用静态方法
result = MathUtils.add(3, 5)
print(result)

#在上述代码中，MathUtils 类的 add 方法被定义为静态方法。通过 @staticmethod 装饰器，该方法与类关联，但不依赖于类的实例。可以直接通过类名调用，无需创建类的实例。

```

#### 类方法：

- 在 Python 中，类方法使用 `@classmethod` 装饰器进行定义。类方法的第一个参数通常命名为 `cls`，它代表类本身，而非类的实例。通过 `cls`，类方法可以访问和修改类属性，以及调用其他类方法。

```

class Company:
    company_name = "示例公司"
    @classmethod
    def get_company_name(cls):
        return cls.company_name

print(Company.get_company_name())

#在上述代码中，Company 类定义了一个类属性 company_name 和一个类方法 get_company_name。get_company_name 类方法通过 cls 参数访问并返回类属性 company_name。可以直接通过类名调用这个类方法，无需创建类的实例。
```





# 模块和包

每个 .py文件都可称为一个模块，每个含有 \_\_init\_\_.py文件的文件夹都可以称为一个包。在pycharm中，包文件夹和普通文件夹的图标不同

```python
""" 语法 """
# 导入整个文件，会将模块内的所有全局变量、函数、类等等全部都导入进来
    import 模块名称 [as 别名]

# 导入部分函数、变量、类
    from 模块名称 import 函数/变量/类 [as 别名]
```

在导入模块的时候，会把模块.py文件执行一遍，然后生成一个模块对象，模块中我们定义的函数、变量、类会添加到这个模块对象的属性里面，于是模块中的函数、变量、类能直接使用。所以我们导入if __name__=="__main__":

#### 所以写自动化时所有的执行代码操作放在if __name__=="__main__":里面

![image-20250121115650885](D:\131\测试笔记md\image\image-20250121115650885.png)

导入包的时候，不会将其中的.py文件全部执行，而是只执行这个包里面的 \_\_init\_\_.py文件，也可以理解为导入包的时候，只是导入了\_\_init\_\_.py

Python解释器对模块和包的搜索顺序是：当前目录，PATHONPATH下的每个目录，标准链接库目录（lib），.pth文件的目录。这四部分的路径都存储在sys.path 列表中

# 异常

try：

​	执行代码

except：

​     raise	Exception（"抛出了一个异常”）

​	执行代码出错则继续执行以下代码，raise：在代码错误时主动引发报错使测试用例状态改为失败，Exception可加可不加是用来说明异常原因的

# Python 装饰器

装饰器（decorators）是 Python 中的一种高级功能，它允许你动态地修改函数或类的行为。

装饰器是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数。

装饰器的语法使用 @来应用在函数或方法上。

Python 还提供了一些内置的装饰器，比如 **@staticmethod** 和 **@classmethod**，用于定义静态方法和类方法。

```
def my_decorator(func):
    def wrapper():
        print("在原函数之前执行")
        func()
        print("在原函数之后执行")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

输出：
在原函数之前执行
Hello!
在原函数之后执行
```

被装饰的函数作为参数（func）传入装饰器函数。my_decorator 是一个装饰器函数，它接受 say_hello 作为参数，并返回 wrapper 函数。

#闭包的三个条件
#1.函数嵌套
#2.内函数要使用外函数的局部变量
#3.外函数的返回值是内函数的函数名

# 断言

| 常用断言                     | 作用                     |
| ---------------------------- | ------------------------ |
| self.assertIn(a,b)           | 断言a在b中               |
| self.assertNotIn(a,b)        | 断言a不在b中             |
| self.assertTrue(条件表达式)  | 条件表达式为真时断言通过 |
| self.assertFalse(条件表达式) | 条件表达式为假时断言通过 |

# unittest

```
class TestIwebshop(unittest.TestCase):  # 定义一个测试类，继承自unittest.TestCase
    @classmethod
    def setUpClass(cls) -> None:  # 使用@classmethod装饰器定义类方法，在所有测试开始前运行一次
        print("setupClass")  # 打印"setupClass"，表示类级别的设置完成

    @classmethod
    def tearDownClass(cls) -> None:  # 类方法，在所有测试结束后运行一次
        print("teardownClass")  # 打印"teardownClass"，表示类级别的清理完成

    def setUp(self):  # 实例方法，在每个测试方法执行前运行
        print("setup")  # 打印"setup"，表示每个测试前的设置完成

    def tearDown(self):  # 实例方法，在每个测试方法执行后运行
        print("teardown")  # 打印"teardown"，表示每个测试后的清理完成

    def abc(self):  # 定义一个辅助方法，非测试方法
        print("abc")  # 打印"abc"，示例方法内容
        return 123  # 返回数字123

    def test1(self):  # 定义一个测试方法，以test开头
        print("test1")  # 打印"test1"，表示开始执行test1测试
        self.abc()  # 调用辅助方法abc

    def test2(self):  # 另一个测试方法
        print("test2")  # 打印"test2"，表示开始执行test2测试
```



# 字符串索引和切片操作(取多个值切片用冒号：)

字符串、列表、元组都用方括号切片

```
a = "abcdefghijklmnopqrstuvwxyz"
#语法：开始位置：结束位置：步长
#包前不包后：即从起始位置开始，到结束位置的前一位结束（不包含结束位置本身）
print(a[2])  # 输出: c，索引2对应的字符
print(a[-2])  # 输出: y，负索引-2表示从字符串末尾开始数第二个字符
print(a[:3])  # 输出: abc，从索引0开始到索引3（不包括3）的子字符串
print(a[3:7])  # 输出: defg，从索引3开始到索引7（不包括7）的子字符串
print(a[-4:-1])  # 输出: wxy，注意结束索引-1是不包含的，从倒数第四个字符开始到倒数第一个字符之前的子字符串
print(a[-3:])  # 输出: xyz，从倒数第三个字符开始到字符串末尾的子字符串
print(a[1:13])  # 输出: bcdefghijklm，从索引1开始到索引13（不包括13）的子字符串
print(a[1:13:2])  # 输出应为: bdfhjl，起始索引是 1，对应的字符是 'b'。
结束索引是 13（但不包括索引 13 的字符），所以我们只考虑到索引 12 的字符 'l' 之前的字符。
步长是 2，意味着从起始索引开始，每次增加 2 来选择字符。
print(a[::-1])  # 输出: zyxwvutsrqponmlkjihgfedcba，反转字符串
print(a[7:2:-1])  # 这个切片操作从索引7开始（包含），到索引2结束（不包含），步长为-1。
由于步长为负，所以切片是反向进行的。
它会选择索引为7, 6, 5, 4, 3的字符，即 'h', 'g', 'f', 'e','d'。
结果是一个从'h'到'e'的反向子字符串。

列表切片
l = [1, 2, 3, 4, 5, 6, 7]
print(l[:3])  # 输出: [1, 2, 3]，列表的前三个元素

元组切片
t = (1, 2, 3, 4, 5, 6, 7)
print(t[:3])  # 输出: (1, 2, 3)，元组的前三个元素
元组和列表都支持切片操作，但是元组是不可变的，即你不能修改元组中的元素。

字典切片
f={"a":1,"b"：2}
print(f{"b"})#输出2
```

内置函数操作

**在已赋值的字符串，字典，列表，元组后加一个.接着选择需要的函数**

```
# 计算数据长度用len()函数，可用于字符串，字典，列表，元组
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(len(a))  # 输出: 8
```

## 显式等待（反义 until_not）

```
 WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located(login_link)) #直到元素代码被加载到HTML代码中
 WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located(login_link)) #直到元素在界面可见（非隐藏）并且长宽都大于0
 submit_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[2]/button"))
        )#等待元素高亮显示后点击
```

## 隐式等待

```
driver.implicitly_wait(20)
```

## 强制等待

```
time.sleep(10)
```

# 



## DDT参数化（参数化又叫数据驱动，将代码和数据分离，解耦合）

(data driver test )数据驱动测试，通过装饰器形式调用，可以完美应用于unittest框架实现数据驱动。

使用方法：

1. 安装ddt包

   ```python
   pip install ddt
   ```

ddt中的装饰器：

| 装饰器      | 作用                                |
| ----------- | ----------------------------------- |
| @ddt        | 类装饰器，声明当前类使用ddt         |
| @data       | 函数装饰器，用于给测试用例传递数据  |
| @unpack     | 函数装饰器，将传输的数据解包        |
| @file\_data | 函数装饰器，可直接读取yaml/json文件 |

@unpack使用的注意事项：

1. 数字、字符串和无序数据序列（如集合）不能解包

2. 字典解包时，键的名称和个数必须和用例中的参数保持一致，元组无名称限制

   #### 元组三种参数化方式

```
@ddt
class TestIwebhopSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass
    def setUp(self) -> None:
        pass
        
    @data(1,2,)
    def test_cases(self,a):
        print("test case",a)
    #输出为test case test1 1
		  test case tes1t 2

    @data(("test1","123456"), ("tes1t","1234567"))
    def test_cases(self, a):
        print("test case",a[0],a[1])
        
     #输出为test case test1 123456
	       test case tes1t 1234567

    @data(("test1","123456"), ("tes1t","1234567"))
    @unpack#解包
    def test_cases(self, a, b):
        print("test case", a, b)
    #输出为test case test1 123456
		  test case tes1t 1234567
```

#### 		字典两种种参数化方式

```
@ddt
class TestIwebhopSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass
    def setUp(self) -> None:
        pass
        @data({"username":"test1","password":"123456"},{"username":"tes1t","password":"1234567"})
    def test_cases(self, a):
        print("test case", a["username"],a["password"])
    #输出为test case test1 123456
		  test case tes1t 1234567

    @data({"username": "test1", "password": "123456"}, {"username": "tes1t", "password": "1234567"})
    @unpack
    def test_cases(self, username,password):
        print("test case", username,password)
        
    #输出为test case test1 123456
		  test case tes1t 1234567

    def tearDown(self) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass
```

# 文件IO(读和写)

| 字符  | 含义                                                         |
| ----- | ------------------------------------------------------------ |
| `'r'` | 以只读方式打开文件。文件的指针将会放在文件的开头（默认）     |
| `'w'` | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件 |
| `'x'` | 写模式，新建一个文件，如果该文件已存在则会报错               |
| `'a'` | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入 |
| `'b'` | 二进制模式                                                   |
| `'t'` | 文本模式（默认）                                             |
| `'+'` | 打开一个文件进行更新(可读可写)                               |

文件对象常用方法：

| 方法名                 | 说明                                                         |
| ---------------------- | ------------------------------------------------------------ |
| read(\[size])          | 从文件读取size个字节或字符内容返回,若省略\[size],则读取到文件末尾,即一次读取文件所有内容 |
| readline()             | 从文本文件中读取一行内容                                     |
| resdlines()            | 把文本文件中的每一行都作为独立的字符串对象,并将这些对象放入列表中返回 |
| write(str)             | 将字符串str内容写入文件                                      |
| writelines(s)          | 将字符串列表s写入文本文件,不添加换行符                       |
| seek(offset\[,whence]) | 把文件指针移动到新位置,offset表示相对于whence的位置:&#xA;offset:  &#xA;    offset为正,往结束方向移动;offset为负,往开始方向移动&#xA;0: 从文件头开始计算(默认)&#xA;1: 从当前位置开始计算&#xA;2: 从文件尾开始计算 |
| tell()                 | 返回文件指针当前位置                                         |
| truncate(\[size])      | 不问指针在什么位置,只留下指针前size个字节的内容,其余全部删除&#xA;如果没有传入size,则当前指针位置到文件末尾全部删除 |
| flush()                | 把缓冲区的内容写入文件,但不关闭文件                          |
| close()                | 把缓冲区的内容写入文件,同时关闭文件,并释放资源               |

```
#只读方式操作
fp=open("./test_io.txt","r")
data=fp.read()#读
print(data)
fp.close()#关闭
```

```
#只写方式操作，打开文件会清除原文件内容
fp=open("./test_io.txt","w")
fp.write("Hello World!")#写
fp.close()
```

```
#用读写的方式打开，注意光标位置
fp=open("./test_io.txt","r+")#打开文件后，光标在文件开头
data=fp.read()
print(data)
fp.write("ABC!")
fp.close()
```

```
#以追加的方式打开文件，光标在最后，可以支持读操作。
fp=open("./test_io.txt","a+")
fp.write("123!")
fp.seek(0)
data=fp.read()
print(data)
fp.close()
```

# 浅拷贝和深拷贝

1. #### 浅拷贝只是拷贝了引用。用列表举例，如果修改内部列表，会同时影响原列表和浅拷贝后的列表

   ```
   import copy
   
   # 原始列表，包含一个普通元素和一个嵌套列表
   original = [10, [20, 30]]
   
   # 进行浅拷贝
   copied = copy.copy(original)
   
   # 打印两个列表的内容（看起来一样）
   print("原始列表:", original)    # 输出: [10, [20, 30]]
   print("拷贝列表:", copied)      # 输出: [10, [20, 30]]
   
   # 修改拷贝列表中的普通元素
   copied[0] = 100
   print("\n修改普通元素后:")
   print("原始列表:", original)    # 输出: [10, [20, 30]]（不受影响）
   print("拷贝列表:", copied)      # 输出: [100, [20, 30]]
   
   # 修改拷贝列表中的嵌套列表元素
   copied[1][0] = 200
   print("\n修改嵌套元素后:")
   print("原始列表:", original)    # 输出: [10, [200, 30]]（被影响了！）
   print("拷贝列表:", copied)      # 输出: [100, [200, 30]]
    
   ```

   

2. #### 原列表和深拷贝后的列表内部的列表是不同的对象。当修改原列表内部的列表时，深拷贝后的列表不受影响

   ```
   import copy
   
   # 原始列表，包含普通元素和嵌套列表
   original = [10, [20, 30]]
   
   # 进行深拷贝
   deep_copied = copy.deepcopy(original)
   
   # 打印初始状态
   print("初始状态:")
   print("原始列表:", original)       # [10, [20, 30]]
   print("深拷贝列表:", deep_copied)  # [10, [20, 30]]
   
   # 修改深拷贝列表中的普通元素
   deep_copied[0] = 100
   print("\n修改普通元素后:")
   print("原始列表:", original)       # [10, [20, 30]]（不受影响）
   print("深拷贝列表:", deep_copied)  # [100, [20, 30]]
   
   # 修改深拷贝列表中的嵌套元素
   deep_copied[1][0] = 200
   print("\n修改嵌套元素后:")
   print("原始列表:", original)       # [10, [20, 30]]（依然不受影响！）
   print("深拷贝列表:", deep_copied)  # [100, [200, 30]]
        
   ```

   

3. #### 总结来说，浅拷贝适用于对象内部可变对象不会被修改，或者希望通过共享内部可变对象节省内存和提高效率的场景；深拷贝则适用于需要完全独立的对象副本，避免修改一个对象影响到另一个对象的场景。

# 函数参数的特殊语法

### 1. `*args`（非关键字可变参数）

- 定义与功能
  - `*args` 用于收集所有位置参数（按顺序传递给函数的参数），并将它们打包成一个元组。在函数定义中，`*args` 必须出现在普通参数之后。
  - 它允许函数接受任意数量的位置参数，为函数编写提供了灵活性，无需预先知道会传入多少个参数。

```
def print_args(*args):
    print(f"接收到的位置参数元组: {args}")
    for arg in args:
        print(arg)


print_args(1)
print_args(1, 2, 3)
print_args('a', 'b', 'c', 'd')
```

### 2. `**kwargs`（关键字可变参数）

- 定义与功能
  - `**kwargs` 用于收集所有关键字参数（以 `key=value` 形式传递给函数的参数），并将它们打包成一个字典。在函数定义中，`**kwargs` 必须出现在普通参数和 `*args` 之后（如果有 `*args`）。
  - 它允许函数接受任意数量的关键字参数，提供了一种灵活的方式来处理额外的参数信息。

```
def print_kwargs(**kwargs):
    print(f"接收到的关键字参数字典: {kwargs}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name='Alice', age = 30)
print_kwargs(city='Shanghai', country='China', population=25000000)
```

### 3. 组合使用 `*args` 和 `**kwargs`

- **规则**：在函数定义中，普通参数在前，`*args` 次之，`**kwargs` 最后。即 `def function_name(arg1, arg2, *args, **kwargs):`。

  ```
  def combined_function(arg1, arg2, *args, **kwargs):
      print(f"普通参数 arg1: {arg1}, arg2: {arg2}")
      print(f"位置参数元组 args: {args}")
      print(f"关键字参数字典 kwargs: {kwargs}")
  
  
  combined_function(1, 2, 3, 4, key1='value1', key2='value2')
  ```

# 导包的区别

## 第一种方式

### 语法：import	模块名

### 调用方法：模块名.功能名

```
导入整个 datetime 模块到当前命名空间。使用模块中的 datetime 类时，需通过模块名前缀 datetime. 来访问。
例如：
import datetime
now = datetime.datetime.now()
print(now)
```

## 第二种方式

### 语法：from	模块名	import	功能1，功能2..

### 调用方法：直接输入功能即可，不需要添加模块名

```
从 datetime 模块中直接导入 datetime 类到当前命名空间。在使用时，可直接使用类名 datetime 来调用其方法和属性，无需使用模块名作为前缀。
例如：
from datetime import datetime
now = datetime.now()
print(now)
```

