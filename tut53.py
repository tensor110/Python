# Async IO 

import time
import asyncio

async def function1():
    await asyncio.sleep(3)
    print("func1")
async def function2():
    await asyncio.sleep(2)
    print("func2")
async def function3():
    await asyncio.sleep(1)
    print("func3")

# Method 1 
# async def main1():
#     task = asyncio.create_task(function1())   #When the task is completed it will show 
#     await function2()
#     await function3()
# asyncio.run(main1())

# Method 2
async def main2():
    L = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    print(L)
asyncio.run(main2())