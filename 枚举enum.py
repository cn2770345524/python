from enum import Enum, unique

# 创建方式一
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


# 创建方式二（推荐）
# 通过继承Eunm类来实现
# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 通过属性取值
day1 = Weekday.Fri
print(day1)
# 通过dict方式取值
day2 = Weekday['Fri']
print(day2)
print(day1 == day2)
# 通过value方式取值
day3 = Weekday(5)
print(day3)
print(day3 == day1)

# 遍历成员
for name, member in Weekday.__members__.items():
    print(name, '=>', member,'value =>',member.value)
