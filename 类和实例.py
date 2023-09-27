# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
class Student(object):
    pass


# 创建实例是通过类名+()实现的
a = Student()

# 可以自由地给一个实例变量绑定属性
a.name = 'hahah'

print(a.name)

