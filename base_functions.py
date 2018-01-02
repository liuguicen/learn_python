# print(max(1,2,3,4,5,6))
# from base_custom_function import my_abs
# print(my_abs(-566))
import math;

# def qudratic(a, b, c):
#     if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
#         raise TypeError("bad operand type")
#     det = b * b - 4 * a * c;
#     if det > 0:
#        return (-b + math.sqrt(det)) / (2 * a), (-b - math.sqrt(det)) / (2 * a)
#     if det == 0:
#         return -b / (2 * a)
#     else: return
#
# print(qudratic(5, -3, 1))

# def power(a, n=2):
#     s = 1
#     while (n > 0):
#         n -= 1;
#         s *= a
#     return s
#
# print(power(5, 0))

# 变长参数
# def variable_params_method(a, w=4, *args, b = 2):
#     print(a, w, args, b)
#
# variable_params_method(1,2,3,4)

#关键字参数
# def person(name, age, **kw):
#     print(name, age, kw)
#
# person("小明", 5, country = "china", gender = "男")
#
# m = {"country" : "china", "gender" : "男"}
# person("小明", 5, **m)
L = [1, 2]
D = {'ssd': 1, 'sd': 2}


def f1(a, b, c):
    print(a, b, c)

f1(*L)

