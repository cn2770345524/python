### 数学函数
max()  # 求最大值
abs()  # 求绝对值

### 进制转换
hex()  # 将所给数值转换为16进制的字符串

### 判断实例
isinstance()

### 获取实例类型
type()
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types

# sorted filter map reduce针对数组list tuple的操作
sorted()

import functools
filter()
map()
functools.reduce()


def fn():
    pass


# 获取实例对象的类型
print(type(fn) == types.FunctionType)
# True

print(type(abs) == types.BuiltinFunctionType)
# True

print(type(lambda x: x) == types.LambdaType)
# True

print(type((x for x in range(100))) == types.GeneratorType)
# True


### dir()函数获取一个对象所有属性和方法 返回一个字符串List
dir()
### hasattr()函数可以判断一个对象是否有对应属性或方法
hasattr()
### setattr()函数可以设置个实例属性的值
setattr()
### getattr()函数可以获取一个实例属性的值或方法 如果试图获取不存在的属性，会抛出AttributeError的错误：
getattr()