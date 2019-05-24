# NoSQL

> 关系数据库关注在关系上，NoSQL关注在存储上。
![](http://ww2.sinaimg.cn/large/006tNc79gy1g3c8vjkuiij30tz0h8dij.jpg)

# 1 NoSQL 产生背景 (NoSQL = Not Only SQL )
   
## 1.1 传统关系数据库的瓶颈
传统的关系数据库在应付web2.0网站，特别是超大规模和高并发的社会性网络服务类型的web2.0纯动态网站已经显得力不从心，暴露了很多难以克服的问题，而非关系型、分布式数据存储则由于其本身的特点得到了快速的发展，它们不保证关系数据的ACID特性。

NoSQL概念在2009年被提了出来。NoSQL最常见的解释是“non-relational”，“Not Only SQL”也被很多人接受。在不到一年的时间，NoSQL就开始风生水起，大大小小的Web站点在追求高性能高可靠性方面，不由自主都选择了NoSQL技术作为优先考虑的方面。

## 1.2 RDBMS 数据的 ACID 特性
![](http://ww3.sinaimg.cn/large/006tNc79gy1g3c82bfa2dj30hs0aeq3s.jpg)

    *  Atomic（原子性) - 只有使据库中所有的操作执行成功，才算整个事务成功；事务中任何一个SQL语句执行失败，那么已经执行成功的SQL语句也必须撤销，数据库状态应该退回到执行事务前的状态。
    *  Consistency（一致性）
    *  Isolation（隔离性）
    *  Durability（持久性）

## 1.3 分布式是NoSQL数据库的必要条件
当数据库不能严格遵循 ACID 理论时，以CAP理论为基础的 NoSQL Database 开始出现。

分布式系统每个节点一般不采用高性能的服务器，而是使用性能相对一般的普通PC服务器。提升分布式系统的整体性能是通过横向扩展（增加更多的服务器），而不是纵向扩展（提升每个节点的服务器性能）实现。

### 1.3.1 分布式存储的问题 – CAP理论
如果我们期待实现一套严格满足ACID的分布式事务，很可能出现的情况就是系统的可用性和严格一致性发生冲突。在可用性和一致性之间永远无法存在一个两全其美的方案。由于NoSQL的基本需求就是支持分布式存储，严格一致性与可用性需要互相取舍，由此延伸出了CAP理论来定义分布式存储遇到的问题。

```
CAP理论告诉我们：一个分布式系统不可能同时满足一致性(C:Consistency)、可用性(A:Availability)、分区容错性(P:Partitiontolerance)这三个基本需求，并且最多只能满足其中的两项。
```
对于一个分布式系统来说，**分区容错是基本需求，否则不能称之为分布式系统**。因此架构师需要在C和A之间寻求平衡。
![](http://ww2.sinaimg.cn/large/006tNc79gy1g3c8ff7lrwj30hs0fbaaj.jpg)
### 1.3.2 分布式存储算法
* 一致性算法 – Paxos
* 分区（Partitioning）
* 分片（Replication）
* 一致性哈希（Consistent Hashing）



#  2 为什么NoSQL得到了快速发展？

关键原因是：传统关系型数据库遇到了性能瓶颈。

高并发读写、对海量数据的高效率存储和访问以及对数据库的高可扩展性和高可用性成了关系型数据库难以逾越的鸿沟，关系型数据库应对这三大问题显得力不从心，暴露了很多难以克服的问题，例如：
* High performance - 对数据库高并发读写的需求 
关系数据库应付上万次SQL查询还勉强顶得住，但是应付上万次SQL写数据请求，硬盘IO就已经无法承受了。
* Huge Storage - 对海量数据的高效率存储和访问的需求
对于关系数据库来说，在一张2.5亿条记录的表里面进行SQL查询，效率是极其低下乃至不可忍受的。
* High Scalability && High Availability- 对数据库的高可扩展性和高可用性的需求 
在基于web的架构当中，数据库是最难进行横向扩展的，当一个应用系统的用户量和访问量与日俱增的时候，你的数据库却没有办法像web server和app server那样简单的通过添加更多的硬件和服务节点来扩展性能和负载能力。对于很多需要提供24小时不间断服务的网站来说，对数据库系统进行升级和扩展是非常痛苦的事情，往往需要停机维护和数据迁移。

# 3 NoSQL 分类
NoSQL 被我们用得最多的当数 key-value 存储，当然还有其他的文档型的、列存储、图型数据库、xml 数据库等。
![](http://ww4.sinaimg.cn/large/006tNc79gy1g3c7qomhbpj30jp0jp40c.jpg)

## 3.1 Key-Value 
产品：Riak、Redis、Memcached、Amazon’s Dynamo、Project Voldemort

有谁在使用：GitHub (Riak)、BestBuy (Riak)、Twitter (Redis和Memcached)、StackOverFlow (Redis)、 Instagram (Redis)、Youtube (Memcached)、Wikipedia(Memcached)

适用的场景：储存用户信息，比如会话、配置文件、参数、购物车等等。这些信息一般都和ID(键)挂钩，这种情景下键值数据库是个很好的选择。
## 3.2 Document-Oriented
产品：MongoDB、CouchDB、RavenDB

有谁在使用：SAP (MongoDB)、Codecademy (MongoDB)、Foursquare (MongoDB)、NBC News (RavenDB)

适用的场景：
* 日志。企业环境下，每个应用程序都有不同的日志信息。Document-Oriented数据库并没有固定的模式，所以我们可以使用它储存不同的信息。
* 分析。鉴于它的弱模式结构，不改变模式下就可以储存不同的度量方法及添加新的度量。

## 3.3 Wide Column Store/Column-Family
产品：Cassandra、HBase

有谁在使用：Ebay (Cassandra)、Instagram (Cassandra)、NASA (Cassandra)、Twitter (Cassandra and HBase)、Facebook (HBase)、Yahoo!(HBase)

适用的场景：
* 日志。因为我们可以将数据储存在不同的列中，每个应用程序可以将信息写入自己的列族中。
* 博客平台。我们储存每个信息到不同的列族中。举个例子，标签可以储存在一个，类别可以在一个，而文章则在另一个。

## 3.4 Graph-Oriented
产品：Neo4J、Infinite Graph、OrientDB

有谁在使用：Adobe (Neo4J)、Cisco (Neo4J)、T-Mobile (Neo4J)

适用的场景：
* 在一些关系性强的数据中
* 推荐引擎。如果我们将数据以图的形式表现，那么将会非常有益于推荐的制定

# 4 NoSQL 特点
advantage:
* 易扩展 - 数据之间无关系，这样就非常容易扩展。也无形之间，在架构的层面上带来了可扩展的能力。
* 大数据量，高性能
* 灵活的数据模型 - NoSQL无需事先为要存储的数据建立字段，随时可以存储自定义的数据格式。
* 高可用

disadvantage:
* 没有标准
* 没有存储过程
* 不支持SQL
* 支持的特性不够丰富，产品不够成熟


# 5 主流NoSQL数据库介绍

## 5.1 Redis
Redis是一个开源的使用ANSI C语言编写、支持网络、可基于内存亦可持久化的日志型、Key-Value数据库

## 5.2 MongoDB
MongoDB 是一个基于分布式文件存储的数据库

## 5.3 HBase
HBase是一个分布式的、面向列的开源数据库

---
for more, you can check
[NoSQL 还是 SQL ？这一篇讲清楚](https://juejin.im/post/5b6d62ddf265da0f491bd200)
