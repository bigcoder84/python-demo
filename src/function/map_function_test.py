from functools import reduce


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    result = reduce(lambda x, y: x + y, numbers)
    print(type(result))
    print(result)