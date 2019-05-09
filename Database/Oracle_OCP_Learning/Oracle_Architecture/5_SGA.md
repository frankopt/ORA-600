# 系统全局区 SGA
注 ： Oracle UPS 后备电源


![](https://ws4.sinaimg.cn/large/006tNc79gy1g2qjbhndl9j30h20bojt2.jpg)

System Global Area <SGA>

```
SQL> show parameter sga_target
NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
sga_target                           big integer 2496M
```

查询视图 获得 SGA 具体组件分配情况
```
SQL> select * from v$sgainfo;
NAME                                  BYTES RES     CON_ID
-------------------------------- ---------- --- ----------
Fixed SGA Size                      9182024 No           0
Redo Buffers                        7593984 No           0
Buffer Cache Size                1023410176 Yes          0
In-Memory Area Size                       0 No           0
Shared Pool Size                 1560281088 Yes          0
Large Pool Size                    16777216 Yes          0
Java Pool Size                            0 Yes          0
Streams Pool Size                         0 Yes          0
Shared IO Pool Size               134217728 Yes          0
Data Transfer Cache Size                  0 Yes          0
Granule Size                       16777216 No           0
NAME                                  BYTES RES     CON_ID
-------------------------------- ---------- --- ----------
Maximum SGA Size                 2617244488 No           0
Startup overhead in Shared Pool   407427992 No           0
Free SGA Memory Available                 0              0
14 rows selected.
```

## 共享池 Shared Pool
* 语句执行方式。软分析、硬分析
* 数据字典高速缓存区

## 数据库缓冲区高速缓存 Database Buffer Cache

## 重做日志缓冲区 Redo Log Buffer
数据出现故障，不一致，会用到
进而找到放到磁盘上的 Redo Log Files(联机重做日志文件)