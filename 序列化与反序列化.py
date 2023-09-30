'''
我们把变量从内存中变成可存储或传输的过程称之为序列化
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
'''

# Python提供了pickle模块来实现序列化。

'''
json/pickle模块主要有四个比较重要的函数，分别是：

dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象

pickle也有这四个函数，作用大同小异
'''

import pickle


def dump(obj, file_path):
    try:
        with open(file_path, 'wb') as f:
            p = pickle.dumps(obj)
            f.write(p)
    except BaseException as e:
        print('error:', e)


def load(file_path):
    try:
        with open(file_path, 'rb') as f:
            d = f.read()
            return pickle.loads(d)
    except BaseException as e:
        print('error:', e)


def main():
    fp = 'C:\\Users\\12589\\Desktop\\t.txt'
    d = dict()
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    dump(d, fp)
    s = load(fp)
    pass


#### json
import json


def test_json():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    test_json()
