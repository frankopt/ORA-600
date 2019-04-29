# SQLPLUS 常用命令

1. show user - 显示当前用户
2. select * from tab; - 显示表


## desc (object_name) - 描述对象结构

```
SQL> desc emp
```

## ed

```
<显示默认编辑器>
SQL> define
...
DEFINE _EDITOR      ="ed" (CHAR)
...

<修改默认编辑器为 vi>
SQL> define _editor='vi'
SQL> ed /tmp/test.txt (调用vi编辑器)

另外一种方式：
SQL> host vi /tmp/test.txt

```

## spool (filename) [rep/append]
将屏幕输出保留到指定文件中，

* 替换内容使用 replace
* 追加内容使用 append
* 关闭屏幕内容输出到文件使用 spool off

```
SQL> spool /tmp/test.txt

SQL> select * from tab;

SQL> spool off
```

## prompt 定义提示符
比如修改连接到 SQLPLUS 的doc

```
SQL> prompt frank>
frank>
```

## accept 提示用户输入变量的值

```
SQL> help accept 
```


## save (fname) 保存buf中的sql到文件

```
SQL> select * from dept
SQL> save /tmp/test.sql
```

## get (fname) 读入到buf中但不执行
```
SQL> get /tmp/test.sql
  1*  select * from dept

SQL> run
  1*  select * from dept

SQL> l
  1*  select * from dept

SQL> list
  1*  select * from dept
```
## start (fname) 读入到buf中并执行


## & 定义临时变量(传值)

```
SQL> select ename,sal from emp where empno=&e;
(定义临时变量)

Enter value for e: 7788

SQL> /
(可反复调用)
```

## && - 变量的引用
```
SQL> select &&e,ename,sal from emp where &e=7900;

Enter value for e: empno
```

## define [变量] - 定义临时变量
```
SQL> define e=7902;

SQL> select ename,sal from emp where empno=&e;

```

## undefine [变量]
取消临时变量的定义

```
SQL> undefine e
```

## var[iable] [变量]
定义一个 sql 可调用的变量

```
SQL> var v1 number
SQL> exec :v1 :=7900
PL/SQL procedure successfully completed.

SQL> select ename,sal from emp where empno=:v1;
ENAME     SAL
------  ------
JAMES       950
```

## show

```
SQL> show all
<查看所有变量设置情况>
```

## set
```
SQL> show timing
timing off

SQL> set timing on
<显示执行SQL语句所用时间>

SQL> ***
...
Elapsed: 00:00:00:00

```


<上述方式为临时设置，若要永久修改>
**vi login.sql**

```
define _editor='vi'
set timing on
```


