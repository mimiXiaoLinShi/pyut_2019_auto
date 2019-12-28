# coding: utf-8
from datetime import datetime, timedelta
import time

# 函数装饰器做一个记时器
def demo_super1(func_all):
    def inner(*args, **kwargs):
        now1 = time.time()
        # nowTime1 = time.strftime('%H:%M:%S', time.localtime(now1))
        nowTime = datetime.fromtimestamp(now1).strftime('%H:%M:%S')
        print('当前的时间是%s' % nowTime)

        result = func_all(*args, **kwargs)
        time.sleep(1)
        now2 = time.time()
        timeNow2 = datetime.fromtimestamp(now2).strftime('%H:%M%S')
        print('运行后的时间为%s' % timeNow2)
        timeRe = now2 - now1
        print('运行时间为%d s' % timeRe)
    return inner

@demo_super1
def sum(a, b, c):
    return a


##########类装饰器############
def dome_class(func):
    def inner(self, *args, **kwargs):
        a, b = args
        assert isinstance(a, int) and isinstance(b, int) and isinstance(self.sumber,int)
        return func(self, *args, **kwargs)
    return inner

class Mate:
    def __init__(self, sumber):
        self.sumber = sumber

    @dome_class
    def sum(self, a, b):
        return a * b


##########################python的多继承之路###########
class SupperClass:
    def view(self, a, b):
        print(a, b)
        return 'haha'

class SupperClass1():
    def view(self, a, b):
        print('这是子类1')
        return super().view(a, b)

class SupperClassMate:
    def view(self, a, b):
        print(a, b)
        return 'haha'

class SupperClass2(SupperClassMate):

    def views(self, a, b):
        print('这是子类2')
        return super().view(a, b)

class Son(SupperClass1, SupperClass2, SupperClass):
    def view(self, a, b):
        print('这是儿子')
        return super().view(a, b)


if __name__ == '__main__':
    # mate = Mate(99)
    # print(mate.sum(3, 4))
    son = Son()
    print(son.view(3, 5))

