import _thread
import threading
import time

exitFlag = 0


# 为线程定义一个函数
def print_now_time(thred_name, delay):
    count = 0

    while count < 10:
        time.sleep(delay)
        count += 1
        print("%s %s" % (thred_name, time.ctime(time.time())))


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter
        pass

    def run(self):

        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)
        pass


if __name__ == "__main__":
    # _thread.start_new_thread(print_now_time, ("Thred-1", 2))
    # _thread.start_new_thread(print_now_time, ("Thred-2", 6))
    # while 1:
    #    pass
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
