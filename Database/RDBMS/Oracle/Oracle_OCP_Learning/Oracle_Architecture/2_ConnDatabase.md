# 如何连接到数据库
* 程序访问数据库，需要安装驱动程序
![](https://ws3.sinaimg.cn/large/006tNc79gy1g2qikv5nyvj30hs0bujs2.jpg)

```
JAVA 调用 Database

<jdbc 1.8版本的 JDK 包>
[crsusr@rws00cre:/scratch/oracle/CrsHome/jdbc/lib][0]$ ls
ojdbc8dms_g.jar  ojdbc8dms.jar  ojdbc8_g.jar  ojdbc8.jar  simplefan.jar
```

* 客户端工具访问数据库，需要把Oracle中的监听打开，配置Oracle当中的本地命名

1. sqlplus
2. sqldevelop
3. toad
4. pl/sql developer
...


查看监听是否跑起来？
```
[Sun May 05 07:55:59][25994][crsusr@rws00cre:/scratch/oracle/CrsHome/network/admin][0]$ lsnrctl status
LSNRCTL for Linux: Version 20.0.0.0.0 - Development on 05-MAY-2019 07:56:05
Copyright (c) 1991, 2019, Oracle.  All rights reserved.
Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=IPC)(KEY=LISTENER)))
STATUS of the LISTENER
------------------------
Alias                     LISTENER
Version                   TNSLSNR for Linux: Version 20.0.0.0.0 - Development
Start Date                05-MAY-2019 07:41:42
Uptime                    0 days 0 hr. 14 min. 23 sec
Trace Level               off
Security                  ON: Local OS Authentication
SNMP                      OFF
Listener Parameter File   /scratch/oracle/CrsHome/network/admin/listener.ora
Listener Log File         /scratch/oracle/crsbase/diag/tnslsnr/rws00cre/listener/alert/log.xml
Listening Endpoints Summary...
  (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=LISTENER)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=10.214.74.96)(PORT=1521)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=10.214.74.164)(PORT=1521)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=rws00cre.us.oracle.com)(PORT=5500))(Security=(my_wallet_directory=/scratch/oracle/base/homes/OraDB20Home1/admin/orcl/xdb_wallet))(Presentation=HTTP)(Session=RAW))
Services Summary...
Service "+APX" has 1 instance(s).
  Instance "+APX1", status READY, has 1 handler(s) for this service...
Service "+ASM" has 1 instance(s).
  Instance "+ASM1", status READY, has 1 handler(s) for this service...
Service "+ASM_DATA" has 1 instance(s).
  Instance "+ASM1", status READY, has 1 handler(s) for this service...
Service "+ASM_MAY" has 1 instance(s).
  Instance "+ASM1", status READY, has 1 handler(s) for this service...
Service "+ASM_MGMT" has 1 instance(s).
  Instance "+ASM1", status READY, has 1 handler(s) for this service...
Service "+IOS" has 1 instance(s).
  Instance "+IOS1", status READY, has 1 handler(s) for this service...
Service "87e6d80ee2a50825e053aa04e80af7e5.us.oracle.com" has 1 instance(s).
  Instance "orcl1", status READY, has 1 handler(s) for this service...
Service "8823ed770d7f6de2e053604ad60a84f0.us.oracle.com" has 1 instance(s).
  Instance "orcl1", status READY, has 1 handler(s) for this service...
Service "orcl.us.oracle.com" has 1 instance(s).
  Instance "orcl1", status READY, has 1 handler(s) for this service...
Service "orclXDB.us.oracle.com" has 1 instance(s).
  Instance "orcl1", status READY, has 1 handler(s) for this service...
Service "pdb.us.oracle.com" has 1 instance(s).
  Instance "orcl1", status READY, has 1 handler(s) for this service...
The command completed successfully
```

连接CDB
```
sqlplus sys/Welcome1@10.214.74.96:1521/orcl.us.oracle.com as sysdba

```

连接PDB
```
sqlplus sys/Welcome1@10.214.74.96:1521/pdb.us.oracle.com as sysdba

```

查看服务名
```
SQL> show con_name
CON_NAME
------------------------------
CDB$ROOT


SQL> show parameter service_name
NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
service_names                        string      orcl.us.oracle.com


SQL> show parameter dispatcher
NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
dispatchers                          string      (PROTOCOL=TCP) (SERVICE=orclXD
                                                 B)
enable_dnfs_dispatcher               boolean     FALSE
max_dispatchers                      integer


SQL> select name from v$pdbs;
NAME
--------------------------------------------------------------------------------------------------------------------------------
PDB$SEED
PDB
```


在实际应用中，调用PDB 要先配置好tnsnames.ora 文件，
通过这种方式调用PDB比较实用安全

```
Service "orcl.us.oracle.com" has 1 instance(s).
Service "orclXDB.us.oracle.com" has 1 instance(s).
Service "pdb.us.oracle.com" has 1 instance(s).
```

```

sqlplus scott/tiger@pdb.us.oracle.com
```