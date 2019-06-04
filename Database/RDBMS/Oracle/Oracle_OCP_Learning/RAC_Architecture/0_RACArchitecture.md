# RAC (Real Application Cluster) 架构

![](https://ws1.sinaimg.cn/large/006tNc79gy1g2wluvuhekj30se0l2433.jpg)

## 概述 What is Cluster?
集群：多台服务器提供一种 高可用、高性能、负载均衡、动态管理的功能。

包含RAC选件的Oracle数据库允许依托一组共享的数据库，在集群中的不同服务器上运行多个数据库实例。该数据库跨越多个硬件系统，但是在应用程序看来，它是一个统一的数据库。
这样就能利用商用硬件降低总拥有成本并为支持各种应用程序负载提供一个可伸缩的计算环境。

* Oracle RAC 是 Oracle首要的共享磁盘数据库集群技术。

![](http://ww2.sinaimg.cn/large/006tNc79gy1g3p4dwevtqj30cd0a4dit.jpg)

## Oracle Clusterware <集群>
* key part of Oracle_GI
* integrated with Oracle_ASM
* the basis for ACFS
* a foundation for Oracle RAC

Shared Disk 要求 能够 1 load balance 负载均衡 2 failover
没有ASM的情况下，RAID

## 1 Oracle Clusterware Networking
![](https://ws4.sinaimg.cn/large/006tNc79ly1g2wma1s2rtj30ff07mdg5.jpg)

* 每个节点至少 2 个 network adapter
* private network adapter 只需要支持 TCP/IP
* public network 需支持 TCP/IP，DNS

NAS（network attached storage）
iSCSI

## 2 Oracle Clusterware Architecture

init daemon.

![](https://ws2.sinaimg.cn/large/006tNc79ly1g2wmp7ybwrj30r80jcwix.jpg)

![](https://ws3.sinaimg.cn/large/006tNc79gy1g2xerc3ihoj30ec0dpn23.jpg)

* ohasd.bin reboot: 整个stack的最早的进程，kill掉机器不会重启，kill掉的话init.d会自动重启一个新的ohasd.bin。reboot表示它是OS reboot时自动启动的进程，如果是ohasd.bin restart，则表示它是被kill掉以后被init.d重启的进程。使用功能上没有区别，只是表示两种启动方式。
* ocssd.bin: 对应于crsctl stat res -init -t中的ora.cssd资源，是整个stack最关键的进程，如果kill掉这个进程的话，node会自动reboot
* cssdagent: ocssd.bin的agent进程，负责监控ocssd.bin的，它和cssdmonitor进程是同样的功能，用的是一样的代码，实质上是两份拷贝。这两者只要一个被kill掉的话，它自己会自动respawn，但是不能太频繁，否则会被disable掉，这时只能重启stack来enable。
* cssdmonitor: 对应于-init中的ora.cssdmonitor资源，它是cssd的agent进程，负责监控monitor ocssd的。
* octssd.bin: 对应于-init中的ora.ctssd资源，只负责cluster内部时间的同步，不是关键的进程，有两种运行模式：Observer和Active模式。
* diskmon.bin -d -f: 对应于-init中的ora.diskmon资源，主要负责disk的监控（包括对voting disk），如果启不来，后面的crs就无法正常启动了。11203上默认是offline的，除非是Exadata环境。（对应进程：$ch/bin/diskmon -d -f）
* crsd.bin reboot: 对应于-init中的ora.crsd资源
* evmd.bin: 对应于-init中的ora.evmd资源，该资源主要负责消息的管理，如果启不来，后面的crs就无法正常启动了。
  $ch/opmn/bin/ons -d: 对应于ora.ons（Oracle Notification Service）资源，它是消息传递的通道，负责传递evmd的消息
* gipcd.bin: 对应于-init中的ora.gipcd资源
* gpnpd.bin: 对应于-init中的ora.gpnpd资源，Grid Plugin and Play即插即用，负责node的身份验证，里面保存了这个cluster的所有node的map信息以及ASM的discovery_string和cluster_interconnect，用于添加和删除节点。如果没有成功启动的话，后面的整个stack就都启不来了。对于Rim node来说，Hub node会将GPnP profile的信息注册到GNS中去，Rim node通过GNS anchor来获取GPnP profile的信息。
* mdnsd.bin: 对应于-init中的ora.mdnsd资源
* ora.storage：因为ora.crsd -init并不非得依赖于本地的ASM，所以引入了一个ora.storage资源，表示只要这个cluster-wide的范围内能够访问到ASM disk即可。ora.storage的主要任务就是确保OCR能够访问，如果OCR放在ASM上面，只要确保loca ASM instance running。在第一个node上面，先起ora.asm -init资源，再起ora.storage资源；在其他node上面，先起ora.storage资源，再起ora.asm -init资源。如果ora.storage资源被disable掉了，那么，正在运行的GI stack不会受到任何影响，因为一旦ora.storage起来了，它的使命就完成了，CRSD就会自己去和ASM instance去通信了；但是，下次GI stack启动就无法起来了，“ora.asm -init”资源和ASM instance自己可以起来，但是ora.crsd却起不来，这是因为ora.crsd的启动依赖于ora.storage。
如果disable了第二个Hub的ora.storage，重启这个Hub上面的GI stack，它上面的ora.ctssd、“ora.asm -init”和ocssd.bin都可以起来，但是ora.crsd/crsd.bin和ora.storage都起不来了，Local ASM instance也根本不会尝试启动的。

```

[Fri May 10 19:14:06][26518][root@rws00cre:~][0]# crsctl stat res -init -t
--------------------------------------------------------------------------------
Name           Target  State        Server                   State details
--------------------------------------------------------------------------------
Cluster Resources
--------------------------------------------------------------------------------
ora.asm
      1        ONLINE  ONLINE       rws00cre                 Started,STABLE
ora.cluster_interconnect.haip
      1        ONLINE  ONLINE       rws00cre                 STABLE
ora.crf
      1        ONLINE  ONLINE       rws00cre                 STABLE
ora.crsd
      1        ONLINE  ONLINE       rws00cre                 STABLE
ora.cssd
      1        ONLINE  ONLINE       rws00cre                 STABLE
ora.cssdmonitor
      1        ONLINE  ONLINE       rws00cre                 STABLE
ora.ctssd
      1        ONLINE  ONLINE       rws00cre                 ACTIVE:0,STABLE
ora.diskmon
      1        OFFLINE OFFLINE                               STABLE
ora.driver.afd
      1        ONLINE  ONLINE       rws00cre                 STABLE
ora.drivers.acfs
      1        ONLINE  ONLINE       rws00cre                 STABLE
ora.evmd
      1        ONLINE  ONLINE       rws00cre                 STABLE
ora.gipcd
      1        ONLINE  ONLINE       rws00cre                 STABLE
ora.gpnpd
      1        ONLINE  ONLINE       rws00cre                 STABLE
ora.mdnsd
      1        ONLINE  ONLINE       rws00cre                 STABLE
ora.storage
      1        ONLINE  ONLINE       rws00cre                 STABLE
```

### GPnP Profile

![](https://ws2.sinaimg.cn/large/006tNc79gy1g2xeqnjbsdj30r40jgjvx.jpg)

```
cat /scratch/oracle/CrsHome/gpnp/profiles/peer/profile.xml

<?xml version="1.0" encoding="UTF-8"?><gpnp:GPnP-Profile Version="1.0" xmlns="http://www.grid-pnp.org/2005/11/gpnp-profile" xmlns:gpnp="http://www.grid-pnp.org/2005/11/gpnp-profile" xmlns:orcl="http://www.oracle.com/gpnp/2005/11/gpnp-profile" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.grid-pnp.org/2005/11/gpnp-profile gpnp-profile.xsd" ProfileSequence="6" ClusterUId="c5f6b0b50aa06ff0ffeb5544adf4e873" ClusterName="rws00cr-cluster" PALocation=""><gpnp:Network-Profile><gpnp:HostNetwork id="gen" HostName="*"><gpnp:Network id="net1" IP="10.214.64.0" Adapter="eth0" Use="public"/><gpnp:Network id="net2" IP="10.196.0.0" Adapter="eth1" Use="asm,cluster_interconnect"/></gpnp:HostNetwork></gpnp:Network-Profile><orcl:CSS-Profile id="css" DiscoveryString="+asm" LeaseDuration="400"/><orcl:ASM-Profile id="asm" DiscoveryString="/dev/fdisk/,AFD:*" SPFile="+DATA/rws00cr-cluster/ASMPARAMETERFILE/registry.253.1007389541" Mode="remote" Extended="false"/><orcl:BC-BigCluster id="bc" DiscoveryVIP="rws00crecrh-g"/><ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:SignedInfo><ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/><ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/><ds:Reference URI=""><ds:Transforms><ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/><ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"> <InclusiveNamespaces xmlns="http://www.w3.org/2001/10/xml-exc-c14n#" PrefixList="gpnp orcl xsi"/></ds:Transform></ds:Transforms><ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/><ds:DigestValue>coc6ZrlXHhQkXFnNo9E2Nq9dIfk=</ds:DigestValue></ds:Reference></ds:SignedInfo><ds:SignatureValue>bdJHdBfNuJwYgz/aNAHAbxDvMyLAtBDazJwaxFZ2LAS0Q9ahqRTC92FYob5HD/DyXzp7J4zH6VLX83QAYkkylMg8DPnT4RXw0BWZlNiBVAkX6Z7fsoutSCCj1LZ5PnulHCmeyoJpf6HAYC643N9VjnGEnEqQFdqQ2w9SMIASvFc=</ds:SignatureValue></ds:Signature></gpnp:GPnP-Profile>
```

### GNS (Grid Naming Service) 


### SCAN (Single Client Access Name)
is the address used by clients connecting to the cluster

### 集群数据库的访问 gv$

```
$ dsql  < ---- 连接本机数据库，而不是集群数据库
SQL*Plus: Release 20.0.0.0.0 - Development on Wed May 15 17:06:15 2019
Version 20.1.0.0.0
Copyright (c) 1982, 2019, Oracle.  All rights reserved.
Connected to:
Oracle Database 20c Enterprise Edition Release 20.0.0.0.0 - Development
Version 20.1.0.0.0

SQL> select name from v$database;
NAME
---------
ORCL

SQL> select instance_name from gv$instance;
INSTANCE_NAME
----------------
orcl1
orcl2

SQL> show parameter thread
NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
ofs_threads                          integer     4
parallel_threads_per_cpu             integer     1
thread     (线程号)                   integer     1
threaded_execution                   boolean     FALSE

线程号=1，此节点线程编号均为1 
# ps -ef | grep pmon
crsusr    1181     1  0 May04 ?        00:05:31 ios_pmon_+IOS1
crsusr    1675     1  0 May04 ?        00:00:54 asm_pmon_+ASM1
root      2255 29246  0 17:11 pts/7    00:00:00 grep --color=auto pmon
crsusr    8054     1  0 May04 ?        00:00:51 apx_pmon_+APX1
crsusr   10654     1  0 May04 ?        00:01:42 mdb_pmon_-MGMTDB
racusr   28784     1  0 May09 ?        00:00:34 ora_pmon_orcl1

SQL> show parameter undo_t
NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
undo_tablespace                      string      UNDOTBS1

```

## 瓶颈 和 限制
* 优点
ORACLE RAC是目前市面上真正唯一做到并行模式的集群，RAC的所有集群成员都可以同时接收客户端请求，这样我们将能使用较低廉的服务器来实现高可用性、高吞吐量的集群环境，这要比通过对某台高端服务器增加硬件实现高可用性、高吞吐量花费的成本低很多。

* 存在的问题
    * 部署困难 - 涉及 服务器、存储设备、网卡、操作系统等多方面技术
    * 架构复杂 - 对硬件设备的稳定性、设备与操作系统的兼容性上要求较高
    * 实际千兆网络环境中，从单机环境迁移到RAC，系统性能不一定提升





