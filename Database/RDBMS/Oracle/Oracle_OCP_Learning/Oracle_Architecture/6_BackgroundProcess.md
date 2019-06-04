# Instance后台进程

Instance = SGA + Background_Process

![](https://ws4.sinaimg.cn/large/006tNc79gy1g2qjbhndl9j30h20bojt2.jpg)

### CKPT 维护数据库一致性的后台进程
下面三个文件的 时间戳 必须相同
* Data Files
* Control Files
* Redo Log Files

数据库才能正常启动。

**用户进程发出 事物提交、DML、DDL、DCL，均会触发 CKPT。
查询操作不会触发。**

### DBWR <数据写进程> ---> Data Files
将 Database Buffer Cache中的数据写入到 Data Files所在的磁盘上去

### LGWR <日志写进程：写的频率较快>
将Redo Log Buffer中的 更改 记录到 Redo Log Files中


> 以上 三个进程 能保证数据库不丢数据


### SMON:System_MON

## PMON:Process_MON



1. 查看后台进程

```
SQL> desc v$process
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 ADDR                                               RAW(8)
 PID                                                NUMBER
 SOSID                                              VARCHAR2(24)
 SPID                                               VARCHAR2(24)
 STID                                               VARCHAR2(24)
 EXECUTION_TYPE                                     VARCHAR2(20)
 PNAME                                              VARCHAR2(5)
 USERNAME                                           VARCHAR2(15)
 SERIAL#                                            NUMBER
 TERMINAL                                           VARCHAR2(30)
 PROGRAM                                            VARCHAR2(84)
 TRACEID                                            VARCHAR2(255)
 TRACEFILE                                          VARCHAR2(513)
 /**BACKGROUND**/                                   VARCHAR2(1)
 LATCHWAIT                                          VARCHAR2(16)
 LATCHSPIN                                          VARCHAR2(16)
 PGA_USED_MEM                                       NUMBER
 PGA_ALLOC_MEM                                      NUMBER
 PGA_FREEABLE_MEM                                   NUMBER
 PGA_MAX_MEM                                        NUMBER
 NUMA_DEFAULT                                       NUMBER
 NUMA_CURR                                          NUMBER
 CPU_USED                                           NUMBER
 CON_ID                                             NUMBER

SQL> desc v$bgprocess
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 PADDR                                              RAW(8)
 PSERIAL#                                           NUMBER
 NAME                                               VARCHAR2(5)
 DESCRIPTION                                        VARCHAR2(64)
 ERROR                                              NUMBER
 TYPE                                               VARCHAR2(5)
 PRIORITY                                           VARCHAR2(8)
 CON_ID                                             NUMBER
```

```
SQL> select paddr,name from v$bgprocess;
PADDR            NAME
---------------- -----
00 (两个0 表示未启动后台进程)  ABMR
00               ACFS
00               AMB1
00               AMB2
00               AMB3
...
```
查看当前正在使用的后台进程 个数
```
SQL> select paddr,name from v$bgprocess where paddr<>'00'; 
注: <> 不等于
PADDR            NAME
---------------- -----
0000000084532220 PMON
00000000845337E8 CLMN
0000000084534DB0 PSP0
0000000084536378 IPC0
0000000084537940 VKTM
0000000084538F08 GEN0
000000008453A4D0 MMAN
000000008453BA98 LCK0
000000008453D060 GEN1
000000008453E628 SCMN
000000008453FBF0 DIAG
...
88 rows selected.
```