# scope = The region that a variable is recognized, A variable is only avaliable from inside the region it is created. A
#   global and locally scoped versions of a variable can be created.

#name = "Andrew" #global scope (avaiable inside & outside functions)

#ef display_name():
   # name = "Andrew"         #local scope (avaibale only inside this function)
    #print(name)

#display_name()
#(name)

#-----------------------------------------------------------------------------------------------------------------------
# *args = parameter that will pack all arguments into a tuple useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    args = list(args)
    args[0]=0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))