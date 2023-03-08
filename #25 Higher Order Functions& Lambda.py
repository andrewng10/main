# Higher Order Function = a function that either:
#           1. accpets a function as an arguyment
#                   or
#           2. returns a function
#                  (In python, function are also treated as objects)

#Definition #1
#def loud(text):
    #return text.upper()

#def quiet(text):
    #return text.lower()

#def hello(func):
    #text = func("Hello")
    #print(text)

#hello(loud)
#hello(quiet)


#Definition #2

#def divisor(x):
    #def dividend(y):
        #return y / x
    #return dividend

#divide = divisor(2)
#print(divide(10))

#-----------------------------------------------------------------------------------------------------------------------

#lambda function = function writrten in 1 line using lambda keyword accepts any number of arguments, but only has one
# expression. (think of it as a shortcut) (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

#def double (x)
    #return x * 2

#print(double(5))

double = lambda x:x *2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name +" "+last_name
age_check = lambda age:True if age >= 18 else False
print(age_check(19))