# 可以通过在类中定义__slots__变量来进行限定。需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。
# 当定义了slots后，slots中定义的变量变成了类的描述符，相当于java，c++中的成员变量声明
# 类的实例只能拥有slots中定义的变量，不能再增加新的变量。注意：定义了slots后，就不再有dict

class User(object):
    __slots__ = ('__name', '__age', '__gender')

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender


u = User('张三', 18, '男')
u.pname = '李四'
