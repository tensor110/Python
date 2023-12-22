# Dictionary and Dictionary Methods
info={'name':'Lucky', 'age':21, 'eligible':True}
print(info)
print(info.items())
print(info['name'])
print(info.get('name'))
# print(info['name2'])  #It will throw error
# print(info.get('name2'))  #But it don't throw error and gine None
print(info.keys())
print(info.values())
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")
for key,value in info.items():
    print(f"The value corresponding to the key {key} is {value}")


dict1={122:45, 123:89, 567:69}
dict2={124:76, 568:95}
# dict1.update(dict2)
# dict1.clear()
# dict1.pop(122)
dict1.popitem()
del dict2
# print(dic2)  #Throws error b/c dict2 is deleted
del dict1[122]
print(dict1)