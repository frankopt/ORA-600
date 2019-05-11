# 集群管理 crs 指令

| crsctl  | clusterware-related |
| --- | --- |
|  | start and stop Oracle Clusterware |
|  | enable and disable Oracle Clusterware daemons |
|  | register cluster resources |
|  |  |
| srvctl | resource-related |
|  | start and stop db instance and services |


## Clusterware

* crsctl check/start/stop crs

```
[Sat May 11 08:51:21 ][crsusr@rws00cre.us.oracle.com:/scratch/oracle/CrsHome]$crsctl check crs
CRS-4638: Oracle High Availability Services is online
CRS-4537: Cluster Ready Services is online
CRS-4529: Cluster Synchronization Services is online
CRS-4533: Event Manager is online
[Sat May 11 08:51:25 ][crsusr@rws00cre.us.oracle.com:/scratch/oracle/CrsHome]$
[Sat May 11 08:51:26 ][crsusr@rws00cre.us.oracle.com:/scratch/oracle/CrsHome]$crsctl check cluster
CRS-4537: Cluster Ready Services is online
CRS-4529: Cluster Synchronization Services is online
CRS-4533: Event Manager is online
```

* voting disk and OCR (Oracle Cluster Registry)

```
$crsctl query css votedisk
##  STATE    File Universal Id                File Name Disk group
--  -----    -----------------                --------- ---------
 1. ONLINE   03eb395983194f21bff7a5c76f5dac01 (AFD:DATA1) [DATA]
Located 1 voting disk(s).
```

```
$cat /etc/oracle/ocr.loc
#Device/file +DATA getting replaced by device +DATA/rws00cr-cluster/OCRFILE/registry.255.1007389551
ocrconfig_loc=+DATA/rws00cr-cluster/OCRFILE/registry.255.1007389551
```

可通过 ASMCMD 查看
```
$asmcmd
ASMCMD> ls
DATA/
MAY/
MGMT/
REPL/

ASMCMD> ls DATA/rws00cr-cluster/OCRFILE/
REGISTRY.255.1007389551
<通过 cp 备份>
```