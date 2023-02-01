"""
本模块用于测试python的 Exception
"""
import logging


class CustomException(Exception):
    def __init__(self, code, msg):
        super().__init__(code, msg)
        self.code = code
        self.msg = msg


def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e


def example2():
    try:
        int('N/A')
    except ValueError as e:
        logging.exception(e)
        return 0


if __name__ == '__main__':
    # try:
    #     raise CustomException(-1, "系统错误")
    # except CustomException as e:
    #     print(e.msg)
    print(example2())
