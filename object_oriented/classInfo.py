#
# type(123)
#
# import types
#
# def fn():
#
#     pass
#
# type(fn) == types.FunctionType
# print(dir(fn))
# print(getattr(fn, '__call__'))
# print(hasattr(fn, 'abc'))


class Student(object):
    pass

s = Student()
def set_age(self, age): # 定义一个函数作为实例方法
    print("输入了年龄")


from types import MethodType
s.set_age(25) # 调用实例方法
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法



