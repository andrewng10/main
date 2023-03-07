#import os

#path = "C:\\Users\\andre\\OneDrive\\Desktop\\test.txt"

#if os.path.exists(path):
    #print("That location exists!")
    #if os.path.isfile(path):
        #print("That is a file")
    #elif os.path.isdir(path):
        #print("That is a directory!")   #Or a folder
#else:
    #print("That location doesn't exist!")

#-----------------------------------------------------------------------------------------------------------------------
try:
    with open('text.txt') as file:  #"with open" command closes for file afterwards
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
