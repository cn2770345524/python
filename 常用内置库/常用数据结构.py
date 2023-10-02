from collections import namedtuple

# # 命名元组
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))

# deque适用于双向列表和栈
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('f')
print(q)  # deque(['f', 'a', 'b', 'c', 'd'])

# 具有默认值的字典defaultdict
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
print(dd['key'])  # N/A

# OrderedDict可以保持dict的键有序
from collections import OrderedDict

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))  # ['z', 'y', 'x']

# ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。

from collections import ChainMap

d1 = dict()
d1['color'] = 'red'
d1['size'] = '14px'

d2 = dict()
d2['color'] = 'blue'
d2['weight'] = 'default'

cm = ChainMap(d1, d2)
print(cm['color'])  # red
print(cm['size'])  # 14px
print(cm['weight'])  # default
