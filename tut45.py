# # Time Module 
import time
def fortime():
    for i in range(5000):
        i = i+1
        print(i)
def whiletime():
    i = 0
    while i<5000:
        i = i+1
        print(i)
# Measure time for fortime
init = time.time()
fortime()
print("Time taken by fortime:", time.time() - init)

# Measure time for whiletime
init = time.time()
whiletime()
print("Time taken by whiletime:", time.time() - init)

# time.sleep()- Delay execution time of programs
print(1)
time.sleep(3)   # 3 second of delay
print(2)

# strftime() function is used to convert date and time objects to their string representation
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)