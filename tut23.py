# Local and Global Variable  

x=10  # Global Variable
def  function():
    # To access global variable
    global x
    x=5 # x value is changed from 10 to 5
    y=7 # Local Variale
function()
print(x) # 5 will be printed as the value is changed
# print(y) # error occur as y is a local variable