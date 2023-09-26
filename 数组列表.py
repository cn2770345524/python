### Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
# 注意：list里面的元素的数据类型也可以不同
classmates=['张三','李四','王五']

# 直接打印
print(classmates)

# 求长度
a=len(classmates)
print(a)

# 通过索引访问
print(classmates[0])
print(classmates[1])
print(classmates[2])

# 通过索引倒序访问
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

# 追加元素
classmates.append('李六')

# 插入到指定位置
classmates.insert(1,'钱七')

print(classmates)

# 删除最后一个元素
classmates.pop()

# 删除指定位置的元素
classmates.pop(1)

# 数组内的元素可以不同类型
arr=['a',1,1324.5,['a','b','c']]
al = len(arr[3])
print(al)

# 二维数组
array=[['a','b','c'],['d','e','f']]
print(array[0][0])
print(array[1][1])


### 指向不变的数组tuple
# 也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素（引入指针不变）
array2=(1,2,3,4)



##### 高级特性
### 特性1:切片 
L=['A','B','C','D','E','F','H','J','K','G']
# 取数组L中从索引1到3(不包括3)的元素
print(L[1:3])
# 取数组L中从索引0到4(不包括4)的元素
print(L[0:4])
print(L[:4])

# 取后面的5个数
print(L[-5:])
# 取前面5个数 在五个数中每隔2个数取一个
print(L[:5:2])
# 取后面5个数 在五个数中每隔2个数取一个
print(L[-5::2])
# 原样复制一个数组
print(L[:])


### python支持函数式编程，可以将函数赋给变量，变量可去执行，去传递给函数
from functools import reduce


f=abs

def fun(a,b,f):
    return f(a)+f(b)

print(fun(-5,6,f))

### map/reduce
# Python内建了map()和reduce()函数。
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
L=[1,2,3,4,5,6]
def fun(a):
    return a*a
L=list(map(fun,L))
print(L)

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def fun(a,b):
    return a*10+b
L=[1,2,4,5]
print(reduce(fun,L))

## 实例：将字符串数字转为int类型数字
a='123456'
def toInt(s):
    al_dict={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return al_dict[s]

def fn(x,y):
    return x*10+y
res=reduce(fn,map(toInt,a))
print(res)


### filter()过滤函数
L=[1,2,3,4,5,6,7,8,9,10]
def fn(e):
    return e%2==0
print(list(filter(fn,L)))


### sorted()排序函数 默认从小到大排序
L=[232,434,6,767,87,231,677,3,57,20]
print(sorted(L))
L=[-5,-88,99,10,67]
# 按绝对值排序
print(sorted(L,key=abs))
# [-5, 10, 67, -88, 99]
## 按绝对值排序，反转顺序
print(sorted(L,key=abs,reverse=True))
# [99, -88, 67, 10, -5]