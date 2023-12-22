# Exception Handling, finally keyword and Raising Custom Errors
try:
    a=int(input("Enter the number: "))
    print(f"Multiplication Table aof {a} is: ")
    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")
except:
    print("Some error occured")


try:
    num=int(input("Enter a number: "))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error")
finally:
    print("I am always executed")
print("I am always executed")
# Difference b/w finally and above statement
def func1():
    try:
        l=[1,5,6,7]
        i=int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("Function ends here")
    # print("Function ends here") # Here this statement is not executed but finally statement is executed


# Raising custom errors
a= int(input("Enter any value between 5 and 9"))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 0")