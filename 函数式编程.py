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

### 返回函数
def lazy_sum():
    def sum(*args):
        return reduce(lambda x,y:x+y,args)
    return sum
L=[1,2,3,4,5]
fn_sum=lazy_sum()
print(fn_sum(L))

### 匿名函数 lambda
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
f=lambda x:x*x