
""" 主进程，分发任务，使用多线程发送任务和接收结果"""

import random, time, queue
from multiprocessing.managers import BaseManager
import threading

# 发送任务的队列:
send_task = queue.Queue()
# 接收结果的队列:
result_task = queue.Queue()


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


def get_send_task():
    return send_task


def get_result_task():
    return result_task


def task_send(number, post):
    # 放几个任务进去:
    print('send thread start')
    for i in range(number):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        time.sleep(1)
        post.put(n)


def task_result(number, result):
    print('results thread start...')
    # 从result队列读取结果:
    for i in range(number):
        r = result.get(timeout=10)
        print('get Result from worker: %s', r)


def start():
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    QueueManager.register('send_task_queue', callable=get_send_task)
    QueueManager.register('result_task_queue', callable=get_result_task)

    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # 启动Queue:
    manager.start()

    # 获得通过网络访问的Queue对象:
    post = manager.send_task_queue()
    result = manager.result_task_queue()

    send_thread = threading.Thread(target=task_send, args=(10, post))
    result_thread = threading.Thread(target=task_result, args=(10, result))
    send_thread.start()
    result_thread.start()
    send_thread.join()
    result_thread.join()
    # 关闭:
    manager.shutdown()
    print('master exit.')


if __name__ == '__main__':
    start()
