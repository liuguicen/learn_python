# from collections import Iterable
# def f(x):
#     return x * x
# l = map(f, range(1,10))
# for item in l:
#     print(item)

# reduce
from functools import reduce


# def add(a, b):
#     return a + b
# print(reduce(add, range(1, 10)))
#
def joint(a, b):
    return a * 10 + b


# print(reduce(joint, [x for x in range(1, 10) if x % 2 == 1]))

# practice
# def normalize(name):
#     assert isinstance(name, str)
#     return name.capitalize()
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# def str2float(s):
#     assert isinstance(s, str)
#     index = s.find('.')
#     return reduce(joint, s[:index]) + reduce(reduceMultiply, s[index + 1:]) / 10
#
#
# def reduceMultiply(x, y):
#     return x + y / 10


def my_key(x):
    return x


list1 = [5, 4, 3, 2, 1]
print(sorted(list1, key=my_key))
