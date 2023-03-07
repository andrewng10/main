#Write a file


#text = "Yoooooo\nThis is some text\nHave a good one!\n"

#with open('Write_a_File.txt','w') as file:  #"w" is a print once statement, and "a" prints as many times as you summon
   #file.write(text)

#-----------------------------------------------------------------------------------------------------------------------
#Copy a file
    # copyfile() = copies contents of a file
    # copy() = copyfile() + permission mode + destination can be a directory
    # copy2() = copy() + copies metadate (file's creation and modification times)

#import shutil

#shutil.copyfile('test.txt','copy.txt')# source and destinaton       # copies 'test.txt' into a new file

#-----------------------------------------------------------------------------------------------------------------------
import os

#source = "test.text"
#destination = "C:\\Users\\andre\\OneDrive"

#try:
    #if os.path.exists(destination):
        #print("There is already a file there")
    #else:
        #os.replace(source,destination)
    #print(source+" was moved")
#except FileNotFoundError:
    #print(source+" was not found")
#----------------------------------------------------------------------------------------------------------------------
import os

path = "text.txt"
try:
    #os.remove(path)        #delete a file
    #os.rmdir(path)         #delete an empty directory
    #shutil.rmtree(path)    #delete a directory containing files
    os.remove('test.txt')
except FileNotFoundError
    print("The file was not found")
except PermissionError
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")
