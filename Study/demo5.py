# 2019年5月8日09:46:18
# 函数赋值给变量

def say():
    print("Hello world!")
says=say()
says
print(type(says))

num={1,2,3,4}
print(type(num))
num={1,2,3,4,5,5,4,3,2,1}
print(num)

# frozenset 不可变集合

fz=frozenset([1,2,3,4,5])
print(fz)
# 可变set 集合
num.add(7)
print(num)