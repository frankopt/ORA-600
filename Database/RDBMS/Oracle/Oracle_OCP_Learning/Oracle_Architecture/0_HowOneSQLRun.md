# SQL 语句是怎么执行的 ？
![](https://ws4.sinaimg.cn/large/006tNc79gy1g2qjbhndl9j30h20bojt2.jpg)

用户进程与服务器进程建立连接之后，
用户进程执行操作

## 查询操作
服务器进程PGA里 进行 哈希运算 得到 Hash Value，
传递给 Shared Pool的 Library Cache(库高速缓存区)，进行比较。

* 存在 - 软分析
Oracle Shared Pool里面的优化器 判断 a 全局扫描 b 索引
* 不存在 - 硬分析

---> 经过 Data Dictionary Cache(数据字典高速缓存)，获取数据存储的具体block。
---> 经过 Database Buffer Cache(数据库缓冲区高速缓存) check 是否要寻找的 block 在内存中
* 在，直接在内存中操作
* 不在，通过服务器进程 将 Data Files中的 block 读入到 Database Buffer Cache中缓存，在内存中操作


## DML操作（增删改查）
... 同上

---> 修改 Database Buffer Cache 后，要求 Redo Log Buffer 记录更改过程
---> 通过 LGWR 进程 写入到 磁盘的 Redo Log Files
* 写入成功，DML 继续
* 写入失败，DML hang ,用户进程 hang，甚至 DB down


## SMON / PMON / DBWR/ LGWR /CKPT 
这五个进程 kill 任何一个 都会导致 数据库 宕机

1. CKPT 写数据文件 和 控制文件 的头，实现一致性 需求。
2. CKPT 通知 DBWR 写数据， DBWR 写数据前 要求 LGWR 先写
3. CKPT 一触发，数据文件 + 控制文件 + 联机重做日志文件 一致

注：
如果 数据文件不一致，database 在下一次 进程写入 或 重启 的时候，通过 restart instance，通过 Redo Log Files 重新将 数据写入 Data Files，从而保证 数据不丢失。