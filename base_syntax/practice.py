# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d * %d = %0d "%(i, j, i * j), end='')
#     print()
#
# l = ['qwwq', '343',44566,111111111111111111111111111111111111111,'wewrwre',True,False];
# l.pop()
# l.insert(0, "I am the first element")
# l.append("I am the end element")
#
# print(l)
# for e in l:
#     print(e, end=" ")

# m = {"first":"中国",2:"Japan", 3:"XINGAPO", 4:"Tailand", 5:"India"}
# print(m["first"])

# s = set([1, 2, 3])
# t = set([2, 3, 4])
# print(s | t)
# help(abs)
#
# import time
#
#
# def log_time(func):
#     def decorator(*args, **kw):
#         s = time.time()
#         func(*args, **kw)
#         e = time.time()
#         print(e - s)
#     return decorator
#
#
# @log_time
# def test_runtime():
#     return test_runtime(0, 0)
#
#
# @log_time
# def test_runtime(a, b):
#     s = 0
#     for i in range(1, 100000):
#         s += (s + i)/i
#     return a + b + s
#
#
# test_runtime()

from package_test import module
import numpy

module.test()
module._private_test()


print('hahaha')

