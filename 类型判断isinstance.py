from collections.abc import Iterable

### 当前对象是否是指定的类型的实例
L=[1,2,3,4,5]
res = isinstance(L,Iterable)
print(res)