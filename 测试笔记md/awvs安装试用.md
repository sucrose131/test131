网盘下载：

https://pan.baidu.com/s/1_RIYFLW8zv5ckJb0YPJaOg#list/path=%2F提取码: 33v8



在安装工具之前，将以下内容添加到 hosts 文件中 C:\Windows\System32\drivers\etc\hosts

127.0.0.1 erp.acunetix.com

127.0.0.1 erp.acunetix.com.

::1 erp.acunetix.com

::1 erp.acunetix.com.

127.0.0.1 discovery-service.invicti.com

127.0.0.1 discovery-service.invicti.com.

::1 discovery-service.invicti.com

::1 discovery-service.invicti.com.

127.0.0.1 cdn.pendo.io

127.0.0.1 cdn.pendo.io.

::1 cdn.pendo.io

::1 cdn.pendo.io.

127.0.0.1 bxss.me

127.0.0.1 bxss.me.

::1 bxss.me

::1 bxss.me.

127.0.0.1 jwtsigner.invicti.com

127.0.0.1 jwtsigner.invicti.com.

::1 jwtsigner.invicti.com

::1 jwtsigner.invicti.com.

127.0.0.1 sca.acunetix.com

127.0.0.1 sca.acunetix.com.

::1 sca.acunetix.com

::1 sca.acunetix.com.

192.178.49.174 telemetry.invicti.com

192.178.49.174 telemetry.invicti.com.

2607:f8b0:402a:80a::200e telemetry.invicti.com

2607:f8b0:402a:80a::200e telemetry.invicti.com.

复制hosts文件里的东西到本地的hosts文件中


![img](D:\工作工具\文档摸版\学习笔记md\image\313e951975bf30ede2fe8d9de2166d16.png)

点击右键属性

点击安全 点击编辑

![img](D:\工作工具\文档摸版\学习笔记md\image\9ceea535102ad8a3fca9c6c4c646da17.png)

点击打勾修改

![img](D:\工作工具\文档摸版\学习笔记md\image\8dd76c13b3b729223e88b29538fe0f5a.png)

然后 一路点击应用

然后就可以保存了

然后双击进行安装

![img](D:\工作工具\文档摸版\学习笔记md\image\64da65c3e70be323d7323379e7cb109f.png)

安装完成后输入之前填写的账号密码自动自动登录

![img](https://i-blog.csdnimg.cn/img_convert/f44fde839e6aaaec77088abc6555caf4.png)



然后搜索服务打开

![img](D:\工作工具\文档摸版\学习笔记md\image\4f4805b418f7b33d2818e0d44a5b2dfc.png)

关闭这两个服务

![img](D:\工作工具\文档摸版\学习笔记md\image\eda833ade20b6c6f76f8d7c25d24e84b.png)

然后复制wvsc.exe文件到软件安装目录

![img](D:\工作工具\文档摸版\学习笔记md\image\9198a8936d1b04a93bbb849e5220c323.png)

去替换

然后复制这两个文件到保存目录

![img](D:\工作工具\文档摸版\学习笔记md\image\39d4d3ebd23106e6460171cc6002efc2.png)

![img](D:\工作工具\文档摸版\学习笔记md\image\20a9d8b3c8505de1145d8a173e33a814.png)

然后右键属性改成只读

![img](D:\工作工具\文档摸版\学习笔记md\image\c5f0a78a904900c3840ff68dca190e7e.png)

然后开启刚才关闭的两个服务

![img](D:\工作工具\文档摸版\学习笔记md\image\9b937fb763a03bdd0dffae506d8d62d1.png)

登录就可以使用https://localhost:3443/#/