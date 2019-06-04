import time as  t
# 制作定时器
class A():
    # 被打印的时候后需要输出时的值相当于Java toString
    def __str__(self):
        return "AAA"

class B():
    def __repr__(self):
        return "BBB"
a=A()
b=B()
# print(a) AAA
# print(b) BBB

class MyTimer():
    prompt = "总共运行了"
    def __init__(self):
        self.prompt = "总共运行了"
        self.lasted = []
        self.begin = 0
        self.end= 0

    def __str__(self):
        return  self.prompt

    __repr__=__str__

    #开始计时
    def star(self):
        self.begin=t.localtime()
        print("计时开始...")
    #停止计时
    def stop(self):
        self.end=t.localtime()
        self._calc()
        print("计时结束!")
    # 内部方法,计算运行时间
    def _calc(self):
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            self.prompt+=str(self.lasted[index])


t1=MyTimer()
t1.star()
t.sleep(3)
t1.stop()
print(t1)