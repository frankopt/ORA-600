# Postmark - 用来测试产品的后端存储性能
[Postmark Intro](http://www.filesystems.org/docs/auto-pilot/Postmark.html)

Postmark主要用于测试文件系统在邮件系统或电子商务系统中性能，这类应用的特点是：**需要频繁、大量地存取小文件**。
Postmark is a benchmark designed to simulate the behavior of mail servers. Postmark consists of three phases. In the first phase a pool of files are created. In the next phase four types of transactions are executed: files are created, deleted, read, and appended to. In the last phase, all files in the pool are deleted.

Postmark is a single threaded benchmark, but Auto-pilot can automatically run several concurrent processes and analyze the results. Postmark generates a small workload by default: only 500 files are created and 500 transactions performed. Auto-pilot increases the workload to a pool of 20,000 files, and performs 200,000 transactions by default.

## 测试原理
Postmark的测试原理是创建一个测试文件池。文件的数量和最大、最小长度可以设定，数据总量是一定的。创建完成后，Postmark对文件池进行一系列的事务（transaction）操作，根据从实际应用中统计的结果，设定每一个事务包括一次创建或删除操作和一次读或添加操作，在有些情况下，文件系统的缓存策略可能对性能造成影响，Postmark可以通过对创建/删除以及读/添加操作的比例进行修改来抵消这种影响。事务操作进行完毕后，Post对文件池进行删除操作，并结束测试，输出结果。

* Postmark是用随机数来产生所操作文件的序号，从而使测试更加贴近于现实应用。

* 输出结果中比较重要的输出数据包括测试总时间、每秒钟平均完成的事务数、在事务处理中平均每秒创建和删除的文件数，以及读和写的平均传输速度。


## Install 
postmark软件只有一个.c文件，在gcc下编译即可。假定编译之后的可执行文件名为postmark。

```
-rwxr-xr-x.  1 grid oinstall      70680 May 31 16:42 postmark.c


$ gcc -Os postmark.c -o postmark
/tmp/ccJDQqdD.o: In function `cli_show':
postmark.c:(.text+0x607): warning: the `getwd' function is dangerous and should not be used.
---> skip the warning

# cp -a postmark /usr/local/bin

#postmark
PostMark v1.5 : 3/27/01
pm>?
set size - Sets low and high bounds of files
set number - Sets number of simultaneous files
set seed - Sets seed for random number generator
set transactions - Sets number of transactions
set location - Sets location of working files
set subdirectories - Sets number of subdirectories
set read - Sets read block size
set write - Sets write block size
set buffering - Sets usage of buffered I/O
set bias read - Sets the chance of choosing read over append
set bias create - Sets the chance of choosing create over delete
set report - Choose verbose or terse report format
run - Runs one iteration of benchmark
show - Displays current configuration
help - Prints out available commands
quit - Exit program

pm>show
Current configuration is:
The base number of files is 500
Transactions: 500
Files range between 500 bytes and 9.77 kilobytes in size
Working directory: /scratch/grid/frank
Block sizes are: read=512 bytes, write=512 bytes
Biases are: read/append=5, create/delete=5
Using Unix buffered file I/O
Random number generator seed is 42
Report format is verbose.

pm>run
Creating files...Done
Performing transactions..........Done
Deleting files...Done
Time:
        1 seconds total
        1 seconds of transactions (500 per second)
Files:
        764 created (764 per second)
                Creation alone: 500 files (500 per second)
                Mixed with transactions: 264 files (264 per second)
        243 read (243 per second)
        257 appended (257 per second)
        764 deleted (764 per second)
                Deletion alone: 528 files (528 per second)
                Mixed with transactions: 236 files (236 per second)
Data:
        1.36 megabytes read (1.36 megabytes per second)
        4.45 megabytes written (4.45 megabytes per second)
```


```
-------------------------------------------------------------
PACKAGE:  postmark-1.5.tgz
Wed Jul 11 02:40:47 PDT 2007

### UNPACK ###
UNPACK WARNING:  Target directory '/usr/builds/postmark-1.5' already exists
  Removing /usr/builds/postmark-1.5
tar zxf /cruc/packages/postmark/postmark-1.5.tgz --directory /usr/builds/postmark-1.5 --strip-components 1
UNPACK STATUS:  0
### PATCH ###

### CONFIGURE ###
Skipping configure

### BUILD ###
postmark build:
make -f postmark.mk
gcc -Os postmark-1_5.c -o postmark
/tmp/ccZIKYHy.o: In function `cli_show':
postmark-1_5.c:(.text+0xa64): warning: the `getwd' function is dangerous and should not be used.
postmark build: return 0

Skipping make check

install: cp -a postmark /usr/local/bin
```

