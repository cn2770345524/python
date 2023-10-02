# 获取当前时间
from datetime import datetime, timedelta

now = datetime.now()
print(now)
# 2023-10-02 00:24:20.193616

# 获取指定日期
s = datetime(year=2000, month=1, day=1, hour=1, minute=30, second=55)
print(s)
# 2000-01-01 01:30:55

# 获取timestamp
# 注意Python的timestamp是一个浮点数，整数位表示秒
# 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
now = datetime.now()
print(now.timestamp())

# 根据timestamp生成datetime对象
p = datetime.fromtimestamp(datetime.now().timestamp())
print(p)

# timestamp也可以直接被转换到UTC标准时区的时间
t = datetime.now().timestamp()
ut = datetime.utcfromtimestamp(t)
print(t)

# 字符串(str)转为datetime
# 字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。详细的说明请参考https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
s = '2000-10-01 12:00:00'
datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
print(s)

# 安装特定格式获取时间字符串
now = datetime.now()
print(now.strftime('%Y-%m-%d'))

# datetime运算
now = datetime(year=2000, month=2, day=2)
now = now + timedelta(days=10)
print(now)  # 2000-02-12 00:00:00
now = now - timedelta(hours=13)
print(now)

