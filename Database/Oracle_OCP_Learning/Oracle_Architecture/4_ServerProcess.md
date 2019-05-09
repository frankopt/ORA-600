# 服务器进程 v$process
所有的用户进程均要与服务器进程进行交互
* dedicate 用户进程与服务器进程1对1
* none 用户进程与服务器进程1对多

![](https://ws4.sinaimg.cn/large/006tNc79gy1g2qjbhndl9j30h20bojt2.jpg)

```
 SQL> select server,process,machine,program,paddr from v$session;

SERVER      PROCESS    MACHINE                          PROGRAM         PADDR(内存的进程地址)
-----------------------------------------------------------------------
DEDICATED     24605   rws00cre.us.oracle.com       oracle@rws00cre.us.oracle.com (PMON)     0000000084532220


SQL> select spid from v$process where addr='0000000084532220';
SPID
------------------------
24605


SQL> ho ps -ef | grep 24605
crsusr   21175 18772  0 09:28 pts/8    00:00:00 /bin/bash -c ps -ef | grep 24605
crsusr   21177 21175  0 09:28 pts/8    00:00:00 grep 24605
racusr   24605     1  0 May05 ?        00:00:06 ora_pmon_orcl1

```



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
 BACKGROUND                                         VARCHAR2(1)
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
```

## 服务器进程的信息查询
```
SQL> select spid from v$process where addr in (select paddr from v$session where username='SYS');
SPID
------------------------
24723
18773
31081

SQL> ho ps -ef | grep 24723
crsusr    5695 31080  0 10:20 pts/10   00:00:00 /bin/bash -c ps -ef | grep 24723
crsusr    5697  5695  0 10:20 pts/10   00:00:00 grep 24723
racusr   24723     1  0 May05 ?        00:00:02 ora_ofsd_orcl1

SQL> ho ps -ef | grep 18773
crsusr    9390 31080  0 10:23 pts/10   00:00:00 /bin/bash -c ps -ef | grep 18773
crsusr    9392  9390  0 10:23 pts/10   00:00:00 grep 18773
racusr   18773 18772  0 08:17 ?        00:00:00 oracleorcl1 (DESCRIPTION=(LOCAL=YES)(ADDRESS=(PROTOCOL=beq)))
```

```
$ top -p 18773

top - 10:24:48 up 1 day, 20:54, 10 users,  load average: 0.44, 0.39, 0.48
Tasks:   1 total,   0 running,   1 sleeping,   0 stopped,   0 zombie
%Cpu(s):  4.4 us,  3.3 sy,  0.0 ni, 90.4 id,  1.5 wa,  0.0 hi,  0.2 si,  0.4 st
KiB Mem : 23320224 total,   462620 free,  8595692 used, 14261912 buff/cache
KiB Swap: 19989484 total, 19987180 free,     2304 used.  1658604 avail Mem
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
18773 racusr    20   0 3348600 149024 142976 S   0.0  0.6   0:00.08 oracle_18773_or
```

## PGA
从11g开始，有 SGA+PGA 全自动管理，会控制其总的大小。
* PGA 在32位系统上，最大1.7G; 64位系统上，最大4G

```
SQL> show parameter pga
NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
pga_aggregate_limit                  big integer 2G
pga_aggregate_target                 big integer 832M
```

修改 PGA 大小

```
SQL> alter system set pga_aggregate_target=3g;
```

## Kill -9 SPID 可以中断进程