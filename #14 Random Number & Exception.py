#import random

#x = random.randint(1,6)
#y = random.random()

#yList = ['rock','paper','scissors']
#z = random.choice(myList)

#suites = ["Hearts", "Spades", "Diamonds", "Clubs"]
#card_number = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

#s = random.choice(card_number)
#c = random.choice(suites)

#print(s,c)

#----------------------------------------------------------------------------------------------------------------------

#exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide:"))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("Enter only numbers please")
except Exception as e:
    print(e)
    print("Something Went Wrong :(")
else:
    print(result)
finally:
    print("This will always execute")