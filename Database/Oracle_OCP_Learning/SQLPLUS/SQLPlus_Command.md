# SQLPLUS 常用命令

本机上没有装Database，但是装有 SQLPlus，可以连接远程的数据库。


1. show user - 显示当前用户
2. select * from tab; - 显示表


## desc (object_name) - 描述对象结构

```
SQL> desc emp
```

## ho[st] / !  调用操作系统命令

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

## list  查看buf中的SQL
```
SQL> l
(查看缓冲区的命令)
  1*  select * from dept

SQL> list
  1*  select * from dept
```
## start (fname) 读入到buf中并执行
```
SQL> start /tmp/test.sql
(or SQL> @ /tmp/test.sql)
```

## del 删除buf中的SQL

## clear buffer 删除buf中所以SQL
```
SQL> cle buff
<可简写为>
```
## clear screen 清屏
```
SQL> cle scr
<可简写为>
```

## c[hange] /old_value/new_value 更改第一次出现的字符
```
SQL> select * from dpet;
select * from dpet;
                *
ERROR at line 1:
ORA-00942: table or view does not exist

SQL> l
    1*  select * from dpet;  <SQL 在 buf 中>

SQL> c/pe/ep
    1*  select * from dept;

SQL> /  <执行>

```

## I[NPUT]
```
SQL> l
    1  select deptno,dname
    2* from dept;
    
SQL> 1
    1  select deptno,dname
    
SQL> i ,loc
    
SQL> l
    1  select deptno,dname
    2  ,loc
    3* from dept;
            
```


## A[PPEND]
```
SQL> select deptno
    2   from dept;
    
    DEPTNO
----------
        10
        20
        30        
SQL> l
    1  select deptno
    2* from dept;

SQL> 1
    1  select deptno
    
SQL> a, dname
    1  select deptno,dname

SQL> l
    1  select deptno,dname
    2* from dept;    
```

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

* set heading off/on 列标题
* set feedback off/on 行返回值
* set pagesize 0/n 行数
* set linesize n 行的长度
* set newpage 1/n/none 返回值行间隔
* set null text
* set numformat format
* set numwidth 10/n
* set autocommit 事物自动提交
* set long
* set timing on/off
* set autotrace
* set array

## col
COL[UMN] [{column | expr} [option...]]

```
SQL> col dname heading 'deptpartment | name'

SQL> select * from dept;

DEPTNO    deptpartment  LOC
              name
    10    ACCOUNTING    NEW YORK
    20    RESEARCH      DALLAS
    30    SALES         CHICAGO

```


