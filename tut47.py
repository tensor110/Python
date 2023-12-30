# The Walrus Operator
# The Walrus operator(:=) gives us a new syntax for assigning variables in the middle of expressions.

a = True
print(a)
# Using Walrus Operator
print(a := False)

numbers= [1, 2, 3, 4, 5]
while(n := len(numbers))>0:
    print(numbers.pop())
