### 数学函数
max()  # 求最大值
abs()  # 求绝对值

### 进制转换
hex()  # 将所给数值转换为16进制的字符串

### 判断实例
isinstance()

### 获取实例类型
type()
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types

# sorted filter map reduce针对数组list tuple的操作
sorted()

import functools

filter()
map()
functools.reduce()


def fn():
    pass


# 获取实例对象的类型
print(type(fn) == types.FunctionType)
# True

print(type(abs) == types.BuiltinFunctionType)
# True

print(type(lambda x: x) == types.LambdaType)
# True

print(type((x for x in range(100))) == types.GeneratorType)
# True


### dir()函数获取一个对象所有属性和方法 返回一个字符串List
dir()
### hasattr()函数可以判断一个对象是否有对应属性或方法
hasattr()
### setattr()函数可以设置个实例属性的值
setattr()
### getattr()函数可以获取一个实例属性的值或方法 如果试图获取不存在的属性，会抛出AttributeError的错误：
getattr()


# __str__()函数决定打印变量打印出来的是类信息地址，还是自定义的信息类似java中toString的效果，
# __repr__()函数决定python在脚本模式，调试式打印的变量信息是地址还是自定义的信息，一般在设置__str__函数也设置这个函数
# __repr__=__str__

# __iter__()如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


f = Fib()
i = 0
for g in f:
    if i > 10:
        break
    print(g)


# __getitem__():__iter__()函数可以使实例可以被迭代，但是并不代表它返回的就是一个list，如果需要像list那样可以使用下标(index)或者切片(slice)就需要实现__getitem__()函数了
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引 支持索引取值
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片 支持切片取值
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


# __setitem__():与__getitem__()对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。


# __getattr__()函数：当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样就给了一个机会让我们搞事情
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    # 当前调用student.score时，发现student对象上没有这个属性，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值
    def __getattr__(self, attr):
        if attr == 'score':
            return 99


# __call__()函数：__call__函数用来支持对象本身当做函数调用
class P(object):

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('this is P class called')


p = P()
p()  # 将一个对象当做函数来调用

## callable()函数：判断一个对象实例是否可被调用__call__()函数可以通过callable()函数来判断
callable(Student())
True
callable(max)
True
callable([1, 2, 3])
False
callable(None)
False
callable('str')
False
