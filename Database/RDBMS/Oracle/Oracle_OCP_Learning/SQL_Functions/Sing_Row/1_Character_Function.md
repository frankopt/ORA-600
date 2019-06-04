# Two Types of SQL Functions
* Single-Row
* Multiple-Row

## Single-Row Functions

### 作用：
1. 操作数据
2. 对输入的变量进行处理，每行返回一个结果
3. 处理返回的每一行
4. 转换数据类型
5. 嵌套使用
6. 传入的变量可以是列的值，也可以是表达式的值

### 分类
1. character (字符)
2. Numeber
3. Date
4. General （空值）
5. Conversion （转换）


-------
#### 1. Character Functions
大小写类：(前3个)
字符处理类：（其余）

* Lower    ---all    A-Z
* Upper    ---all    a-z
* Initcap    ---first


* Concat    ---连接函数，只能连接两个表达式
* Substr    ---切片函数，substr(expr,m,n); m<|+- num>; **n>0**
* Length    ---长度计算函数:Length,LengthB,LengthC,Length2,Lengh4
* Instr    ---查找指定的字符出现位置，instr(expr,'char')
* Lpad / Rpad    ---左/右填充
* Trim    ---删除，trim(both|leading|trailing 'char' from expr)
* Replace    ---替换，replace(expr,old,new)

##### Lower Upper Initcap
```
SQL> select ename from emp where deptno=10;

SQL> select lower(ename) from emp where deptno=10;
SQL> select initcap(ename) from emp where deptno=10;

SQL> select upper('king scott') from dual;
UPPER('KING
----------
KING SCOTT

```

##### concat
```
SQL> select concat(ename, 'is work'),job from emp where deptno=10;

SQL> select concat( concat(ename, 'is work'),job) from emp where deptno=10;
```

##### substr
```
SQL> select ename from emp where substr(ename,2,1)='A';
```

##### length
```
SQL> select length(ename),ename from emp;
```
三个字节存储一个汉字，使用 Length 计算长度时 会体现出不同。

##### instr
```
SQL> select instr(ename,'A'),ename from emp;
```
##### rpad lpad
rpad, lpad
默认情况下 数字列靠右对齐，字符列靠左对齐。
可以使用上述两个函数调整对齐方式：

```
SQL> select deptno, lpad(dename,15,' ')dename,loc from dept;
```
此方式只是调整数据行，欲使标题列也变动，需要单独调整。

```
SQL> col dname just right
```
##### trim
Eg:

```
trim('A' from 'AAABBBCCCAAA')
BBBCCC
<both 默认省略>

trim(leading 'A' from 'AAABBBCCCAAA')
BBBCCCAAA

trim(trailing 'A' from 'AAABBBCCCAAA')
AAABBBCCC
```

下面两个在Oracle 10g及之后 才支持

* ltrim(expr,'char')
* rtrim(expr,'char')

##### replace

