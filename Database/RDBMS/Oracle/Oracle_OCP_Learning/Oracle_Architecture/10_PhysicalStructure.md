


# Oracle存储体系 - 物理结构

## 数据文件

## 控制文件

## 联机重做日志文件

## 归档重做日志文件

## 备份文件

## 参数文件

## 口令文件

## 告警日志 & 跟踪文件

查看数据库告警日志所在位置：
```
SQL> show parameter background_dump_dest
NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
background_dump_dest                 string      /scratch/oracle/base/homes/Ora
                                                 DB20Home1/rdbms/log
                                                 
SQL> ho ls -l /scratch/oracle/base/homes/OraDB20Home1/rdbms/log
total 700
drwxr-x--- 2 racusr oinstall   4096 May  5 05:10 8823C77EFDCC5E2FE053604AD60A7CCB
drwxr-x--- 2 racusr oinstall   4096 May  5 05:15 8823ED770D7F6DE2E053604AD60A84F0
-rw-r----- 1 racusr oinstall    173 May  5 05:08 dp.log
drwxr-x--- 3 racusr dba        4096 May  9 19:57 opatch
-rw-r----- 1 racusr oinstall   1491 May  5 05:00 orcl1_ora_12787.trc
-rw-r----- 1 racusr oinstall    715 May  5 05:06 orcl1_ora_1375.trc
-rw-r----- 1 racusr oinstall   1489 May  5 05:06 orcl1_ora_1383.trc
-rw-r----- 1 racusr oinstall   1491 May  5 05:02 orcl1_ora_18063.trc
-rw-r----- 1 racusr oinstall   1491 May  5 05:03 orcl1_ora_20483.trc
-rw-r----- 1 racusr oinstall    717 May  5 05:13 orcl1_ora_24059.trc
-rw-r----- 1 racusr oinstall   1453 May  5 05:13 orcl1_ora_24282.trc
-rw-r----- 1 racusr oinstall   1453 May  9 19:56 orcl1_ora_28590.trc
-rw-r----- 1 racusr oinstall    120 May  5 05:08 qopatch.log
-rw-r----- 1 racusr oinstall   7909 May  9 19:57 qopatch_log.log
-rw-r----- 1 racusr dba         820 May  5 05:10 stout_orcl1_12074.txt
-rw-r----- 1 racusr dba         820 May  5 05:10 stout_orcl1_14765.txt
-rw-r--r-- 1 racusr dba      323478 May  5 05:10 xml_file_orcl1_12074.xml
-rw-r--r-- 1 racusr dba      323478 May  5 05:10 xml_file_orcl1_14765.xml                                                 
```