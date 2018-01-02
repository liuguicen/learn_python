# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
#
#
# f = lazy_sum(1, 3, 5, 7, 9)
# print(f())


# class CF:
#     y = 1000
#
#
# def create_counter(x):
#     n = 10
#     cf = CF()
#
#     def f():
#         m = 5
#         while True:
#             m = m + x + n
#             cf.y = cf.y + 10
#             print(cf.y)
#             yield m
#     return f().__next__
#
# counterA = create_counter(10)
# print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
# counterB = create_counter(10)
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

#
# def hard(x):
#     for i in range(1, x):
#         print(i)
#         yield i
#
#
# m = hard(10).__next__
# m()
# m()
# m()


# f = lambda x, y, z: print(x + y + z), x + y + z
import functools

# 函数装饰器
# def log(func):
#     @functools.wraps(func)
#     def wrapper(x):
#         print('start' + func.__name__)
#         ret = func(x)
#         print('end' + func.__name__)
#         return ret
#
#     return wrapper


# 带参数的函数装饰器
# def log(text):
#
#     def decorator(fun):
#         def wrapper(x):
#             print(text + fun.__name__)
#             ret = fun(x)
#             print(text + fun.__name__)
#             return ret
#         return wrapper
#     return decorator
#
#
# @log('我是带参数的装饰器的测试代码')
# def abs(x):
#     if x > 0:
#         return x
#     else:
#         return -x
#
#
# abs = log("带参装饰器的参数")(abs)
# print(abs(-11))

pf = functools.partial(abs, 8)
print(pf())
