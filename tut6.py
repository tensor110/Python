# string slicing and operations on strings

fruit="Mango"
fruitlen=len(fruit)
print(fruitlen)
print(fruit[0:4])  #Including 0 but not 4
print(fruit[:3])  # Means [0-2]
print(fruit[0:-3])  # same as fruit[:len(fruit)-3]
print(fruit[:len(fruit)-3])
print(fruit[-4:-1])  #same as fruit[len(fruit)-4:len(fruit)-1]``