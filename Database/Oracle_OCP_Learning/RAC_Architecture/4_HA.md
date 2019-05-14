# Making Applications Highly Available with Oracle Clusterware
# RAC 应用高可用管理
![](https://ws1.sinaimg.cn/large/006tNc79ly1g30w928vh7j30ot0d0ad5.jpg)
## High Availability Components
组件包括：
* resource / resource dependancy
* action program
* privileges
* application VIP
* ONS
* SCAN
* OCR

## Resource
有两种：本地 / 远程

```
$crsctl stat res -t
--------------------------------------------------------------------------------
Name           Target  State        Server                   State details
--------------------------------------------------------------------------------
Local Resources
--------------------------------------------------------------------------------
ora.LISTENER.lsnr
               ONLINE  ONLINE       rws00cri                 STABLE
               ONLINE  ONLINE       rws00crj                 STABLE
               ONLINE  ONLINE       rws00crk                 STABLE
               ONLINE  ONLINE       rws00crl                 STABLE
ora.ST.PRI.advm
               ONLINE  ONLINE       rws00cri                 STABLE
               ONLINE  ONLINE       rws00crj                 STABLE
               ONLINE  ONLINE       rws00crk                 STABLE
               ONLINE  ONLINE       rws00crl                 STABLE
ora.chad
               ONLINE  ONLINE       rws00cri                 STABLE
               ONLINE  ONLINE       rws00crj                 STABLE
               ONLINE  ONLINE       rws00crk                 STABLE
               ONLINE  ONLINE       rws00crl                 STABLE
ora.net1.network
               ONLINE  ONLINE       rws00cri                 STABLE
               ONLINE  ONLINE       rws00crj                 STABLE
               ONLINE  ONLINE       rws00crk                 STABLE
               ONLINE  ONLINE       rws00crl                 STABLE
ora.ons
               ONLINE  ONLINE       rws00cri                 STABLE
               ONLINE  ONLINE       rws00crj                 STABLE
               ONLINE  ONLINE       rws00crk                 STABLE
               ONLINE  ONLINE       rws00crl                 STABLE
ora.proxy_advm
               ONLINE  ONLINE       rws00cri                 STABLE
               ONLINE  ONLINE       rws00crj                 STABLE
               ONLINE  ONLINE       rws00crk                 STABLE
               ONLINE  ONLINE       rws00crl                 STABLE
ora.st.pri.acfs
               ONLINE  ONLINE       rws00cri                 mounted on /mnt/pri,
                                                             STABLE
               ONLINE  ONLINE       rws00crj                 mounted on /mnt/pri,
                                                             STABLE
               ONLINE  ONLINE       rws00crk                 mounted on /mnt/pri,
                                                             STABLE
               ONLINE  ONLINE       rws00crl                 mounted on /mnt/pri,
                                                             STABLE
--------------------------------------------------------------------------------
Cluster Resources
--------------------------------------------------------------------------------
ora.ASMNET1LSNR_ASM.lsnr(ora.asmgroup)
      1        ONLINE  ONLINE       rws00crk                 STABLE
      2        ONLINE  ONLINE       rws00crj                 STABLE
      3        ONLINE  ONLINE       rws00cri                 STABLE
ora.DATA.dg(ora.asmgroup)
      1        ONLINE  ONLINE       rws00crk                 STABLE
      2        ONLINE  ONLINE       rws00crj                 STABLE
      3        ONLINE  ONLINE       rws00cri                 STABLE
ora.LISTENER_SCAN1.lsnr
      1        ONLINE  ONLINE       rws00crj                 STABLE
ora.LISTENER_SCAN2.lsnr
      1        ONLINE  ONLINE       rws00crk                 STABLE
ora.LISTENER_SCAN3.lsnr
      1        ONLINE  ONLINE       rws00cri                 STABLE
ora.ST.dg(ora.asmgroup)
      1        ONLINE  ONLINE       rws00crk                 STABLE
      2        ONLINE  ONLINE       rws00crj                 STABLE
      3        ONLINE  ONLINE       rws00cri                 STABLE
ora.asm(ora.asmgroup)
      1        ONLINE  ONLINE       rws00crk                 Started,STABLE
      2        ONLINE  ONLINE       rws00crj                 Started,STABLE
      3        ONLINE  ONLINE       rws00cri                 Started,STABLE
ora.asmnet1.asmnetwork(ora.asmgroup)
      1        ONLINE  ONLINE       rws00crk                 STABLE
      2        ONLINE  ONLINE       rws00crj                 STABLE
      3        ONLINE  ONLINE       rws00cri                 STABLE
ora.cvu
      1        ONLINE  ONLINE       rws00cri                 STABLE
ora.gns
      1        ONLINE  ONLINE       rws00crj                 STABLE
ora.gns.vip
      1        ONLINE  ONLINE       rws00crj                 STABLE
ora.qosmserver
      1        ONLINE  ONLINE       rws00crk                 STABLE
ora.repl.dupd.st.pri.acfs
      1        ONLINE  ONLINE       rws00cri                 STABLE
ora.rws00cri.vip
      1        ONLINE  ONLINE       rws00cri                 STABLE
ora.rws00crj.vip
      1        ONLINE  ONLINE       rws00crj                 STABLE
ora.rws00crk.vip
      1        ONLINE  ONLINE       rws00crk                 STABLE
ora.rws00crl.vip
      1        ONLINE  ONLINE       rws00crl                 STABLE
ora.scan1.vip
      1        ONLINE  ONLINE       rws00crj                 STABLE
ora.scan2.vip
      1        ONLINE  ONLINE       rws00crk                 STABLE
ora.scan3.vip
      1        ONLINE  ONLINE       rws00cri                 STABLE
--------------------------------------------------------------------------------
```

## Policy-managed / administration-managed database
这是两种资源管理的模式

## Server pools function
1. 使用以下两个指令进行管理：
* crsctl
* srvctl

```
$crsctl status server -f
NAME=rws00cri
MEMORY_SIZE=22773
CPU_COUNT=2
CPU_CLOCK_RATE=2294
CPU_HYPERTHREADING=0
CPU_EQUIVALENCY=1000
DEPLOYMENT=other
CONFIGURED_CSS_ROLE=hub
RESOURCE_USE_ENABLED=1
SERVER_LABEL=
PHYSICAL_HOSTNAME=
CSS_CRITICAL=no
CSS_CRITICAL_TOTAL=0
RESOURCE_TOTAL=0
SITE_NAME=rws00cr-cluster
STATE=ONLINE
ACTIVE_POOLS=Free
STATE_DETAILS=
ACTIVE_CSS_ROLE=hub
WORKLOAD_CPU_REMAINING=200
NAME=rws00crj
MEMORY_SIZE=22773
CPU_COUNT=2
CPU_CLOCK_RATE=2294
CPU_HYPERTHREADING=0
CPU_EQUIVALENCY=1000
DEPLOYMENT=other
CONFIGURED_CSS_ROLE=hub
RESOURCE_USE_ENABLED=1
SERVER_LABEL=
PHYSICAL_HOSTNAME=
CSS_CRITICAL=no
CSS_CRITICAL_TOTAL=0
RESOURCE_TOTAL=0
SITE_NAME=rws00cr-cluster
STATE=ONLINE
ACTIVE_POOLS=Free
STATE_DETAILS=
ACTIVE_CSS_ROLE=hub
WORKLOAD_CPU_REMAINING=200
NAME=rws00crk
MEMORY_SIZE=22773
CPU_COUNT=2
CPU_CLOCK_RATE=2294
CPU_HYPERTHREADING=0
CPU_EQUIVALENCY=1000
DEPLOYMENT=other
CONFIGURED_CSS_ROLE=hub
RESOURCE_USE_ENABLED=1
SERVER_LABEL=
PHYSICAL_HOSTNAME=
CSS_CRITICAL=no
CSS_CRITICAL_TOTAL=0
RESOURCE_TOTAL=0
SITE_NAME=rws00cr-cluster
STATE=ONLINE
ACTIVE_POOLS=Free
STATE_DETAILS=
ACTIVE_CSS_ROLE=hub
WORKLOAD_CPU_REMAINING=200
NAME=rws00crl
MEMORY_SIZE=22773
CPU_COUNT=2
CPU_CLOCK_RATE=2292
CPU_HYPERTHREADING=0
CPU_EQUIVALENCY=1000
DEPLOYMENT=other
CONFIGURED_CSS_ROLE=hub
RESOURCE_USE_ENABLED=1
SERVER_LABEL=
PHYSICAL_HOSTNAME=
CSS_CRITICAL=no
CSS_CRITICAL_TOTAL=0
RESOURCE_TOTAL=0
SITE_NAME=rws00cr-cluster
STATE=ONLINE
ACTIVE_POOLS=Free
STATE_DETAILS=
ACTIVE_CSS_ROLE=hub
WORKLOAD_CPU_REMAINING=200
```
管理服务池
```
$crsctl add/delete/remove/modify serverpool
```
## Create application Virtual IP using crsctl
```
#  crsctl add type <typeName> -basetype <baseTypeName> 

Eg:
1 添加属性
# crsctl add type app.appvip.type -basetype ora.cluster_vip.type 

2 添加资源
# crsctl add resource app.appvip -type app.appvip.type -attr "RESTART_ATTEMPTS=2,
START_TIMEOUT=100,STOP_TIMEOUT=100,CHECK_INTERVAL=10,
USR_ORA_VIP=172.16.0.0,
START_DEPENDENCIES=hard(ora.net1.network)pullup(ora.net1.network),
STOP_DEPENDENCIES=hard(ora.net1.network)"

3 绑定vip
# appvipcfg create -network=1 -ip=172.16.0.0 -vipname=MyAppVIP -user=root
```

## ONS (Oracle Notification Server)
```
1 current ONS 配置：

# srvctl config nodeapps
Network 1 exists
Subnet IPv4: 10.214.64.0/255.255.240.0/eth0, static
Subnet IPv6:
Ping Targets:
Network is enabled
Network is individually enabled on nodes:
Network is individually disabled on nodes:
VIP exists: network number 1, hosting node rws00cri
VIP Name: rws00cri-v.us.oracle.com
VIP IPv4 Address: 10.214.74.168
VIP IPv6 Address:
VIP is enabled.
VIP is individually enabled on nodes:
VIP is individually disabled on nodes:
VIP exists: network number 1, hosting node rws00crj
VIP Name: rws00crj-v.us.oracle.com
VIP IPv4 Address: 10.214.74.169
VIP IPv6 Address:
VIP is enabled.
VIP is individually enabled on nodes:
VIP is individually disabled on nodes:
VIP exists: network number 1, hosting node rws00crk
VIP Name: rws00crk-v.us.oracle.com
VIP IPv4 Address: 10.214.74.170
VIP IPv6 Address:
VIP is enabled.
VIP is individually enabled on nodes:
VIP is individually disabled on nodes:
VIP exists: network number 1, hosting node rws00crl
VIP Name: rws00crl-v.us.oracle.com
VIP IPv4 Address: 10.214.74.171
VIP IPv6 Address:
VIP is enabled.
VIP is individually enabled on nodes:
VIP is individually disabled on nodes:
ONS exists: Local port 6100, remote port 6200, EM port 2016, Uses SSL true
ONS is enabled
ONS is individually enabled on nodes:
ONS is individually disabled on nodes:

$ srvctl config nodeapps -s
ONS exists: Local port 6100, remote port 6200, EM port 2016, Uses SSL true
ONS is enabled
ONS is individually enabled on nodes:
ONS is individually disabled on nodes:

2 添加 ONS
srvctl add nodeapps { { -node <node_name> -address {<vip_name>|<ip>}/<netmask>[/if1[|if2...]] [-skip]} | { -subnet <subnet>/<netmask>[/if1[|if2...]] } } [-emport <em_port>] [-onslocalport <ons_local_port>]  [-onsremoteport <ons_remote_port>] [-remoteservers <host>[:<port>][,<host>[:<port>]...]] [-clientdata <file> [-scanclient]] [-pingtarget "<pingtarget_list>"] [-vipless] [-verbose]

3 start/stop ONS
srvctl start/stop nodeapps
```

## SCAN
```
# srvctl config scan
SCAN name: rws00cricrl-r, Network: 1
Subnet IPv4: 10.214.64.0/255.255.240.0/eth0, static
Subnet IPv6:
SCAN 1 IPv4 VIP: 10.214.75.8
SCAN VIP is enabled.
SCAN 2 IPv4 VIP: 10.214.75.7
SCAN VIP is enabled.
SCAN 3 IPv4 VIP: 10.214.75.9
SCAN VIP is enabled.
```

## Manage application resources
通过 crsctl 和 srvctl 操作