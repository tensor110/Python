# String methods 

# Strings are immutable
a="!!!Lucky!!!!  !!!  Lucky!!!"
print(a)
print(len(a))
print(a.upper())
print(a.lower())
print(a.count("Lucky"))
print(a.rstrip("!"))
print(a.replace("Lucky","Harry"))
print(a.split(" ")) # split when " "(space) is found

heading="Welcome tO PyThon proGraMMing"
print(heading.capitalize())
print(len(heading))
print(heading.center(50))
print(len(heading.center(50)))
print(heading.startswith("Welcome"))
print(heading.endswith("ing"))
print(heading.endswith("tO",4,10))

str="He's name is Luck. He is a good boy"
print(str.find("is"))
print(str.index("is"))
print(str.find("issh"))

str1="Heisagood2boy"
print(str1.isalnum())
print(str1.isalpha())

str2="  welcome  "
print(str2.islower())
print(str2.isspace())

str3=("Hello\nI am Lucky")
print(str3.isprintable())

str4="World Health Organisation"
str5="world health organisAtion"
print(str4.istitle())
print(str5.title())

str6= "Python is a Interpreted Language"
print(str6.swapcase())