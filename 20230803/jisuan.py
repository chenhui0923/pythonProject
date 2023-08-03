import calendar


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


if __name__ == '__main__':
    # sum()
    # calendardate()
    main()
