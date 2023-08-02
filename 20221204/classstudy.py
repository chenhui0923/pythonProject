class people():
    name: ''
    age = 0
    height = 0
    __weight = 0 # 私有方法

    # 定义个构造方法
    def __init__(self, n, a, h):
        self.name = n
        self.age = a
        self.height = h

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))
        print("{n} 说：我{a}岁，我有{h}M高".format(n=self.name, a=self.age, h=self.height))


# 单继承的方式
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
        # super().speak() # 子类调用父类的方法

class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多继承的方式
class sample(speaker, student):
    zone = ''

    def __init__(self, n, a, w, g, t, z):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)
        self.zone = z

if __name__ == '__main__':
    p = people('runoob', 10, 1.7)
    p.speak()
    st = student("Tim", 25, 80, 4)
    st.speak()
    test = sample("Tim", 25, 80, 4, "Python", "java")
    test.speak() #方法名同，默认调用的是class类在括号中参数位置排前父类的方法
    # super(student,st).speak() # 写法super(子类，子类的申明)，父类的方法 ， 用子类对象调用父类已被覆盖的方法