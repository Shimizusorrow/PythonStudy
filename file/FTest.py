# 绝对路径读取文件
# f=open("E:\\PythonSave\\file\\TestFile.txt",'r',encoding='UTF-8')
# f2=open("E:\\PythonSave\\file\\TestFile.txt",'rb')
# f3=open("E:\\PythonSave\\file\\TestFile.txt",'r')

#打印文件信息
# print(f)

# 关闭文件 python 有垃圾清理机制 在文件的引用计算器里面，
# 当计数为0的时候会自动关闭文件

# f.close()

# 从文件读取size个字符
# UnicodeDecodeError: 'gbk' codec can't decode byte 0xaf in position 4: illegal multibyte sequence
# 解决方案: 1.FILE_OBJECT= open('order.log','r', encoding='UTF-8')
#           2.FILE_OBJECT= open('order.log','rb')

# print(f.read())

# f2 读的 不知道什么进制的文件
# print(f2.read())

# print(f3.read())
# ---------------------------------------------------

# 打印读取的个数
# print(f.read(3))

# print(f.readline())

# print(f.readline()) limit限制读取一行的字数

# 将所有的字符转换为列表
# print(list(f))

# 将每行文字打印出来
# for each_line in  f:
#     print(each_line)

#        写入文件
#  需要注意需要给w或者a 的权限
# f=open("E:\\PythonSave\\file\\TestFile.txt",'w',encoding='UTF-8')

# 返回所写入的字符个数
# 覆盖了原有文件的值
# print(f.write("Hello world"))
# f.close()

# 在同一个文件夹内可以直接读取
f4=open('TestFile.txt')
print(f4.read())


# 将读取指针重置到0的位置，从头开始阅读
f4.seek(0)

print("开始筛选aaa")
for each_line in f4:
    if each_line[:3]!="aaa":
        # print(each_line[:3])
        # print("-------")
        print(each_line)
    else:
        print('这里是aaa 啊\n')


