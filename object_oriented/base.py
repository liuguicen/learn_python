
class People(object):
    pass


class Student(People, object):
    def __init__(self, name, score):
        self.__name = name
        self.score = score

    def print(self):
        print(self.__name + " 分数 = " + str(self.score))

    def __private_method(self):
        print("I am a private method")


xm = Student('xiaoming', 100)

xm._Student__private_method = xm.print

def fu():
    print('I am a external function')

xm.fu = fu
xm.fu()