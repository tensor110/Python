# Decorators 
def greet(fn):
    def mod_fn(*args,**kwargs):
        print("Hello")
        fn(*args,**kwargs)
        print("Thanks for using this function")
    return mod_fn

# @greet
# def hello():
#     print("Hello World")
# hello()

# or 

# greet(hello)()



@greet
def add(a, b):
    print(a + b)
add(1,2)

# or 

# greet(add)(1,2)