"""
本模块主要测试 函数装饰器
"""
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print(f'call {func.__name__}():')
        return func(*args, **kw)

    return wrapper


def superLog(content):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(f'{content} {func.__name__}():')
            return func(*args, **kw)

        return wrapper

    return decorator


@log
def now():
    print('2015-3-25')


if __name__ == '__main__':
    now()
    print(now.__name__)
