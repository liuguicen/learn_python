import threading

global_local = threading.local()


def process_student():
    print('hello, %s (in %s)' % (global_local.student, threading.current_thread().name))


def process_thread(name):
    global_local.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name="Thread-1")
t2 = threading.Thread(target=process_thread, args=('Bob',), name="Thread-2")
t1.start()
t2.start()
print(global_local.student)
