# Exadata
Exadata的全称是 Exadata Database Machine,
中文官方名称是 Exadata数据库云平台，俗称数据库一体机。

* Exa - EB级，EB是TB的一百万倍。
        * Teradata 知名数据仓库厂商，Tera表示TB级的数据

* data - Oracle不止是一家数据库公司，围绕数据开展的业务还包括：
        * 数据操作
        * 数据存储
        * 数据集成
        * 数据安全

## Exadata发展历史

![](http://ww1.sinaimg.cn/large/006tNc79gy1g3oysm2v9cj30u00gwabq.jpg)

很多大型数据库系统特别是数据仓库系统的瓶颈在I/O层面，
    - - 2000年前后，Oracle内部启动 SAGE(Storage Appliance for Grid Environments)的项目，这是Exadata的雏形。

    1. 2008，Exadata V1，Oracle提供软件，HP提供硬件。这一代产品仅支持数据仓库和商务智能等OLAP工作负载。
    2. 2009.09，Exadata V2，变化一：SUN提供硬件；变化二：在Exadata存储节点中首次采用Flash卡，从而同时支持OLAP和OLTP类型的负载。2010年1月，Oracle收购SUN。
    3. 2010.09，Exadata X2。变化一：数据库整合平台-新定位；变化二：增加存储扩展柜，存储可单独扩展。
    4. 2012.09，Exadata X3，变化：支持1/8机架，降低使用门槛。1/8机架的计算能力和存储容量是1/4机架的一半。
    5. 2013.10，Exadata X4，首次提出 DBaaS(Database as a Service)。这一年Oracle 12c云数据库发布。
    6. 2015.01，Exadata X5，变化一：支持非固定配置，计算节点和存储节点灵活配置；变化二：全闪存EF(Extreme Flash)存储节点。
    7. 2016.04,Exadata X6，支持Exadata 公有云服务和公有云私有化部署。
    8. 2017.10，Exadata X7，内存计算改进。
    9. 2019.04，Exadata X8，新增XT(Extended)类型的存储节点。

## Exadata 适用场景
    
![](http://ww3.sinaimg.cn/large/006tNc79gy1g3p1byj16jj30u00gw0u6.jpg)

* 数据仓库分析 - 涵盖场景1和4
* 数据库整合 - 涵盖场景2和3

## Exadata 与国产数据库一体机的区别
硬件方面采用的都是开放的标准件，如X86服务器，Intel CPU，Infiniband交换机，Flash卡。
本质的区别在软件层面，Exadata比较重要的技术特性包括：
1. Smart Scan - 解决IO瓶颈（10-100倍数据处理）
2. Smart Flash Cache - 提升处理效率（10-100倍IO速度）
3. Hybrid Columnar Compression - 节省存储成本（10-50倍压缩比）

## Exadata 高可用性
硬件层面 - 冗余部件，多路径和RAID等技术实现
软件层面 - 沿用Oracle数据库的高可用架构。Eg：备份，RAC，ADG，ASM等
![](http://ww3.sinaimg.cn/large/006tNc79gy1g3p3wkmlb5j30u00gwmys.jpg)

## Exadata 扩展性
水平扩展 - Exadata最小配置为1/8机架，1/8的唯一升级路径是到1/4机架，在1/4机架基础上，可以进行灵活扩展

垂直扩展 - 增加内存




