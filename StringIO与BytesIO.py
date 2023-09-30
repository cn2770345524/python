'''
StringIO与BytesIO是python提供在内存中读写的IO 很多时候，数据读写不一定是文件，也可以在内存中读写。
'''

# StringIO
from io import StringIO

f = None
try:
    f = StringIO()
    f.write('hello world')
    str = f.getvalue()
    print(str)
except BaseException as e:
    print('exception:', e)
finally:
    if f:
        f.close()

# BytesIO
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
c = f.getvalue()
print(c.decode('utf-8'))
