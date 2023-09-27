# python中的实例的属性的getter setter方法需要用到个装饰器@property

class Person(object):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print('getter name')
        return self.__name

    @name.setter
    def name(self, name):
        print('setter name')
        self.__name = name


p = Person('张三')
print(p.name)
p.name='李四'
print(p.name)
