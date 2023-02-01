"""
本模块主要测试 @property
"""


class Person(object):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("name is not str type")
        self.__name = value


if __name__ == '__main__':
    per = Person("张三")
    print(per.name)
    per.name = "123"
