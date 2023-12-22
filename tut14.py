# f-strings and Docstrings

letter= "Hey my name is {} and I am from {}"
letter1= "Hey my name is {1} and I am from {0}"
name="Lucky"
country="India"
print(letter.format(name,country))
print(letter1.format(country,name))

print(f"Hey my name is {name} and I am from {country}")
# to print the f-string format
print(f"Hey my name is {{name}} and I am from {{country}}")
price=49.987654321
txt= f"The price of this is {price:.2f} dollars"
print(txt)
print(f"{2*35}")
print(type(f"{2*35}"))

# Docstring -> The comment like string just after a function declaration
def square(n):
    '''Takes a number n,returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)