# 使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中，
# 因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。但是也要注意，尽量不要与内置函数名字冲突
# 为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）
# 请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，
# 而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块

from PIL import Image
import hello

hello.test()


# 安装第三方模块
# 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索
# 在Python中，安装第三方模块，是通过包管理工具pip完成的、


url = 'C:\\Users\\12589\\Desktop\\Snipaste_2023-09-27_17-14-18.png'
im = Image.open(url)
im.show()
