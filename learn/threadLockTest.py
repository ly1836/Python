import threading
import time

def print_time(name,counter,delay):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (name, time.ctime(time.time())))
        counter -= 1

class myThread(threading.Thread):

    def __init__(self,threadId,threadName,counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.threadName = threadName
        self.counter = counter

    def run(self):
        print("开始线程:"+self.threadName)

        #线程加锁
        threadLock.acquire()
        print_time(self.threadName,self.counter,2)
        # 释放锁，开启下一个线程
        threadLock.release()

        pass

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 3)
thread2 = myThread(2, "Thread-2", 3)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")