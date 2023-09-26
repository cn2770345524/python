### 调用函数
# python内置常用的函数
# http://docs.python.org/3/library/functions.html#abs
import math


a=abs(10)
b=abs(-20)
print(a,b)

c=max(1,2,3,4,5,6,7)
d=[1,2,3,4,5,65,6,7,8,93,3]
print(c)
print(max(d))

print(int(123))
print(int(12.3))
print(int('12'))
print(float('12.3'))
print(float(12))
print(str(1))
print(str(12.3))

print(hex(100))

### 起别名
# 函数可以赋给变量，相当于给函数起了别名
a=abs
print(a(-10))
m=max
print(m([1,1,2,4,5,6,767,1,787,87]))


### 定义函数
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
    
print(my_abs(100))

### 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
def nop():
    pass

### 返回多个值
# python是支持返回多个值的，其实是返回一个tuple（不可变数组）
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x,y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)
print(x,y)
print(r)


### 默认参数
def power(x,n=2):
    return x**n
print(power(2))
print(power(2,3))
print(power(2,5))
# 注意： 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    return L
a1=add_end([1,2,3])
a2=add_end(['a','b','c'])
print(a1,a2)
# 注意a3与a4的结果
a3=add_end()
a4=add_end()
print(a3,a4)
# 正确写法使用None
def add_end(L=None):
    if L==None:
        L=[]
    L.append('end')
    return L









### 可变参数
# 函数内部接受的其实是一个list或者tuple
def calc(*numbers):
    sum=0
    for n in numbers:
        sum+=n
    return sum

# 针对外部的list也可以通过加*的方式传入
a=[1,1,2,3,4,5,6]
print(calc(*a))







### 关键字参数
# 可变参数接受的是个数组，那么关键字接受的就是一个map，python里面叫字典(dict)参数
def person(name,age=18,**extra):
    print('name={0} age={1} other info={2}'.format(name,age,extra))
    if 'city' in extra:
        print('city',extra['city'])
    pass

person('张三',18,city='武汉',country='中国',brithday=18)

# 接受dict类型参数
dict1={'attr1':'属性1','attr2':'属性2','attr3':'属性3'}
person('李四',18,**dict1)









### 命名关键字
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
def user(name,*,city='北京',job='无业'):
    print('user={0},city={1},job={2}'.format(name,city,job))
    pass

user('李四')
user('张三',city='武汉',job='软件工程师')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def user1(name, age, *args, city, job):
    print(name, age, args, city, job)


### 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

