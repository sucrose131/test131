在 CentOS 7 上安装宝塔面板，需要先解决官方源停止维护的问题（CentOS 7 官方支持已结束，默认源失效），再执行安装步骤。以下是详细流程：

### **步骤 1：替换 CentOS 7 的 yum 源（解决源失效问题）**

```
连接虚拟机：
ip a   查看ech33的地址
打开powershell  输入：ssh 用户名@ech33的地址
再输入密码

切换超级管理员：su
```



1. 登录服务器（以 root 用户操作），备份原有源文件：

   ```bash
   mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
   ```

   

2. 下载阿里云或清华的 CentOS 7 归档源（二选一，推荐阿里云，兼容性更好）：

   - 阿里云源

     （推荐）：

     ```bash
     wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
     ```

   - 清华源：

     ```bash
     wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.tuna.tsinghua.edu.cn/centos-vault/7.9.2009/os/x86_64/CentOS-Base.repo
     ```

3. 清除缓存并生成新缓存：

   ```bash
   yum clean all && yum makecache
   ```

4. （可选）更新系统包（确保依赖兼容）：

   ```bash
   yum update -y
   ```

   

### **步骤 2：安装宝塔面板**

1. 执行官方安装脚本（适用于 CentOS 7）：

   ```bash
   yum install -y wget && wget -O install.sh https://download.bt.cn/install/install_6.0.sh && sh install.sh ed8484bec
   ```

   

2. 安装过程中会提示 “是否安装”，输入 `y` 并回车，等待 10-20 分钟（根据服务器网速）。

### **步骤 3：获取登录信息**

安装完成后，终端会显示面板登录地址、用户名和密码（**务必保存！**），示例：

```plaintext
外网面板地址: http://xxx.xxx.xxx.xxx:8888/xxxxxx
内网面板地址: http://xxx.xxx.xxx.xxx:8888/xxxxxx
username: xxxxxxxx
password: xxxxxxxx
```

### **步骤 4：登录并初始化**

1. 打开浏览器，访问上述 “外网面板地址”，输入用户名和密码登录。
2. 首次登录会提示选择 “推荐套件”（如 LNMP：Nginx+MySQL+PHP，或 LAMP：Apache+MySQL+PHP），选择后点击 “一键安装”，等待套件安装完成即可使用。

### **常见问题解决**

- 若安装过程中提示 “wget: command not found”

  ：先手动安装 wget：

  ```bash
  yum install -y wget
  ```

- 若端口 8888 无法访问

  ：检查防火墙是否开放（新手可临时关闭防火墙）：

  ```bash
  systemctl stop firewalld && systemctl disable firewalld
  ```

  

- **忘记登录密码**：通过 SSH 执行 `bt` 命令，选择 “重置面板密码”。

按照以上步骤，即可在 CentOS 7 上成功安装宝塔面板。