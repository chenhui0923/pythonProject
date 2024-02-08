import tkinter as tk
from tkinter import GROOVE, X, BOTTOM, HORIZONTAL, RIGHT, Y, LEFT, BOTH

# 布局https://c.biancheng.net/tkinter/layout-manager-method.html

height=800
width = 800

# 显示指定的文本
def text_label():
    textlabel = tk.Label(chuankou,text="TK学习").pack()
    text_blue = tk.Label(chuankou, text="红色", bg="red", relief=GROOVE).pack(fill=X, pady='10px')  #fill指向x轴横向填充 pady 说明上下偏移距离
# 显示按钮
def first_button():
    say_hello = tk.Button(chuankou,text="点击执行回调函数",fg='blue',command=eat).pack(row=1,column=5)
def eat():
    print("你好")
# 面积
def area(a,b):
    return a * b
# 窗口居中
def windhewi():
    scrheight = chuankou.winfo_screenheight()
    scrwidth  = chuankou.winfo_screenwidth()
    # print("高度：",scrheight,"宽度：",scrwidth,"面积：",area(scrheight,scrwidth))
    chuankou.geometry("%dx%d+%d+%d" % (width, height, (scrwidth-width)/2, (scrheight-height)/2))  # 居中

def chengfakoujue():
    for i in range(0,15):
        for j in range(0,15):
            tk.Button(chuankou,text="("+str(i)+","+str(j)+")",bg='#D1EEEE',width=10).grid(row=i,column=j) # row 代表第几行，column 代表第几列


# 创建一个窗口
chuankou = tk.Tk()
# 背景色
chuankou["background"]="#8DEEEE"
# icon的图标
chuankou.iconbitmap("蔬菜.ico")
# 标题
chuankou.title("TK的学习文件")
# 窗口大小 这玩意一定是string类型的其他的类型不管用
chuankou.geometry(str(width) + "x" + str(height))
#
windhewi()
# text_label()
# first_button()
chengfakoujue()

# 显示窗口
chuankou.mainloop()

