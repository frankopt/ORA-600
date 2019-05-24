# Storage
![](http://ww4.sinaimg.cn/large/006tNc79gy1g3bds6vu0jj30kz0b4te7.jpg)

## Amazon Elastic Block Store (Amazon EBS)
给Amazon的EC2实例提供了高可用高可靠的块级存储卷。EBS适合于一些需要访问块设备的应用，比如数据库、文件系统等。

# Amazon Simple Storage Service (Amazon S3) 
Amazon Simple Storage Service (Amazon S3) stores data as objects within resources that are called buckets. You can store as many objects as you want within a bucket, and you can write, read, and delete objects in your bucket. Objects can be up to 5 TB in size.

![](http://ww1.sinaimg.cn/large/006tNc79gy1g3bfhh0pdfj31d60k0dlz.jpg)

You can control access to both the bucket and the objects (who can create, delete, and retrieve objects in the bucket for example), and view access logs for the bucket and its objects. You can also choose the AWS Region where a bucket is stored to optimize for latency, minimize costs, or address regulatory requirements.

Amazon Simple Storage Service (Amazon S3) 是一种对象存储服务，提供行业领先的可扩展性、数据可用性、安全性和性能。这意味着各种规模和行业的客户都可以使用它来存储和保护各种用例（如网站、移动应用程序、备份和还原、存档、企业应用程序、IoT 设备和大数据分析）的任意数量的数据。Amazon S3 提供了易于使用的管理功能，因此您可以组织数据并配置精细调整过的访问控制以满足特定的业务、组织和合规性要求。Amazon S3 可达到 99.999999999%（11 个 9）的持久性，并为全球各地的公司存储数百万个应用程序的数据。

# Amazon Elastic File System (Amazon EFS) ​
Amazon Elastic File System (Amazon EFS) ​为基于 Linux 的工作负载提供简单、可扩展的弹性文件系统，可与 ​AWS 云服务和本地资源配合使用。它可在不中断应用程序的情况下按需扩展到 PB 级，在您添加或删除文件时自动扩展或缩减，从而让您的应用程序在需要时获得所需存储。它旨在为数千个 Amazon EC2 实例提供大规模并行共享访问模式，可让您的应用程序在一致、低延迟的状态下实现高水平的总吞吐量和 IOPS。Amazon EFS 是一项完全托管的服务，不需要对现有应用程序和工具进行更改，并通过标准的文件系统界面提供访问以实现无缝集成。Amazon EFS 提供标准和不频繁访问存储类。通过使用生命周期管理，可将 30 天未访问的文件自动移动到成本优化型不频繁访问存储类，让您可以在同一文件系统中轻松存储和访问活动的不经常访问文件系统数据，同时存储成本降低高达 85%。Amazon EFS 是一种用于在多个可用区 (AZ) 中存储数据以提供高可用性和持久性的区域服务。您可以跨可用区、区域和 VPC 访问文件系统，并可以通过 AWS Direct Connect 或 AWS VPN 在数千个 Amazon EC2 实例与本地服务器之间共享文件。

Amazon EFS 还非常适合用来支持各种使用案例，从要求超高吞吐量的高度并行化的横向扩展工作负载到单线程的延迟敏感型工作负载，均适用。例如，直接迁移企业应用程序、大数据分析、Web 服务和内容管理、应用程序开发和测试、媒体和娱乐工作流程、数据库备份和容器存储。