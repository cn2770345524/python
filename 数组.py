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