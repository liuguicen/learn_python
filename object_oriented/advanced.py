# 重载下标运算
# class Fib(object):
#
#     def __getitem__(self, n):
#         if isinstance(n, int):
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice):
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             l = []
#             for x in range(stop):
#                 if x > start:
#                     l.append(a)
#                 a, b = b, a + b
#             return l
#
#
# fib = Fib()
#
# print(fib[1], fib[2], fib[3], fib[4])
# print(fib[4: 10])

# 重载.,实现属性链式调用
# class Chain:
#     def __init__(self, path="HTTP:/"):
#         self.path = path
#
#     def __getattr__(self, item):
#         return Chain(self.path + '/' + item)
#
#     def __str__(self):
#         return self.path
#
#     __repr = __str__
#
#
# print(Chain().status.user.timeline)
#
# class Chain(object):
#     def __init__(self, path = ''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
#     __call__ = __getattr__
#
#     __repr__ = __str__
#
#
# print(Chain().status.user.timeline.list)
# print(Chain().users('Zhangsan').repos.transferParmas("transfer a parameter"))


# 使用枚举

from enum import Enum, unique
#
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr'))
#
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Fri)
print(Weekday(2))
print(Weekday(1))
print(Weekday(1) == Weekday.Mon)
print(Weekday(1) == Weekday.Sun)
print(Weekday.Sat.name + ':' + str(Weekday.Sat.value))
print('xiaoming'.join(' is a good boy'))

pow(3, 5)
