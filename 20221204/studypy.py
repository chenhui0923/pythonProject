from collectstudy import *


str1 = "this is string example....wow!!!";
list1 = ['sty', 'school']


# numbers1 = len(list1)  # 计算列表元素个数
# numbers2 = list1[0]  # 返回第0个元素
# list1.append('red')  # 在尾部添加一个元素
# list1.extend(['blue', 'yellow'])  # 在尾部添加多个元素
# list1.insert(1, 'blue')  # 在1的位置插入元素 blue
# list1.remove('red')  # 删除列表中的第一个为blue的元素
# list1.pop(0)  # 删除第0个元素
# numbers3 = list1.count("blue")  # 返回list中出现blue的次数
# print(numbers3)
# print(list1)
# list1.reverse()  # 翻转列表数据
# print(list1)
# list1.clear()  # 清空列表
# print(numbers1, numbers2)
# dict1 = {"englist": "张三", "math": "李四"}
# test = dict1.get("mat", 0)  # get方法用于获取字典中对应key的值，若不存在则返回0
# test1 = dict1.keys()  # 返回key
# test2 = dict1.values()  # 返回value
# for k, v in dict1.items():  # 返回key与value
#     print('{key} -- {value}'.format(key=k, value=v))
# dict1["englist"] = "Ray"  # 直接改变值
# del dict1["englist"]  # 删除
# del dict1  # 删除
# print(dict1)
str = "runoob.com"
# print(str.isalnum()) # 判断所有字符都是数字或者字母
# print(str.isalpha()) # 判断所有字符都是字母
# print(str.isdigit()) # 判断所有字符都是数字
# print(str.islower()) # 判断所有字符都是小写
# print(str.isupper()) # 判断所有字符都是大写
# print(str.istitle()) # 判断所有单词都是首字母大写，像标题
# print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r

def cap(rem):
    test = []
    for item in rem:
        # test.append(item)
        test.append(item.capitalize())  # 首字符大写的方法
        test.append(item.center(10, '-'))  # 填充字符的方法
    return test


def findtes(rem, listtxt):
    num = listtxt.find(rem) # 检测字符串中是否包含子字符串 str ，不包括 返回-1
    return num


if __name__ == '__main__':
    # print(sum_number(2, 3))
    print(cap(list1))
    print(findtes("u", str1))
