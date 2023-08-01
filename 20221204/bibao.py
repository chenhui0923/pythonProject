import time


# 装饰器
def record_time(func):

    def wrapper(*kwargs):
        print('function start at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
        total = func(*kwargs)
        print('function end at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
        return total
    return wrapper


# 闭包
def out():
    cherr = 'hello'

    def inner(name):
        return cherr + '--' + name

    return inner


@record_time

def sum(*kwargs):
    total = 0
    for ele in kwargs:
        total = total + ele
    time.sleep(2)
    return total
if __name__ == '__main__':
    print(sum(11, 22, 33, 44), out()('lihua'))