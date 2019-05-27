# How to measure disk performance with fio and IOPing
@Unixmen[ByGiuseppe Molica]

![](http://ww4.sinaimg.cn/large/006tNc79ly1g3fue00unqj30m80h0406.jpg)

## Introduction
Whether it’s a server, or a PC for work, what usually limits performances is disk speed. Even if using SSDs, their speed is not yet comparable to that of RAM and CPU.
There are different tools with or without a graphical interface, written for testing disks speed. There are also people who use dd, for example:
```
dd if=/dev/zero of=test_file bs=64k count=16k conv=fdatasync
```
However, in our opinion dd is the worst software for benchmarking I/O performance.
In fact:

* it is a _single-threaded, sequential-write test_. Of course, if running a web server, services do not do long-running sequential writes, and use more than one thread
* it writes a small amount of data, so the result can be influenced by _caching or by RAID’s controller_
* it executes for just a few seconds, and everyone knows that in this way it’s not possible to have _consistent results_
* there are _no reading speed tests_

All these points just lead to one conclusion: better to use anything else. 
For disk benchmarking there are two kind of parameters that give a complete overview: 
* IOPS (I/O Per Second) 
* latency. 

This tutorial explains how to measure IOPS with fio, and disk latency with IOPing on a RHEL 7 system.

## Testing IOPS with fio (Flexible I/O)
* **Sequential Reads** – Async mode – 8K block size – Direct IO – 100% Reads
```
fio --name=seqread --rw=read --direct=1 --ioengine=libaio --bs=8k --numjobs=8 --size=1G --runtime=600  --group_reporting
```

* **Sequential Writes** – Async mode – 32K block size – Direct IO – 100% Writes
```
fio --name=seqwrite --rw=write --direct=1 --ioengine=libaio --bs=32k --numjobs=4 --size=2G --runtime=600 --group_reporting
```
* **Random Reads** – Async mode – 8K block size – Direct IO – 100% Reads
```
fio --name=randread --rw=randread --direct=1 --ioengine=libaio --bs=8k --numjobs=16 --size=1G --runtime=600 --group_reporting
```

* **Random Writes** – Async mode – 64K block size – Direct IO – 100% Writes
```
fio --name=randwrite --rw=randwrite --direct=1 --ioengine=libaio --bs=64k --numjobs=8 --size=512m --runtime=600 --group_reporting
```

* **Random Read/Writes** – Async mode – 16K block size – Direct IO – 90% Reads/10% Writes
```
fio --name=randrw --rw=randrw --direct=1 --ioengine=libaio --bs=16k --numjobs=8 --rwmixread=90 --size=1G --runtime=600 --group_reporting
```

## Sample Output
```
[Mon May 27 15:32:28][54570][root@rwsoda408c1n1.us.oracle.com:/mnt/ora][0]# fio --name=randrw --ioengine=libaio --iodepth=1 --rw=randrw --bs=64k --direct=1 --size=512m --numjobs=8 --runtime=300 --group_reporting --time_based --rwmixread=70
randrw: (g=0): rw=randrw, bs=(R) 64.0KiB-64.0KiB, (W) 64.0KiB-64.0KiB, (T) 64.0KiB-64.0KiB, ioengine=libaio, iodepth=1
...
fio-3.1
Starting 8 processes
randrw: Laying out IO file (1 file / 512MiB)
randrw: Laying out IO file (1 file / 512MiB)
randrw: Laying out IO file (1 file / 512MiB)
randrw: Laying out IO file (1 file / 512MiB)
randrw: Laying out IO file (1 file / 512MiB)
randrw: Laying out IO file (1 file / 512MiB)
randrw: Laying out IO file (1 file / 512MiB)
randrw: Laying out IO file (1 file / 512MiB)
Jobs: 3 (f=3): [_(2),m(2),_(2),m(1),_(1)][20.6%][r=124MiB/s,w=56.4MiB/s][r=1987,w=901 IOPS][eta 19m:21s]
randrw: (groupid=0, jobs=8): err= 0: pid=28093: Mon May 27 15:38:10 2019
   read: IOPS=12.8k, BW=797MiB/s (836MB/s)(235GiB/301767msec)
    slat (usec): min=5, max=329, avg= 8.70, stdev= 4.27
    clat (nsec): min=999, max=2646.4M, avg=584075.73, stdev=24517674.64
     lat (usec): min=37, max=2646.4k, avg=592.88, stdev=24518.10
    clat percentiles (usec):
     |  1.00th=[     35],  5.00th=[     35], 10.00th=[     35],
     | 20.00th=[     36], 30.00th=[     36], 40.00th=[     36],
     | 50.00th=[     36], 60.00th=[     37], 70.00th=[     38],
     | 80.00th=[     43], 90.00th=[     47], 95.00th=[     54],
     | 99.00th=[     72], 99.50th=[     89], 99.90th=[  72877],
     | 99.95th=[ 274727], 99.99th=[1300235]
   bw (  KiB/s): min=  128, max=920064, per=19.13%, avg=156157.50, stdev=332417.67, samples=3149
   iops        : min=    2, max=14376, avg=2439.95, stdev=5194.02, samples=3149
  write: IOPS=5463, BW=341MiB/s (358MB/s)(101GiB/301767msec)
    slat (usec): min=6, max=496, avg=11.45, stdev= 4.63
    clat (nsec): min=1237, max=1137.0M, avg=59669.91, stdev=1498952.17
     lat (usec): min=41, max=1137.0k, avg=71.24, stdev=1499.10
    clat percentiles (usec):
     |  1.00th=[   37],  5.00th=[   38], 10.00th=[   38], 20.00th=[   39],
     | 30.00th=[   39], 40.00th=[   39], 50.00th=[   39], 60.00th=[   40],
     | 70.00th=[   43], 80.00th=[   48], 90.00th=[   56], 95.00th=[   64],
     | 99.00th=[   85], 99.50th=[   98], 99.90th=[  151], 99.95th=[ 5407],
     | 99.99th=[39584]
   bw (  KiB/s): min=  128, max=400896, per=28.26%, avg=98805.87, stdev=163717.69, samples=2132
   iops        : min=    2, max= 6264, avg=1543.83, stdev=2558.08, samples=2132
  lat (nsec)   : 1000=0.01%
  lat (usec)   : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.01%, 50=91.14%
  lat (usec)   : 100=8.47%, 250=0.19%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=0.01%, 10=0.04%, 20=0.03%, 50=0.03%
  lat (msec)   : 100=0.02%, 250=0.03%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2000=0.01%, >=2000=0.01%
  cpu          : usr=0.91%, sys=2.64%, ctx=5498484, majf=0, minf=113
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=3848182,1648595,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1
Run status group 0 (all jobs):
   READ: bw=797MiB/s (836MB/s), 797MiB/s-797MiB/s (836MB/s-836MB/s), io=235GiB (252GB), run=301767-301767msec
  WRITE: bw=341MiB/s (358MB/s), 341MiB/s-341MiB/s (358MB/s-358MB/s), io=101GiB (108GB), run=301767-301767msec
Disk stats (read/write):
    dm-0: ios=3848182/1649190, merge=0/0, ticks=2252346/97460, in_queue=2352889, util=100.00%, aggrios=3848182/1657230, aggrmerge=0/39465, aggrticks=2255572/298661, aggrin_queue=2553993, aggrutil=100.00%
  sda: ios=3848182/1657230, merge=0/39465, ticks=2255572/298661, in_queue=2553993, util=100.00%

```