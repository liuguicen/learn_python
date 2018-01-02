from collections import Iterable

L = [1, 2, 3, 4, 5, 6, 7,  8, 9]
# print(L[5:11])
# print(L[::2])
#  print(isinstance(L, Iterable))
# for i, value in enumerate(L):
#     print("the", i,  "item is", value, end = " ", sep= "")

# L = ['Hello', 'World', 18, 'Apple', None]
# L2 = [x.lower() for x in L if isinstance(x, str)]
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')
#
# L = [x * y for x in range(1, 11)  for y in range(-10, -1) if x % 2 == 0 and y % 3 == 0]
# print(L)

# 生成器
g = (x * x for x in range(10))
print(next(g))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


print(next(fib(3)))
print(next(fib(3)))
print(next(fib(3)))
print(next(fib(3)))
