import threading
import time

# exitFlag = 0
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, delay):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.delay = delay
#     def run(self):
#         print ("开始线程：" + self.name)
#         print_time(self.name, self.delay, 5)
#         print ("退出线程：" + self.name)
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()  # 等他结束
# thread2.join()  # 等他结束
# print ("退出主线程")
class myThread (threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.delay, 3)
        # 释放锁，开启下一个线程
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-3", 3)

# 开启新线程
thread1.start()
thread2.start()
thread3.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)


# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")