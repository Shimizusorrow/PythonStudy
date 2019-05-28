import math
# from Study import *
# import Study



a=10.4
b=3
print("sss"'{:d}'.format(b)+"sssss"+'{:f}'.format(a))
print(dir(math))
print(math.cos(3.14*60))
if a!=10:
    print("a>10")
b,c=10,20
if b!=c:
    print("ss")
print(math.pow(2, 3))
list1=[1,2,3,4,5,6]
print(2 in list1)

#测试python 中的for 循环
for i in list1:
    # print(i in list1)
    # print(i)
    if i in list1:
        print(i)

#    测试python 中的类
class Study:
    a=10
    b=20
    def fun(name):
        print(name+str(a))

Study.fun("js")
#  测试eval 函数的作用->可以实现字符串的运算
print(type(eval("4*4")))
# help(str)
list2=[1,2,3,4,5,67]
print(list2[1:])
l=[]
l+=list2[:-1]
# print(l)
# print(l.pop(object=l[-2]))