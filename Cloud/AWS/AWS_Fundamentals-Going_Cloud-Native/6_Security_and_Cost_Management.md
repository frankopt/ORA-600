# Security and Cost Management

 AWS offers a wide range of encryption tools, whether it's simply a bring-your-own-encryption to automatic server-side encryption on S3 and EBS. Or perhaps, you'd like a more robust managed keys, using AWS CloudHSM or KMS, the Key Management Service. That allows you to retain high level controls even when you've got security like a FIPS 140-2 compliance, we can take care of that and give you the validations needed, so you can prove your certifications.
 
 ![](http://ww3.sinaimg.cn/large/006tNc79gy1g3cg7h8jkgj30xo0igdjc.jpg)
 
 AWS 负责“云本身的安全” – AWS 负责保护运行所有 AWS 云服务的基础设施。该基础实施由运行 AWS 云服务的硬件、软件、网络和设备组成。

客户负责“云内部的安全” – 客户责任由客户所选的 AWS 云服务确定。这决定了客户在履行安全责任时必须完成的配置工作量。例如，Amazon Elastic Compute Cloud (Amazon EC2) 等服务被归类为基础设施即服务 (IaaS)，因此要求客户执行所有必要的安全配置和管理任务。部署 Amazon EC2 实例的客户需要负责来宾操作系统（包括更新和安全补丁）的管理、客户在实例上安装的任何应用程序软件或实用工具，以及每个实例上 AWS 提供的防火墙（称为安全组）的配置。 对于抽象化服务，例如 Amazon S3 和 Amazon DynamoDB，AWS 运营基础设施层、操作系统和平台，而客户通过访问终端节点存储和检索数据。客户负责管理其数据（包括加密选项），对其资产进行分类，以及使用 IAM 工具分配适当的权限。