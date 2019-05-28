# Test Python 3的类

class Ball:
    name="666"
    def __init__(self):
        print("我被创创建了")

    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name

a=Ball()
a.setName("Jack")
print(a.getName())
b=Ball();
print(b.getName())
b.setName("777")
print(b.getName())

# 测试私有
class Person:
    __name="Helloworld"
    def getName(self):
        return self.__name
p=Person()
print(p.getName())
# print(p._Person_name)