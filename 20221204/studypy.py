list1 = ['sty', 'school']
numbers1 = len(list1)  # 计算列表元素个数
numbers2 = list1[0]  # 返回第0个元素
list1.append('red')  # 在尾部添加一个元素
list1.extend(['blue', 'yellow'])  # 在尾部添加多个元素
list1.insert(1, 'blue')  # 在1的位置插入元素 blue
list1.remove('blue') #删除列表中的第一个为blue的元素
list1.pop(0) #删除第0个元素

list1.clear() #清空列表
print(numbers1, numbers2)
print(list1)

