# 抓包工具fiddler

# fiddler抓包原理

开启fiddler后，会给系统设置代理，可在Windows 10的设置中查看

![](image/image_ePOFw3uooT.png)

![](image/image_jT3Z0eT6FI.png)

代理相当于一个中间服务器，电脑的请求会首先发送给代理，经由代理处理后再决定去向。

# fiddler的重要设置

设置的开启

![](image/image__u-8WrCRvj.png)

## 允许监听HTTPS

![](image/image_ehZvGQ0zoK.png)

## 允许远程设备连接

![](image/image_BVOH1B3BlP.png)

# fiddler基础操作

## 开启和关闭抓包

![](image/image_qXsvgvPha2.png)

## 过滤进程

![](image/image_XD1m_mjLdy.png)

## 底部栏含义

![](image/image_9dIjgVfR39.png)

## 内置加密解密工具

![](image/image_D4aDiaIo98.png)

![](image/image_UYtJhwWh1_.png)

# 过滤host

![](image/image_8qHKKkrDXM.png)

# 自动响应

fiddler可以拦截某一请求，并重定向到本地的资源，或者使用Fiddler的内置响应。

用途：

*   调试服务器端代码而无需修改服务器端的代码和配置

*   测试前后端分离的项目时

    *   有时前后端进度不一样，当前端模块完成而后端还没有完成时，可以使用这个功能模拟后端响应，称为mock测试。一般使后台正确响应来测试前端；

    *   也可用于定位缺陷来源：模拟正确的响应，如果仍然出现缺陷，则是前端的问题，如果不再出现缺陷，则是后端的问题

*   mock测试就是在测试过程中，对于某些不容易构造或者不容易获取的对象，用一个虚拟的对象来创建以便测试的测试方法

![](image/image_xzgDdcB2Yi.png)

![](image/image_f-ay2Porwi.png)

![](image/image_bq1Ba4D5xJ.png)

## 保存响应文件

如果只是部分地修改响应文件，可以保存原来的响应文件，在此基础上进行修改

![](image/image_e4vRTgvxxj.png)

# composer

在composer中可以手动构造和请求，可用于做接口测试

![](image/image_KcyjraS3ym.png)

# 断点和修改数据

添加断点的两种方法

方法一：

![](image/image_ocHBZMBood.png)

![](image/image_sB5O7gzerc.png)

![](image/image_Ps5QNRWHlo.png)

方法二：

![](image/image__VZwJafwjO.png)

拦截请求的时候，可以直接修改请求内容；拦截响应的时候，可以直接修改响应内容

![](image/image_jnGPtpqjz7.png)

![](image/image_mQTKqwW7jy.png)

# 限速

![](image/image_jcrngF9ZoR.png)

![](image/image_RwZTsxGWnr.png)

常用延迟参数的设置：

2G

```text
上行：2.7K
下行：9.6K
上行：[1/(2.7/8)]X1000=2962ms
下行：[1/(9.6/8)]X1000=833ms

```

3G

```纯文本
电信：
上行：1.8M 1.8x1024
下行：3.1M 3.1x1024
上行：{1/[(1.8x1024)/8]}x1000=4.34ms
下行：{1/[(3.1x1024)/8]}x1000=2.52ms

移动：
上行：384k
下行：2.8M
上行：[1/(384/8)]x1000=20.8ms
下行：{1/[(2.8x1024)/8]}x1000=2.79ms

联通：
上行：5.76M
下行：7.2M
上行：{1/[(5.76x1024)/8]}x1000=1.35ms
下行：{1/[(7.2x1024)/8]}x1000=1ms
```

## 其他限速方式

路由器一般可以指定设备限速

电脑开启热点，有些软件（如360热点）有限速功能

# 抓取手机APP的包

1.  在fiddler的Tools（工具）的Options（设置）中，选中Connections选项卡，勾选允许远程计算机连接；

2.  确保手机和电脑连接在同一路由器下；

3.  设置手机的代理为电脑的IP地址，端口为8888，此时已经能抓取HTTP请求，如果想抓取HTTPS请求，需要安装证书：在手机浏览器中输入http\://电脑的IP地址:8888，然后下载证书并安装证书。

如果连接不上，尝试关闭电脑防火墙和杀毒软件

# 统计信息

![](image/fiddler统计数据含义_K4dRO9lzB8.png)
