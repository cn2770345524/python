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


# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
a='ABCDEFGJKLHMN'
print(a[:5])
print(a[-7:-2:2])




#### 特性2：迭代
# 迭代器可以迭代任何支持迭代的类型例如：字典（dict）字符串

# 字符串可以被迭代
for c in a:
    print(c)
    pass

# 字典也可以被迭代
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



#### 特性3： 列表表达式
L=[x*x for x in range(100)]
print(L)
# 打印结果 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81 ...]

## 加上if条件筛选
G=[x*x for x in range(10) if x%2==0]
print(G)
# 结果 [0, 4, 16, 36, 64]

## 双层for循环
H=[m*n for m in range(100) if m%2==0 for n in range(100) if n%3==0]
print(H)

# 三层和三层以上的循环就很少用到了。

# 两个变量
dict1={'a':1,'b':2,'c':3}
F=[k+'='+str(v) for k,v in dict1.items()]
print(F)
# 结果：['a=1', 'b=2', 'c=3']


### generator生成器
# 列表元素可以按照某种算法推算出来 不必创建完整的list，从而节省大量的空间
# 第一种：要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
# 第二种：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator函数，调用一个generator函数将返回一个generator
G=(x for x in range(100) if x%2==0)
print(G)
# 结果 <generator object <genexpr> at 0x0000024A4FF1A9B0> 

# 遍历生成器对象和普通的for一样
for item in G:
    print(item)

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n+=1
    return 'done'

o=fib(10)
for i in range(10):
    print(next(o))