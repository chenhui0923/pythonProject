import tkinter as tk
import random
import time
from tkinter import messagebox

# https://zhuanlan.zhihu.com/p/573356149?utm_id=0  看着慢慢写

side = 30
lattice = 20
height = lattice * side
width = lattice * side
margin = 4
snake = []  # 蛇身的坐标
move = [1, 0]  # 移动方向
cookie = []  # cookie
score = [0]  # 得分
t = []  # 时间



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
                canvas.create_rectangle(i * side, j * side, (i + 1) * side - margin, (j + 1) * side - margin,fill="red")
    t.append(time.time())  # 初始时间
    update()
def set_cookie():
    ci = random.randint(1,lattice-2)
    cj = random.randint(1,lattice-2)
    while [ci, cj] in snake:
        ci = random.randint(1, lattice - 2)
        cj = random.randint(1, lattice - 2)

    return  [ci,cj]

# 自定义蛇的移动
def snake_move():

    del(snake[0])
    snake.append([snake[len(snake)-1][0]+move[0] , snake[len(snake)-1][1]+move[1]])

def update():
    win.update()
    if check():
        eat()
    canvas.create_rectangle(snake[0][0] * side, snake[0][1] * side, (snake[0][0] + 1) * side - margin,
                            (snake[0][1] + 1) * side - margin, fill="grey")
    snake_move()
    canvas.create_rectangle((snake[len(snake) - 1][0]) * side, (snake[len(snake) - 1][1]) * side,
                            (snake[len(snake) - 1][0] + 1) * side - margin,
                            (snake[len(snake) - 1][1] + 1) * side - margin, fill="yellow")
    if check_lose():
        t.append(time.time())
        result = "Your Score is " + str(score[0]) + ", time is " + str(int(t[1] - t[0])) + " second"
        messagebox.showinfo("Game Over!", result)  # 弹窗显示分数和时间
        time.sleep(2000)
        win.destroy()
        return
    win.after(500, update)

def rotage(event):
    if move[1] and event.keysym == 'Left':
        move[0] = -1
        move[1] = 0
    elif move[1] and event.keysym == 'Right':
        move[0] = 1
        move[1] = 0
    elif move[0] and event.keysym == 'Up':
        move[0] = 0
        move[1] = -1
    elif move[0] and event.keysym == 'Down':
        move[0] = 0
        move[1] = 1
# 吃积分
def check():
    if snake[len(snake)-1] == cookie[0]:
        return True
    return False

# 吃完积分后的操作
def eat():
    score[0] += 10  # 得分加10分
    cookie[0][0], cookie[0][1] = set_cookie()
    canvas.create_rectangle(cookie[0][0] * side, cookie[0][1] * side, (cookie[0][0] + 1) * side - margin,
                            (cookie[0][1] + 1) * side - margin, fill="red")
    snake.insert(0, [snake[0][0] - move[0], snake[0][1] - move[1]])
    if snake[0][0] >= lattice-1 or snake[0][0] <= 0 or snake[0][1] >= lattice-1 or snake[0][1] <= 0:
        canvas.create_rectangle(snake[0][0] * side, snake[0][1] * side, (snake[0][0] + 1) * side - margin,
                                (snake[0][1] + 1) * side - margin, fill="black")
def check_lose():
    # 蛇头的坐标
    x = snake[len(snake) - 1][0]
    y = snake[len(snake) - 1][1]
    # 蛇身
    check = []
    for i in range(len(snake)):
        check.append([snake[i][0], snake[i][1]])
    del (check[len(check) - 1])
    if [x, y] in check:
        return True
    if x <= 0 or x >= lattice-1 or y <= 0 or y >= lattice-1:
        return True
    return False

win = tk.Tk()  # 创建窗口
win.title("我写个小游戏")
s = str(width) + "x" + str(height)
win.geometry(s)
canvas = tk.Canvas(win, height=height, width=width)  # 新建画布工具
canvas.pack()  # 放置在指定地方
canvas.focus_set()  # 聚焦
canvas.bind("<KeyPress-Left>", rotage)
canvas.bind("<KeyPress-Right>", rotage)
canvas.bind("<KeyPress-Up>", rotage)
canvas.bind("<KeyPress-Down>", rotage)
init()
win.mainloop()  # mainloop函数负责接收操作系统发来的事件，只有程序运行结束，才能退出该函数。
