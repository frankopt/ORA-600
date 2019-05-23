# Networking and Storage

## VPC (Virtual Private Cloud) 
Which is used to isolate your application from the millions, hundreds of millions of other applications all running on AWS as well. 

借助 Amazon Virtual Private Cloud (Amazon VPC)，您可以在 AWS 云中预置一个逻辑隔离的部分，从而在自己定义的虚拟网络中启动 AWS 资源。您可以完全掌控您的虚拟联网环境，包括选择自己的 IP 地址范围、创建子网以及配置路由表和网络网关。您在 VPC 中可以使用 IPv4 和 IPv6，因此能够轻松安全地访问资源和应用程序。

您可以轻松自定义 Amazon VPC 的网络配置。例如，您可以为可访问 Internet 的 Web 服务器创建公有子网，而将数据库或应用程序服务器等后端系统放在不能访问 Internet 的私有子网中。您可以利用安全组和网络访问控制列表等多种安全层，对各个子网中 Amazon EC2 实例的访问进行控制。

### VPC 和子网基础知识
下图显示了具有 IPv4 CIDR 块的新 VPC 及主路由表。
![](http://ww3.sinaimg.cn/large/006tNc79gy1g3bcyfmtf7j30dv0h274x.jpg)

VPC 跨越区域中的所有可用区。在创建 VPC 之后，您可以在每个可用区中添加一个或多个子网。在创建子网时，指定子网的 CIDR 块，它是 VPC CIDR 块的子集。每个子网都必须完全位于一个可用区之内，不能跨越多个可用区。可用区是被设计为可以隔离其他可用区的故障的不同位置。通过启动独立可用区内的实例，您可以保护您的应用程序不受单一位置故障的影响。我们为每个子网指定一个唯一 ID。

# Quiz
1. When creating a VPC, what items must you include? (Select two)
    * IP Range
    * Region
