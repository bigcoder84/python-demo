if __name__ == '__main__':
    arr = [1, 2, 3]
    arr2 = [3, 4, 5]
    # 序列的重复操作
    print(arr * 2)
    # 序列的连接操作
    print(arr + arr2)
    # 序列的成员关系操作符
    print(3 in arr)
    print(4 not in arr)
    # 序列的切片操作（前闭后开区间）
    print(arr[1:3])