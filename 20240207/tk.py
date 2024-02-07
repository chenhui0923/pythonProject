import tkinter as tk
from tkinter import GROOVE, X

height=800
width = 800

# 显示指定的文本
def text_label():
    textlabel = tk.Label(chuankou,text="TK学习").pack()
    text_blue = tk.Label(chuankou, text="红色", bg="red", relief=GROOVE).pack(fill=X, pady='10px')  #fill指向x轴横向填充 pady 说明上下偏移距离


# 显示按钮
def first_button():
    say_hello = tk.Button(chuankou,text="点击执行回调函数",fg='blue',command=eat).pack()



def eat():
    print("你好")


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


text_label()

first_button()
# 显示窗口
chuankou.mainloop()

