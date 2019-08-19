x86/x86_64 CPU控制寄存器（Control Registers）
x86/x86_64 CPU中提供了控制寄存器，来决定CPU的操作模式和当前执行任务的属性。这些寄存器在32位模式下是32bit，在64位模式中，控制寄存器扩展为64位。

CPU架构中共有CR0、CR1、CR2、CR3、CR4、CR8共6个控制寄存器，如下图。
各个控制寄存器的作用如下：

![](https://i.loli.net/2019/08/19/InqBKwcmaRTE6iH.jpg)

CR0：包含当前处理器运行的控制标志。
CR1：保留。
CR2：包含发生页面错误时的线性地址。
CR3：页面目录表（Page Directory Table）的物理地址。
CR4：包含处理器扩展功能的标志位。
CR8：提供对任务优先级寄存器（Task Priority Register）的读写（仅在64位模式下存在）。
对控制寄存器的读写是通过MOV CRn指令来实现