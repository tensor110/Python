# if __name__=="__main__"

def welcome():
    print("Hey you are welcome")

print(__name__)

# if __name__=="__main__" is used to determine whether the script is being run directly or being imported as a module into another script
if __name__=="__main__":
    welcome()