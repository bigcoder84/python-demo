"""
this is function1 module
"""
import math
import sys


def move(x, y, step=1):
    return x + step, y + step


def hello(param):
    print(param)


# 校验参数类型
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 可变参数
def my_sum(step, *param):
    print(param)


# 关键字参数
def person(name, age, **kw):
    print(name)
    print(age)
    print(kw)


def multiParam():
    return [1, 2, 3]


if __name__ == '__main__':
    # hello("Hello World")
    # my_abs("123")

    # x, y = move(1, 1)
    # print(x, y)
    # my_sum(1, 2, 3)

    person("张三", 18, gender='M', job='Engineer')
    print(sys.path)

    a, b = multiParam()
    print(a, b)
