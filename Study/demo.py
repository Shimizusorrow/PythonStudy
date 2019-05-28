import random
secret=random.randint(1,10)
temp = input("Hello world")
guess = int(temp)
a = 0
while 1:
    if a>=2:
        print("失败三次了哦")
        break
    if guess == 8:
        print("Right!")
        break
    else:
        print("Wrong")
        temp = input("猜错了请重新输入")
    a+=1
    guess = int(temp)
    print(secret)
print("end!")