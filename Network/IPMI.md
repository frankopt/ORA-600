## IPMI的功能
通过web访问IPMI，你可以实现对机器的操作，linux 下可以通过ipmitool 直接访问:

* 开机，关机，重启，查看机器当前的通电状态
* 安装系统。有些服务器的IPMI，没有内置iKVM，无法实现系统的安装。这个估计和成本有关
* 修改IPMI的网络和IP地址
* 修改bios设置，可以通过IPMI进入bios
* 设置Raid。这个目前对鼠标支持很差。要想设置raid，就只能用键盘操作。这方面IBM，Dell，HP做的不错，他们完全是可以使用鼠标操作。


## IPMItool使用
很多人希望使用IPMI做带外管理。如果直接使用是有问题的。在OS层面上，你是可以修改IPMI的设置。也就是说，对于linux来说，有专门的驱动，让你修改底层IPMI的设置，包括修改你的IPMI的用户名和密码。

安装IPMItool无论是centos，还是ubuntu都可以直接安装，源里都有
yum -y install ipmitool
apt-get -y install ipmitool

内核加载

```
modprobe ipmi_msghandler
modprobe ipmi_devintf
modprobe ipmi_si
```

这个时候，你就基本可以对IPMI进行各种设置，你web可以做到的，命令行下都应该可以实现。
DELL的<channel_no>是1，HP的是2 ，超微的是1，如果提示你输入channel_no 就输入就可以。
查看IPMI用户IPMItool，可以查看本地的ＢＭＣ的设置，查看本地是不需要身份验证。如果查看远程，需要提供IPMI 的用户名和密码。

```
# ipmitool user list 1
ID  Name             Callin  Link Auth  IPMI Msg   Channel Priv Limit
2   ADMIN            false   false      true
# ipmitool user list 1 ID Name Callin Link Auth IPMI Msg Channel Priv Limit 2 ADMIN false false true ADMINISTRATOR
```

重设管理员密码，2表示管理员ID，后面就是管理员的新密码

```
ipmitool user set password 2 chenshake


我尝试添加用户，是没问题，不过无法给用户设置管理员权限。这个问题以后慢慢解决。
设置IPMI ip 地址

```
# ipmitool lan set 1 ipsrc dhcp
# ipmitool lan print 1
# ipmitool lan set 1 ipsrc static
# ipmitool lan set 1 ipaddress 10.1.199.211 Setting LAN IP Address to 10.1.199.211
# ipmitool lan set 1 netmask 255.255.255.0 Setting LAN Subnet Mask to 255.255.255.0
# ipmitool lan set 1 defgw ipaddr 10.1.199.1 Setting LAN Default Gateway IP to 10.1.199.1 
# ipmitool lan print 1
```

命令说明:
使用静态地址：ipmitool lan set <channel_no> ipsrc static
使用动态地址：ipmitool lan set <channel_no> ipsrc dhcp
设置IP：ipmitool lan set <channel_no> ipaddr <x.x.x.x>
设置掩码：ipmitool lan set <channel_no> netmask <x.x.x.x>
设置网关：ipmitool lan set <channel_no> defgw ipaddr <x.x.x.x>
本地操作 -I open 表示接口本地：ipmitool -I open lan print 1
操作远程机器 -I lan 表示接口远程：ipmitool -I lan -H 10.1.199.12 -U ADMIN -P ADMIN lan print 1

改变服务器引导方式:
ipmitool -I lan -H 10.1.199.212 -U ADMIN -P ADMIN chassis bootdev pxe
ipmitool -I lan -H 10.1.199.212 -U ADMIN -P ADMIN chassis bootdev disk
ipmitool -I lan -H 10.1.199.212 -U ADMIN -P ADMIN chassis bootdev cdrom

服务器电源管理:
ipmitool -I lan -H 10.1.199.212 -U ADMIN -P ADMIN chassis power off
ipmitool -I lan -H 10.1.199.212 -U ADMIN -P ADMIN chassis power reset
ipmitool -I lan -H 10.1.199.212 -U ADMIN -P ADMIN chassis power on
ipmitool -I lan -H 10.1.199.212 -U ADMIN -P ADMIN chassis power status

其他
IPMI需要进入bios，进行设置IP地址。这个本身没什么特别。不过有时候你会发现设置完IPMI的IP地址后，无法访问，也无法ping通。你会以为IPMI出问题了。
这个时候，你需要完全拔掉机器的电源，等待5分钟，把网线插入IPMI的网卡。这个时候，插上电源，就算不开机，也应该可以ping通，访问。这个问题折腾了我很长时间。
机器加电前，需要把IPMI的网线插上，这样可以初始化。
另外默认IPMI是DHCP获得IP。
