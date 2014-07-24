from multiprocessing import Process
import os

def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid3'):  # only available on Unix
        print 'parent process3:', os.getppid()
    print 'process id3:', os.getpid(),'\n'

def f(name):
    info('function f')
    print 'hello', name
    print 'p process fid2:', os.getpid()
    if hasattr(os, 'getppid2'):  # only available on Unix
        print 'parent process2:', os.getppid()

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p0 = Process(target=info, args=('title bob',))
    p1 = Process(target=info, args=('title bob title',))#every process has a pid and the main function has a pid.
    p.start()
    p0.start()
    p1.start()
    p1.join()
    p0.join()
    p.join()
    if hasattr(os, 'getppid1'):  # only available on Unix
        print 'parent process1:', os.getppid()
