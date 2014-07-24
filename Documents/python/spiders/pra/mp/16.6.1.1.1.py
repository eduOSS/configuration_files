from multiprocessing import Process
import os

def f(name):
    print 'hello f', name
    print os.getppid()
    print os.getpid()

def f1(name):
    print 'hello f1', name
    print os.getppid()
    print os.getpid()

if __name__ == '__main__':
    print os.getppid()
    print os.getpid()
    p = Process(target=f, args=('bbobbobb',))
    p1 = Process(target=f1, args=('bobb',))
    p2 = Process(target=f1, args=('bargsobb',))
    p2.start()
    p1.start()
    p.start()
    p1.join()
    p.join()
    p2.join()
