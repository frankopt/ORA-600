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

## ocr

```
$ ocrcheck
Status of Oracle Cluster Registry is as follows :
         Version                  :          4
         Total space (kbytes)     :     491684
         Used space (kbytes)      :      86808
         Available space (kbytes) :     404876
         ID                       : 1817734379
         Device/File Name         :      +DATA
                                    Device/File integrity check succeeded
                                    Device/File not configured
                                    Device/File not configured
                                    Device/File not configured
                                    Device/File not configured
         Cluster registry integrity check succeeded
         Logical corruption check bypassed due to non-privileged user
```

or

```
$ cluvfy comp ocr -n all -verbose
Performing following verification checks ...
  OCR Integrity ...PASSED
Verification of OCR integrity was successful.
CVU operation performed:      OCR integrity
Date:                         May 13, 2019 7:07:43 AM
Clusterware version:          20.0.0.0.0
CVU home:                     /scratch/oracle/CrsHome
Grid home:                    /scratch/oracle/CrsHome
User:                         crsusr
Operating system:             Linux4.14.35-1913.el7uek.x86_64
```
The OCR is backed up automatically
```
$ ocrconfig -showbackup auto
rws00cre     2019/05/13 03:57:05     +MGMT:/rws00cr-cluster/OCRBACKUP/backup00.ocr.335.1008129413     0
rws00cre     2019/05/12 23:56:51     +MGMT:/rws00cr-cluster/OCRBACKUP/backup01.ocr.337.1008114997     0
rws00cre     2019/05/12 19:56:37     +MGMT:/rws00cr-cluster/OCRBACKUP/backup02.ocr.305.1008100583     0
rws00cre     2019/05/12 03:55:32     +MGMT:/rws00cr-cluster/OCRBACKUP/day.ocr.300.1008042935     0
rws00cre     2019/05/04 18:43:37     +MGMT:/rws00cr-cluster/OCRBACKUP/week.ocr.301.1007405019     0
```

## voting disk
```
# crsctl add css votedisk path_to_voting_disk
# crsctl delete css votedisk path_to_voting_disk
```

## Network

```
$ oifcfg iflist -p -n
eth0  10.214.64.0  PRIVATE  255.255.240.0
eth1  10.196.0.0  PRIVATE  255.255.240.0
eth1  169.254.0.0  UNKNOWN  255.255.224.0
eth2  10.196.16.0  PRIVATE  255.255.240.0
eth0  2606:b400:400:88b0::  UNKNOWN  /64
eth1  2606:b400:400:88b0::  UNKNOWN  /64
eth2  2606:b400:400:88b0::  UNKNOWN  /64

$ oifcfg getif
eth0  10.214.64.0  global  public
eth1  10.196.0.0  global  cluster_interconnect,asm

$ srvctl config nodeapps -a
Network 1 exists
Subnet IPv4: 10.214.64.0/255.255.240.0/eth0, static
Subnet IPv6:
Ping Targets:
Network is enabled
Network is individually enabled on nodes:
Network is individually disabled on nodes:
VIP exists: network number 1, hosting node rws00cre
VIP Name: rws00cre-v.us.oracle.com
VIP IPv4 Address: 10.214.74.164
VIP IPv6 Address:
VIP is enabled.
VIP is individually enabled on nodes:
VIP is individually disabled on nodes:
VIP exists: network number 1, hosting node rws00crf
VIP Name: rws00crf-v.us.oracle.com
VIP IPv4 Address: 10.214.74.165
VIP IPv6 Address:
VIP is enabled.
VIP is individually enabled on nodes:
VIP is individually disabled on nodes:
```