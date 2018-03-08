import os
import random
import time
from multiprocessing import Queue, Process


def write(q):
    print("Progress %d to write..." % os.getpid())
    for value in ['A', 'B', 'C', 'D']:
        q.put(value)
        print("put %s to Queue" % value)
        time.sleep(random.random())


def read(q):
    print('Progress %d to read...' % os.getpid())
    while True:
        value = q.get(True)
        print('get %s is from queue.' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
    print("Write and Read Child Process is finish")
