# keyword arugments = arugments preceded by an identifier when we pass them to a function
#   The order of the arguments doesn't matter, unlike positional arguments. Python knows the names of the arguments
#   that our function recieves

#def hello(first,middle,last):
    #print("Hello "+first+" "+middle+" "+last)


#hello(last="Ng",middle="awesome",first="Andrew")

#-----------------------------------------------------------------------------------------------------------------------

# nested functions calls = functions calls inside other function calls. Innermost function calls are resolved first,
# returned value is used as argument for the next outer function

num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))  #Same as the function above but in less lines of code