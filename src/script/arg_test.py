"""
本模块用于测试python中获取命令参数：
python3 arg_test.py test1 test2  # 输出 ['arg_test.py', 'test1', 'test2']
"""

import sys

args = sys.argv
print(args)  # 输出 ['arg_test.py', 'test1', 'test2']
