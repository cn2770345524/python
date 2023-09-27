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
        pass

    # 静态就是不需要实例化就可以调用的方法
    @staticmethod
    def is_valid(person):
        return isinstance(person, Person)

    # 类方法被@classmethod修饰，参数约定叫做cls，cls里面包含当前类的所属的元信息
    @classmethod
    def new_instance(cls):
        print(cls) # <class '__main__.Person'>
        return cls('default')


d = Person.new_instance()
