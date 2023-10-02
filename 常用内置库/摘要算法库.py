import hashlib

message = 'hello i\'m Liu Hao'
md5v = hashlib.md5()
md5v.update(message.encode('utf-8'))
print(md5v.hexdigest())

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

# 摘要算法的应用
'''
1.防纂改
2.数据库密码防泄漏 在数据库中不存入明文数据，存密码的hash值，用户登录是只需要比对hash一不一致就可以知道密码对不对
但是这种会有泄露的问题，一些简单密码的hash值可以反推出来，例如123,456 8888这种，黑客完全可以搞个hash表提前根据哈希算法算出来
因此为了避免这种问题，就需要加“盐”，这个“盐”一般保存在服务端，用户很难获取到，因此从一定程度保护了安全
'''