# RAC (Real Application Cluster) 架构


## 1 What is RAC?

依托一组共享的数据库，在集群中的不同服务器上运行多个数据库实例。该数据库跨越多个硬件系统，但是在应用程序看来，它是一个统一的数据库。
这样就能利用商用硬件降低总拥有成本并为支持各种应用程序负载提供一个可伸缩的计算环境。

## 2 Why RAC?
1. 数据库 数据量和访问量 快速增长，单一设备无法承担。
2. 单硬件的升级有性能天花板，通过几个中小服务器组件集群，可实现数据库的持续扩展和负载均衡。
3. 单节点故障下，集群系统可转移故障节点应用数据，实现高可用。
4. 实现数据冗余备份。

![](http://ww2.sinaimg.cn/large/006tNc79gy1g3p4dwevtqj30cd0a4dit.jpg)

## 3 市面上的数据库集群产品
* 基于数据库引擎：
    * Oracle RAC
    * AWS EC2
    * Microsoft MSCS
    * IBM DB2UDB
    * Sybase ASE

* 基于数据库网关（中间件）：
    * ICX-UDS

## 4 Oracle RAC 概述
Oracle RAC的核心是共享磁盘子系统，集群中所有节点必须能够访问所有数据、重做日志文件、控制文件和参数文件。

RAC 为Oracle数据库提供了最高级别的可用性、可伸缩性和低成本计算能力。如果集群内的一个节点发生故障，Oracle可以在其余节点上继续运行。

Key Feature：**Cache Fusion 缓存融合**
缓存融合使得节点通过集群互联同步其 高速缓存，从而最大限度地低降低磁盘 I/O。
 - - - Oracle 是唯一具备这一能力的数据库厂商

> Cache Fusion 就是通过互联网络（高速的 Private interconnect）在集群内各节点的 SGA 之间进行块传递，这是RAC最核心的工作机制，他把所有实例的SGA虚拟成一个大的SGA区，每当不同的实例请求相同的数据块时，这个数据块就通过 Private interconnect 在实例间进行传递。以避免首先将块推送到磁盘，然后再重新读入其他实例的缓存中这样一种低效的实现方式(OPS 的实现)。当一个块被读入 RAC 环境中某个实例的缓存时，该块会被赋予一个锁资源（与行级锁不同），以确保其他实例知道该块正在被使用。之后，如果另一个实例请求该块的一个副本，而该块已经处于前一个实例的缓存内，那么该块会通过互联网络直接被传递到另一个实例的 SGA。如果内存中的块已经被改变，但改变尚未提交，那么将会传递一个 CR 副本。这就意味着只要可能，数据块无需写回磁盘即可在各实例的缓存之间移动，从而避免了同步多实例的缓存所花费的额外 I/O。很明显，不同的实例缓存的数据可以是不同的，也就是在一个实例要访问特定块之前，而它又从未访问过这个块，那么它要么从其他实例 cache fusion 过来，或者从磁盘中读入。GCS（Global Cache Service，全局内存服务）和 GES（Global EnquenceService，全局队列服务）进程管理使用集群节点之间的数据块同步互联。


## 5 RAC 体系结构
![](https://ws1.sinaimg.cn/large/006tNc79gy1g2wluvuhekj30se0l2433.jpg)

#### 5.1 Oracle Clusterware Architecture
一个RAC Cluster包含：
    1. >= 2个节点
    2. private network - 处理节点间通信 与 cache fusion
    3. public network - 客户端和应用 访问
    4. shared storage


#### 5.2 Oracle Clusterware Networking

集群各节点之间通过 心跳线 互联，通过心跳确定 成员信息、在某个时间点的运行状况，保证集群的正常运行。

![](https://ws4.sinaimg.cn/large/006tNc79ly1g2wma1s2rtj30ff07mdg5.jpg)

* 每个节点至少 2 个 network adapter
* private network adapter 只需要支持 TCP/IP
* public network 需支持 TCP/IP，DNS

NAS（network attached storage）
iSCSI

当一个客户端发送请求到某一台服务器的listener之后，这台服务器根据load balance策略，会把请求发送给本机的RAC组件处理。

##### 5.2.1 private network
private network 通常是用千兆以太网构建，每个集群节点通过专用高速网络连接到所有其他节点。
Oracle Cache Fusion 技术使用这种网络将每个主机的物理内存 (RAM) 有效地组合成一个高速缓存。某个 Oracle 实例高速缓存中存储的数据允许其他实例访问，还通过在集群节点中传输锁定和其他同步信息保持数据完整性和高速缓存一致性。

#### 5.3 Oracle Clusterware 后台进程

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
* ora.storage：因为ora.crsd -init并不非得依赖于本地的ASM，所以引入了一个ora.storage资源，表示只要这个cluster-wide的范围内能够访问到ASM disk即可。ora.storage的主要任务就是确保OCR能够访问，如果OCR放在ASM上面，只要确保loca ASM instance running。在第一个node上面，先起ora.asm -init资源，再起ora.storage资源；在其他node上面，先起ora.storage资源，再起ora.asm -init资源。如果ora.storage资源被disable掉了，那么，正在运行的GI stack不会受到任何影响，因为一旦ora.storage起来了，它的使命就完成了，CRSD就会自己去和ASM instance去通信了；但是，下次GI stack启动就无法起来了，“ora.asm -init”资源和ASM instance自己可以起来，但是ora.crsd却起不来，这是因为ora.crsd的启动依赖于ora.storage。如果disable了第二个Hub的ora.storage，重启这个Hub上面的GI stack，它上面的ora.ctssd、“ora.asm -init”和ocssd.bin都可以起来，但是ora.crsd/crsd.bin和ora.storage都起不来了，Local ASM instance也根本不会尝试启动的。

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

#### 5.4 RAC 共享存储
OCR 和 Votedisk 以及数据文件都需要放到共享存储中。


-------

#### 5.5 RAC 相关组件

##### 5.5.1 GPnP Profile

![](https://ws2.sinaimg.cn/large/006tNc79gy1g2xeqnjbsdj30r40jgjvx.jpg)

```
cat /scratch/oracle/CrsHome/gpnp/profiles/peer/profile.xml

<?xml version="1.0" encoding="UTF-8"?><gpnp:GPnP-Profile Version="1.0" xmlns="http://www.grid-pnp.org/2005/11/gpnp-profile" xmlns:gpnp="http://www.grid-pnp.org/2005/11/gpnp-profile" xmlns:orcl="http://www.oracle.com/gpnp/2005/11/gpnp-profile" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.grid-pnp.org/2005/11/gpnp-profile gpnp-profile.xsd" ProfileSequence="6" ClusterUId="c5f6b0b50aa06ff0ffeb5544adf4e873" ClusterName="rws00cr-cluster" PALocation=""><gpnp:Network-Profile><gpnp:HostNetwork id="gen" HostName="*"><gpnp:Network id="net1" IP="10.214.64.0" Adapter="eth0" Use="public"/><gpnp:Network id="net2" IP="10.196.0.0" Adapter="eth1" Use="asm,cluster_interconnect"/></gpnp:HostNetwork></gpnp:Network-Profile><orcl:CSS-Profile id="css" DiscoveryString="+asm" LeaseDuration="400"/><orcl:ASM-Profile id="asm" DiscoveryString="/dev/fdisk/,AFD:*" SPFile="+DATA/rws00cr-cluster/ASMPARAMETERFILE/registry.253.1007389541" Mode="remote" Extended="false"/><orcl:BC-BigCluster id="bc" DiscoveryVIP="rws00crecrh-g"/><ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:SignedInfo><ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/><ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/><ds:Reference URI=""><ds:Transforms><ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/><ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"> <InclusiveNamespaces xmlns="http://www.w3.org/2001/10/xml-exc-c14n#" PrefixList="gpnp orcl xsi"/></ds:Transform></ds:Transforms><ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/><ds:DigestValue>coc6ZrlXHhQkXFnNo9E2Nq9dIfk=</ds:DigestValue></ds:Reference></ds:SignedInfo><ds:SignatureValue>bdJHdBfNuJwYgz/aNAHAbxDvMyLAtBDazJwaxFZ2LAS0Q9ahqRTC92FYob5HD/DyXzp7J4zH6VLX83QAYkkylMg8DPnT4RXw0BWZlNiBVAkX6Z7fsoutSCCj1LZ5PnulHCmeyoJpf6HAYC643N9VjnGEnEqQFdqQ2w9SMIASvFc=</ds:SignatureValue></ds:Signature></gpnp:GPnP-Profile>
```

##### 5.5.2 GNS (Grid Naming Service) 


##### 5.5.3 SCAN (Single Client Access Name)
is the address used by clients connecting to the cluster

##### 5.5.4 OCR （Oracle Cluster Registry ）
The OCR contains cluster and database configuration information for RAC and Cluster Ready Services (CRS) such as the cluster node list, and cluster database instances to node mapping, and CRS application resource profiles.  The OCR is a shared file located in a cluster file system.  

* 大小通常是 100M - 1G
* OCR最多只能有2个。Primary OCR and Mirror OCR，两个OCR磁盘互为镜像，以防止OCR磁盘的单点故障

```
1. 校验OCR文件
# ocrcheck
Status of Oracle Cluster Registry is as follows :
         Version                  :          4
         Total space (kbytes)     :     491684
         Used space (kbytes)      :      86572
         Available space (kbytes) :     405112
         ID                       : 1882045584
         Device/File Name         :      +DATA    <-- OCR (primary)
                                    Device/File integrity check succeeded
                                    Device/File not configured <-- OCR Mirror (not configured)
                                    Device/File not configured
                                    Device/File not configured
                                    Device/File not configured
         Cluster registry integrity check succeeded
         Logical corruption check succeeded

2. GI安装过程中，会提示用户指定OCR安装位置，此位置记录在如下文件中
# more /etc/oracle/ocr.loc
#Device/file +DATA getting replaced by device +DATA/rws00cr-cluster/OCRFILE/registry.255.1009179037
ocrconfig_loc=+DATA/rws00cr-cluster/OCRFILE/registry.255.1009179037
local_only=false
```


##### 5.5.5 Voting Disk
Voting Disk 这个文件主要用于记录节点成员状态，在出现脑裂时，决定那个 Partion 获得控制权，其他的Partion 必须从集群中剔除。在安装 Clusterware 时也会提示指定这个位置。

```
# crsctl query css votedisk
##  STATE    File Universal Id                File Name Disk group
--  -----    -----------------                --------- ---------
 1. ONLINE   706feb81507a4fd7bf3d981e4e920d4a (AFD:DATA1) [DATA]
Located 1 voting disk(s).
```

## 6 集群数据库的访问 gv$

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

## 7 RAC 瓶颈 和 限制
* 优点
ORACLE RAC是目前市面上真正唯一做到并行模式的集群，RAC的所有集群成员都可以同时接收客户端请求，这样我们将能使用较低廉的服务器来实现高可用性、高吞吐量的集群环境，这要比通过对某台高端服务器增加硬件实现高可用性、高吞吐量花费的成本低很多。

* 存在的问题
    * 部署困难 - 涉及 服务器、存储设备、网卡、操作系统等多方面技术
    * 架构复杂 - 对硬件设备的稳定性、设备与操作系统的兼容性上要求较高
    * 实际千兆网络环境中，从单机环境迁移到RAC，系统性能不一定提升



## 参考文档
[RAC相关基础知识](https://www.cnblogs.com/lhrbest/p/7076782.html)

