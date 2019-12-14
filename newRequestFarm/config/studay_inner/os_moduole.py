# coding:utf-8

import os


import pickle
# 系统模块的使用（os)
# print(os.name)  # 是在什么系统中使用os模块
# print(os.getcwd()) # python工作的脚本路径

# os.chdir(r'D:\360downloads')  # 更改python工作的脚本目录
print(os.getcwd())

# print(os.listdir(os.path.abspath(r'D:\Git\autoMateds\newRequestFarm\config\studay_inner'))) # 查看当前目录下有哪些文件或文件夹
# print(os.path.abspath('.'))
# os.remove(os.path.join(os.path.abspath('.'), 'files/myFirst.txt')) # 删除一个文件

# os.chdir()  # 进入指定目录
# os.system()  # 打开shell
# print(os.path.split(os.path.abspath(__file__))) # 返回最后一个文件或文件夹
# print(os.path.splitext(os.path.abspath(__file__)))  # 返回文件的后缀
# print(help(os))
# print(os.path.abspath(__file__))
# print(os.path.abspath(__file__))  # 返回当前文件

# print(os.path.isfile(os.getcwd())) # 判断是否是文件
# print(os.path.isdir()) # 判断是否是一个文件夹
# os.path.exists()  # 判断文件路径是否存在
# print(os.path.getsize(os.path.abspath(__file__))) # 获取文件大小
# print(os.environ)  # 获取环境变量,返回的是一个字典，是系统的环境变量
# print(os.putenv(dictName,Value)) # 设置环境变量的值
