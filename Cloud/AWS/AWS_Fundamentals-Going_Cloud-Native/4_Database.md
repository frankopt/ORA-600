# Relational and NoSQL databases on AWS
databases are one of the most important parts of any application. 

![](http://ww2.sinaimg.cn/large/006tNc79gy1g3cd3975v9j30c10ao0v8.jpg)

* One of the great things about AWS is by simply moving your database onto EC2

## RDS (Amazon Relational Database Service)
Amazon RDS currently supports six database engines:

Amazon Aurora: https://aws.amazon.com/rds/aurora/
PostgreSQL: https://aws.amazon.com/rds/postgresql/
MySQL: https://aws.amazon.com/rds/mysql/
MariaDB: https://aws.amazon.com/rds/mariadb/
Oracle: https://aws.amazon.com/rds/oracle/
Microsoft SQL Server: https://aws.amazon.com/rds/sqlserver/

## AWS DMS
AWS Database Migration Service 可帮助您快速并安全地将数据库迁移至 AWS。源数据库在迁移过程中可继续正常运行，从而最大程度地减少依赖该数据库的应用程序的停机时间。AWS Database Migration Service 可以在广泛使用的开源商业数据库之间迁移您的数据。

AWS Database Migration Service 支持同构迁移（例如从 Oracle 迁移至 Oracle），以及不同数据库平台之间的异构迁移（例如从 Oracle 或 Microsoft SQL Server 迁移至 Amazon Aurora）。借助 AWS Database Migration Service，您可以持续地以高可用性复制数据，并通过将数据流式传输到 Amazon Redshift 和 Amazon S3，将数据库整合到 PB 级的数据仓库中。

## DynamoDB (NoSQL database)
Amazon DynamoDB 是一个键/值和文档数据库，可以在任何规模的环境中提供个位数的毫秒级性能。它是一个完全托管的多区域多主数据库，具有适用于 Internet 规模的应用程序的内置安全性、备份和恢复和内存缓存。DynamoDB 每天可处理超过 10 万亿个请求，并支持每秒超过 2000 万个请求的峰值