下载地址：网页https://www.sonarsource.com/   ，文档https://docs.sonarsource.com/

安装完成后启动：sonarqube-8.9.10.61524\sonarqube-8.9.10.61524\bin\windows-x86-64目录下的StartSonar.bat

下载对应版本的汉化包：https://github.com/xuhuisheng/sonar-l10n-zh/releases

然后将其拷贝到SonarQube所在部署服务器的\extensions\plugins 目录，重启SonarQube即可。

![image-20241227111226236](D:\131\测试笔记md\image\image-20241227111226236.png)

安装数据库

![image-20241227112624588](D:\131\测试笔记md\image\image-20241227112624588.png)

https://www.postgresql.org/download/

参考：https://www.cnblogs.com/Simple-Small?page=3

安装完成后启动

![image-20241227114741774](D:\131\测试笔记md\image\image-20241227114741774.png)

创建用户：

![image-20241227115252161](D:\131\测试笔记md\image\image-20241227115252161.png)

填写名字和密码还有权限

创建数据库：

![image-20241227115444981](D:\131\测试笔记md\image\image-20241227115444981.png)

填写名字和使用用户

打开sonarqube-8.9.10.61524\sonarqube-8.9.10.61524\conf目录下sonar.properties文件

修改

sonar.jdbc.username=test    （用户名）
sonar.jdbc.password=abcd1234      （密码）

![img](D:\131\测试笔记md\image\1416283-20200513155819087-1036225681.png)



重启



安装sonar-scanner

https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/scanners/sonarscanner/

修改sonar-scanner-cli-6.2.1.4610-windows-x64\sonar-scanner-6.2.1.4610-windows-x64\conf

# 

#----- SonarQube server URL (default to SonarCloud)
sonar.host.url=http://localhost:9000

#sonar.scanner.proxyHost=myproxy.mycompany.com
sonar.scanner.proxyPort=8002
sonar.sourceEncoding=UTF-8
sonar.login=admin
sonar.password=abcd1234

将bin目录配置到环境变量cmd输入sonar-scanner -h检查



Java代码扫描

1、获取1份java项目源代码(svn/git上下载均可）
2、项目代码根目录src存在的目录中添加sonar-project.properties

内容为：

#must be unique in a given SonarQube instance

sonar.projectKey=lemon-java    

#--- optional properties ---

#defaults to project key

sonar.projectName=lemon-java

#defaults to 'not provided'

#sonar.projectVersion=1.0

#Path is relative to the sonar-project.properties file. Defaults to .

sonar.sources=. 

#Encoding of the source code. Default is default system encoding

sonar.sourceEncoding=UTF-8
sonar.java.binaries=target/classes

接着添加target文件夹

3、文件内容如下：

sonar.projectKey=在sonarQube上的实例键名(唯一)
sonar.projectName=在sonarQube上的项目名称
sonar.projectVersion=1.0(项目版本号)
sonar.sources=.(java源代码目录指定）
sonar.sourceEncoding=UTF-8（编码格式指定）
sonar.language=java(指明只扫描java语言）
sonar.java.binaries=target/classes(class文件的目录)
4、在项目代码根目录下，运行命令：sonar-scanner
5、等待扫描完成。