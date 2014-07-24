from multiprocessing import Process, Pipe
import os

def f0(iconn):
    iconn.send([os.getpid(), None, 'ihello'])
    iconn.close()

def f(iconn):
    iconn.send([os.getpid(), None, 'f1hello'])
    iconn.send([os.getpid(), None, 'f2hello'])
    f0(iconn)

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()#here parent and child much be assigned at the same time
    iparent_conn, ichild_conn = Pipe()#here parent and child much be assigned at the same time
    p = Process(target=f, args=(child_conn,))
    ip = Process(target=f, args=(ichild_conn,))
    p.start() #who start first whose pid is smaller
    ip.start()
    print parent_conn.recv(),parent_conn.recv(), parent_conn.recv(),'\n' # prints "[42, None, 'hello']" FIFO
    print iparent_conn.recv(),iparent_conn.recv(), iparent_conn.recv(),'i\n' # prints "[42, None, 'hello']" FIFO
    p.join()
    ip.join()
