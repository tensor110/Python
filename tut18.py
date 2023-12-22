# enumerate function 

marks=[12,34,45,67,82,94,54,26]
# index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("Awesome!!")
#     index+=1

# We can write the same program by using enumerate function like this
for index, mark in enumerate(marks):
    print(index, mark)

for index, mark in enumerate(marks, start=1):
    print(index, mark)
