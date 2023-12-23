# seek(), tell() and truncate() function

# The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes
with open('tut26a.txt', 'r') as f:
    print(type(f))
    f.seek(10)  # Move to the 10th byte in the file
    data= f.read(5)  # Read the next 5 bytes
    print(data)

# The te11() function returns the current position within the file in bytes
with open('tut26a.txt', 'r') as f:
    data= f.read(10)  # Read the first  10 bytes
    current_pos= f.tell()  # Save the current position
    print(current_pos)

# The treucate() function returns the values from 1st to that position
with open('tut26b.txt', 'w') as f:
    f.write("Hello World")
    f.truncate(5)  # Returns values from 1st to 5th position
with open('tut26b.txt', 'r') as f:
    print(f.read())