from multiprocessing import Process
import os


def run_proc(name, test):
    print('I am a child process, my name is %s my test value is %d and my pid = %d' % (name, test, os.getpid()))


if __name__ == '__main__':
    print('parent process %d' % os.getpid())
    p = Process(target=run_proc, args=('first process', 100))
    p.start()
    p.join()
    print('oh my child process id run finish')
