# SQLPLUS 常用命令

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
(or SQL> r or SQL> /)  <----运行缓冲区中的语句 
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