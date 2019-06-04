# RMAN <Recovery Manager>
备份和恢复数据库的管理工具

1. 由 server process 进行备份和恢复
2. RMAN 可备份的文件种类
    * datafile (database,tablespace,datafile)
    * control file, spfile
    * archivelog

## 非归档模式下，RMAN只能 冷备，并在mount下做
冷备 --> 需要先把 database shutdown 
```
1. 
shutdown immediately

2.
SQL > startup mount;

3.
RMAN > backup database;
```

## 归档模式下，RMAN 支持 热备

## RMAN 架构
![](http://ww1.sinaimg.cn/large/006tNc79gy1g3dmg8jhcbj30io0d2q43.jpg)
1. 可连接三类数据库：target database, catalog database, duplicate database