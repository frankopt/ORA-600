# SQLPLUS 连接

字符界面

## sqlplus 连接

* 本地连接

>  ps -ef | grep pmon
>  export ORACLE_SID= orcl
>  export ORACLE_HOME=/scratch/base/OraHome
>  export PATH=$ORACLE_HOME/bin:$PATH
>  sqlplus "/as sysdba"

```
$ sqlplus / as sysdba

SQL*Plus: Release 20.0.0.0 - Development on Yhu Apr 25 18:14:08 2019
Version 20.1.0.0.0
Copyright(c) 1982,2019 Oracle. All rights reserved.

Connect to:
Oracle Database 20c Enterprise Edition Release 20.0.0.0.0 - Development Version 20.1.0.0.0

SQL> select open_mode from v$database;
<查看数据库 有没有启动>

OPEN_MODE
---------
READ WRITE
```

* 网络连接

```
$ sqlplus sys/Welcome1@_______/orcl as sysdba
```
ps: 修改用户密码

```
sqlplus / as sysdba

SQL> alter user sys identified by Welcome1;
User altered. 
```

## sqlplus 连接
```
$ sqlplus / nolog

SQL> conn / as sysdba
Connected.

SQL> alter user scott identified by tiger account unlock;
User altered.

SQL> conn scott/tiger
Connected.

SQL> show user
USER is "SCOTT"


```

