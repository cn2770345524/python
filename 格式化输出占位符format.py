### 占位符与C语言占位符同理
# %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
print('Hello %s I\'m coming'%'world')

print('Hi，%s you have $%d'%('陌生人',10000))

a=1.2436
print('a=%.2f'%(a)) #保留两位小数


### 采用format函数(有点类似C#语言)
print('hello {0} you score is {1:.2f}'.format('小明',17.23353))

### f-string
# 一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换
r=2.5
s=3.14*r**2
print(f'The area of a circle with radius {r} is {s:.2f}')