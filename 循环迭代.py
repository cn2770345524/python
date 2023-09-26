# for
names=['a','b','c','d']
for name in names:
    print(name)

sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum+=x

print(sum)

a=list(range(100))
print(a)

# while
n=99
while n>=0:
    n=n-1
print(n)

# break
n=0
while n<100:
    if(n>=10):
        break
    n+=1
print(n)

# contiune
n=0
while n<10:
    n+=1
    if(n%2==0):
        continue
print(n)

### 高级特性
# 迭代器可以迭代任何支持迭代的类型例如：字典（dict）字符串
dict1={'a':1,'b':2,'c':3}
# 迭代key
for key in dict1:
    print(key)
    pass

# 迭代值
for value in dict1.values():
    print(key)
    pass
# 迭代 k 与 v
for k,v in dict1.items():
    print(k,v)


### 判断一个对象是否可以迭代
from collections.abc import Iterable

### 当前对象是否是指定的类型的实例
L=[1,2,3,4,5]
res = isinstance(L,Iterable)
print(res)


### 取下标
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for index,value in enumerate(L):
    print(index,value)