# AWS 云计算

全球云基础设施即服务魔力象限 评估了全球云 IaaS 市场中的 6 家供应商。Amazon Web Services 再次被置于领导者象限中，被认为拥有最强大的执行能力和深刻的洞察力。 
![](http://ww3.sinaimg.cn/large/006tNc79gy1g3a55nhidej30u00u076v.jpg)


## Amazon EC2
Amazon Elastic Compute Cloud (Amazon EC2) 是一种 Web 服务，可以在云中提供安全并且可调整大小的计算容量。该服务旨在让开发人员能够更轻松地进行 Web 规模的云计算。

Amazon EC2 的 Web 服务接口非常简单，您可以最小的阻力轻松获取和配置容量。使用该服务，您可以完全控制您的计算资源，并可以在成熟的 Amazon 计算环境中运行。Amazon EC2 将获取并启动新服务器实例所需要的时间缩短至几分钟，这样一来，在您的计算要求发生变化时，您便可以快速扩展或缩减计算容量。Amazon EC2 按您实际使用的容量收费，改变了计算的成本结算方式。Amazon EC2 还为开发人员提供了创建故障恢复应用程序以及排除常见故障情况的工具。


# Amazon EC2 实例类型
A1
T2 T3 T3a 
M4 M5 M5a

## T2 实例
可突增的性能实例，提供基本级别的CPU性能并能够突增到基准之上。

T2 Unlimited 实例可以在工作负载需要时保持较高的 CPU 性能。对于大多数通用工作负载而言，T2 Unlimited 实例无需额外花费即可提供丰富的性能。如果实例需要长期以较高的 CPU 使用率运行，您需要额外支付每个 vCPU 小时 5 美分的固定费用。

基本性能和突增能力受到 CPU 积分的限制。T2 实例根据实例大小以固定的速度持续接收 CPU 积分，实例闲置时累积 CPU 积分，实例使用时消耗 CPU 积分。对于包括微服务、低延迟交互应用程序、中小型数据库、虚拟桌面、开发、构建和暂存环境、代码库和产品原型在内的各种通用工作负载，T2 实例是一种很好的选择。

#### 特点：
* 高频 Intel Xeon 处理器
* 性能可突增的 CPU，受到 CPU 积分的限制，持续基本性能
* 成本最低的通用实例类型，支持免费套餐*
* 计算、内存和网络资源的平衡

#### 使用案例

网站和 Web 应用程序、开发环境、构建服务器、代码存储库、微服务、测试和暂存环境以及众多业务应用程序。 

## Amazon Lightsail
Amazon Lightsail is the easiest way to get started with AWS for developers, small businesses, students, and other users who need a simple virtual private server (VPS) solution. Lightsail provides developers compute, storage, and networking capacity, and it also provides capabilities to deploy and manage websites and web applications in the cloud. Lightsail includes everything you need to launch your project quickly--a virtual machine, solid state drive (SSD)-based storage, data transfer, Domain Name System (DNS) management, and a static IP--for a low, predictable monthly price.