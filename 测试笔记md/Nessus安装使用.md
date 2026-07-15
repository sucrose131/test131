# 1.下载

https://www.tenable.com/downloads/nessus

![img](D:\131\测试笔记md\image\c55f19073532335a0c0d296461d0537d.png)

# 2.安装

![img](D:\131\测试笔记md\image\72861c4aa921289d0b2091a1fe1d71f2.png)

![img](D:\131\测试笔记md\image\c1f10293feb365e49e0925e1ae2b0279.png)

![img](D:\131\测试笔记md\image\d93b4405f4fee916b20aee6eb36a82dd.png)

![img](D:\131\测试笔记md\image\32dbb2439682cc27576c939b1885eee0.png)

## 安装成功后是这个页面![img](D:\131\测试笔记md\image\777dab44fc1c559af1de4006844fe179.png)

## 建议安装到C盘记住安装路径

以管理员运行cmd进入安装目录输入nessuscli.exe fetch --challenge 

目录在C盘：cd "C:\Program Files\Tenable\Nessus"

目录在D盘：cd /d "C:\Program Files\Tenable\Nessus"



![image-20250616102138514](D:\131\测试笔记md\image\image-20250616102138514.png)

# 3.点击链接进入网址注册（邮箱可能需要企业邮箱），勾选选项然后点击 Get Started

![img](D:\131\测试笔记md\image\753152677fcc6bea37c839b92e981d67.png)

打开邮箱查看你收到的验证码

![img](D:\131\测试笔记md\image\ea8625d63d8aa7ea0f7a183ac4d61580.png)

# 4.访问链接，上面的填 cmd 中的，下面的填邮箱里的

https://plugins.nessus.org/v2/offline.php

![img](D:\131\测试笔记md\image\ba77601d43040b2f62e4c0df2ac23e45.png)

点击链接下载文件

![img](D:\131\测试笔记md\image\5a9f2e3711e3a4aca4eed96aff333480.png)

还有最下面的文件

![img](D:\131\测试笔记md\image\72e969e86904e3532aea1821406a5f88.png)



将文件放在安装的 Nessus 目录下

![img](D:\131\测试笔记md\image\a65d8746baab3c9e5790dd1766692e67.png)

输入命令停止服务

net stop "Tenable Nessus" 

![img](D:\131\测试笔记md\image\320e1612869a45531cc3299671131f5d.png)



输入命令安装这个插件

nessuscli.exe update all-2.0.tar.gz 

![img](D:\131\测试笔记md\image\993485a977b9cff539b50f4d7c7c9d1a.png)

记住图中第一行 info 的 version 后的数字

修改 plugin_feed_info.inc 文件内容如下，其中 PLUGIN_SET 数字为你的 version 后的数字

这个文件一个在 nessus 目录下，另一个在 nessus\plugins 目录下，两个均修改

PLUGIN_SET = "202402261439"

PLUGIN_FEED = "ProfessionalFeed(Direct)"

PLUGIN_FEED_TRANSPORT = "TenableNetwork Security Lightning";

原文链接：https://blog.csdn.net/2302_82189125/article/details/138159165

输入命令（具体路径为你的电脑上的路径）

E:\Nessus>attrib +s +r +h "E:\Nessus\nessus\plugins\*.*"

E:\Nessus>attrib -s -r -h "E:\Nessus\nessus\plugins\plugin_feed_info.inc"

E:\Nessus>attrib +s +r +h "E:\Nessus\nessus\plugin_feed_info.inc" 
输入命令

nessuscli.exe fetch --register-offline nessus.license 

最后启动服务

net start "Tenable Nessus" 

# 5.使用Nessus

创建新扫描

![img](D:\131\测试笔记md\image\9005091b19d31b2e9fc892e40bc7708a.png)

可选则类型如下（这里选择第二个即可）

![img](D:\131\测试笔记md\image\e7cfeca7bf930002886811d2b372cf39.png)

配置参数

![img](D:\131\测试笔记md\image\77e48d3a3c006930951506fbd5fd1b42.png)

配置主机扫描

![img](D:\131\测试笔记md\image\c098eb81b8e688b8c45e2d9c2f8d334d.png)

配置端口扫描

![img](D:\131\测试笔记md\image\ee3c91787bb86b87cee5d5980fc06293.png)

配置服务发现

![img](D:\131\测试笔记md\image\88e4f2613a82026cd502b94d4e6df8af.png)

最后一个适用于扫描 Windows 系统 

![img](D:\131\测试笔记md\image\9cae482d00d4e37659893f3a967ea606.png)



设置准确度

![img](D:\131\测试笔记md\image\08854fe8ddec51630fd8a2ceee26b76c.png)

配置好后点击 Save 保存，点击三角开始扫描

![img](D:\131\测试笔记md\image\be06318cbdbb2d9483f6fb4df6e27e61.png)

查看扫描结果

![img](D:\131\测试笔记md\image\56a92125be5c736382f107633f678321.png)