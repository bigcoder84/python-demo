"""
本模块主要用来测试python的多继承
"""


class Base1(object):
    def hello(self):
        print("Base1")


class Base2(object):
    def hello(self):
        print("Base2")


class Sub(Base1, Base2):
    pass


if __name__ == '__main__':
    s = Sub()
    s.hello()
