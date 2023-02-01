import requests
import src.function.function1

# 通过url直接加上请求参数，与通过params传参效果是一样的
response = requests.get(url='http://www.baidu.com/s?wd=requests模块')
# 通过params传参
response2 = requests.get(url='http://www.baidu.com/s', params={"wd": "requests模块"})
print(response.content.decode('utf-8'))  # 打印状态码
# print(response.text)		# 获取响应内容

x, y = src.function.function1.move(1, 2, 3)
print(x, y)