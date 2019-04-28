# 常用数字函数

| Function |  Example  |Result |  
| --- | --- | --- |
| 按指定的小数四舍五入  |Round(45.926,2) | 45.93 | 
| 按指定的小数截断数据  |Trunc(45.926,2) | 45.92 |
|  两数相除，返回余数 |Mod(1600,300) | 100 |
|  取绝对值 | abs(-123) | 123 |

## round / trunc
```
SQL> select round(456.789, -2),trunc(456.789,2) from dual

round(456.789, -2)  trunc(456.789,2)
-----------------   -----------------
            500               456.78

SQL> c/-2/-1
    1* select round(456.789, -1),trunc(456.789,2) from dual

SQL> /

ROUND(456.789, -2)  TRUNC(456.789,2)
-----------------   -----------------
            460               456.78

```
## mod
```
SQL> select mod(2001,5) from dual;

MOD(2001,5)
-----------
          1
```

## abs
```
SQL> select abs(-123) from dual;

 ABS(-123)
-----------
         123
```


