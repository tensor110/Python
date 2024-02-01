from time import *
import random as r
import time

# For counting no. of errors
def mistakes(partest,input):
    error = 0
    for i in range(len(partest)):
        if(partest[i]!=input[i]):
            error = error+1
    return error

# For calculating speed 
def speed(start, end, user_input):
    sp = len(user_input)/(end-start)
    return round(sp, 2)

test = ["It was a weird concept", "The thing that's great",
"Hopes and dreams were dashed","She was infatuated with color"]
test1 = r.choice(test)
print(test1)
start_time = time.time()

# User Input 
ans = input()
mistakes(test1, ans)
end_time = time.time()
print("Speed :", speed(start_time, end_time, ans), "words/sec")
print("Error :", mistakes(test1, ans))