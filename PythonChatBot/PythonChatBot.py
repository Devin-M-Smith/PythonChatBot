from wordHandler import fixIt
from time import sleep
def central():
    x = ""
    while x != "shutdown":
        x = input("You: ")
        x = fixIt(x)
        print("You said: " + x)

    print("Shutting down")
        


print("Welcome to PyChat! \nPlease see Readme.md for important updates and features. \nHello!")
central()
