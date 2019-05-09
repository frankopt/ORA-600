# 用户进程

![](https://ws4.sinaimg.cn/large/006tNc79gy1g2qj7ubjzij30q00idk5w.jpg)

## 远程连接：
用户进程   -- TCP/IP协议（三次握手） --  Oracle服务器进程，
产生进程(会话)信息，保存在 PGA

![](https://ws4.sinaimg.cn/large/006tNc79gy1g2qjbhndl9j30h20bojt2.jpg)

## 用户进程信息
```
SQL> desc v$session
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 SADDR                                              RAW(8)
 SID                                                NUMBER
 SERIAL#                                            NUMBER
 AUDSID                                             NUMBER
 PADDR                                              RAW(8)
 USER#                                              NUMBER
 USERNAME                                           VARCHAR2(128)
 COMMAND                                            NUMBER
 OWNERID                                            NUMBER
 
 SQL> select server,process,machine,program,paddr from v$session;

SERVER      PROCESS    MACHINE                          PROGRAM         PADDR
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