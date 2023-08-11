import calendar
import time
import datetime  # 时间
import random  # 随机数


# 求和
def sum():
    num1 = input('请输入第一个数字:')
    num2 = input('请输入第二个数字:')
    sum = float(num2) + float(num1)
    print('{a}与{b}相加的结果为{c}'.format(a=num1, b=num2, c=sum))


# 日历
def calendardate():
    y = int(input('输入年份：'))
    m = int(input('输入月份：'))
    try:
        print(calendar.month(y, m))
    except:
        print("输入错误")


# 分鱼
def main():
    fish = 1
    while True:
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish += 1


# 昨天日期
def yesterday():
    # datetime.timedelta 对于日期时间 进行加减操作，正数时为加，负数时为减
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday


# n个数的平方相加
def sumOfSeries():
    n = int(input("输入数字："))
    sumnum = 0
    for i in range(1, n + 1):
        sumnum += i * i
    return sumnum


def randomnum(a, b):
    num = random.random()
    if (a > b):
        a, b = b, a
    num1 = random.randint(a, b)  # 区间随机数
    num2 =random.randrange(a,b)
    print(num, num1)
    print(num2)


if __name__ == '__main__':
    # sum()
    # calendardate()
    # main()
    # print(yesterday())
    # print(sumOfSeries())
    x = int(input('输入数值：'))
    y = int(input('输入数值：'))
    randomnum(x, y)
