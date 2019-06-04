# SGA 的其他组件

![](https://ws2.sinaimg.cn/large/006tNc79gy1g2v6gof5znj30je0bc7d0.jpg)

![](https://ws4.sinaimg.cn/large/006tNc79ly1g2vau1wtndj30eb08vwfz.jpg)

## Database Buffer Cache 数据库高速缓存区
存放从 数据文件 读取的 block

## Redo Log Buffer 重做日志缓存区
记录数据库中 所有更改 信息
包含重做条目，这些条目包含由 DML 和 DDL 等操作进行的重做更改的相关信息

## Shared Pool 共享池
包括
* 库高速缓存 - 共享SQL区域
* 数据字典高速缓存
* 控制结构

## Large Pool 大型池
* I/O 缓冲区
* 空闲内存
* 响应队列
* 请求队列

## Java Pool
存储 JAVA代码 和 Oracle与JAVA 之间交互的信息

## PGA 的组件

![](https://ws3.sinaimg.cn/large/006tNc79ly1g2vb9bhqn0j30oa0hiwro.jpg)