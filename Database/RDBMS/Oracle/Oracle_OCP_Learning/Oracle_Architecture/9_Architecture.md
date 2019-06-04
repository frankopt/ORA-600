

# 进程体系结构
![](https://ws1.sinaimg.cn/large/006tNc79ly1g2vbinha4dj30my0gpdsi.jpg)
## 1 用户进程 - 用于连接到Oracle Database
## 2 数据库进程

1. 服务器进程：用户建立会话时启动，可连接到Oracle Instance

2. 后台进程：启动 Oracle Instance时启动

* DBWR 数据库写进程：将Database Buffer Cache中修改的 缓冲区（灰数据缓冲区）

    写入磁盘的两种方式
（1）在执行其他处理时异步执行
（2）推进检查点

```
SQL> show parameter db_wr
NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
db_writer_processes                  integer     1
SQL> alter system set db_writer_processes=30
  2  ;
alter system set db_writer_processes=30
                 *
ERROR at line 1:
ORA-02095: specified initialization parameter cannot be modified
SQL> a scope=spfile
  1* alter system set db_writer_processes=30scope=spfile
SQL> /
System altered.
```

* LGWR 日志写进程：将 Redo Log Buffer 写入 Redo Log Files
    在以下情况下执行写操作：
    （1）User Process 提交事物处理
    （2）Redo Log Buffer 的 1/3 已满
    （3）DBWR进程将经过修改的缓冲区 写入磁盘前
    （4）每隔3s
    （5）每满 1M

* CKPT 检查点进程
    将检查点信息记录在以下位置：
    （1）控制文件
    （2）每个数据文件头
    
```
[Thu May 09 19:54:14][29289][root@rws00cre:/etc][0]# ps -ef | grep ora_ | grep orcl | grep ckpt
racusr   24793     1  0 May04 ?        00:03:43 ora_ckpt_orcl1

[Thu May 09 19:56:28][29289][root@rws00cre:/etc][0]# kill -9 24793

[Thu May 09 19:56:52][29289][root@rws00cre:/etc][1]# ps -ef | grep ora_ | grep orcl | grep ckpt
racusr   29033     1  0 19:57 ?        00:00:00 ora_ckpt_orcl1
<grid 产品高可用性 会restart 重要进程>
```

* SMON 系统监视进程
    （1）实例启动时执行恢复
    （2）清除不使用的临时段

* PMON 进程监视进程
    （1）用户进程 失败时 执行 进程恢复
    （2）监听会话是否发生空闲会话超时
    （3）将数据库服务动态注册到监听程序
    
* RECO 恢复器进程 - RAC集群使用
    （1）自动连接到 与有问题的分布式事物处理有关的 数据库
    （2）自动解决 有问题的事物处理
    （3）删除对应于有问题的事物处理的所有行
    


## 3 守护进程

* 网络监听程序
* Grid Infrastructure 守护进程

![](https://ws4.sinaimg.cn/large/006tNc79gy1g2w11mqsvvj30pj09ajym.jpg)

主要的进程服务：

| *ohas | 高可用服务 |
| --- | --- |
| ocssd | 集群就绪服务 |
| diskmon | 磁盘监控进程 |
| orarootagent | * |
| oraagent | * |
| cssdagent | * |

Oracle GI 20c 提供的完整服务：
```
[Thu May 09 20:00:53][29289][root@rws00cre:/etc][0]# ps -ef | grep /scratch/oracle/CrsHome/bin/
root       369     1  0 May04 ?        01:06:52 /scratch/oracle/CrsHome/bin/ohasd.bin reboot BLOCKING_STACK_LOCALE_OHAS=AMERICAN_AMERICA.AL32UTF8
root       476     1  0 May04 ?        00:20:35 /scratch/oracle/CrsHome/bin/orarootagent.bin
root       550 29289  0 20:00 pts/7    00:00:00 grep --color=auto /scratch/oracle/CrsHome/bin/
crsusr     661     1  0 May04 ?        00:23:17 /scratch/oracle/CrsHome/bin/oraagent.bin
crsusr     708     1  0 May04 ?        00:08:36 /scratch/oracle/CrsHome/bin/mdnsd.bin
crsusr     710     1  0 May04 ?        00:21:18 /scratch/oracle/CrsHome/bin/evmd.bin
crsusr     740     1  0 May04 ?        00:10:03 /scratch/oracle/CrsHome/bin/gpnpd.bin
crsusr     793   710  0 May04 ?        00:08:16 /scratch/oracle/CrsHome/bin/evmlogger.bin -o /scratch/oracle/CrsHome/log/[HOSTNAME]/evmd/evmlogger.info -l /scratch/oracle/CrsHome/log/[HOSTNAME]/evmd/evmlogger.log
crsusr     816     1  0 May04 ?        00:29:47 /scratch/oracle/CrsHome/bin/gipcd.bin
root       849     1  0 May04 ?        00:17:12 /scratch/oracle/CrsHome/bin/cssdmonitor
root       869     1  0 May04 ?        00:17:00 /scratch/oracle/CrsHome/bin/cssdagent
root       874     1  2 May04 ?        02:54:28 /scratch/oracle/CrsHome/bin/osysmond.bin
crsusr     906     1  0 May04 ?        00:50:36 /scratch/oracle/CrsHome/bin/onmd.bin  -S 1
crsusr     908     1  0 May04 ?        00:35:14 /scratch/oracle/CrsHome/bin/ocssd.bin  -S 1
root      1485     1  0 May04 ?        00:45:45 /scratch/oracle/CrsHome/bin/ologgerd -M
root      1502     1  0 May04 ?        00:22:43 /scratch/oracle/CrsHome/bin/octssd.bin reboot
root      1782     1  0 May04 ?        01:09:31 /scratch/oracle/CrsHome/bin/crsd.bin reboot
root      2704   874  0 May04 ?        00:07:41 /scratch/oracle/CrsHome/perl/bin/perl /scratch/oracle/CrsHome/bin/diagsnap.pl start
crsusr    3335     1  2 May04 ?        02:58:52 /scratch/oracle/CrsHome/bin/oraagent.bin
crsusr    3362     1  0 May04 ?        00:02:33 /scratch/oracle/CrsHome/bin/tnslsnr ASMNET1LSNR_ASM -no_crs_notify -inherit
crsusr    3756     1  0 May04 ?        00:15:04 /scratch/oracle/CrsHome/bin/gnsd.bin -trace-level 1 -ip-address 10.214.74.214 -startup-endpoint ipc://GNS_rws00cre_3312_e63bdf19f01c83a9
crsusr    4047     1  0 May04 ?        00:00:13 /scratch/oracle/CrsHome/bin/tnslsnr LISTENER_SCAN1 -no_crs_notify -inherit
crsusr    4067     1  0 May04 ?        00:00:13 /scratch/oracle/CrsHome/bin/tnslsnr LISTENER_SCAN2 -no_crs_notify -inherit
crsusr    4621     1  0 May04 ?        00:15:38 /scratch/oracle/CrsHome/bin/crscdpd.bin
crsusr    4652     1  0 May04 ?        00:15:45 /scratch/oracle/CrsHome/bin/crscdpd.bin
crsusr    7914  7164  0 May04 pts/2    00:00:06 /scratch/oracle/CrsHome/bin/sqlplus -S -N
crsusr    7926  7164  0 May04 pts/2    00:00:06 /scratch/oracle/CrsHome/bin/sqlplus -S -N
crsusr   10412     1  0 May04 ?        00:00:12 /scratch/oracle/CrsHome/bin/tnslsnr MGMTLSNR -no_crs_notify -inherit
crsusr   12612  9163  0 May04 ?        00:00:00 /bin/sh /scratch/oracle/CrsHome/bin/cluvfy comp healthcheck -mandatory -_format -_check_type partial
crsusr   16599     1  0 May05 ?        00:00:11 /scratch/oracle/CrsHome/bin/tnslsnr LISTENER -inherit
root     17875     1  1 13:35 ?        00:04:36 /scratch/oracle/CrsHome/bin/orarootagent.bin
crsusr   25744     1  0 May04 pts/2    00:00:00 /bin/sh /scratch/oracle/CrsHome/bin/cluvfy comp baseline -collect cluster -installer -homename grid -n all
racusr   28498     1  0 19:56 ?        00:00:00 /scratch/oracle/CrsHome/bin/oraagent.bin
crsusr   30228 12709  0 May04 ?        00:00:00 /usr/bin/ssh -o FallBackToRsh=no -o PasswordAuthentication=no -o StrictHostKeyChecking=yes -o NumberOfPasswordPrompts=0 rws00crf -n /bin/sh -c 'ORACLE_HOME=/scratch/oracle/CrsHome LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 NLS_LANG=American_America.UTF8 /scratch/oracle/CrsHome/bin/cluvfy comp software -json_file_only '
crsusr   32528 25782  0 May04 pts/2    00:00:00 /usr/bin/ssh -o FallBackToRsh=no -o PasswordAuthentication=no -o StrictHostKeyChecking=yes -o NumberOfPasswordPrompts=0 rws00crf -n /bin/sh -c 'ORACLE_HOME=/scratch/oracle/CrsHome LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 NLS_LANG=American_America.UTF8 /scratch/oracle/CrsHome/bin/cluvfy comp software -allfiles -json_file_only '
```

Oracle GI 安装程序 会修改 /etc/inittab 文件
确保
每次启动计算机在 设定的运行级别启动 Oracle GI