from multiprocessing import Process, Queue
import os

def f(q):
    q.put([os.getpid(), None, 'hello0'])
    q.put([os.getpid(), None, 'hello1'])
    

if __name__ == '__main__':
    print os.getpid()
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    p.join()
    q0 = Queue()
    p0 = Process(target=f, args=(q0,))
    p0.start()
    p0.join()
    print q.get(), q.get()
    print q0.get()    
