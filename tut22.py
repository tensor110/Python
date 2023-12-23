# os Module 

# The os module in Python is a built-in library that provides functions for interacting with the operating system. It allows you to perform a wide variety Of tasks, such as reading and writing files, interacting with the file system, and running system commands.

import os

# To make a directory
# if(not os.path.exists("data")):
#     os.mkdir("data")

# To make many folders inside a directory 
# for i in range(0,100):
#     os.mkdir(f"data/Day{i+1}")

# To rename the folders 
# for i in range(0,100):
#     os.reneme(f"data/Day{i+1}", f"data/Tutorial{i+1}")

# To print the folders inside a directory 
# folders= os.listdir('data')
# print(folders)
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))

# To know the present directory 
# print(os.getcwd())
# os.chdir("/")
# print(os.getcwd())

# To remove a file 
# os.remove("data/Day10/read.md")

# To remove an empty directory
# os.rmdir("data/Day1")