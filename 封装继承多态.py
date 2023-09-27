class Animal(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('animal name={0} age={1} is running'.format(self._name, self._age))


class Cat(Animal):

    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self._weight = weight


def animal_run(animal):
    animal.run()


a = Animal('animal', 18)
animal_run(a)
c = Cat('cat', 18, 120)
animal_run(a)


# 多继承
class FlyInterface(object):

    def fly(self):
        '''
        继承此对象下的所有子类都有fly方法
        :return:
        '''
        pass

class RunInterface(object):

    def run(self):
        '''
        继承此对象下的所有子类都有run方法
        :return:
        '''
        pass

class Test(FlyInterface,RunInterface):
    pass
