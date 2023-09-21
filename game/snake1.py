import tkinter as tk
import random
from tkinter import messagebox

# https://zhuanlan.zhihu.com/p/573356149?utm_id=0  看着慢慢写


side = 30
lattice = 10
height = lattice * side
width = lattice * side
margin = 4
snake = []
cookie = []



def init():
    # 循环次数
    start_x = int(lattice/2-3)  # 蛇的初始坐标
    start_y = int(lattice/2-3)
    ci, cj = set_cookie()
    cookie.append([ci, cj])

    for i in range(lattice):
        for j in range(lattice):
            canvas.create_rectangle(i * side, j * side, (i + 1) * side - margin, (j + 1) * side - margin, fill="grey")
            if (i == 0 or i == lattice-1 or j == 0 or j == lattice-1):  # 墙体显示
                canvas.create_rectangle(i * side, j * side, (i + 1) * side - margin, (j + 1) * side - margin, fill="black")

            if ((i == start_x and j == start_y) or (i == start_x + 1 and j == start_y)):  # 蛇的初始移动向右
                canvas.create_rectangle(i * side, j * side, (i + 1) * side - margin, (j + 1) * side - margin,fill="yellow")
                snake.append([i, j])
                # messagebox.showinfo("Game Over!", snake)
            if i == ci and j == cj:  # 食物
                canvas.create_rectangle(i * side, j * side, (i + 1) * side - margin, (j + 1) * side - margin,fill="blue")
def set_cookie():
    ci = random.randint(1,lattice-2)
    cj = random.randint(1,lattice-2)
    while [ci, cj] in snake:
        ci = random.randint(1, lattice - 2)
        cj = random.randint(1, lattice - 2)

    return  [ci,cj]

win = tk.Tk()  # 创建窗口
win.title("我写个小游戏")
s = str(width) + "x" + str(height)
win.geometry(s)
canvas = tk.Canvas(win, height=height, width=width)  # 创建画布
canvas.pack()  # 放置在指定地方
init()
win.mainloop()  # mainloop函数负责接收操作系统发来的事件，只有程序运行结束，才能退出该函数。
