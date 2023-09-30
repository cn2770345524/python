fp = 'C:\\Users\\12589\\Desktop\\test.txt'

'''
'r'
open for reading (default)
'w'
open for writing, truncating the file first
'x'
create a new file and open it for writing
'a'
open for writing, appending to the end of the file if it exists
'b'
binary mode
't'
text mode (default)
'+'
open a disk file for updating (reading and writing)
'''
##### 读文件
f = open(fp, 'r')
content = f.read()
f.close()  # 释放资源
print(content)

'''
read(size)读取指定大小的内容
readline()读取一行
readlines()读取所有的行，返回一个list
'''
# 常用写法
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 简介写法
with open('/path/to/file', 'r') as f:
    print(f.read())

# 读取二进制文件
f = open('/Users/michael/test.jpg', 'rb')
f.read(1024)
# 读取字符以特定的编码
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
f.read(1024)
# 字符以特定的编码，如果有错误忽略错误
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

###### 写文件
fp = 'C:\\Users\\12589\\Desktop\\test.txt'

# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
# 要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。
# 常规写法
try:
    f = open(fp, 'a', encoding='utf-8')
    f.write('english is very large\n')
except:
    if f:
        f.close()

# 简洁写法（不用写close语句）
with open(fp, 'a') as f:
    f.write('test\n')

######## 读写二进制数据
file_path = 'C:\\Users\\12589\\Desktop\\s.png'
to_path = 'C:\\Users\\12589\\Desktop\\G.png'

from time import sleep


def main():
    # 读取照片的二进制数据
    try:
        fo = open(file_path, 'rb')
        go = open(to_path, 'xb')
        while True:
            d = fo.read(1024 * 200)
            if d == b'':
                break
            print(d)
            go.write(d)
            sleep(1)
    except BaseException as e:
        print('exception:', e)
    finally:
        if fo:
            fo.close()
        if go:
            go.close()
    pass


if __name__ == '__main__':
    main()
