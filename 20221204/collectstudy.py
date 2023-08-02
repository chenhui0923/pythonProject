my_students = ["kevin", "lihong"]
coure_rank = {"math": "kevin", "logic": "lihong", "english": "lishi"}
my_students_rank = {}
args = [2, 4, 5]
onezone= 20


def class_log():  # 无形参数
    print("hello world")


def is_true(x):
    return x > 0


def min_number(x, y):
    if x >= y:
        x, y = y, x
    return y


def sum_number(*args):
    total = 0
    for k in args:
        total += k
    return total


# def write(letter):
#     l=[]
#     for k in letter:
#         l.append(k)
#     return l
def write(letter):  # 简化
    return [l for l in letter]


def write_determine(x):
    return [l for l in x if 'g' in l]


def count_student(**kwargs):
    for k, v in kwargs.items():
        print('{0}--{1}'.format(k, v))


def square(l):
    list= []
    for x in l:
        list.append(x*x)
    return list

def xgglobal():
    global onezone #套娃， 使用父级的 参数 ，也可以通过方法赋值调用
    print(onezone)
    onezone = 123
    print(onezone)
    num  = 10
    def xgnonlocal():
        nonlocal num #套娃， 使用父级的 参数
        print(num)
        num = 456
        print(num)
    return xgnonlocal()



a=lambda l:[x*x for x in l] #匿名函数简化写法

if __name__ == '__main__':
    #     for k, v in coure_rank.items():
    #         if v in my_students:
    #             my_students_rank[v] = k  # 将 coure_rank的 k值 给 my_students 的value
    # p_len = len(my_students_rank)
    # while (p_len > 0):
    #     for p in my_students_rank.keys():
    #         print('{person}--{coure}'.format(person=p, coure=my_students_rank[p]))
    #     p_len -= 1
    # class_log()
    # total = sum_number(1, 2)
    # print(total)
    # min = min_number(1, 2)
    # print(min)
    # count_student(math='kecin', login='emli')
    # print(write('appent'))
    # print(write_determine(['appent', 'banner', 'orange']))
    # print(square(args))
    # print(a(args))
    print(xgglobal(),onezone,)

