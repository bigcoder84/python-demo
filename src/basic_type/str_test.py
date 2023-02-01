if __name__ == '__main__':
    str = "Hello World!"
    str2 = "Hello Python!"

    # 序列的重复操作
    print(str * 2) # Hello World!Hello World!
    # 序列的连接操作
    print(str + str2) # Hello World!Hello Python!
    # 序列的成员关系操作符
    print('W' in str) # True
    print('P' not in str2) # False
    # 序列的切片操作（前闭后开区间）
    print(str[1:3]) # el