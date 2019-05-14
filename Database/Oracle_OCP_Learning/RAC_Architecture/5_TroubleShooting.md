# RAC 集群故障调整

## Locate Oracle Clusterware log
** golden rule in debugging Oracle Clusterware **
1. 时间同步 NTP / CTSS (需要连外部网络)
2. facilitate log
3. reading GV$ view

## CVU
https://www.oracle.com/technetwork/database/enterprise-edition/downloads/cvu-faq-163307.html#What_is_CVU_What_are_its_objectives_and
```
$/scratch/oracle/CrsHome/bin/cluvfy -help
USAGE:
cluvfy [-help|-version]
cluvfy stage {-list|-help}
cluvfy stage {-pre|-post} <stage-name> <stage-specific options>  [-verbose]
cluvfy comp  {-list|-help}
cluvfy comp  <component-name> <component-specific options>  [-verbose]
```
## TFA (Trace File Analyzer)
![](https://ws3.sinaimg.cn/large/006tNc79ly1g30y9dzo93j30zp0fgtb6.jpg)
```
-rwxr-xr-x 1 root oinstall 2508 May 13 07:27 tfactl
```
客户在和技术支持的工程师解决GI（RAC）问题的时候，一个最大的问题就是及时的收集各个节点上和问题相关的日志和诊断数据，特别是收集的数据还有跨节点。另外，RAC里的trace日志文件是轮循使用的，如果发生问题之后不及时收集日志就会被覆盖。对于单机的环境ADR（Automatic Diagnostic Repository）虽然可以很好的避免这个问题，它会对故障发生后对故障生成的文件进行打包，但是ADR并不能收集RAC的日志。对于Cluster的日志收集我们以前会经常使用diagcollection.pl这个脚本，但是这个脚本的弊端是它不会甄别日志里的内容，会把所有的RAC日志从头至尾都收集一遍。如果您曾经使用过diagcollection.pl一定会知道这个脚本收集的日志是非常大的,而且diagcollection.pl的脚本必须要在各个节点上分别使用root用户分别运行,使用不便利。
TFA基本上克服了上边的这些问题，TFA通过在每一个节点上运行一个Java的虚拟环境，来判断什么时候需要启动来收集，压缩日志，并且来判断哪些日志是解决问题必要，TFA是运行在GI和RDBMS之外的产品，所以它甚至和当前使用的版本和平台都没有关系。

所以，在处理Oracle GI 和 RAC问题时，使用 TFA可以一键收集所有需要的日志，而且会过滤掉不需要的日志。也有客户担心使用TFA会对系统有影响，了解了上述它的功能之后，您就可以知道它只是一个日志收集工具，并不会对系统产生变更，他对OS的负载压力是轻量级的。


## Enable resource debug
```
Usage:
  crsctl set log {mdns|gpnp|css|crf|crs|ctss|evm|gipc} "<name1>=<lvl1>,..."
 where
   mdns          multicast Domain Name Server
   gpnp          Grid Plug and Play Service
   css           Cluster Synchronization Services
   crf           Cluster Health Monitor
   crs           Cluster Ready Services
   ctss          Cluster Time Synchronization Service
   evm           Event Manager
   gipc          Grid Interprocess Communications
   <name1>, ...    Module names ("all" for all names)
   <lvl1>, ...     Module log levels
  crsctl set log res <resname>=<lvl>
 where
 <resname>     Resource name
   <lvl>                  Agent log levels
```
## Enable component-level debugging
![](https://ws1.sinaimg.cn/large/006tNc79ly1g30ywub5ksj30sg0lc0vt.jpg)
## Enable tracing for Java-based tools
To enable tracing for srvctl/netca/cluvfy,
set:
```
export SRVM_TRACE=true

Eg: srvctl
export SRVCTL_TRACEFILE=srvctl_`date +%Y-%m-%d-%H-%M-%S`
```

## Determine which process caused REBOOT
* ocssd
```
/var/log/messages
<GridHome>/log/<hostname>/cssd/ocssd.log
```

* oclskd <需要在客户端检查>
```
<GridHome>/log/<hostname>/client/oclskd.log
```
* hangcheck-timer <内核模块，11gR2后取消>
```
/var/log/messages
```

## Troubleshoot the Oracle Cluster Registry file