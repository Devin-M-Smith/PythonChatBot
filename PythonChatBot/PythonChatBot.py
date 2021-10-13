from wordHandler import fixIt
from time import sleep
import sys
def prnt(x):              #Alternative Print method for single line printing
    sys.stdout.write(x)
    sys.stdout.flush()

def central():              #Main Function
    x = ""
    while x != "shutdown":          #Loop for user interaction
        x = input("You: ")          #Get text input
        x = fixIt(x)                #Scrub input of punctuation and make lowercase
        print("You said: " + x)

    
        


print("Welcome to PyChat! \nPlease see Readme.md for important updates and features. \nHello!") #Welcome Message

central() #Call Main Function


prnt("Shutting Down")   #Shutdown Message
sleep(.5)
prnt(".")
sleep(.5)
prnt(".")
sleep(.5)
prnt(".")
sleep(.5)
