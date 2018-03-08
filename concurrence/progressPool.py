import os, time, random
from multiprocessing import Pool


def long_time_task(name):
    print('run task %d id = (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %.2f second' % (name, end - start))


if __name__ == '__main__':
    print("Parent Process is ", os.getpid())
    p = Pool()
    for i in range(9):
        p.apply_async(long_time_task, args=(i,))

    print("wait for subprocess down")
    p.close()
    p.join()
    print('All subprocess done.')


