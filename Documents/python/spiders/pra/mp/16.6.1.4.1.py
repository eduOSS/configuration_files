from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

def f0(n, a):
    n.value = 3.1415927
    for i in range(9):
        a[i] = i

if __name__ == '__main__':
    num = Value('d', 0.0)#d indicates a double precision float
    arr = Array('i', range(10))#i indicates a signed integer
    #print num, arr
    num0 = Value('d', 0.0)#8
    arr0 = []

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()
    p0 = Process(target=f0, args=(num0, arr0))
    p0.start()
    p0.join()

    print num.value
    print arr[:]
    print num0.value
    print arr0
