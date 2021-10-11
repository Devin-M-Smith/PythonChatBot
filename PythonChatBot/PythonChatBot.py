def central():
    
    x = input("Hello \nYou: ")
    while x.lower() != "shutdown":
        print("You said: " + x)
        x = input("You: ")


print("Welcome to PyChat! \nPlease see Readme.md for important updates and features.")
central()
