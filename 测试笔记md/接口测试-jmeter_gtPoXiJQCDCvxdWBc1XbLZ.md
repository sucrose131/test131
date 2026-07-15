# 接口测试-jmeter

# 什么是Jmeter

Apache JMeter是Apache组织开发的基于java的压力测试工具

适用的测试领域

*   对软件做压力测试。可用于测试静态和动态资源，例如：静态文件、Java小程序、CGI脚本、Java对象、数据库、FTP服务器等等。模拟巨大的负载，来自不同压力类别下测试它们的强度和整体性能

*   对应用程序做功能、回归测试，通过创建带有断言的脚本来验证程序返回的结果是否符合期望。允许使用正则表达式创建断言

*   接口测试

*   数据库压力测试

*   批量产生测试数据

# jmeter元件

**作用域**

所有组件都会作用于它的父级、同级、同级组件的子组件

**执行顺序**

在同一个作用域范围内，元件按照以下顺序执行：

1.  测试计划：jmeter的起点和容器

2.  线程组：代表一定的虚拟用户

3.  配置元件：请求期的配置信息

4.  前置处理器：在请求之前的操作

5.  定时器：是否延迟或间隔发送请求

6.  取样器：发送请求的最小单元

7.  后置处理器：在请求之后的操作

8.  断言：判断请求的响应是否与需求一致

9.  监听器：负责收集测试结果

同一元件的组件一般按上下顺序运行，但是也有例外，如配置元件"用户定义的变量"无论它处于测试树的哪个位置，总是在测试的最开始执行

# 线程组

线程执行的顺序：

![](image/image_-0799Jqa11.png)

如果勾选了独立运行每个线程组，则按上下顺序运行；如果没有勾选，则同时运行

setUP线程组：在所有线程组之前运行，如果有多个都是等价的

普通线程组

tearDown线程组：在所有线程组之后运行，如果有多个都是等价的

# 参数化

使用变量代替值，称为参数化，也叫数据驱动

变量的引用方式为 \${变量名}

**参数化的作用：**

1.  参数化可以方便有大量请求不同测试数据时的接口测试，例如有100组请求参数数据，如果一个个在请求取样器中更改效率就会很低，而参数化后，看放在csv文件中，一次性执行完成；

2.  对于要多次用到的参数值，参数化可以方便修改，例如在自定义用户变量定义某个变量A后，在多个请求中都用到了此变量，如果需要改变参数值，可以直接修改变量A的值，而不必在用到此变量的请求中去更改；

3.  对于自动化接口测试，参数化更是必须的

# 配置元件

## CSV数据文件设置

用于从文件中读入大量测试数据依次赋值给变量，并进行测试

*   在最外层的线程组（默认叫线程组，可以改名字）中设置循环次数为数据的个数

    ![](image/image-20220225124235196_o8pB-r7yrk.png)

![](image/image_xtQ2nq4X8G.png)

*   可用txt格式的文件，要使用分隔符

*   也可用csv格式文件，csv是表格形式的文件，可用表格编辑软件打开，编辑起来更方便直观

## http信息头管理器

*   放在http请求下面时只会显示所属的http请求的信息头

*   放在线程组下时对所有http请求生效

常用情景：

*   需要token

*   请求体传参数时，请求体要使用content-type:application/json

## http请求默认值

*   不填http数据时生效，填了以填写的为准

## HTTP Cookie管理器

cookie鉴权原理：

客户端第一次访问服务器的，服务器会生成Cookie，然后通过响应头中的Set-Cookie传输到客户端，然后保存在客户端中；第2次以上访问时，同过请求头中的Cookie把我们保存在本地的Cookie信息传输到服务以实现鉴权

Cookie管理器的作用：

1.  **Cookie 管理器就像一个 web 浏览器那样存储并发送 cookie**

    如果 HTTP 请求的返回结果里包含 cookie，那么 Cookie 管理器会自动将该 cookie 保存起来，而且以后所有的对该网站的请求都使用此 cookie。每个 JMeter 线程都有自己独立的"cookie 保存区域"。注意这些 cookie 不会显示在 Cookie 管理器里，可以通过察看结果树来对其进行查看

2.  **接收到的 cookie 数据可以作为 Jmeter 线程的参数进行存储**

    要将 cookie 存储为参数，定义属性"CookieManager.save.cookies=true"。cookie 在被保存之前会在名字上加上 “COOKIE\_” 前缀(避免和本地参数重复)。设置好一会名字为 TEST 的 cookie 可以用 \${COOKIE\_TEST} 进行引用。如果不希望这个前缀可以对属性 “CookieManager.name.prefix=” 进行定义&#x20;

3.  **手动添加一个 cookie 到 Cookie 管理器**

    &#x20;手动添加的cookie 将被所有 JMeter 线程所共享。这种方式用于创建有很长过期日期的 cookie

## 用户定义的变量

![](image/image_zsPCctS5oF.png)

# 前置处理器

## 用户参数

无论用户参数和用户定义的变量这两个变量放置的位置在哪，都有：用户定义的变量是全局的，所有线程可用；用户参数是局部的，同一线程组下可用

![](image/image_GyrO2xFhhX.png)

# 定时器

## 同步定时器

与线程组的线程数配合使用。可用于设置集合点，模拟多用户并发

![](image/image_RyOdnfg6Bm.png)

使用用表格查看结果树可以更清晰地看到是否并发访问

![](image/image_l9IoyOB4Xv.png)

## 固定定时器

间隔指定时间后执行后面的请求，常用于模拟用户的思考时间

# 取样器

## HTTP取样器

![](image/无标题_wRdZye1EZw.png)

## 调试取样器

## BeanShell取样器

BeanShell取样器可以理解为一个小型的Java解释器

常用脚本

| \${变量名};                      | 在请求处可看到此变量的值                                                 |
| ----------------------------- | ------------------------------------------------------------ |
| ResponseMessage="\${变量名}"     | 在响应处可看到此变量的值                                                 |
| \${\_\_setProperty(变量名,变量值,)} | 设置一个全局变量，但是调用时必须用property函数调用。如果变量值填写一个局部变量，则可将一个局部变量设置为全局变量 |
| \${\_\_property(变量名,,)}       | 调用setProperty定义的全局变量                                         |



# 后置处理器

## 正则表达式

一般格式：left(元字符+限定符)right

**元字符**

| 元字符       | 意义             |
| --------- | -------------- |
| .         | 任意单个字符         |
| \d        | 任意单个数字         |
| \[0-9]    | 0至9之间的任意一个     |
| \[a-zA-Z] | a至z或A-Z之间的任意一个 |

**限定符**

| 限定符            | 意义                                |
| -------------- | --------------------------------- |
| +              | 匹配至少大于1次                          |
| ？              | 遇到第一个右边界停止，如果不加会在遇到换行符前的最后一个右边界停止 |
| \*             | 匹配0次或多次，贪婪匹配                      |
| {n,}、{n,m}、{n} | 匹配限定次数                            |

验证匹配是否正确可以在“查看结果树”的正则表达式测试或去在线正则表达式网站测试

## 正则表达式提取器

如果想在某个请求的响应结果里面拿到某个值，可以使用后置处理器中的正则表达式提取器

步骤

1.  确定左右边界

2.  写正则表达式，常用left(.\*?)right

![](image/image_A0Q29AevyN.png)

## json提取器

![](image/image_ZmIAxY2ldj.png)

| Names of created variables             | 接收提取值的变量名，此变量不能跨线程使用                                     |
| -------------------------------------- | -------------------------------------------------------- |
| JSON Path expression                   | json path 表达式                                            |
| Match No.(0 for Random)                | 取第几个值&#xA;0：随机，**默认**&#xA;-1：所有&#xA;1：第一个值               |
| Compute concatenation var(suffix\_ALL) | 勾选后，如果匹配到多个值，则将它们都连接起来，不同值之间用 , 分隔；变量会在原来基础上自动添加\_ALL的后缀 |
| Default Values                         | 匹配不到值的时候取该值，可写error                                      |

多个json path表达式用分号（；）隔开，此时参数名、匹配数字和默认值应当与json path表达式一一对应，且都是用分号隔开。

**json path表达式格式：**

1.  \$代表根目录

2.  取得键对应的值

    \$\["键名"]

    \$.键名

3.  如果键的值是一个列表，可使用索引取得列表元素

    \$.键名\[索引]

    注意列表索引从0开始

**获取多个数据的2种方法**：

| \$.键名\[\*] | 提取列表中的所有元素   |
| ---------- | ------------ |
| \$..键名     | 提取所有层级下指定键的值 |

# 断言

用于检查测试中得到的响应数据等是否符合预期

使用断言的目的：在request的返回层面增加一层判断机制，因为request成功了，不代表结果一定正确，通过断言可以看到请求是否真的成功

## 响应断言

![](image/image_vFgJ9g3Oyt.png)

1.  apply to：通常发出一个请求只触发一个请求，所以勾选“main sampie only”就可以；若发一个请求可以触发多个服务器请求，就有main sample 和sub-sample之分了。另外，如果发起重定向请求，并且勾选“跟随重定向”， 则把重定向后的请求视为main-sample

2.  测试字段：
    (1)一般的http响应，都勾选“响应文本”；
    (2)url样本是对sample的url进行断言，如果请求没有重定向，就请求url，如果有重定向，就请求url和重定向url；
    (3)响应代码：http响应代码，如101,200,302,404,501等。当我们要验证4xx,5xx的http响应代码时，**需要勾选“忽略状态**（ ignore status）”。因为当http 响应代码为400,500时，jmeter默认这个请求时失败的；
    (4)响应信息：响应代码对应得响应信息，例如“OK"

3.  模式匹配：
    (1)包括：返回结果包括你指定的内容，支持正则匹配
    (2)匹配： 相当于 equals 。当返回值固定时，可以返回值做断言，效果和equals相同 ；
    正则匹配 。 用正则表达式匹配返回结果，但必须全部匹配。 即正则表达式必须能匹配整个返回值，而不是返回值的一部分。
    (3) SubString：与 “包括”差不多，都是指返回结果包括你指定的内容，但是subString不支持正则字符串
    (4) 否：就相当于取反。 如果断言结果为true，勾选“否”后，最终断言结果为false。如果断言结果为false，勾选“否”后，则最终断言结果为 true

4.  测试模式：输入结果期望值（空格要去掉）

注意，在jmeter的察看结果树处，应该选择Text形式，而不能选择JSON格式，JSON格式方便查看但是不能匹配

## 大小断言

![](image/image__7ITWGy_OR.png)

## 断言响应时间

从请求到返回数据的时间，如果超过设定的时间则失败

![](image/image_tXMJikUz1M.png)

# 监听器

## 查看结果树

*   css选择器

*   HTML

*   JSON

*   Document

*   Regexp\_Tester（测试正则表达式）

*   XPath Tester

## 以表格查看结果数

![](image/image_VlmH4QVYXB.png)

Sample#：编号类似id

Start Time：开始时间

Thread Name：线程名称

Label：请求名称

Sample Time：取样时间ms

Status：状态

Bytes：接受字节数

Sent Bytes：发送字节数

Latency：等待时间

Connect Time：链接时间

## 聚合报告

![](image/image_mPBJf3saoP.png)

1.  Label:在不勾选"Include group name in label?"复选框的情况下，为请求取样器的名称，否则为“请求取样器所在线程组:请求取样器名称”

2.  Samples:用同一个请求取样器，发送请求的数量(注意：该值是不断累计的)。比如，10个线程数设置为10，循环10次，那么每运行一次测试，该值就增加10\*10=100，只要没有清除结果

3.  Average:请求的平均响应时间

4.  Median:中位数。50%的样本都没有超过这个时间。这个值是指把所有数据按由小到大将其排列，就是排列在第50%的值。

5.  90% Line：90%的样本都没有超过这个时间。这个值是指把所有数据按由小到大将其排列，就是排列在第90%的值。

6.  Min:针对同一请求取样器，请求样本的最小响应时间

7.  Max:针对同一请求取样器，请求样本的最大响应时间

8.  Error %:出现错误的请求样本的百分比

9.  Throughput：吞吐量以“requests/second、requests /minute、requests /hour来衡量。时间单位已经被选取为second，所以，显示速率至少是1.0，即每秒1个请求。

10. Received KB/sec - 收到的千字节每秒的吞吐量测试。

11. Kb/sec - 以Kilobytes/seond来衡量的吞吐量(发送的千字节每秒的吞吐量测试)

# 逻辑控制器

## ForEach控制器

循环使用后缀按索引变化的变量

![](image/image_g9ADsLwYTl.png)

## 如果（if）控制器

满足指定的条件才会执行其下的请求

![](image/image_TZnvIq2b1G.png)

## 交替控制器

与线程组的循环配合使用，每次循环会按从上到下顺序依次执行其下的请求

## 循环控制器

将其下的请求循环指定的次数

![](image/image_Md2CXYkPlG.png)

## While控制器

条件为真时继续循环，条件为假时跳出循环

![](image/image_OLyELacw8m.png)

## 仅一次控制器

与线程组的循环配合使用，当线程组的循环大于1次时，“仅一次控制器”下的组件只会在第一次时候执行一次

## 随机控制器

随机执行其下的请求

## 事务控制器

其下的请求是完成某个事务的一组请求，再聚合报告中会单独列出来

# jmeter结合fiddler

jmeter的http请求中设置代理

![](image/image-20220224170046340_oF7ZNfJZXf.png)

利用fiddler截获http请求能更清楚的查看http报文的情况

# 函数

打开函数助手

![](image/image_3QXKhlJRIc.png)

或

![](image/image_yuIgAOprW4.png)

函数助手的使用

![](image/image_6lfOFBqWTx.png)

## Random

返回指定范围内的随机整数，可以重复

![](image/image_TWTrp0FOPZ.png)

## RandomString

从自定字符串中随机组合成指定长度的字符串，有可能会有重复

![](image/image_IZ_QLH2bse.png)

## count

返回值从1开始，每次循环会加1。如果第一个参数为FALSE，意味着不同线程也会加1；如果为TRUE，意味着每个用户独立计数

![](image/image_6DhOxDrcX0.png)

## setProperty和property

使用这两个函数可以将局部变量（仅在线程组内使用）转换为全局变量（可跨线程组使用），全局变量也成为属性，可在测试计划中右键添加属性显示来查看

![](image/image_Pjz_uY9kKl.png)

setProprty定义全局变量（属性）

![](image/image_T27MLPHgTc.png)

定义好后需要将函数写入局部变量所在线程组的BeanShell取样器的脚本中

![](image/image_tCT1d7eUdt.png)

运行此线程后，可在属性显示中查看是否设置成功

![](image/image_PgTsj0pPQs.png)

property使用属性

![](image/image_ArdomnDQ9X.png)

在另一线程组中使用函数

![](image/image_AMsGZzz7_R.png)

# 连接数据库

首先在测试计划中添加连接MySQL的jar包

![](image/image_DwmYgiZWll.png)

## JDBC Connection Configuration

![](image/image_4vnDLf8tUR.png)

![](image/image_oD9xpC8Ery.png)

## JDBC Request

![](image/image_K96NG-VL6U.png)

# 生成测试报告

使用jmeter命令可以自动生成测试报告

## 自带的性能测试报告

1.  打开cmd，进入jmeter目录下的bin目录下，可在目录下的路径栏直接输入cmd，回车，进入cmd后就是在当前目录下了

    ![](image/image_ur2M4Xqqz0.png)

    ![](image/image_CEFN9KWjzO.png)

    ![](image/image_CFUq18OSe-.png)

2.  此时有两种命令可生成测试报告

    方法一，将查看结果树的结果保存在一个文件中，后缀为jtl

    ![](image/image_PDHucOWw4J.png)

    在cmd中（当前路径需在jmeter的bin目录下）运行如下命令

    ```bash
    jmeter -g 结果（jtl文件）路径 -o 报告输出目录（必须是空目录）
    ```

    ![](image/image_1gh7gkNXmY.png)

    方法二：使用命令执行jmx文件，然后生成结果和报告

    ```bash
    jmeter -n -t jmx文件路径 -l 结果文件存放路径（自定义文件名称） -e -o 报告输出目录（必须是空目录）
    ```

    ![](image/image_y3kvcwlZTp.png)

## 使用ant插件生成

下载ant应用，转移插件，配置好jmeter.properties和build.xml文件。在含有build.xml的目录下打开cmd，输入ant命令

