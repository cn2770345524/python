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