# iperf测试网络性能
iperf是美国伊利诺斯大学（University of Illinois）开发的一种开源的网络性能测试工具。

## Target
用来测试网络节点间 TCP或UDP连接的性能，包括带宽、抖动以及丢包率
*  带宽测试 适应于TCP和UDP
*  抖动和丢包率 适应于UDP测试

## Theory
iperf是基于server-client模式工作的，因此，要使用iperf测试带宽，需要建立一个服务端（用于丢弃流量）和一个客户端（用于产生流量）

## How to Test Network Throughput Between 2 Linux Servers

* 服务器

Firt connect to the remote machine which you will use as the server and fireup iperf3 in server mode using -s flag, it will listen on port 5201 by default.

You can specify the format (k, m, g for Kbits, Mbits, Gbits or K, M, G for KBytes, Mbytes, Gbytes) to report in, using the -f switch as shown.
```
# [rwsoda408c1n1] iperf3 -s -f g
```

If port 5201 is being used by another program on your server, you can specify a different port (e.g 3000) using the -p switch as shown.
```
$ iperf 3 -s -p 3000
```
Optionally, you can run the server as a daemon, using the -D flag and write server messages to a log file, as follows.
```
$ iperf 3 -s -D > iperf3log 
```


Then on your local machine which we will treat as the client (where the actual benchmarking takes place), run iperf3 in client mode using -c flag and specify the host on which the server is running on (either using its IP address or domain or hostname).

*  客户端

Then on your local machine which we will treat as the client (where the actual benchmarking takes place), run iperf3 in client mode using -c flag and specify the host on which the server is running on (either using its IP address or domain or hostname).
```
# [rwsoda408c1n2] iperf3 -c 10.214.72.43 -f G
```
注意：iperf默认测试的是TCP协议的带宽，如果需要测试UDP的带宽，则需要加上-u选项


## 常用选项
* 通用选项
```
-f <kmKM>    报告输出格式。 [kmKM]   format to report: Kbits, Mbits, KBytes, MBytes
-i <sec>    在周期性报告带宽之间暂停n秒。如周期是10s，则-i指定为2，则每隔2秒报告一次带宽测试情况,则共计报告5次
-p    设置服务端监听的端口，默认是5201
-u    使用UDP协议测试
-w n<K/M>   指定TCP窗口大小
-m    输出MTU大小
-M    设置MTU大小
-o <filename>    结果输出至文件
```

* 服务端选项
```
-s    iperf服务器模式
-d    以后台模式运行服务端
-U    运行一个单一线程的UDP模式
```

* 客户端选项
```
-b , --bandwidth n[KM]    指定客户端通过UDP协议发送数据的带宽（bit/s）。默认是1Mbit/s
-c <ServerIP>    以客户端模式运行iperf，并且连接至服务端主机ServerIP。 eg:  iperf -c <server_ip>
-d    双向测试
-t    指定iperf带宽测试时间，默认是10s。  eg:  iperf -c <server_ip> -t 20
-P    指定客户端并发线程数，默认只运行一个线程。 eg,指定3个线程 : iperf -c <server_ip> -P 3
-T    指定TTL值
```

## benchmark
After about 18 to 20 seconds, the client should terminate and produce results indicating the average throughput for the benchmark, as shown in the following screenshot.

### UDP模式
服务器端：
```
[Mon May 27 13:48:02][54570][root@rwsoda408c1n1.us.oracle.com:~][0]# iperf3 -s
-----------------------------------------------------------
Server listening on 5201
-----------------------------------------------------------
Accepted connection from 10.214.72.44, port 45864
[  5] local 10.214.72.43 port 5201 connected to 10.214.72.44 port 37196
[ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
[  5]   0.00-1.00   sec  5.72 MBytes  48.0 Mbits/sec  0.014 ms  0/4140 (0%)
[  5]   1.00-2.00   sec  5.96 MBytes  50.0 Mbits/sec  0.010 ms  0/4317 (0%)
[  5]   2.00-3.00   sec  5.96 MBytes  50.0 Mbits/sec  0.007 ms  0/4316 (0%)
[  5]   3.00-4.00   sec  5.96 MBytes  50.0 Mbits/sec  0.012 ms  0/4316 (0%)
[  5]   4.00-5.00   sec  5.96 MBytes  50.0 Mbits/sec  0.011 ms  0/4316 (0%)
[  5]   5.00-6.00   sec  5.96 MBytes  50.0 Mbits/sec  0.012 ms  0/4317 (0%)
[  5]   6.00-7.00   sec  5.96 MBytes  50.0 Mbits/sec  0.011 ms  0/4316 (0%)
[  5]   7.00-8.00   sec  5.96 MBytes  50.0 Mbits/sec  0.009 ms  0/4317 (0%)
[  5]   8.00-9.00   sec  5.96 MBytes  50.0 Mbits/sec  0.010 ms  0/4316 (0%)
[  5]   9.00-10.00  sec  5.96 MBytes  50.0 Mbits/sec  0.011 ms  0/4316 (0%)
[  5]  10.00-10.04  sec   245 KBytes  49.8 Mbits/sec  0.009 ms  0/173 (0%)
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
[  5]   0.00-10.04  sec  59.6 MBytes  49.8 Mbits/sec  0.009 ms  0/43160 (0%)  receiver
```

客户端：
在udp模式下，以50Mbps为数据发送速率，客户端到服务器192.168.0.103上传带宽测试，测试时间为10秒。
```
[Mon May 27 13:48:20][22515][root@rwsoda408c1n2.us.oracle.com:~][0]# iperf3 -u -c 10.214.72.43 -b 50M -t 10
Connecting to host 10.214.72.43, port 5201
[  5] local 10.214.72.44 port 37196 connected to 10.214.72.43 port 5201
[ ID] Interval           Transfer     Bitrate         Total Datagrams
[  5]   0.00-1.00   sec  5.96 MBytes  50.0 Mbits/sec  4313
[  5]   1.00-2.00   sec  5.96 MBytes  50.0 Mbits/sec  4316
[  5]   2.00-3.00   sec  5.96 MBytes  50.0 Mbits/sec  4317
[  5]   3.00-4.00   sec  5.96 MBytes  50.0 Mbits/sec  4316
[  5]   4.00-5.00   sec  5.96 MBytes  50.0 Mbits/sec  4316
[  5]   5.00-6.00   sec  5.96 MBytes  50.0 Mbits/sec  4316
[  5]   6.00-7.00   sec  5.96 MBytes  50.0 Mbits/sec  4317
[  5]   7.00-8.00   sec  5.96 MBytes  50.0 Mbits/sec  4316
[  5]   8.00-9.00   sec  5.96 MBytes  50.0 Mbits/sec  4316
[  5]   9.00-10.00  sec  5.96 MBytes  50.0 Mbits/sec  4317
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
[  5]   0.00-10.00  sec  59.6 MBytes  50.0 Mbits/sec  0.000 ms  0/43160 (0%)  sender
[  5]   0.00-10.04  sec  59.6 MBytes  49.8 Mbits/sec  0.009 ms  0/43160 (0%)  receiver
iperf Done.
```

### TCP模式
服务器端：
```
[Mon May 27 13:53:44][54570][root@rwsoda408c1n1.us.oracle.com:~][1]# iperf3 -s
-----------------------------------------------------------
Server listening on 5201
-----------------------------------------------------------
Accepted connection from 10.214.72.44, port 45906
[  5] local 10.214.72.43 port 5201 connected to 10.214.72.44 port 45908
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-1.00   sec  1.05 GBytes  9.00 Gbits/sec
[  5]   1.00-2.00   sec  1.10 GBytes  9.42 Gbits/sec
[  5]   2.00-3.00   sec  1.10 GBytes  9.42 Gbits/sec
[  5]   3.00-4.00   sec  1.10 GBytes  9.42 Gbits/sec
[  5]   4.00-5.00   sec  1.10 GBytes  9.42 Gbits/sec
[  5]   5.00-6.00   sec  1.10 GBytes  9.42 Gbits/sec
[  5]   6.00-7.00   sec  1.10 GBytes  9.42 Gbits/sec
[  5]   7.00-8.00   sec  1.10 GBytes  9.42 Gbits/sec
[  5]   8.00-9.00   sec  1.10 GBytes  9.42 Gbits/sec
[  5]   9.00-10.00  sec  1.10 GBytes  9.41 Gbits/sec
[  5]  10.00-10.04  sec  44.9 MBytes  9.39 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-10.04  sec  11.0 GBytes  9.37 Gbits/sec                  receiver
```

客户端：
在tcp模式下，客户端到服务器10.214.72.43上传带宽测试，测试时间为10秒

```
[Mon May 27 13:53:57][22515][root@rwsoda408c1n2.us.oracle.com:~][0]# iperf3 -c 10.214.72.43 -b -t 10
Connecting to host 10.214.72.43, port 5201
[  5] local 10.214.72.44 port 45908 connected to 10.214.72.43 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.09 GBytes  9.40 Gbits/sec    3    701 KBytes
[  5]   1.00-2.00   sec  1.10 GBytes  9.42 Gbits/sec    0    728 KBytes
[  5]   2.00-3.00   sec  1.10 GBytes  9.42 Gbits/sec    0    748 KBytes
[  5]   3.00-4.00   sec  1.10 GBytes  9.42 Gbits/sec    0    755 KBytes
[  5]   4.00-5.00   sec  1.10 GBytes  9.42 Gbits/sec    0    764 KBytes
[  5]   5.00-6.00   sec  1.10 GBytes  9.42 Gbits/sec    0    769 KBytes
[  5]   6.00-7.00   sec  1.10 GBytes  9.42 Gbits/sec    0    772 KBytes
[  5]   7.00-8.00   sec  1.10 GBytes  9.42 Gbits/sec    0    776 KBytes
[  5]   8.00-9.00   sec  1.10 GBytes  9.42 Gbits/sec    0    781 KBytes
[  5]   9.00-10.00  sec  1.10 GBytes  9.42 Gbits/sec    0    790 KBytes
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  11.0 GBytes  9.41 Gbits/sec    3             sender
[  5]   0.00-10.04  sec  11.0 GBytes  9.37 Gbits/sec                  receiver
iperf Done.
```