"""
本模块主要测试函数的闭包
"""


def func1(arr):
    def func2():
        result = 0
        for value in arr:
            result += value
        return result

    return func2


def inc():
    x = 0

    def fn():
        # 读取外部局部变量的值，必须使用 nonlocal 关键字声明，否则 x 会认为是内层函数的局部变量，未声明该变量就读取，就会导致报错
        nonlocal x
        x = x + 1
        return x

    return fn




if __name__ == '__main__':
    # inc()()
    # arr = [1, 2]
    # f = func1(arr)
    # print(f())
    # arr.append(3)
    # print(f())

    now()
