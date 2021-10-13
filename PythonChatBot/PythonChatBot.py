import wordHandler as wh
def central():
    
    x = input("Hello \nYou: ")
    x = wh.fixIt(x)
    while x != "shutdown":
        print("You said: " + x)
        x = input("You: ")
        x = wh.fixIt(x)


print("Welcome to PyChat! \nPlease see Readme.md for important updates and features.")
central()
