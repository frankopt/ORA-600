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


