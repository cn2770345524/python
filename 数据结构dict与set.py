d = dict()
d = {}
d = {'name': '张三', 'age': 18}
print('name' in d)
print(d.get('sex', '男'))
d.pop('name')
print(d)

# 定义
s1 = set([1, 2, 3])
s2 = set([4, 2, 3])
# 添加
s1.add(5)
s2.add(6)
# 交并差
print(s1 & s2)
print(s1.intersection(s1))
print(s1 | s2)
print(s1.union(s2))
print(s1 - s2)
print(s1.difference(s2))
# 删除
s1.remove(5)
s2.remove(6)
print(s1)
print(s2)
# 遍历
for e in s1:
    print(e)
