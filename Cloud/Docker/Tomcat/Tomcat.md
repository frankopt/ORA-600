![](http://ww1.sinaimg.cn/large/006tNc79gy1g3w44tk61tj30xc0m8mzf.jpg)

# 1 Tomcat是什么
Tomcat是一个被广泛使用的Java WEB应用服务器
类似功能的还有：Jetty、Resin、Websphere、weblogic、JBoss、Glassfish、GonAS等，它们的市场占有率如下，可以看到Tomcat是最受欢迎的Java WEB应用服务器

![](http://ww2.sinaimg.cn/large/006tNc79gy1g3w46oh62jj30w80ii3zx.jpg)

 Tomcat在技术实现上所处的位置如下：
 ![](http://ww4.sinaimg.cn/large/006tNc79gy1g3w47rruc5j30fe05hjrv.jpg)

下面我们来了解下Tomcat与这些技术之间的关系:

## 1.1 Tomcat与Java
* Tomcat与Java SE - Tomcat是用Java语言编写的，需要运行在Java虚拟机上，所以一般需要先安装JDK，以提供运行环境。
* Tomcat与Java EE - Tomcat实现了几个Java EE规范，包括Java Servlet、Java Server Pages（JSP），Java Expression Language和Java WebSocket等，这些是都下载Tomcat安装包默认提供的，可以在源码中看到相关Java EE 规范API源码引用

# 2 Tomcat Install
2.1 解压jdk压缩包

```
cd /usr/local/
tar -xvf jdk-8u211-linux-i586.tar
# 解包成功后会有一个 jdk1.8.0_211 的文件夹
```

2.2 解压 tomcat
```
cd /usr/local/
tar -xvf apache-tomcat-8.5.41.tar
# 更名为tomcat8
mv apache-tomcat-8.5.41 tomcat8
```

2.3 配置环境变量

在文件最后添加
```
vi /etc/profile

# jdk evn
JAVA_HOME=/usr/local/jdk1.8.0_211
PATH=$JAVA_HOME/bin:$PATH
CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar

export JAVA_HOME
export PATH
export CLASSPATH

# tomcat evn
CATALINA_HOME=/usr/local/tomcat8
export CATALINA_HOME
```

保存退出后执行下面的命令,使其生效

``` 
source /etc/profile
```

验证jdk是否配置成功

```
# java -version
openjdk version "1.8.0_181"
OpenJDK Runtime Environment (build 1.8.0_181-b13)
OpenJDK 64-Bit Server VM (build 25.181-b13, mixed mode)
```

2.4 配置tomcat的 catalina.sh

```
# vi /usr/local/tomcat8/bin/catalina.sh

#找到 # OS specific support，然后在这行下面添加以下配置
# OS specific support.  $var _must_ be set to either true or false.
CATALINA_HOME=/usr/local/tomcat8
JAVA_HOME=/usr/local/jdk1.8.0_211
#保存退出
```

2.5 安装tomcat服务

```
cd /usr/local/tomcat8/bin/
cp catalina.sh /etc/init.d/tomcat
```

2.6 测试tomcat启停

```
cd /usr/local/tomcat8/bin

./startup.sh
Using CATALINA_BASE:   /usr/local/tomcat8
Using CATALINA_HOME:   /usr/local/tomcat8
Using CATALINA_TMPDIR: /usr/local/tomcat8/temp
Using JRE_HOME:        /usr/local/jdk1.8.0_211
Using CLASSPATH:       /usr/local/tomcat8/bin/bootstrap.jar:/usr/local/tomcat8/bin/tomcat-juli.jar
Tomcat started.


./shutdown.sh
Using CATALINA_BASE:   /usr/local/tomcat8
Using CATALINA_HOME:   /usr/local/tomcat8
Using CATALINA_TMPDIR: /usr/local/tomcat8/temp
Using JRE_HOME:        /usr/local/jdk1.8.0_211
Using CLASSPATH:       /usr/local/tomcat8/bin/bootstrap.jar:/usr/local/tomcat8/bin/tomcat-juli.jar

#没有报错的话，证明已经配置成功了
```

# 3 Tomcat 目录解析

```
# ls -lt --group-directories-first
total 132
drwxr-x---. 2 root root  4096 Jun 10 16:45 bin   -- 启动、关闭和其他脚本
drwx------. 3 root root  4096 Jun 10 16:41 conf   --- 配置文件及相关数据文件存放目录   
drwxr-x---. 3 root root    22 Jun 10 15:37 work  -- Tomcat工作目录，如存放JSP编译后的类文件
drwxr-x---. 2 root root  4096 Jun 10 15:37 logs -- 默认的日志文件存放目录，如访问日志，可以通过server.xml文件配置到其他目录
drwxr-x---. 2 root root  4096 Jun 10 15:26 lib  -- Tomcat使用的库文件存放目录，如Servlet规范的API
drwxr-x---. 2 root root    30 Jun 10 15:26 temp
drwxr-x---. 7 root root    81 May  4 17:18 webapps  -- 应用程序部署目录，可以通过server.xml文件配置
-rw-r-----. 1 root root 19539 May  4 17:22 BUILDING.txt
-rw-r-----. 1 root root  5407 May  4 17:22 CONTRIBUTING.md
-rw-r-----. 1 root root 57092 May  4 17:22 LICENSE
-rw-r-----. 1 root root  1726 May  4 17:22 NOTICE
-rw-r-----. 1 root root  3255 May  4 17:22 README.md
-rw-r-----. 1 root root  7139 May  4 17:22 RELEASE-NOTES
-rw-r-----. 1 root root 16262 May  4 17:22 RUNNING.txt
```


# 4 Tomcat基本框架及相关配置

Tomcat可以按功能划分许多不同的组件，这些组件都可以通过/conf/server.xml文件中可定义和配置。

![](http://ww3.sinaimg.cn/large/006tNc79gy1g3w61zc2khj30cx08sjs7.jpg)
一般可分为以下四类：
1. 顶级组件：位于配置层次的顶级，并且彼此间有着严格的对应关系，有Server组件、Service组件
2. 连接器：连接客户端（可以是浏览器或Web服务器）请求至Servlet容器，只有Connector组件
3. 容器：表示其功能是处理传入请求的组件，并创建相应的响应。如Engine处理对一个Service的所有请求，Host处理对特定虚拟主机的所有请求，并且Context处理对特定web应用的所有请求
4. 被嵌套的组件：位于一个容器当中，但不能包含其它组件；一些组件可以嵌套在任何Container中，而另一些只能嵌套在Context中

## 4.1 server.xml默认配置
![](http://ww3.sinaimg.cn/large/006tNc79gy1g3w68dns1pj30h50c6dii.jpg)


