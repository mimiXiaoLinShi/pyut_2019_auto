# coding: utf-8

'''装饰器的作用，可以在调用某个方法之前打印一段信息或者做一些校验,
实质是函数中嵌套函数，并返回函数的对象
'''

# def outer(fun):
#     def inner(*args, **kwargs):
#         print('执行函数之前的操作')
#         return fun(*args, **kwargs)
#     return inner
#
#
# def func(num):
#     print('num is {}'.format(num))
#
# # 闭包的调用
# result = outer(func)     # 传入func对象到outer作为参数，执行了inner函数，并返回inner对象给result
# result('haha')  # 相当于调用func()方法

# 所以我们可以利用闭包做为装饰器来使用
def outer(fun):
    def inner(*args, **kwargs):
        print('执行函数之前的操作')
        return fun(*args, **kwargs)
    return inner

@outer
def func(num):    # 返回inner对象
    print('num is {}'.format(num))

# func('haha')   # 相当于调用了inner('haha')


# 一个除法计算器
def portal(numA, numB):
    A = int(numA)
    B = int(numB)
    return A/B


# 正常调用函数
print(portal(9,99))
# 使用偏函数
from functools import partial
si = partial(portal, numB=99)  # 默认numB=99
print(si(9))
print(si(99))
