'''
event条件变量，只适合单次场景，多次请使用condition
'''
from threading import Event,Thread

# def task(n, event):
#     print('子线程 starting')
#     while n > 0:
#         print('子线程 %d' % (n,))
#         time.sleep(5)
#         n = n - 1
#     event.set()
#
#
# started_event = Event()
# print('main is starting')
# t = Thread(target=task, args=(2, started_event))
# t.start()
# started_event.wait()
# print('main ended')


import threading
import time
from collections import deque
from threading import Lock, Condition


class BlockingQueue(object):
    '''
    使用condition实现一个阻塞队列
    '''

    def __init__(self, size):
        self.__queue = deque()
        self.__size = size
        self.__count = 0
        self.__lock = Lock()
        self.__not_empty = Condition(self.__lock)
        self.__not_full = Condition(self.__lock)

    def offer(self, ele):
        '''
        队列处于不满的状态可以装入
        :param ele:
        :return:
        '''
        acquire = False
        try:
            acquire = self.__not_full.acquire()
            self.__queue.append(ele)
            self.__count += 1
            # 通知，当队列现在处于不空的状态
            self.__not_empty.notify_all()
            # 当队列不满的情况才能添加，否则一直阻塞
            if self.__count > self.__size:
                print('当前队列已满，等待消费')
                self.__not_full.wait()
        except Exception as e:
            print('添加元素失败', e)
        finally:
            if acquire: self.__not_full.release()

    def pop(self):
        '''
        当队列处于不空的状态才可以弹出
        :return:
        '''
        acquire = False
        try:
            acquire = self.__not_empty.acquire()
            ele = self.__queue.pop()
            self.__count -= 1
            # 通知当前队列处于不满的状态
            self.__not_full.notify_all()
            # 当队列处于不空的状态才可以弹出 否则一直阻塞
            if self.__count < 1:
                print('当前元素个位为0')
                self.__not_empty.wait()
            return ele
        except Exception as e:
            print('弹出元素失败', e)
        finally:
            if acquire: self.__not_empty.release()


class Producer(threading.Thread):

    def __init__(self, queue):
        super().__init__(daemon=True)
        self.__queue = queue

    def run(self):
        '''
        每个一秒生产一个消息到队列里面
        :return:
        '''
        while True:
            self.__queue.offer('')
            print('生产一个消息')
            time.sleep(1)


class Consumer(threading.Thread):

    def __init__(self, queue):
        super().__init__(daemon=True)
        self.__queue = queue

    def run(self):
        '''
        每个2秒生产一个消息到队列里面
        :return:
        '''
        while True:
            self.__queue.pop()
            print('消费一个消息')
            time.sleep(2)


queue = BlockingQueue(5)
p = Producer(queue)
c = Consumer(queue)
p.start()
c.start()
time.sleep(20)
print('end')