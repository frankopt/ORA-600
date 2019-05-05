# Oracle数据库 体系结构
* Oracle DB 的主要体系结构
* 内存结构
* 后台进程
* 逻辑存储与物理存储
* ASM




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