# ASM (Automatic Storage Management) 实例
![](https://ws3.sinaimg.cn/large/006tNc79gy1g315h7g4wlj313a0h60wd.jpg)

```
# ps -ef | grep pmon
crsusr    1181     1  0 May04 ?        00:04:47 ios_pmon_+IOS1
crsusr    1675     1  0 May04 ?        00:00:47 asm_pmon_+ASM1
crsusr    8054     1  0 May04 ?        00:00:44 apx_pmon_+APX1
crsusr   10654     1  0 May04 ?        00:01:29 mdb_pmon_-MGMTDB
root     25962  8902  0 06:11 pts/0    00:00:00 grep --color=auto pmon
racusr   28784     1  0 May09 ?        00:00:25 ora_pmon_orcl1
```

## Initialization Parameters

| ALTER SYSTEM |
| --- |
| ALTER SESSION |

* INSTANCE_TYPE=ASM
* MEMORY_TARGET
* ASM_DISKGROUPS
* ASM_DISKSTRING
* ASM_POWER_LIMIT <负载均衡 粒度>
    *     default is 1
    *     allowable range is 0-11
* CLUSTER_DATABASE=TRUE <集群>

## Manage ASM instance and associated process
1. Use SRVCTL (Sever Control Utility) to start / stop ASM Instance
2. conn ASM

```
[Tue May 14 06:29:12][7764][crsusr@rws00cre:~][0]$ export ORACLE_SID=+ASM1
[Tue May 14 06:29:20][7764][crsusr@rws00cre:~][0]$ export ORACLE_HOME=/scratch/oracle/CrsHome
[Tue May 14 06:29:24][7764][crsusr@rws00cre:~][0]$ export PATH=$ORACLE_HOME/bin:$PATH
[Tue May 14 06:29:30][7764][crsusr@rws00cre:~][0]$ sqlplus "/as sysasm"
SQL*Plus: Release 20.0.0.0.0 - Development on Tue May 14 06:29:35 2019
Version 20.1.0.0.0
Copyright (c) 1982, 2019, Oracle.  All rights reserved.
Connected to:
Oracle Database 20c Enterprise Edition Release 20.0.0.0.0 - Development
Version 20.1.0.0.0
SQL>
```


## Monitor ASM using V$ASM dynamic performance views
1. ASM-related views

* V$ASM_DISK <---important
* V$ASM_DISKGROUP <---important
* V$ASM_DISK_IOSTAT
* V$ASM_FILE
* V$ASM_DISKGROUP_STAT
* V$ASM_ACFSVOLUME
* V$ASM_OPERATION
* V$ASM_TEMPLATE
* V$ASM_FILESYSTEM
* V$ASM_CLIENT

```
$ asmcmd ls DATA/rws00cr-cluster/OCRFILE/
REGISTRY.255.1007389551
```
