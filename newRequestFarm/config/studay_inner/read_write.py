# coding:utf-8

# 读取文件： r：只读 文件描述符在开头, rb代表读取二进制文件，文件描述符在开头
import json
import time

f = open(r'D:\Git\autoMateds\newRequestFarm\config\studay_inner\files\myFirst.txt', 'r', encoding='utf-8')
# print(f.read())  # ==> 读取整个文本内容
print('---------')
f.seek(5)   # 设置文本的文件描述符的位置
print(f.read())
print('0000000000000000')

f.close()


# f = open(r'D:\Git\autoMateds\newRequestFarm\config\studay_inner\files\myFirst.txt', 'r')
# print(f.readline(10))    # 表示读取文件的字节数
#
# print(f.readlines())    # 重读取的文件描述符开始一行一行读取整个文件
# f.close()


# 写文件，w表示写文件，没有则重建文件，有则重新覆盖文件，wb是写二进制文件，文件描述符在开头，a是读或写，写时追加

# f = open(r'D:\Git\autoMateds\newRequestFarm\config\studay_inner\files\myFirst.txt', 'w')
# f.write('nihao')    # 写文件不会立马就写到文件当中，只用使用f.flush()或者关闭文件才能立刻写入
# f.flush()
# time.sleep(10)
# f.close()


# 读写json文件
# [{
#     "name":{"n1":"wangfei", "n2": "zhangxiaosan"}
# }, {"age":{"a1":12, "a2":19}}
# ]
f = open(r'D:\Git\autoMateds\newRequestFarm\config\studay_inner\files\info.json', 'r')
print(type(f))
obj = json.load(f)
print(type(obj))
print(obj)
f.close()

f = open(r'D:\Git\autoMateds\newRequestFarm\config\studay_inner\files\info.json', 'a')
print(type(f))
obj = json.dump({"nihao":"shijie"}, f)
# print(type(obj))
# print(obj)