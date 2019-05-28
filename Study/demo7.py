# Test easygui
# from  easygui import *
import easygui  as g
import sys
g.msgbox("helloworld")
while 1:
    g.msgbox("first")
    msg="1"
    title="2"
    choices=["3","4","5","6"]

    choice=g.choicebox(msg,title,choices)

    g.msgbox("你的选择是:"+str(choice),"结果")

    msg="你希望重新开始吗?"
    title="请选择"
    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)
