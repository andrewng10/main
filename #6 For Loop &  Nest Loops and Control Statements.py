import time
 # for loop: a statement that will execute it's blovk of code a limited amount of times
        #while loop = unlimited
        #for loop = limited

#for i in range (10):
    #print(i+1)

#for i in range (1, 100, 2):
    #print(i+1)

#for i in "Andrew Ng":
    #print(i)

#for seconds in range (10, 0,-1):
    #print(seconds)
    #time.sleep(1)
#print("Happy New Years!")

#----------------------------------------------------------------------------------------------------------------------
 # nested loops = the "inner loop" will finish all of it's iterationms before finisfhing one iteration of the "outer loop"

#rows= int(input("How many rows?: "))
#columns = int(input("How many columns?: "))
#symbol = input("Enter a symbol to use: ")

#or i in range(rows):
    #for j in range(columns):
        #print(symbol, end="")
    #print()

#-----------------------------------------------------------------------------------------------------------------------
 # Loop Control Statements = chnage a loops execution from its normal sequence
    #break = used to terimate the loop entirely
    #continue = skips the next iteration of the loop
    #pass = does nothing, acts as a placeholder

#while True:
    #name = input("Enter your name: ")
    #if name != "":
        #break

#phone_number = "123-456-7890"

#for i in phone_number:
    #if i == "-":
        #continue
    #print(i, end="")

#for i in range(1,21):
    #if i == 13:     #if you wanted to skip the number 13
        #pass
    #else:
        #print(i)