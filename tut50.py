# Generators 

# A Python generator function allows you to declare a function that behaves like an iterator, providing a faster and easier way to create iterators. 
# They can be used on an abstract container of data to turn it into an iterable object like lists, dictionaries and strings.

def my_generator():
    for i in range(5):
        yield i
gen = my_generator()
print(list(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for j in gen:
#     print(j)