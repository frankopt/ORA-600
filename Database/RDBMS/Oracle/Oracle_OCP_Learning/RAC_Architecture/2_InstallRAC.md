# RAC Install

使用ASM作为 共享存储。

| redundancy | min of disks | OCR files | Voting Disk Files |  |
| --- | --- | --- | --- | --- |
| external | 1 | 280 MB |  |  |
| normal | 3 | 560 MB |  |  |
| high | 5 | 840 MB |  |  |
| flex | 5 |  |  |  |


## OCR (Oracle Clusterware Repository)
![](https://ws1.sinaimg.cn/large/006tNc79gy1g2xfjaidcnj30fe0bbmyu.jpg)

## DNS
```
[Sat May 11 04:18:01][13147][root@rws00cre:~][0]# cat /etc/resolv.conf
#
# Optional values recommended by GIT
#
options timeout:1
options attempts:2
#
#
search us.oracle.com oracle.com oraclecorp.com
nameserver 10.209.76.197
nameserver 10.209.76.198
nameserver 192.135.82.132
```
验证 DNS 是否配置正常
```
[Sat May 11 04:18:08][13147][root@rws00cre:~][0]# nslookup rws00cre
Server:         10.209.76.197
Address:        10.209.76.197#53
Non-authoritative answer:
Name:   rws00cre.us.oracle.com
Address: 10.214.74.96
```

## 主机名解析
```
[Sat May 11 04:18:19][13147][root@rws00cre:~][0]# cat /etc/hosts
# Do not remove the following line, or various programs
# that require network functionality will fail.

127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

10.214.74.96 rws00cre.us.oracle.com rws00cre
```

## SSH 等效性

## 时间同步

## Udev 规则编写

## CVU 检测
```
[Sat May 11 08:39:53 ][crsusr@rws00cre.us.oracle.com:/scratch/oracle/CrsHome]$./runcluvfy.sh -help
USAGE:
runcluvfy.sh [-help|-version]
runcluvfy.sh stage {-list|-help}
runcluvfy.sh stage {-pre|-post} <stage-name> <stage-specific options>  [-verbose]
runcluvfy.sh comp  {-list|-help}
runcluvfy.sh comp  <component-name> <component-specific options>  [-verbose]
```