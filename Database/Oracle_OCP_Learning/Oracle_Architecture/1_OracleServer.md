# Oracle数据库 体系结构
* Oracle DB 的主要体系结构
* 内存结构
* 后台进程
* 逻辑存储与物理存储
* ASM

![](https://ws2.sinaimg.cn/large/006tNc79gy1g2v6gof5znj30je0bc7d0.jpg)


![](https://ws4.sinaimg.cn/large/006tNc79gy1g2qjbhndl9j30h20bojt2.jpg)


| Oracle Server |  |  |
| --- | --- | --- |
|  | Instance | Database |

Instance: 处理数据库中大部分的操作
DB: 表空间、日志/数据文件、视图

```
alias dsql='export ORACLE_HOME= && export ORACLE_SID= && rlwrap /bin/sqlplus "/ as sysdba"'

[Sun May 05 05:55:02][11819][crsusr@rws00cre:~][0]$ dsql
SQL*Plus: Release 20.0.0.0.0 - Development on Sun May 5 05:55:03 2019
Version 20.1.0.0.0
Copyright (c) 1982, 2019, Oracle.  All rights reserved.
Connected to:
Oracle Database 20c Enterprise Edition Release 20.0.0.0.0 - Development
Version 20.1.0.0.0
SQL>  


<显示CDB名称>
SQL> show con_name
CON_NAME
------------------------------
CDB$ROOT

<显示CDB编号>
SQL> show con_id
CON_ID
------------------------------
1
```

## 访问 Instance
```
SQL> select instance_name from v$instance;

INSTANCE_NAME
----------------
orcl1
```

## 访问 Database - CDB
```
SQL> select name from v$database;

NAME
--------
ORCL

SQL> select db_unique_name from v$database;
DB_UNIQUE_NAME
------------------------------
orcl
```


```
<mount后 物理结构 可用>
SQL> alter database mount;
alter database mount
*
ERROR at line 1:
ORA-01100: database already mounted

<open后 逻辑结构 可用>
SQL> alter database open;
alter database open
*
ERROR at line 1:
ORA-01531: a database already open by the instance
```

## 访问 Database - PDB
```
SQL> desc v$pdbs
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 CON_ID                                             NUMBER
 DBID                                               NUMBER
 CON_UID                                            NUMBER
 GUID                                               RAW(16)
 NAME                                               VARCHAR2(128)
 OPEN_MODE                                          VARCHAR2(10)
 RESTRICTED                                         VARCHAR2(3)
 OPEN_TIME                                          TIMESTAMP(3) WITH TIME ZONE
 CREATE_SCN                                         NUMBER
 TOTAL_SIZE                                         NUMBER
 BLOCK_SIZE                                         NUMBER
 RECOVERY_STATUS                                    VARCHAR2(26)
 SNAPSHOT_PARENT_CON_ID                             NUMBER
 APPLICATION_ROOT                                   VARCHAR2(3)
 APPLICATION_PDB                                    VARCHAR2(3)
 APPLICATION_SEED                                   VARCHAR2(3)
 APPLICATION_ROOT_CON_ID                            NUMBER
 APPLICATION_ROOT_CLONE                             VARCHAR2(3)
 PROXY_PDB                                          VARCHAR2(3)
 LOCAL_UNDO                                         NUMBER
 UNDO_SCN                                           NUMBER
 UNDO_TIMESTAMP                                     DATE
 CREATION_TIME                                      DATE
 DIAGNOSTICS_SIZE                                   NUMBER
 PDB_COUNT                                          NUMBER
 AUDIT_FILES_SIZE                                   NUMBER
 MAX_SIZE                                           NUMBER
 MAX_DIAGNOSTICS_SIZE                               NUMBER
 MAX_AUDIT_SIZE                                     NUMBER
 LAST_CHANGED_BY                                    VARCHAR2(11)
 TEMPLATE                                           VARCHAR2(3)
 TENANT_ID                                          VARCHAR2(256)
 UPGRADE_LEVEL                                      NUMBER
 GUID_BASE64                                        VARCHAR2(30)
 
 SQL> select con_id,name from v$pdbs;
    CON_ID NAME
---------- -----------------------
         2 PDB$SEED  <Oracle PDB 模板，永远处于mount状态，但不能open，用于克隆新的PDB>
         3 PDB <自己创建的完整PDB，可在上面run实际应用程序>

```

此处报错 **ORA-12170**
```
[Sun May 05 06:20:02][27809][crsusr@rws00cre:~][0]$ sqlplus sys/Welcome1@orcl.com:1521/pdb as sysdba
SQL*Plus: Release 20.0.0.0.0 - Development on Sun May 5 06:20:04 2019
Version 20.1.0.0.0
Copyright (c) 1982, 2019, Oracle.  All rights reserved.
ERROR:
ORA-12170: TNS:Connect timeout occurred
Enter user-name:
```


修正：

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
其中，
```
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=10.214.74.96)(PORT=1521)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=10.214.74.164)(PORT=1521)))
  
Service "orcl.us.oracle.com" has 1 instance(s).
Service "orclXDB.us.oracle.com" has 1 instance(s).
Service "pdb.us.oracle.com" has 1 instance(s).
```
连接CDB
```
sqlplus sys/Welcome1@10.214.74.96:1521/orcl.us.oracle.com as sysdba

```

连接PDB
```
sqlplus sys/Welcome1@10.214.74.96:1521/pdb.us.oracle.com as sysdba

```