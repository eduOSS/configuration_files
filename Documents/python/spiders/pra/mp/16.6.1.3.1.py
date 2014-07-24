from multiprocessing import Process, Lock
import time

def f(l, i):
    l.acquire()
    for ii in xrange(i):
        print 'hello world', ii
    #time.sleep(0.5)
    l.release()#if there are several processes can use a function, add a lock to make sure it can be only use by one process in a point of time

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
