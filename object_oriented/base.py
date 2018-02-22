
class People(object):
    pass


class Student(People, object):
    @staticmethod
    def my_static_method():
        print("A static method has be invoke")

    @classmethod
    def my_class_method(cls):
        print("I am a class method")

    def __init__(self, name, score):
        s = self
        self.__name = name
        self.score = score

    def print(self):
        print(self.__name + " 分数 = " + str(self.score))

    def __private_method(self):
        print("I am a private method")

#
# xm = Student('xiaoming', 100)
#
# xm._Student__private_method = xm.print
#
# def fu():
#     print('I am a external function')
#
# xm.fu = fu
# xm.fu()

s = Student("xiaoming", 12)

print(type(Student))

print(type(Student.my_class_method))
Student.my_static_method()
print(type(5))