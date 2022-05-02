"""
Threading and Processing
"""

# from threading import Thread, Lock, current_thread
import time
from queue import Queue

#%%

from multiprocessing import Process, Value, Array, Lock
import os
#%%
database_var = 0

def afunction(lock):
    global database_var
    
    with lock:
        local_copy = database_var
        local_copy +=1 
        time.sleep(0.1)
        database_var = local_copy



if __name__ == '__main__':
    # How to thread
    lock = Lock()
    print(database_var)
    thread1 = Thread(target = afunction, args = (lock,))
    thread2 = Thread(target = afunction, args = (lock,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print("end",database_var)
    
    
    
#%%
def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name__ == '__main__':
    q = Queue()
    
    num_thread = 10
    
    lock = Lock()
    
    for i in range(num_thread):
        thread = Thread(target = worker, args = (q, lock))
        thread.daemon = True
        thread.start()
    
    for i in range(1,21):
        q.put(i)
        
    q.join()
    
    print("end main")
    
    
#%%
from multiprocessing import Lock

def add_100(number, lock):
    for _ in range(100):
        time.sleep(0.01)
        # lock the state
        lock.acquire()
        
        number.value += 1
        
        # unlock the state
        lock.release()

def add_100_array(numbers, lock):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            lock.acquire()
            numbers[i] += 1
            lock.release()


if __name__ == "__main__":

    # create a lock
    lock = Lock()
    
    shared_number = Value('i', 0) 
    print('Value at beginning:', shared_number.value)

    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning:', shared_array[:])

    # pass the lock to the target function
    process1 = Process(target=add_100, args=(shared_number, lock))
    process2 = Process(target=add_100, args=(shared_number, lock))

    process3 = Process(target=add_100_array, args=(shared_array, lock))
    process4 = Process(target=add_100_array, args=(shared_array, lock))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print('Value at end:', shared_number.value)
    print('Array at end:', shared_array[:])

    print('end main')


#%%
from multiprocessing import Pool 

def cube(number):
    return number * number * number

    
if __name__ == "__main__":
    numbers = range(10)
    
    p = Pool()

    # by default this allocates the maximum number of available 
    # processors for this task --> os.cpu_count()
    result = p.map(cube,  numbers)
    
    # or 
    # result = [p.apply(cube, args=(i,)) for i in numbers]
    
    p.close()
    p.join()
    
    print(result)
