import tkinter as tk
from tkinter import messagebox
import random
import time

side = 30  # 正方形边长
height = 20 * side  # 20个正方形的边长
width = 20 * side  # 20个正方形的边长
margin = 4  # 间距
snake = []  # 蛇身的坐标
move = [1, 0]  # 移动方向
cookie = []  # cookie
score = [0]  # 得分
t = []  # 时间


# 窗口初始化
def init():
    ci, cj = set_cookie()  # 生成cookie
    start_x = 6  # 蛇的初始坐标
    start_y = 6
    cookie.append([ci, cj])  # 保存cookie
    for i in range(20):
        for j in range(20):
            canvas.create_rectangle(i * side, j * side, (i + 1) * side - margin, (j + 1) * side - margin, fill="grey")
            if (i == 0 or i == 19 or j == 0 or j == 19):  # 墙体显示
                canvas.create_rectangle(i * side, j * side, (i + 1) * side - margin, (j + 1) * side - margin,
                                        fill="black")
            if ((i == start_x and j == start_y) or (i == start_x + 1 and j == start_y)):  # 蛇的初始移动向右
                canvas.create_rectangle(i * side, j * side, (i + 1) * side - margin, (j + 1) * side - margin,
                                        fill="yellow")
                snake.append([i, j])
            if i == ci and j == cj:
                canvas.create_rectangle(i * side, j * side, (i + 1) * side - margin, (j + 1) * side - margin,
                                        fill="blue")
    t.append(time.time())  # 初始时间
    update()


# 生成cookie
def set_cookie():
    ci = random.randint(1, 18)  # 随机生成cookie的横纵坐标
    cj = random.randint(1, 18)
    # 保证生成的cookie不在蛇身里
    while [ci, cj] in snake:
        ci = random.randint(1, 18)  # 随机生成cookie
        cj = random.randint(1, 18)
    return [ci, cj]


# 蛇移动
def snake_move():
    del (snake[0])
    snake.append([snake[len(snake) - 1][0] + move[0], snake[len(snake) - 1][1] + move[1]])


# 更新窗口
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


# 蛇的转向
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


# 检查是否吃到cookie
def check():
    if snake[len(snake) - 1] == cookie[0]:
        return True
    return False


# 蛇吃了cookie会发生什么
def eat():
    score[0] += 10  # 得分加10分
    cookie[0][0], cookie[0][1] = set_cookie()
    canvas.create_rectangle(cookie[0][0] * side, cookie[0][1] * side, (cookie[0][0] + 1) * side - margin,
                            (cookie[0][1] + 1) * side - margin, fill="blue")
    snake.insert(0, [snake[0][0] - move[0], snake[0][1] - move[1]])
    if snake[0][0] >= 19 or snake[0][0] <= 0 or snake[0][1] >= 19 or snake[0][1] <= 0:
        canvas.create_rectangle(snake[0][0] * side, snake[0][1] * side, (snake[0][0] + 1) * side - margin,
                                (snake[0][1] + 1) * side - margin, fill="black")


# 游戏结束
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
    if x <= 0 or x >= 19 or y <= 0 or y >= 19:
        return True
    return False


# 主函数
win = tk.Tk()  # 创建窗口
win.title("AC Snake")  # 标题
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
win.mainloop()