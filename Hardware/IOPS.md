IOPS (Input/Output Per Second)即每秒的输入输出量(或读写次数)，是衡量磁盘性能的主要指标之一。IOPS是指单位时间内系统能处理的I/O请求数量，I/O请求通常为读或写数据操作请求。随机读写频繁的应用，如OLTP(Online Transaction Processing)，IOPS是关键衡量指标。另一个重要指标是数据吞吐量(Throughput)，指单位时间内可以成功传输的数据数量。对于大量顺序读写的应用，如VOD(Video On Demand)，则更关注吞吐量指标。

简而言之：

磁盘的 IOPS，也就是在一秒内，磁盘进行多少次 I/O 读写。

磁盘的吞吐量，也就是每秒磁盘 I/O 的流量，即磁盘写入加上读出的数据的大小。

IOPS 与吞吐量的关系每秒 I/O 吞吐量＝ IOPS* 平均 I/O SIZE。从公式可以看出： I/O SIZE 越大，IOPS 越高，那么每秒 I/O 的吞吐量就越高。因此，我们会认为 IOPS 和吞吐量的数值越高越好。实际上，对于一个磁盘来讲，这两个参数均有其最大值，而且这两个参数也存在着一定的关系。


IOPS可细分为如下几个指标：

Toatal IOPS，混合读写和顺序随机I/O负载情况下的磁盘IOPS，这个与实际I/O情况最为相符，大多数应用关注此指标。
Random Read IOPS，100%随机读负载情况下的IOPS。
Random Write IOPS，100%随机写负载情况下的IOPS。
Sequential Read IOPS，100%顺序读负载情况下的IOPS。



