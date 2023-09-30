'''
1.Python的错误其实也是class，所有的错误类型都继承自BaseException
  Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：https://docs.python.org/3/library/exceptions.html#exception-hierarchy
2.使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用bar()，bar()调用foo()，结果foo()出错了
'''

# 捕捉异常
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
else:  # 非必选
    print('no error')
finally:  # 非必选
    print('finally...')
print('END')


# 抛出异常
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例
class TestError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise TestError('invalid value:%s' % s)
    return 10 / n


# 把错误往上层抛
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!') # raise语句如果不带参数，就会把当前错误原样抛出
        raise  # 在这里接受到了错误，不需要所以在这里往上抛


bar()

import logging