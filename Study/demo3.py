# 测试嵌套函数

def fun2():
    def fun1():
        print("函数一正在被调用...")
    fun1()
    print("函数二正在执行...")

fun2()

# 闭包
def FunX(x):
    def FunY(y):
        return x*y
    return FunY

i=FunX(8)
print(type(i))
print(i(5))

# 测试样例二 闭包

def Fun1():
    x=[5]
    def Fun2():
        x[0] *= x[0]
        return x[0]
    return Fun2()


print(Fun1())

# 第二种实现方法
def Fun3():
    x=5
    def Fun4():
        nonlocal x
        x *= x
        return x
    return Fun4()


print(Fun3())

# 测试lambda表达式

def ds(x):
    return 2*x+1

print(ds(3))

# lambda 表达式的实现
g=lambda x:2*x+1

print(g(3))

# 样例二

def add(x,y):
    return x+y


print(add(3, 4))

c=lambda x,y:x+y

print(c(3, 5))

# print(help(filter))
# 测试Filter

print(list(filter(None, [1, 0, False, True])))

list1=[c,g]
list2=(c,g)
h=list1[1]
# list1
print(h(3))
print(list1[1](6))
# list2
h1=list2[1]
print(list2[1](6))
print(h1(3))

# filter 使用
odd=lambda x:x%2
temp=range(10)
show=filter(odd,temp)
print(list(show))
