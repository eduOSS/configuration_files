import multiprocessing, time, signal
p = multiprocessing.Process(target=time.sleep, args=(1000,))
print p, p.is_alive()

p.start()
print p.name, p.is_alive()

p.terminate()
time.sleep(0.1)
print p, p.is_alive()

p.join()
print p, p.is_alive()

p.exitcode == -signal.SIGTERM
print p.exitcode 
