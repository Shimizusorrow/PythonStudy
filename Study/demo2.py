a=0
print(isinstance(a, str))
def Myf():
    print("Hello my first Fun!")


print(Myf.__doc__)
print(help(Myf()))
def hey(name,hellp="sss"):
    print(name+"->"+hellp)
hey(name="ll",hellp="jdc")
hey("ss")
# 收集参数
def test(*d):
    print('参数的长度是 : ',len(d));
    print("第二个参数是 : ",d[1]);

test(1,"sss",3.14)

# 测试花括号和小括号和中括号所代表的意义
lists =[1,2,3,4]
arrayList=3,5,4,5
testd={1,2,3,4,5}

print(type(lists))
print(lists)
print(type(arrayList))
print(arrayList)
print(type(testd))
print(testd)
# 测试返回多个函数
def back():
    return [1,2,3,"sss"]

lisd=[]
lisd=back()
print(lisd)

# 测试global 关键字
a=10
def test1():
    global a
    print(a)
    a = 19
    print(a)
test1()
