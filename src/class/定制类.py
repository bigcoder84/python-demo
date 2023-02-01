"""
本模块用于测试 定制类
"""


class Student(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f'Student:(name:{self.__name})'



if __name__ == '__main__':
    stu = Student("张三")
    print(stu)