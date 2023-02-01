"""
本模块用于测试python中使用 type()方法在运行时创建类
"""


def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


if __name__ == '__main__':
    Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
    h = Hello()
    h.hello()  # Hello, world.
    print(type(Hello))  # <class 'type'>
    print(type(h))  # <class '__main__.Hello'>
