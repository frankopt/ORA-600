# Monitoring and Scaling Application

## Amazon CloudWatch
Amazon CloudWatch 是一种面向开发人员、系统操作员、网站可靠性工程师 (SRE) 和 IT 经理的监控和管理服务。CloudWatch 为您提供相关数据和切实见解，以监控应用程序、了解和响应系统范围的性能变化、优化资源利用率，并在统一视图中查看运营状况。

* Amazon CloudWatch Events
* Amazon CloudWatch Logs Metrics

## Load Balance
* HA proxy servers
* F5

### ELB < Amazon Elastic Load Balancer>
Elastic Load Balancing 在多个目标（如 Amazon EC2 实例、容器、IP 地址和 Lambda 函数）之间自动分配传入的应用程序流量。它可以在单个可用区内处理不断变化的应用程序流量负载，也可以跨多个可用区处理此类负载。Elastic Load Balancing 提供三种负载均衡器，它们均能实现高可用性、自动扩展和可靠的安全性，因此能让您的应用程序获得容错能力。
* Application Load Balancer
* 网络负载均衡器
* Classic Load Balancer

# Amazon EC2 Auto Scaling
使用 Amazon EC2 Auto Scaling，您可以维持应用程序的可用性，并且根据您定义的条件自动添加或删除 EC2 实例。您可以使用 EC2 Auto Scaling 的队列管理功能维护队列的运行状况和可用性。您还可以使用 EC2 Auto Scaling 的动态和预测扩展功能添加或删除 EC2 实例。动态扩展响应不断变化的需求，预测扩展会根据预测的需求自动安排正确数量的 EC2 实例。动态扩展和预测扩展可结合使用，以实现更快的扩展。 