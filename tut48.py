# Shutil Module 
# The shutil module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal.

import shutil
# shutil.copy(src, dst) -> The function copies the file located at src to a new location specified by dst.
# shutil.copy("tut48.py", "tut48copy.py")

# shutil.copytree(src, dst) -> This function recursively copies the directory located at src to a new location specified by dst.
# shutil.copytree("Python", "Python Tutorial")

# shutil.move(src, dst) -> This function moves the file located at src to a new location specified by dst.
# shutil.move("Python/tut1.py", "Python/data/tut1.py")

# shutil.rmtree(path) -> This function recursivelhy deletes the diectory docated at path along with all of its contents.
# shutil.rmtree("Python")