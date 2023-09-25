### 字符转为编码
a=ord('A')
print(a)
### 编码转换为字符
b=chr(a)
c=chr(66)
print(b,c)

### 中文unicode编码
d='\u4e2d\u6587'
print(d)
f=ord('中')


### 对于byte数据的编码与解码
### 字符直接转换成byte字节
# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
a=b'A'
print(a)
# 根据指定的encoding编码 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
b='ABC'.encode('ascii')
c='中国'.encode('utf-8')
print(b)
print(c)
# 根据指定的encoding解码 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
d=b.decode('ascii')
e=c.decode('utf-8')
print(d)
print(e)
# 遇到无法解码的字节，decode方法会报错,可以添加ignore参数去忽视部分错误
b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')

### 获取字符串长度
a=len('ABC')
b=len('中国')
print(a,b)
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
c=len(b'\u4e2d\u6587')
print(c)
d=len('中文'.encode('utf-8'))
print(d)