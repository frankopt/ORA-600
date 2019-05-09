![](https://ws4.sinaimg.cn/large/006tNc79gy1g2qjbhndl9j30h20bojt2.jpg)

Database = Data Files + Control Files + Redo Log Files

## Data Files

```
SQL> desc v$datafile
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 FILE#                                              NUMBER
 CREATION_CHANGE#                                   NUMBER
 CREATION_TIME                                      DATE
 TS#                                                NUMBER
 RFILE#                                             NUMBER
 STATUS                                             VARCHAR2(7)
 ENABLED                                            VARCHAR2(10)
 CHECKPOINT_CHANGE#                                 NUMBER
 CHECKPOINT_TIME                                    DATE
 UNRECOVERABLE_CHANGE#                              NUMBER
 UNRECOVERABLE_TIME                                 DATE
 LAST_CHANGE#                                       NUMBER
 LAST_TIME                                          DATE
 OFFLINE_CHANGE#                                    NUMBER
 ONLINE_CHANGE#                                     NUMBER
 ONLINE_TIME                                        DATE
 BYTES                                              NUMBER
 BLOCKS                                             NUMBER
 CREATE_BYTES                                       NUMBER
 BLOCK_SIZE                                         NUMBER
 NAME                                               VARCHAR2(513)
 PLUGGED_IN                                         NUMBER
 BLOCK1_OFFSET                                      NUMBER
 AUX_NAME                                           VARCHAR2(513)
 FIRST_NONLOGGED_SCN                                NUMBER
 FIRST_NONLOGGED_TIME                               DATE
 FOREIGN_DBID                                       NUMBER
 FOREIGN_CREATION_CHANGE#                           NUMBER
 FOREIGN_CREATION_TIME                              DATE
 PLUGGED_READONLY                                   VARCHAR2(3)
 PLUGIN_CHANGE#                                     NUMBER
 PLUGIN_RESETLOGS_CHANGE#                           NUMBER
 PLUGIN_RESETLOGS_TIME                              DATE
 CON_ID                                             NUMBER
```


```
SQL> select name from v$datafile;
NAME
--------------------------------------------------------------------------------
+MGMT/ORCL/DATAFILE/system.312.1007442067
+MGMT/ORCL/DATAFILE/sysaux.313.1007442111
+MGMT/ORCL/DATAFILE/undotbs1.314.1007442137
+MGMT/ORCL/87E6D80EE2A60825E053AA04E80AF7E5/DATAFILE/system.320.1007442245
+MGMT/ORCL/87E6D80EE2A60825E053AA04E80AF7E5/DATAFILE/sysaux.321.1007442245
+MGMT/ORCL/DATAFILE/users.315.1007442139
+MGMT/ORCL/87E6D80EE2A60825E053AA04E80AF7E5/DATAFILE/undotbs1.322.1007442245
+MGMT/ORCL/87E6D80EE2A60825E053AA04E80AF7E5/DATAFILE/undotbs1_temp.323.100744224
+MGMT/ORCL/DATAFILE/undotbs2.325.1007442567
+MGMT/ORCL/8823ED770D7F6DE2E053604AD60A84F0/DATAFILE/system.331.1007442879
+MGMT/ORCL/8823ED770D7F6DE2E053604AD60A84F0/DATAFILE/sysaux.332.1007442881
+MGMT/ORCL/8823ED770D7F6DE2E053604AD60A84F0/DATAFILE/undotbs1.330.1007442879
+MGMT/ORCL/8823ED770D7F6DE2E053604AD60A84F0/DATAFILE/undotbs1_temp.329.100744287
+MGMT/ORCL/8823ED770D7F6DE2E053604AD60A84F0/DATAFILE/users.334.1007442903
14 rows selected.
```

## Control Files -  对 Database 结构及行为进行管理和维护

```
SQL> select name from v$controlfile;
NAME
------------------------------------------------------------------------------------------------------------------------------
+MGMT/ORCL/CONTROLFILE/current.316.1007442203


SQL> show parameter spfile
NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
spfile                               string      +MGMT/ORCL/PARAMETERFILE/spfil
                                                 e.328.1007442695
```
## Redo Log Files
当生产环境使用 主从数据库 架构，
主库上的 Redo Log Files叫 主库联机重做日志文件(online redo log)
备库上的 Redo Log Files叫 备库联机重做日志文件(standby redo log)

* 查找日志文件位置

```
SQL> select member from v$logfile;
MEMBER
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
+MGMT/ORCL/ONLINELOG/group_2.318.1007442207
+MGMT/ORCL/ONLINELOG/group_1.317.1007442207
+MGMT/ORCL/ONLINELOG/group_3.326.1007442691
+MGMT/ORCL/ONLINELOG/group_4.327.1007442693
```








----------------------

## Archived Log Files 归档日志文件