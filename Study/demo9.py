# 学习工厂函数

print(type(len))

class New_int(int ):
    def __add__(self, other):
        return int.__sub__(self,other)
    def __sub__(self, other):
        return int.__add__(self,other)

a=New_int(5)
b=New_int(3)

print(a+b)
# _radd_ 反运算 当加法符号 前面的对象不满足时或者不存在时 调用
class Nint(int ):
    def __radd__(self, other):
        return int.__sub__(self,other)

b=Nint(3)
# 1没有 add方法 所以去调用 b 的反运算方法
print(1 + b)