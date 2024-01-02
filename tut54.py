# Multithreading

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping for {seconds}seconds")
    time.sleep(seconds)

# Normal Case 
timei = time.perf_counter()
func(4)
func(2)
func(1)
timef = time.perf_counter()
print(timei- timef)

# Using Multithreading 
timei = time.perf_counter()
t1 = threading.Thread(target= func, args=[4])
t2 = threading.Thread(target= func, args=[2])
t3 = threading.Thread(target= func, args=[1])
t1.start()  # Starting t1
t2.start()
t3.start()

t1.join()  #Waiting for t1 to finish
t2.join()
t3.join()
timef = time.perf_counter()
print(timei- timef)

# Using ThreadPoolExecutor 
def poolingDemo():
    with ThreadPoolExecutor() as executer:
        fut1 = executer.submit(func, 4)
        fut2 = executer.submit(func, 2)
        fut3 = executer.submit(func, 1)
        print(fut1.result())
        print(fut2.result())
        print(fut3.result())

        l = [4,2,1]
        res = executer.map(func, l)
        for result in res:
            print(result)
            
poolingDemo()