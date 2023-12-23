# File IO 

# Different Modes 
# 1. read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
# 2. write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
# 3. append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
# 4. create (x): This mode creates a file and gives an error if the file already exists.
# 5. text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text. synonym of •rt' ).
# 6. binary (b): used to handle binary files (images. pdfs, etc).

# 1. To read a file
f= open('tut24.txt', 'r')
print(f)
text= f.read()
print(text)

# 2. To write in a file
f= open('tut24.txt', 'w')
f.write("Hello")
f.close()

# 3. To append in a file
f= open('tut24.txt', 'a')
f.write("Hello good morning")
f.close()

# 4. To create a file
# f= open('tut24c.txt', 'x')

# The 'with' statement 
with open('tut24.txt','a') as f:
    f.write("Hello hey i am here")