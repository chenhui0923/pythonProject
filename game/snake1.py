import  tkinter as tk


# https://zhuanlan.zhihu.com/p/573356149?utm_id=0  看着慢慢写


side  = 30
height  = 20*side
width   = 20*side
margin =4

def init():
    # 循环次数
    canvas = tk.Canvas(win,height=height,width=width) # 创建画布
    canvas.pack()
    for i in range(20):
        for j in range(20):
            canvas.create_rectangle(i*side,j*side,(i+1)*side-margin,(j+1)*side-margin,fill="grey")

win = tk.Tk()  # 创建窗口
win.title("我写个小游戏")
s=str(width) + "x"+str(height)
win.geometry(s)
init()
win.mainloop()  #  mainloop函数负责接收操作系统发来的事件，只有程序运行结束，才能退出该函数。
