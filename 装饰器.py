##### decorator装饰器
# 有点类似java中的注解，aop的概念
from datetime import datetime

### 低阶装饰器
def low_log(fn):
    def wrapper(*args,**extra):
        print('function [{0}] exec start time:{1}'.format(fn.__name__,datetime.now()))
        res=fn(*args,**extra)
        print('function [{0}] exec end time:{1}'.format(fn.__name__,datetime.now()))
        return res
    return wrapper

# 调用装饰器。只需要采用@关键字在方法上调用
@low_log
def test():
    print('hello world')

test()
# 结果
# function [test] exec start time:2023-09-27 16:11:43.918957
# hello world
# function [test] exec end time:2023-09-27 16:11:43.920486

### 带参数的低阶装饰器
def low_log_param(param):
    def low_log(fn):
      def wrapper(*args,**extra):
            print('function [{0}] exec start time:{1} param:{2}'.format(fn.__name__,datetime.now(),param))
            res=fn(*args,**extra)
            print('function [{0}] exec end time:{1} param:{2}'.format(fn.__name__,datetime.now(),param))
            return res
      return wrapper
    return low_log

@low_log_param('放进去了一些参数')
def test():
    print('hello world')

test()


## 注意：经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
## 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
## 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下

### 高阶装饰器
import functools
def log(fn):
    @functools.wraps(fn)
    def wrapper(*args,**extra):
        print('function [{0}] exec start time:{1}'.format(fn.__name__,datetime.now()))
        res=fn(*args,**extra)
        print('function [{0}] exec end time:{1}'.format(fn.__name__,datetime.now()))
        return res
    return wrapper

# 带参数的高阶装饰器
def log_param(param):
    def log(fn):
        @functools.wraps(fn)
        def wrapper(*args,**extra):
            print('function [{0}] exec start time:{1} param:{2}'.format(fn.__name__,datetime.now(),param))
            res=fn(*args,**extra)
            print('function [{0}] exec end time:{1} param:{2}'.format(fn.__name__,datetime.now(),param))
            return res
        return wrapper 
    return log