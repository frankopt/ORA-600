# Oracle存储体系 - 逻辑结构

![](https://ws3.sinaimg.cn/large/006tNc79gy1g2w1za03doj30xw0em0vl.jpg)

## Oracle中默认的表空间 SYSTEM 和 SYSAUX
SYSTEM 和 SYSAUX 表空间是在创建数据库时 创建的必须存在的表空间。
* SYSTEM 表空间 - 用于核心功能（eg：数据字典表）
* SYSAUX 表空间 - 附加的数据库组件
* Oracle data block 会映射到 磁盘块。不要使用 SYSTEM 和 SYSAUX 表空间来存储应用程序的数据。

## Oracle 12c

![](https://ws1.sinaimg.cn/large/006tNc79gy1g2w4w2yy8ej31400p00y5.jpg)