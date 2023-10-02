import base64

b = b'binary\x00string'
print(base64.b64encode(b))
p = base64.b64encode(b)
print(base64.b64decode(p))

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
b = b'i\xb7\x1d\xfb\xef\xff'
print(base64.b64encode(b))  # b'abcd++//'
print(base64.urlsafe_b64encode(b)) # b'abcd--__'
print(base64.urlsafe_b64decode(base64.urlsafe_b64encode(b)))

