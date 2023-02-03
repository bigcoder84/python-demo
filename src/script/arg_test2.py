"""
本模块用于测试python中获取命名的命令参数：

python3 arg_test.py --ip 127.0.0.1 --port 80
127.0.0.1
80
"""

import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--ip', type=str, default=None)
parser.add_argument('--port', type=int, default=32)

args = parser.parse_args()

print(args.ip)
print(args.port)

