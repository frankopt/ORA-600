#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
第1行和第2行是标准注释
第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，
第2行注释表示.py文件本身使用标准UTF-8编码；
'''

' tenThousandLineCodeLearningPython '

_author_ = 'frank'



#-- 语法规则
    1. 统一缩进
    2. 可以使用反斜杠(\)来实现多行语句
    # 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)
    3. 标识符名称是对大小写敏感的
    # 标识符的第一个字符必须是字母中的字母（大写或者小写）或者一个下划线（‘_’）
    4. 单引号('')与双引号("")表示相同


#-- 多行注释
    python 中多行注释使用 三个单引号 或 三个双引号。

    #!/usr/bin/python
    # -*- coding: UTF-8 -*-
    # 文件名：test.py

    '''
    这是多行注释，使用单引号。
    这是多行注释，使用单引号。
    这是多行注释，使用单引号。
    '''

    """
    这是多行注释，使用双引号。
    这是多行注释，使用双引号。
    这是多行注释，使用双引号。
    """


#-- pip默认安装路径：
    1. 其实最简单你pip install xxx应用后，你再执行一次这命令，会提示你已经安装过了，然后会把地址给你打印出来
    2.
    frank@Frank-s-Macbook-Pro:~/Python$pip show pexpect
    Name: pexpect
    Version: 4.4.0
    Summary: Pexpect allows easy control of interactive console applications.
    Home-page: https://pexpect.readthedocs.io/
    Author: Noah Spurrier; Thomas Kluyver; Jeff Quast
    Author-email: noah@noah.org, thomas@kluyver.me.uk, contact@jeffquast.com
    License: ISC license
    Location: /Library/Python/2.7/site-packages
    Requires: ptyprocess


#-- Python 内置函数
    >>> dir(__builtins__)
    ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
    >>>


#-- 输入输出
    Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里。比如输入用户的名字：
    name = input()

    print语句也可以跟上多个字符串，用逗号“,”隔开，就可以连成一串输出:
    print ('The quick brown fox', 'jumps over', 'the lazy dog')
    #结果
    The quick brown fox jumps over the lazy dog


#-- 标识符
    在Python里，标识符用字母、数字和下划线组成。
    区分大小写


#-- 保留字（自留地0_0）
    >>> import keyword
    >>> print (keyword.kwlist)
    ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
    >>> print(keyword.iskeyword('from'))
    True
    >>>


#-- 运算符
    #-- 算术运算符
        +
        -
        *
        /
        % 取余
        ** 幂
        // 取整

    #-- 赋值运算符
        =
        += 加法赋值运算符 a += b 等效于 a = a + b
        -=
        *=
        /=
        %=
        **=
        //=

    #-- 比较运算符
        ==
        != 不等于
        < > 不等于，类似 !=
        >
        <
        >=
        <=

    #-- 逻辑运算符
        and
        or
        not

    #-- 成员运算符
        in
        not in

    #-- 身份运算符
        is
        is not

            id()函数 用于获取对象内存地址
            >>> a = 1
            >>> print(id(a))
            140437846251560
            >>>


#-- 转义字符

    在字符串中需要使用特殊字符时，用反斜杠 \  转义字符.
    \       (在行尾时) 续行符
    \       反斜杠符号
    \’      单引号
    \”      双引号
    \a      响铃
    \b      退格(Backspace)
    \e      转义
    \000    空
    \n      换行
    \v      纵向制表符
    \t      横向制表符
    \r      回车
    \f      换页
    \oyy    八进制数，yy代表的字符，例如：\o12代表换行
    \xyy    十六进制数，yy代表的字符，例如：\x0a代表换行
    \other  其它的字符以普通格式输出


#-- 格式化字符串输出

    尽管这样会用到非常复杂的表达式
    最基本的用法是将一个值插入到一个有 字符串格式符 %s 的字符串中

    %s  格式化字符串
    %d  格式化整数
    %f  格式化浮点数字，可指定小数点后的精度


#-- 常用字符串处理函数
    len(s)
    s.upper()
    s.lower()
    s.swapcase()    # 字符串中大小转小写，小写转大写

    >>> s.ljust(20)       # 固定长度，左对齐
    'sadjbf              '
    >>> s.rjust(20)       # 固定长度，右对齐
    '              sadjbf'
    >>> s.center(20)      # 固定长度，中间对齐
    '       sadjbf       '


    >>> mm = 'sdakjhfdwefbkbkfwefukwiuebkefwieubfwe'
    >>> mm.find('bk')     # 要检索的字符串
    11
    >>> mm.find('sadjbf') # 没有，返回 -1
    -1
    >>>
    >>> mm.rfind('bk')    # 从右侧开始搜索
    25
    >>> mm.count('bk')    # 统计 字符串 出现的次数
    3

    >>> mm.index('bk')    # have same function with find, but return error if not find the string
    11
    >>>
    >>> mm.index('bksad')
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    ValueError: substring not found

    >>> mm.replace('bk','love',3)   # replace bk to love, 3 mean 替换的次数
    'sdakjhfdweflovelovefwefukwiueloveefwieubfwe'



    >>> nn ='   asdhbja sajkdb  sakjdb  '
    >>> print(nn.strip())       # 去掉字符串 两边空格
    asdhbja sajkdb  sakjdb
    >>> print(nn.lstrip())
    asdhbja sajkdb  sakjdb
    >>> print(nn.rstrip())
       asdhbja sajkdb  sakjdb


    >>> print(nn.split(' '))        # 按指定字符分割字符串为数组
    ['', '', '', 'asdhbja', 'sajkdb', '', 'sakjdb', '', '']
    >>> print(nn.startswith(' '))       # 字符串是否以 ‘ ’ 开头
    True
    >>> print(nn.endswith(' '))         # 字符串是否以 ‘ ’ 结尾
    True

    print(s.isalnum())  是否全为字母或数字(要么全是字母，要么全是数字)
    print(s.isalpha())  是否全为字母
    print(s.isdigit())  是否全为数字
    print(s.islower())  是否全是小写
    print(s.isupper())  是否全是大写
    print(s.istitle())  s的首字母是否是大写


#-- 判断一个对象的属性是否存在，若不存在就添加该属性
    hasattr(object,name)
    getattr(object,name,[default])
    setattr(object,name,values)


#-- 变量


    #-- 5个标准的数据类型
        1.Numbers
            #--四种不同的数字类型
            int
            long # Python使用 L 显示长整型
            float
            complex(a,b) # 复数,实部a 和 虚部b 都是float

        2.String
            string是由 数字、字母和下划线 组成的一串字符
            str = 'Hello World!'
            print （str[2:5]）      # 输出字符串中第三个至第五个之间的字符串
            print （str[2:]）       # 输出从第三个字符开始的字符串
            print （str * 2）       # 输出字符串两次
            print （str + "TEST"）  # 输出连接的字符串


        3.List # 用[]标识，是Python中 最通用的复合数据类型

            list 里的每个元素都分配一个 位置索引，从0开始记起

            #!/usr/bin/python
            list = [ 'ss', 786 , 2.23, 'joshn', 70.2 ]
            tinylist = [123, 'joshn']

            print (list)               # 输出完整列表
            print (list[0])            # 输出列表的第一个元素
            print (list[1:3])          # 输出第二个至第三个的元素
            print (list[2:])           # 输出从第三个开始至列表末尾的所有元素
            print (tinylist * 2)       # 输出列表两次
            print (list + tinylist)    # 打印组合的列表

            > list 内置方法

            L.append(var) #
            L.extend(list) #追加list,即合并list到L上

            L.insert(index,var) #插入指定的位置

            L.pop(var) #返回最后一个元素，并从list中删除;list.pop(x)#如果不写x，就如同这个操作，默认删除最后一个，并且将该结果返回
            L.remove(var) #删除第一次出现的该元素

            L.count(var) #该元素在列表中出现的个数
            L.index(var) #该元素的位置，没有则抛出异常

            L.sort() #排序
            L.reverse() #倒叙

            > range生成list操作 # range(start, stop, step)是一个内置函数
                >>> range(9) #stop=9，别的都没有写，含义就是range(0,9,1)
                [0, 1, 2, 3, 4, 5, 6, 7, 8] #从0开始，步长为1,增加，直到小于9的那个数



        4.Tuple # 用 () 标识，内部元素用逗号隔开
            a. tuple 内部元素不能二次赋值，相当于只读list
            b. tuple 中的元素值不允许删除
            b. tuple 可以组合

            > tuple 内置函数
            len(tuple)
            max(tuple)
            min(tuple)
            tuple(seq)  # change list to tuple
                >>> list1 = ['google','oracle','apple']
                >>> tuple1 = tuple(list1)
                >>> print(tuple1)
                ('google', 'oracle', 'apple')


        5.Dictionary # dict，{ } ,在某些语言中称为 map，使用key-value 存储，具有极快的查找速度
                a.可存储多个元素的对象称为container(包括 list,tuple,dict)
                b.list是有序的对象集合< 偏移存取 >，dict是无序的对象集合< 键存取 >
            dict 的键
            a.键不允许重复
            b.键不可变更
                可用 数字、字符串、元组 充当，列表不行
            dict 的值可以没有任何限制地取任何Python对象

            > dict 内置函数&方法
            len(dict)
            str(dict) # 以字符串表示
            type(dict) # 返回输入的变量类型

            d.clear() # 删除字典内所有元素
            d.copy() # 返回一个字典的浅复制
            key in dict # 如果键在字典dict里返回true，否则返回false

            d.items() # 以列表返回可遍历的(键, 值)
                    >>> dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
                    >>> print "字典值 : %s" %  dict.items()
                    字典值 : [('Google', 'www.google.com'), ('taobao', 'www.taobao.com'), ('Runoob', 'www.runoob.com')]
            d.keys() # 以列表返回一个字典所有的键
            d.values() # 以列表返回字典中的所有值
            d.get(key, default=None) # 返回指定键的值，如果值不在字典中返回default值
            d.setdefault(key, default=None) # 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
            d.update(dict2) # 把字典dict2的键/值对更新到dict里

            # 遍历字典列表
                for key,values in  dict.items():
                    print key,values

    #-- set：基本数据类型的集合类型
            1. 可变集合 set
            2. 不可变集合 frozenset

            > set 内置方法
            集合add方法：是把要传入的元素做为一个整个添加到集合中
                >>> a = set('sadjbf')
                >>> a.add('oracle')
                >>> a
                set(['a', 'b', 'd', 'f', 'j', 's', 'oracle'])
            集合update方法：是把要传入的元素拆分，做为个体传入到集合中
                >>> a.update('oracle')
                >>> a
                set(['a', 'c', 'b', 'e', 'd', 'f', 'j', 'l', 'o', 's', 'r', 'oracle'])
            集合删除操作方法：remove
                >>> a.remove('oracle')
                >>> a
                set(['a', 'c', 'b', 'e', 'd', 'f', 'j', 'l', 'o', 's', 'r'])

            > set 基本操作
            去重：
                >>> x = set("jihite")
                >>> y = set(['d', 'i', 'm', 'i', 't', 'e'])
                >>> x #把字符串转化为set，去重了
                set(['i', 'h', 'j', 'e', 't'])
                >>> y
                set(['i', 'e', 'm', 'd', 't'])
                >>> x & y #交
                set(['i', 'e', 't'])
                >>> x | y #并
                set(['e', 'd', 'i', 'h', 'j', 'm', 't'])
                >>> x - y #差
                set(['h', 'j'])
                >>> y - x
                set(['m', 'd'])
                >>> x ^ y #对称差：x和y的并集减去交集
                set(['d', 'h', 'j', 'm'])

            > set 内置函数
                >>> x = set('oracle')
                >>> y = set('ora')
                # 长度
                >>> len(x)
                6
                # 是否为子集，return bool
                >>> y.issubset(x)
                True

                >>> z = set('fracle')
                # 并
                >>> x.union(z)
                set(['a', 'c', 'e', 'f', 'l', 'o', 'r'])
                # 交
                >>> x.intersection(z)
                set(['a', 'c', 'r', 'e', 'l'])
                # 差
                >>> x.difference(z)
                set(['o'])
                # 对称差：由 只属于其中一个集合，而不属于另外一个集合的元素组成的 集合
                >>> x.symmetric_difference(z)
                set(['f', 'o'])
                # discard, 如果存在元素，就删除；没有也不返回错误
                >>> y
                set(['a', 1, 'c', 'e', 'l', 'o', 'r'])
                >>> y.discard(2)
                >>> y
                set(['a', 1, 'c', 'e', 'l', 'o', 'r'])
                >>> y.discard(1)
                >>> y
                set(['a', 'c', 'e', 'l', 'o', 'r'])
                # 清除set
                >>> y.clear()
                >>> y
                set([])

                # 随机删除一元素
                >>> x
                set(['a', 'c', 'e', 'l', 'o', 'r'])
                >>> x.pop()
                'a'
                >>> x
                set(['c', 'e', 'l', 'o', 'r'])
                >>> x.pop()

    #-- 多个变量赋值

        当创建一个变量，那么它在内存中保留一些空间
        Python中的变量赋值不需要类型声明

        > Python允许同时为多个变量赋相同值
          a = b = c = 1
          实际上，三个变量被分配到相同的内存空间上。
        > Python允许同时为多个对象赋不同值
          a, b, c = 1, 2, 'frank'


    #-- 数据类型转换
        int(x [,base])  将x转换为一个整数
        long(x [,base] )    将x转换为一个长整数
        float(x)    将x转换到一个浮点数
        complex(real [,imag])   创建一个复数
        str(x)  将对象 x 转换为字符串
        repr(x) 将对象 x 转换为表达式字符串
        eval(str)   用来计算在字符串中的有效Python表达式,并返回一个对象
        tuple(s)    将序列 s 转换为一个元组
        list(s) 将序列 s 转换为一个列表
        set(s)  转换为可变集合
        dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。
        frozenset(s)    转换为不可变集合
        chr(x)  将一个整数转换为一个字符
        unichr(x)   将一个整数转换为Unicode字符
        ord(x)  将一个字符转换为它的整数值
        hex(x)  将一个整数转换为一个十六进制字符串
        oct(x)  将一个整数转换为一个八进制字符串


    #-- zip 拉链
        # 使用zip函数可以把两个列表合并起来，成为一个元组的列表
        L1 = [1,3,5,7]
        L2 = [2,4,6,8]
        #使用zip将两个列表合并
        print zip(L1,L2)
        [(1, 2), (3, 4), (5, 6), (7, 8)]


        >>> for (a,b) in zip(L1,L2):
        ...     print (a,b)
        ...
        (1, 2)
        (3, 4)
        (5, 6)
        (7, 8)
        # 当长度不一的时候，多余的被忽略
        >>> L3 = [2,4,6]
        >>> print zip(L1,L3)
        [(1, 2), (3, 4), (5, 6)]
        # map 当L1和L3长度不一的时候，则不会忽略
        >>> print map(None,L1,L3)
        [(1, 2), (3, 4), (5, 6), (7, None)]
        # 使用zip来造出一个字典
        >>> keys = ['name','age']
        >>> values = ['Chen Zhen ',22]
        >>> zip(keys,values)
        [('name', 'Chen Zhe '), ('age', 22)]
        >>> dict(zip(keys,values))
        {'age': 22, 'name': 'Chen Zhen '}

    #-- what is *args and *kwargs ?
    这两个是python中的可变参数。
    *args表示任何多个无名参数，它是一个tuple；
    **kwargs表示关键字参数，它是一个dict。
    同时使用*args和**kwargs时，必须*args参数列要在**kwargs前
    Eg:
        def foo(*args, **kwargs):
        print 'args = ', args
        print 'kwargs = ', kwargs
        print '---------------------------------------'
        if __name__ == '__main__':
        foo(1,2,3,4)
        foo(a=1,b=2,c=3)
        foo(1,2,3,4, a=1,b=2,c=3)
        foo('a', 1, None, a=1, b='2', c=3)
        输出结果如下：
        args =  (1, 2, 3, 4)
        kwargs =  {}
        ---------------------------------------
        args =  ()
        kwargs =  {'a': 1, 'c': 3, 'b': 2}
        ---------------------------------------
        args =  (1, 2, 3, 4)
        kwargs =  {'a': 1, 'c': 3, 'b': 2}
        ---------------------------------------
        args =  ('a', 1, None)
        kwargs =  {'a': 1, 'c': 3, 'b': '2'}
        ---------------------------------------


#-- 语句汇总
    #-- if语句
        # 单条件
        if 判断条件：
            执行语句……
        else：
            执行语句……

        #多条件
        if 判断条件1:
            执行语句1……
        elif 判断条件2:
            执行语句2……
        elif 判断条件3:
            执行语句3……
        else:
            执行语句4……

    #-- while循环语句
        基本形式：
            while 判断条件：
            执行语句……
        while 语句时还有另外两个重要的命令 continue，break 用来跳过循环，
        continue 用于跳过该次循环，
        break 则是用于退出循环，
        此外"判断条件"还可以是个常值，表示循环必定成立

    #-- for循环语句
        循环控制语句
        #-- for循环语句
            for循环可以遍历<任何序列>的项目，如一个列表或者一个字符串
            > 语法格式
                for <variable> in <sequence>:
                  <statements>
                else:
                  <statements>

                其中
                    break    语句     在语句块执行过程中终止循环，并且跳出整个循环
                    continue 语句     在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
                    pass     语句     pass是空语句，是为了保持程序结构的完整性。

#-- 日期与时间

    Python 提供的模块：

    > datetime模块
    # python中的datetime模块提供了操作日期和时间功能, 该模块提供了五种核心对象：
    datetime(时间日期类型)
    date（日期类型）
    time（时间类型）
    tzinfo（时区类型）
    timedelta（时间差类型）

    > time模块
     # 该模块下的函数都是对同名C函数的直接调用，所以返回的对象都不太pythonic，所以我们一般不用，经常使用的就两个函数：time.sleep(), time.time()
        time 模块包含的函数能实现以下功能：
        1. 获取当前时间
        2. 操作时间和日期
        3. 从字符串读取时间
        4. 格式化时间为字符串

        time 模块中重要的函数:

        a. time() 当前时间 # 返回当前时间的时间戳（1970纪元后经过的浮点秒数）
            >>> import time
            >>> a = time.time()
            >>> print a
            1522574328.36   # 1522574328.36/(60*60*24*365)=48.28
            # 每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。

        b. localtime([]) 将秒数转换为日期元组
            >>> b = time.localtime(a)
            >>> print b
            time.struct_time(tm_year=2018, tm_mon=4, tm_mday=1, tm_hour=17, tm_min=18, tm_sec=48, tm_wday=6, tm_yday=91, tm_isdst=0)

        c. asctime([tuple]) 将时间元组转换为字符串
            >>> c =time.asctime(b)
            >>> print c
            Sun Apr  1 17:18:48 2018

        d. strptime(string[,format]) 将字符串解析为时间元组
            >>> print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            2018-04-01 17:32:44

        e. mktime(tuple) 将时间元组转换为本地时间
            # 将格式字符串转换为时间戳
            a = "Sat Mar 28 22:24:24 2016"
            print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

        f. sleep(secs) 休眠secs秒

        > python中时间日期格式化符号：
            %y 两位数的年份表示（00-99）
            %Y 四位数的年份表示（000-9999）
            %m 月份（01-12）
            %d 月内中的一天（0-31）
            %H 24小时制小时数（0-23）
            %I 12小时制小时数（01-12）
            %M 分钟数（00=59）
            %S 秒（00-59）
            %a 本地简化星期名称
            %A 本地完整星期名称
            %b 本地简化的月份名称
            %B 本地完整的月份名称
            %c 本地相应的日期表示和时间表示
            %j 年内的一天（001-366）
            %p 本地A.M.或P.M.的等价符
            %U 一年中的星期数（00-53）星期天为星期的开始
            %w 星期（0-6），星期天为星期的开始
            %W 一年中的星期数（00-53）星期一为星期的开始
            %x 本地相应的日期表示
            %X 本地相应的时间表示
            %Z 当前时区的名称
            %% %号本身

    > calender模块
            #!/usr/bin/python
            # -*- coding: UTF-8 -*-

            >>> import calendar
            >>> cal = calendar.month(2018,4)
            >>> print cal
                 April 2018
            Mo Tu We Th Fr Sa Su
                               1
             2  3  4  5  6  7  8
             9 10 11 12 13 14 15
            16 17 18 19 20 21 22
            23 24 25 26 27 28 29
            30


#-- 文件操作
    > 输入
    Python提供了两个内置函数从标准输入读入一行文本
    1. raw_input()
    2. input()
     # input()与raw_input()函数基本类似，但input()可以接收Python表达式作为输入，并返回运算结果。
        >>> str = input("请输入：")
        请输入：[x*5 for x in range(2,10,2)]
        >>> print str
        [10, 20, 30, 40]

    > 输出
        print()

    > 操作文件
        如何读写实际的文件？
        Python提供了必要的 函数和方法 进行文件的基本操作
        可用 file对象 实现大部分的文件操作

        > file对象的属性
            1. file.closed # 返回true如果文件已被关闭，否则返回false。
            2. file.mode # 返回被打开文件的访问模式。
            3. file.name # 返回文件的名称。
            4. file. # 如果用print输出后，必须跟一个空格符，则返回false。否则返回true。
                >>> fo = open("tttt.txt","w")
                >>> print fo.name
                tttt.txt
                >>> print fo.closed
                False
                >>> print fo.mode
                w
                >>> print fo.softspace
                0


            open()方法：
                # syntax：
                file object = open(file_name [, access_mode][, buffering])

                    1. file_name：字符串，包含要访问的文件名称
                    2. access_mode：只读，写入，追加 # 默认只读模式
                        r   以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式
                        w   打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
                        a   打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入
                    3. buffering # 如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

                        # http://www.runoob.com/wp-content/uploads/2013/11/2112205-861c05b2bdbc9c28.png

                        模式      r   r+  w   w+  a   a+
                        读        +   +       +       +
                        写        +   +   +   +   +
                        创建              +   +   +   +
                        覆盖              +   +
                        指针在开始 +   +   +   +
                        指针在结尾                  +   +

            close()方法：
                # syntax：
                fileObject.close()
                    # 区分 fileObject.close()方法 与 fileObject.closed()属性
                    >>> fo.close()
                    >>> print fo.closed
                    True

            write()方法： # 可将任何字符串写入一个打开的文件
                # syntax：
                fileObject.write(string)
                    # 打开文件
                    >>> fo = open("tttt.txt","w") # 如果该文件不存在，创建新文件
                    >>> fo.write("come on|\nfrom Oracle to PingCAP")
                    # 关闭刚刚打开的文件
                    >>> fo.close()

            read()方法： # read（）方法从一个打开的文件中读取一个字符串
                # syntax：
                fileObject.read([count])
                # 在这里，被传递的参数是从已打开文件中读取的 字节数。
                    >>> fo = open("tttt.txt","r")
                    >>> fo.read(10)
                    'come on\nfr'
                    >>> fo.close()

            文件定位：
                # 文件内的当前位置
                tell()方法

                # 改变文件当前位置
                seek(offset,[from])
                    1. offset变量表示要移动的字节数
                    2. from变量指定开始移动字节的参考位置
                        (1) from=0 #将 文件开头 作为移动字节的参考位置
                        (2) from=1 #将 当前位置 作为参考位置
                        (3) from=2 #将 文件末尾 作为参考位置
                    # 打开文件 tttt.txt内为 oracle google apple
                    >>> fo = open("tttt.txt","r+")
                    >>> str = fo.read(6)
                    >>> print("reading string is:",str)
                    ('reading string is:', 'oracle')
                    # 查找当前位置
                    >>> position = fo.tell()
                    >>> print("the position now is:",position)
                    ('the position now is:', 6)
                    # 指针重定位到文件开头
                    >>> position = fo.seek(0,0)
                    >>> str = fo.read(13)
                    >>> print("reading string second time is:",str)
                    ('reading string second time is:', 'oracle google')
                    # 关闭文件
                    >>> fo.close()

            重命名文件 # import os 模块
                # syntax：
                os.rename(current_file_name, new_file_name)

                    >>> import os
                    >>> os.rename("tttt.txt","test.txt")

            删除文件 # import os 模块
                # syntax：
                os.remove(file_name)

                    >>> os.remove("test.txt")

            创建、更改和删除目录 # import os 模块

                getcwd() # 获取当前目录
                    >>> os.getcwd()
                    '/Users/frank.shi/Desktop'

                mkdir()方法 # 在当前目录下创建一个新目录new_dir
                    # syntax：
                    os.mkdir("new_dir")

                chdir()方法 # 用chdir()方法来改变当前的目录
                    # syntax：
                    os.chdir("another_dir")
                    # Eg：
                    >>> os.chdir("/Users/frank.shi/Desktop/")
                    >>> os.getcwd()
                    '/Users/frank.shi/Desktop'

                rmdir()方法
                    >>> os.rmdir("newFolder")

                # in addition
                # File 对象方法：http://www.runoob.com/python/file-methods.html
                # OS 对象方法：http://www.runoob.com/python/os-file-methods.html

#-- 模块
    简单地说，模块就是一个保存了Python代码的文件。

    安装第三方模块
        '''
        在Python中，安装第三方模块，是通过setuptools这个工具完成的。
        Python有两个封装了setuptools的包管理工具：easy_install和pip。
        目前官方推荐使用pip。
        '''
        + easy_install
        + pip
            # Eg:
            pip install PIL
            # Python Imaging Library，这是Python下非常强大的处理图像的工具库

    模块文档注释
        任何模块代码的第一个字符串都被视为模块的文档注释
        _author_ # 代码作者

    1. 包
        包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。
        简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。__int__.py用于标识当前文件夹是一个包。

        即，可以通过包来组织模块，为多个模块设置一个顶层包名，只要顶层的包名不与其他冲突，则所有模块都不会与其他冲突。
            # Eg:
            Oracle # 包名
                __init__.py  # 每一个包目录下都会有一个__init__.py 文件,如不存在，Python将此目录识别为普通目录而不是包。__init__.py可为空
                rac.py
                rhp.py
                asm
                    acfs.py # 多层包结构
                    replication.py
                    # replication.py 的模块名为 Oracle.asm.replication

    2. 定位模块
        当导入模块，Python解释器对模块位置的搜索顺序是：
        (1) 当前目录
        (2) shell变量PYTHONPATH 下目录
            > PYTHONPATH变量
            作为环境变量，PYTHONPATH由装在一个列表里的许多目录组成
                在UNIX系统，典型的PYTHONPATH如下：
                set PYTHONPATH=/usr/local/lib/python
        (3) 默认路径 # UNIX下，默认路径一般为/usr/local/lib/python/

            模块搜索路径存储在system模块的sys.path变量中。
                >>> import sys
                >>> sys.path
                ['', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload', '/Library/Python/2.7/site-packages', '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python', '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC']

            如果要添加其他的搜索目录：
            (a) 直接修改sys.path，添加要搜索的目录
                >>> import sys
                >>> sys.path.append('/Users/Download/2018')
                # 此方法是在运行时修改，运行结束后失效。
            (b)设置环境变量PYTHONPATH
                该环境变量的内容会被自动添加到模块搜索路径中。
                设置方式与设置Path环境变量类似。
                注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

    3. 导入模块
        import 语句 # 导包
            想使用Python源文件，只需在另一个源文件里执行import语句.
            当解释器遇到import语句，如果模块在当前的搜索路径就会被导入。
            # syntax：
            import module1, module2,... , moduleN

        from ... import 语句
            Python的from语句让你从模块中导入一个指定的部分到当前命名空间中
                '''
                # 命名空间
                + 变量是拥有匹配对象的名字（标识符）。命名空间是一个包含了变量名称们（键）和它们各自相应的对象们（值）的字典
                + 一个Python表达式可以访问局部命名空间和全局命名空间里的变量。如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量。
                + 每个函数都有自己的命名空间。类的方法的作用域规则和通常函数的一样。
                + Python会智能地猜测一个变量是局部的还是全局的，它假设任何在函数内赋值的变量都是局部的。
                + 如果要给全局变量在一个函数里赋值，必须使用global语句。
                    global VarName的表达式会告诉Python， VarName是一个全局变量，这样Python就不会在局部命名空间里寻找这个变量了。
                '''
            # syntax：
            from modname import name1, name2,... , nameN

            # Eg: 导入模块fib的fibonacci函数
            from fib import fibonacci
            # 这个声明不会把整个fib模块导入到当前的命名空间中，它只会将fib里的fibonacci单个引入到执行这个声明的模块的全局符号表。

        from ... import * 语句 # 这种声明不该被过多地使用
            把一个模块的所有内容全都导入到当前的命名空间
            # syntax：
            from modname import *

    4. 使用模块
        # Eg:

            #!/usr/bin/env python
            # -*- coding: utf-8 -*-

            ' a test module '

            __author__ = 'Michael Liao'
            # 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

            import sys

            def test():
                args = sys.argv
                if len(args)==1:
                    print 'Hello, world!'
                elif len(args)==2:
                    print 'Hello, %s!' % args[1]
                else:
                    print 'Too many arguments!'

            if __name__=='__main__':
                test()

    5. 常用函数
            dir()函数
            # 返回值为 字符串列表(排序后的)，容纳了import的模块中所有定义的 模块，函数和变量
                # Eg:
                >>> import math
                >>> con = dir(math)
                >>> print con
                ['__doc__', '__file__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
                # 在这里，特殊字符串变量__name__指向模块的名字，__file__指向该模块的导入文件名

            globals() and locals()函数
                如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
                如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。

            reload()函数
                当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次,
                如果想重新执行模块里顶层部分的代码，可以用 reload() 函数。
                该函数会重新导入之前导入过的模块。
                # Eg:
                reload(math)

    6. 新特性 __future__
        '''
        Python的每个新版本都会增加一些新的功能，或者对原来的功能作一些改动。
        有些改动是不兼容旧版本的，也就是在当前版本运行正常的代码，到下一个版本运行就可能不正常了。
        从Python 2.7到Python 3.x就有不兼容的一些改动，比如2.x里的字符串用'xxx'表示str，Unicode字符串用u'xxx'表示unicode，而在3.x中，所有字符串都被视为unicode，因此，写u'xxx'和'xxx'是完全一致的，而在2.x中以'xxx'表示的str就必须写成b'xxx'，以此表示“二进制字符串”。+
        要直接把代码升级到3.x是比较冒进的，因为有大量的改动需要测试。相反，可以在2.7版本中先在一部分代码中测试一些3.x的特性，如果没有问题，再移植到3.x不迟。

        Python提供了__future__模块，把下一个新版本的特性导入到当前版本，
        于是我们就可以在当前版本中测试一些新版本的特性。
        '''
            # Eg:
            # 在Python 2.x中，对于除法有两种情况：
            # 如果是整数相除，结果仍是整数，余数会被扔掉，这种除法叫“地板除”
            # 要做精确除法，必须把其中一个数变成浮点数
            # 而在Python 3.x中，所有的除法都是精确除法，地板除用//表示
            from __future__ import division

            print '10 / 3 =', 10 / 3
            print '10.0 / 3 =', 10.0 / 3
            print '10 // 3 =', 10 // 3
            # 结果：
            10 / 3 = 3.33333333333
            10.0 / 3 = 3.33333333333
            10 // 3 = 3

    7. 常用内建模块
        + types
            StringType
            UnicodeType
            ListType
            MethodType
            TypeType
        + sys
            sys.path            # 搜索路径
            sys.path.append()   # 添加搜索路径
            sys.argv            # 命令行参数
        + math
            sin()
            cos()
        + random
            choice()    # 获取随机字符
            randint()   # 获取随机整数
        + string
            letters     # 字符

    8. 常用第三方模块
        + MySQL-python                # MySQL的驱动
        + numpy                       # 用于科学计算的NumPy库
        +Jinja2                       # 用于生成文本的模板工具

        + 图片处理
            + PIL：Python Imaging Library  # 图片处理
                + Image
                    open()  # 打开图片
                    save()  # 保存图片
                    thumbnail() # 缩略图
                    format  # 格式：png，jpg等
                    filter()    # 过滤图片
                    size    # 尺寸
                    mode
                    new()   # 新建图片

        + 文本处理
            + Pythongoose
                '''
                基于NLTK和BeautifulSoup，
                目标是给定任意资讯文章或者任意文章类的网页，
                不仅提取出文章的主体，同时提取出所有元信息以及图片等信息，
                支持中文网页（用到了结巴分词）
                '''
            + NLTK   # 文本处理

        + 网络爬虫
            + scrapy
            + BeautifulSoup # HTML解析
            + requests

        + Web框架
            + Django
            + Flask # 轻量
            + Tornado # 异步高效

        + 数据库
            + MySQL
            + mongodb


#-- 函数
    函数能提高应用的模块性，和代码的重复利用率。
        # syntax：
        def functionname( parameters ):
            "函数_文档字符串"
            function_suite
            return [expression]

    > 函数调用
        函数定义完之后，可以通过另一个函数调用执行，也可以直接使用此定义的Python提示符执行
        #!/usr/bin/env python3
        # _*_ coding: utf-8 _*_
        # 可写函数说明

        def changeme( mylist ):
            "修改传入的列表"
            mylist.append([1,2,3,4])
            print ("the new list is: ", mylist)
            return

        # 调用changeme函数
        mylist = [10,20,30]
        changeme( mylist )

    > 匿名函数 # python 使用 lambda 来创建匿名函数
        # syntax:
        lambda arg1, arg2,** argn:expression

        + lambda只是一个表达式
        + lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数
        # Eg:
            >>> sum = lambda arg1, arg2: arg1 + arg2;
            >>> print ("the num is:", sum(1,2))
            ('the num is:', 3)

    > return 语句
        return or return * 退出函数，并向调用方返回。
        不带参数值的 return 语句返回 None

    > 变量作用域
        + 全局变量
        # 定义在函数内部的变量拥有一个局部作用域
        # 局部变量只能在其被声明的函数内部访问
        + 局部变量
        # 定义在函数外的拥有全局作用域
        # 全局变量可以在整个程序范围内访问

    > 递归函数
        在函数内部，可调用其他函数。如在函数内部调用自身，则为递归。

        使用递归函数需要注意防止栈溢出。
        # 在计算机中，函数调用是通过栈（stack）这种数据结构实现的。
        每当进入一个函数调用，栈就会加一层栈帧，
        每当函数返回，栈就会减一层栈帧。
        由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。

            >>> def fact(n):
            ...     return fact_iter(n, 1)
            ...
            >>> def fact_iter(num, product):
            ...     if num == 1:
            ...         return product
            ...     return fact_iter(num - 1, num * product)
            ...
            >>> print (fact(500))
            1220136825991110068701238785423046926253574342803192842192413588385845373153881997605496447502203281863013616477148203584163378722078177200480785205159329285477907571939330603772960859086270429174547882424912726344305670173270769461062802310452644218878789465754777149863494367781037644274033827365397471386477878495438489595537537990423241061271326984327745715546309977202781014561081188373709531016356324432987029563896628911658974769572087926928871281780070265174507768410719624390394322536422605234945850129918571501248706961568141625359056693423813008856249246891564126775654481886506593847951775360894005745238940335798476363944905313062323749066445048824665075946735862074637925184200459369692981022263971952597190945217823331756934581508552332820762820023402626907898342451712006207714640979456116127629145951237229913340169552363850942885592018727433795173014586357570828355780158735432768888680120399882384702151467605445407663535984174430480128938313896881639487469658817504506926365338175055478128640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

    > 参数传递
        + 位置参数 # Python中在调用函数时，需要给定和形参相同个数的实参并按顺序一一对应

        + 默认参数 # 必选参数在前，默认参数在后；默认参数必须指向不变对象

        + 可变参数
            *args是可变参数，args接收的是一个tuple

            # Eg：以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……(平方)
                def calc1(*numbers):
                    sum = 0
                    for n in numbers:
                        sum = sum + n * n
                    return sum

                print (calc1(1,2,3,4))

        + 关键字参数
            **kw是关键字参数，kw接收的是一个dict



            # Eg:
            def person(name, age, **kw):
            print('name:', name, 'age:', age, 'other:', kw)

            >>> person('Adam', 45, gender='M', job='Engineer')
            name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}


#-- yield 关键字

    > 迭代
        任何可用 for ... in ... 处理的都是迭代对象--- 列表，字符串，文件

            >>> mylist = [x*x for x in range(3)]
            >>> for i in mylist:
            ...    print(i)
            0
            1
            4
            # 使用列表迭代

    > 生成器 # 生成器是迭代器
        iterate over them once：# 只能遍历一次
        because 生成器并没有将所有值放入内存中，而是实时生成这些值

            >>> mygenerator = (x*x for x in range(3))
            >>> for i in mygenerator:
            ...    print(i)
            0
            1
            4
            # 和上例区别：使用 () 代替了 []
            # 生成器迭代的关键是它有一个next()方法，通过重复调用next()，直到捕获异常
            # 带有yield的函数不再是一个普通的函数，而是一个生成器generator

                @简要理解
                yield 就是 return 一个值，并且记住返回的位置，下一次迭代就从这个位置后(下一行)开始


    > yield
        yield 是一个类似 return 的关键字，迭代一次遇到 yield 时就返回 yield 后面的值。
        带有 yield 的函数不再是一个普通函数，而是一个生成器generator，可用于迭代

            yield 的用法起源于对一般 function 中 return 的扩展。在一个 function 中，必须有一个返回值列于 return 之后，可以返回数字也可以返回空值，但是必须要有一个返回值，标志着这个 function 的结束。一旦它结束，那么这个 function 中产生的一切变量将被统统抛弃，有什么可以使一个 function 暂停下来，并且返回当前所在地方的值，当接收到继续的命令时可以继续前进呢？换个说法，就是 return 返回一个值，并且记住这个返回的位置。这个操作有点儿像

            for x in range():
                pass
            这个循环语句中 range() 这个函数干的事情，它给出一个数，当循环完一次以后再在前一个数的基础上拿出另外一个数。但是这里的函数其实是自动生成一个 list 然后从这个 list 第一个开始往后一个一个给出，那么这种方法的劣势显而易见——会有生成一个 list 。也就是说不管你的 for 循环用几回，它都会生成这个 list（比如你有一个庞大的数据库，那么光是生成一个表单就需要很长时间，然而也许你要用的东西就在前几个，那么你建起这个检索目录远远超过你实际所需要的）。这时就是 xrange() 登场的时候了，它就是一个不需要建立 list 却一样完成任务的好命令。那么 xrange() 是什么呢？

            xrange() 其实是一个 generator 生成器，不同于一般的 function，里面就包含着yield。generator 人如其名，是一个生成器，生成什么呢？不妨把它看作生成一组你需要的序列的函数，通常情况下我们只需要自然数这种简单的序列，但是如果让你生成一组斐波那契数列呢？这组数列是无穷的，你想沿着这个数列一直算下去，直到算到你满意的一个数，但是如果你也不知道这个数在哪里，那么你就不能提前给出一个这个数列，因为你不知道在哪里会停下来。面对这个问题时，最好的解决方法就是记住当前的数，记住当前的地址，查看一个这个数符合不符合要求，如果不符合要求，那么继续从这个数／地址开始计算下一个斐波那契数字。这就是 yield 要干的事情了。（其实这么做的好处还有一个就是减少斐波那契数列的运算量，这个数列因为是自循环数列，所以如果按照循环算法的话需要很大的运算量，但是如果是采用动态纪录法的话，那么就会非常简单。这属于优化算法范畴，暂且按下不表。）下面就是斐波那契数列用 yield 的实现法：

            # 斐波那契数列：每一个数都等于前两个数之和
            def fib(to=10):
                curr = 0
                next = 1
                count = 0
                while count < to:
                    yield curr
                    curr = next
                    next = curr + next
                    count += 1

            # 一个用法例子：每一个斐波那契数列的数加1
            if __name__ == '__main__':
                for x in fib(20):
                    print(x+1)


            注意：yield 一旦被采用，那么def后面的代码会立马被认作是一个 generator 而不是一个 function，因为生成的是一个 generator，所以可以被用在 for in 这个循环语句中。而 generator 和 function 从本质上是不同的，两者的区别就涉及到了next()和send()这两个函数的用法。

            如果把这个python文件命名为fi.py，并运行之。那么可以瞬间得到结果:

            1
            2
            3
            5
            9
            17
            33
            65
            129
            257
            513
            1025
            2049
            4097
            8193
            16385
            32769
            65537
            131073
            262145
            用这个方法可以自己研究很多有趣的数学问题，比如找出2万以内的质数之和，找出大于10的0次方，一次方，...，n次方的最小质数。你不需要建立一个很大的索引库，只需要一个一个数字算下去就好。



            Python 是非常灵活的语言，其中 yield 关键字是普遍容易困惑的概念。
            此篇将介绍 yield 关键字，及其相关的概念。




            迭代、可迭代、迭代器
            迭代（iteration）与可迭代（iterable）

            迭代是一种操作；可迭代是对象的一种特性。

            很多数据都是「容器」；它们包含了很多其他类型的元素。实际使用容器时，我们常常需要逐个获取其中的元素。逐个获取元素的过程，就是「迭代」。

            # iteration
            a_list = [1, 2, 3]
            for i in a_list:
                print(i)

            如果我们可以从一个对象中，逐个地获取元素，那么我们就说这个对象是「可迭代的」。

            Python 中的顺序类型，都是可迭代的（list, tuple, string）。其余包括 dict, set, file 也是可迭代的。对于用户自己实现的类型，如果提供了 __iter__() 或者 __getitem__() 方法，那么该类的对象也是可迭代的。

            迭代器（iterator）

            迭代器是一种对象。

            迭代器抽象的是一个「数据流」，是只允许迭代一次的对象。对迭代器不断调用 next() 方法，则可以依次获取下一个元素；当迭代器中没有元素时，调用 next() 方法会抛出 StopIteration 异常。迭代器的 __iter__() 方法返回迭代器自身；因此迭代器也是可迭代的。

            迭代器协议（iterator protocol）

            迭代器协议指的是容器类需要包含一个特殊方法。

            如果一个容器类提供了 __iter__() 方法，并且该方法能返回一个能够逐个访问容器内所有元素的迭代器，则我们说该容器类实现了迭代器协议。

            Python 中的迭代器协议和 Python 中的 for 循环是紧密相连的。

            # iterator protocol and for loop
            for x in something:
                print(x)

            Python 处理 for 循环时，首先会调用内建函数 iter(something)，它实际上会调用 something.__iter__()，返回 something 对应的迭代器。而后，for 循环会调用内建函数 next()，作用在迭代器上，获取迭代器的下一个元素，并赋值给 x。此后，Python 才开始执行循环体。

            生成器、yield 表达式
            生成器函数（generator function）和生成器（generator）

            生成器函数是一种特殊的函数；生成器则是特殊的迭代器。

            如果一个函数包含 yield 表达式，那么它是一个生成器函数；调用它会返回一个特殊的迭代器，称为生成器。

            def func():
                return 1

            def gen():
                yield 1

            print(type(func))   # <class 'function'>
            print(type(gen))    # <class 'function'>

            print(type(func())) # <class 'int'>
            print(type(gen()))  # <class 'generator'>

            如上，生成器 gen 看起来和普通的函数没有太大区别。仅只是将 return 换成了 yield。用 type() 函数打印二者的类型也能发现，func 和 gen 都是函数。然而，二者的返回值的类型就不同了。func() 是一个 int 类型的对象；而 gen() 则是一个迭代器对象。

            yield 表达式

            如前所述，如果一个函数定义中包含 yield 表达式，那么该函数是一个生成器函数（而非普通函数）。实际上，yield 仅能用于定义生成器函数。

            与普通函数不同，生成器函数被调用后，其函数体内的代码并不会立即执行，而是返回一个生成器（generator-iterator）。当返回的生成器调用成员方法时，相应的生成器函数中的代码才会执行。

            def square():
                for x in range(4):
                    yield x ** 2
            square_gen = square()
            for x in square_gen:
                print(x)

            前面说到，for 循环会调用 iter() 函数，获取一个生成器；而后调用 next() 函数，将生成器中的下一个值赋值给 x；再执行循环体。因此，上述 for 循环基本等价于：

            genitor = square_gen.__iter__()
            while True:
                x = geniter.next() # Python 3 是 __next__()
                print(x)

            注意到，square 是一个生成器函数；作为它的返回值，square_gen 已经是一个迭代器；迭代器的 __iter__() 返回它自己。因此 geniter 对应的生成器函数，即是 square。

            每次执行到 x = geniter.next() 时，square 函数会从上一次暂停的位置开始，一直执行到下一个 yield 表达式，将 yield 关键字后的表达式列表返回给调用者，并再次暂停。注意，每次从暂停恢复时，生成器函数的内部变量、指令指针、内部求值栈等内容和暂停时完全一致。

            生成器的方法

            生成器有一些方法。调用这些方法可以控制对应的生成器函数；不过，若是生成器函数已在执行过程中，调用这些方法则会抛出 ValueError 异常。

            generator.next()：从上一次在 yield 表达式暂停的状态恢复，继续执行到下一次遇见 yield 表达式。当该方法被调用时，当前 yield 表达式的值为 None，下一个 yield 表达式中的表达式列表会被返回给该方法的调用者。若没有遇到 yield 表达式，生成器函数就已经退出，那么该方法会抛出 StopIterator 异常。
            generator.send(value)：和 generator.next() 类似，差别仅在与它会将当前 yield 表达式的值设置为 value。
            generator.throw(type[, value[, traceback]])：向生成器函数抛出一个类型为 type 值为 value 调用栈为 traceback 的异常，而后让生成器函数继续执行到下一个 yield 表达式。其余行为与 generator.next() 类似。
            generator.close()：告诉生成器函数，当前生成器作废不再使用。
            举例和说明

            如果你看不懂生成器函数

            如果你还是不太能理解生成器函数，那么大致上你可以这样去理解。

            在函数开始处，加入 result = list()；
            将每个 yield 表达式 yield expr 替换为 result.append(expr)；
            在函数末尾处，加入 return result。
            关于「下一个」yield 表达式

            介绍「生成器的方法」时，我们说当调用 generator.next() 时，生成器函数会从当前位置开始执行到下一个 yield 表达式。这里的「下一个」指的是执行逻辑的下一个。因此

            def f123():
                yield 1
                yield 2
                yield 3

            for item in f123(): # 1, 2, and 3, will be printed
                print(item)

            def f13():
                yield 1
                while False:
                    yield 2
                yield 3

            for item in f13(): # 1 and 3, will be printed
                print(item)

            使用 send() 方法与生成器函数通信

            def func():
                x = 1
                while True:
                    y = (yield x)
                    x += y

            geniter = func()
            geniter.next()  # 1
            geniter.send(3) # 4
            geniter.send(10)# 14

            此处，生成器函数 func 用 yield 表达式，将处理好的 x 发送给生成器的调用者；与此同时，生成器的调用者通过 send 函数，将外部信息作为生成器函数内部的 yield 表达式的值，保存在 y 当中，并参与后续的处理。

            这一特性是使用 yield 在 Python 中使用协程的基础。

            yield 的好处
            Python 的老用户应该会熟悉 Python 2 中的一个特性：内建函数 range 和 xrange。其中，range 函数返回的是一个列表，而 xrange 返回的是一个迭代器。

            在 Python 3 中，range 相当于 Python 2 中的 xrange；而 Python 2 中的 range 可以用 list(range()) 来实现。

            Python 之所以要提供这样的解决方案，是因为在很多时候，我们只是需要逐个顺序访问容器内的元素。大多数时候，我们不需要「一口气获取容器内所有的元素」。比方说，顺序访问容器内的前 5 个元素，可以有两种做法：

            获取容器内的所有元素，然后取出前 5 个；
            从头开始，逐个迭代容器内的元素，迭代 5 个元素之后停止。
            显而易见，如果容器内的元素数量非常多（比如有 10 ** 8 个），或者容器内的元素体积非常大，那么后一种方案能节省巨大的时间、空间开销。

            现在假设，我们有一个函数，其产出（返回值）是一个列表。而若我们知道，调用者对该函数的返回值，只有逐个迭代这一种方式。那么，如果函数生产列表中的每一个元素都需要耗费非常多的时间，或者生成所有元素需要等待很长时间，则使用 yield 把函数变成一个生成器函数，每次只产生一个元素，就能节省很多开销了。



#-- 面向对象

    OOP(object Oriented Programming) 是一种从自然界演绎出的程序设计思想。
        在自然界中，类和实例的概念是很自然的。类是一种抽象的概念，实例是类的具体对象化。

        面向过程的程序设计:
            把计算机程序视为一系列的命令集合，即一组函数的顺序执行。
            为了简化程序设计，面向过程把函数继续切分为子函数，
            即把大块函数通过切割成小块函数来降低系统的复杂度。
        面向对象的程序设计:
            把计算机程序视为一组对象的集合，
            而每个对象都可以接收其他对象发过来的消息，并处理这些消息，
            计算机程序的执行就是一系列消息在各个对象之间传递。


    类与实例：
        类: 用来描述具有相同的属性和方法的对象的集合
            自定义数据类型对象，即成为面向对象中的类（Class）的概念

            class Student(object):
                pass

                class后面紧接着是类名，即Student，类名通常是大写开头的单词，
                紧接着是(object)，表示该类是从哪个类继承下来的，
                通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

            1. Python内置 类属性：
                __dict__    # 类的属性（包含一个字典，由类的数据属性组成）
                __doc__     # 类的文档字符串
                __name__    # 类名
                __module__  # 类定义所在的模块
                __bases__   # 类的所有父类构成元素（包含了几个由所有父类组成的元组）

            2. 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

                垃圾回收机制：
                    在Python内部记录着所有使用中的对象各有多少引用。一个内部跟踪变量，称为一个引用计数器。当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 也就是说， 这个对象的引用计数变为0 时，它被垃圾回收。但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收。

                默认任何在函数内赋值的变量都是局部的。因此，如果要给全局变量在一个函数里赋值，必须使用global语句

        + 方法：方法就是与实例绑定的函数 # 和普通函数不同，方法可以直接访问实例的数据

            通用方法：
            __init__()  构造方法
                由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

                class Student(object):

                    def __init__(self, name, score):
                        self.name = name
                        self.score = score

                注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
                有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
                >>> bart = Student('Bart Simpson', 59)
                >>> bart.name
                'Bart Simpson'
                >>> bart.score
                59
                和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数和关键字参数。

            __del__( self ) 析构函数
            __repr__( self )    转化为供解释器读取的形式
            __str__( self ) 用于将值转化为适于人阅读的形式，Java中的toString()
            __cmp__ ( self, x ) 对象比较

        + 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。

    Features of OOP:

        1. 数据封装
            在上面的Eg. 定义的Student类中，每个实例就拥有各自的name和score这些数据
            可通过函数来访问这些数据
            class Student()
                ...
            def print_score(self):
            print '%s: %s' % (self.name, self.score)
                ...

             >>>print_score(bart)
             >>>Bart Simpson: 59

            '''
            方法：
            既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，
            可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。
            这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法。
            '''
            封装的另一个好处是可以给Student类增加新的方法
            def get_grade(self):
                if self.score >= 90:
                    return 'A'
                elif self.score >= 60:
                    return 'B'
                else:
                    return 'C'

        2. 访问限制（封闭） # 确保了外部代码不能随意修改对象内部的状态，增强代码的健壮性
            如果要让内部属性不被外部访问，可以把属性的名称前加上*两个*下划线__
            在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
            class Student(object):

                def __init__(self, name, score):
                    self.__name = name
                    self.__score = score

                def print_score(self):
                    print '%s: %s' % (self.__name, self.__score)

                >>> bart = Student('Bart Simpson', 98)
                >>> bart.__name
                Traceback (most recent call last):
                  File "<stdin>", line 1, in <module>
                AttributeError: 'Student' object has no attribute '__name'

            '''
            需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
            特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
            '''

        3. 继承 # 类型和子类型关系
            定义一个class的时候，可以从某个现有的class继承，
            新的class称为子类（Subclass），
            被继承的class称为基类、父类或超类（Base class、Super class）
            # Eg:
                class Animal(object):
                    def run(self):
                        print 'Animal is running...'

                class Dog(Animal):
                    def run(self):
                        print 'Dog is running...'
                    def eat(self):
                        print 'Eating meat...'

                class Cat(Animal):
                    def run(self):
                        print 'Cat is running...'

                >>>dog = Dog()
                >>>dog.run()
                >>>Dog is running...

                >>>cat = Cat()
                >>>cat.run()
                >>>Cat is running...

            当子类和父类都存在相同的run()方法时，子类的run()覆盖了父类的run()

        4. 多态
            概念：指对不同类型的变量进行相同的操作，它会根据对象(或类)类型的不同而表现出不同的行为。
            当我们定义一个class的时候，我们实际上就定义了一种数据类型

                a = list() # a是list类型
                b = Animal() # b是Animal类型
                c = Dog() # c是Dog类型
            # 实质：
                在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类

            多态真正的威力：调用方只管调用，不管细节，
            # 而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。
            这就是著名的“开闭”原则：
                对扩展开放：允许新增Animal子类；
                对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

        5. 获取对象信息
            (1) 判断对象类型，使用type()函数。
                Python把每种type类型都定义好了常量，放在types模块里，使用之前，需要先导入：
                    >>> import types
                    >>> type('abc')==types.StringType
                    True
                    >>> type(u'abc')==types.UnicodeType
                    True
                    >>> type([])==types.ListType
                    True
                    >>> type(str)==types.TypeType
                    True

                        # 所有类型本身的类型就是TypeType
                        >>> type(int)==type(str)==types.TypeType
                        True

            (2) isinstance()
                如果继承关系是：
                object -> Animal -> Dog -> Husky
                    先创建3种类型的对象：
                    >>> a = Animal()
                    >>> d = Dog()
                    >>> h = Husky()

                    >>> isinstance(h, Husky)
                    True
                    >>> isinstance(h, Dog)
                    True
                    >>> isinstance(h, Animal)
                    True
                    # isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。

                    Ps:能用type()判断的基本类型也可以用isinstance()判断：
                    >>> isinstance('a', str)
                    True
                    >>> isinstance(u'a', unicode)
                    True
                    >>> isinstance('a', unicode)
                    False

            (3) dir()
                获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
                >>> dir('abc')
                ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

                配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
                    >>> class MyObject(object):
                    ...     def __init__(self):
                    ...         self.x = 9
                    ...     def power(self):
                    ...         return self.x * self.x
                    ...
                    >>> obj = MyObject()

                    >>> hasattr(obj, 'x') # 有属性'x'吗？
                    True
                    >>> hasattr(obj, 'y') # 有属性'y'吗？
                    False
                    >>> setattr(obj, 'y', 19) # 设置一个属性'y'
                    >>> hasattr(obj, 'y') # 有属性'y'吗？
                    True
                    >>> getattr(obj, 'y') # 获取属性'y'
                    19
                    >>> obj.y # 获取属性'y'
                    19

                如果试图获取不存在的属性，会抛出AttributeError的错误：
                    >>> getattr(obj, 'z') # 获取属性'z'
                    Traceback (most recent call last):
                      File "<stdin>", line 1, in <module>
                    AttributeError: 'MyObject' object has no attribute 'z'

                可以传入一个default参数，如果属性不存在，就返回默认值：

                    >>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
                    404
                    也可以获得对象的方法：

                    >>> hasattr(obj, 'power') # 有属性'power'吗？
                    True
                    >>> getattr(obj, 'power') # 获取属性'power'
                    <bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
                    >>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
                    >>> fn # fn指向obj.power
                    <bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
                    >>> fn() # 调用fn()与调用obj.power()是一样的
                    81

#-- 面向对象高级编程
        数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能。

        1. 使用__slots__
            当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
                >>> class Student(object):
                ...     pass
                ...
                >>> s = Student()
                >>> s.name = 'Michael' # 动态给实例绑定一个属性
                >>> print s.name
                Michael
                >>> def set_age(self, age):  # 定义一个函数作为实例方法
                ...     self.age = age
                ...
                >>> from types import MethodType
                >>> s.set_age = MethodType(set_age, s, Student)# 给实例绑定一个方法
                >>> s.set_age(25) # 调用实例方法
                >>> s.age # 测试结果
                25

            但是，给一个实例绑定的方法，对另一个实例是不起作用的：

                >>> s2 = Student() # 创建新的实例
                >>> s2.set_age(25) # 尝试调用方法
                Traceback (most recent call last):
                  File "<stdin>", line 1, in <module>
                AttributeError: 'Student' object has no attribute 'set_age'

            为了给所有实例都绑定方法，可以给class绑定方法：

                >>> def set_score(self, score):
                ...     self.score = score
                ...
                >>> Student.set_score = MethodType(set_score, None, Student)

            但是，如果我们想要限制class的属性怎么办？比如，只允许对Student实例添加name和age属性。

            为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性：
                >>> class Student(object):
                ...     __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
                ...

            使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的

        2. 使用 @property # 装饰器
            #@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

            在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：

                s = Student()
                s.score = 9999

            这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：

                class Student(object):
                    def get_score(self):
                        return self._score
                    def set_score(self, value):
                        if not isinstance(value, int):
                            raise ValueError('score must be an integer!')
                        if value < 0 or value > 100:
                            raise ValueError('score must between 0 ~ 100!')
                        self._score = value

            现在，对任意的Student实例进行操作，就不能随心所欲地设置score了：

                >>> s = Student()
                >>> s.set_score(60) # ok!
                >>> s.get_score()
                60
                >>> s.set_score(9999)
                Traceback (most recent call last):
                  ...
                ValueError: score must between 0 ~ 100!

            有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
            Python内置的 @property 装饰器就是负责把一个方法变成属性调用的：

                class Student(object):

                    @property
                    def score(self):
                        return self._score

                    @score.setter
                    def score(self, value):
                        if not isinstance(value, int):
                            raise ValueError('score must be an integer!')
                        if value < 0 or value > 100:
                            raise ValueError('score must between 0 ~ 100!')
                        self._score = value

            @property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：

                >>> s = Student()
                >>> s.score = 60 # OK，实际转化为s.set_score(60)
                >>> s.score # OK，实际转化为s.get_score()
                60
                >>> s.score = 9999
                Traceback (most recent call last):
                  ...
                ValueError: score must between 0 ~ 100!

        3. 多重继承 # 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
            # 问题背景：
            # 4个动物，哺乳类与非哺乳类，会飞的和不会飞的

                class Animal(object):
                    pass

                # 大类:
                class Mammal(Animal):
                    pass

                class Bird(Animal):
                    pass

                # 多重大类
                class Runnable(object):
                    def run(self):
                        print('Running...')

                class Flyable(object):
                    def fly(self):
                        print('Flying...')
                # 多重继承
                class Dog(Mammal, Runnable):
                    pass

                class Bat(Mammal, Flyable):
                    pass

            Mixin：# Mixin就是一种常见的设计
                在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为Mixin。


            为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixin和FlyableMixin。类似的，你还可以定义出肉食动物CarnivorousMixin和植食动物HerbivoresMixin，让某个动物同时拥有好几个Mixin：

                class Dog(Mammal, RunnableMixin, CarnivorousMixin):
                    pass

            Mixin的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个Mixin的功能，而不是设计多层次的复杂的继承关系。

            Python自带的很多库也使用了Mixin。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixin和ThreadingMixin提供。通过组合，我们就可以创造出合适的服务来。

            比如，编写一个多进程模式的TCP服务，定义如下：

                class MyTCPServer(TCPServer, ForkingMixin):
                    pass

            编写一个多线程模式的UDP服务，定义如下：

                class MyUDPServer(UDPServer, ThreadingMixin):
                    pass

            如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixin：

                class MyTCPServer(TCPServer, CoroutineMixin):
                    pass

            这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。

        4. 定制类








