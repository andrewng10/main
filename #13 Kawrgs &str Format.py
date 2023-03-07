# **kwargs = parameter that will pack all arguments into a dictionary
#             useful so that a function can accept a varying amount og keyword argument


#def hello (**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    #print("Hello",end=" ")
    #for key,value in kwargs.items():
        #print(value,end=" ")


#hello(title="Mr.",first="Andrew",middle="Awesome",last="Ng")

#----------------------------------------------------------------------------------------------------------------------

# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

#print("The "+animal+" jumped over the "+item)
#print("The {} jumped over the {}".format("cow","moon")) #same output as line above just written more elegantly
#print("The {0} jumped over the {1}".format("cow","moon")) #positional argument (indexing position)
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))   #keyword argument

#text = "The {} jumped over the {}"
#print(text.format(animal,item))


name = "Andrew"

#print("Hello, my name is {}".format(name))
#print("Hello, my name is {:10}. Nice to meet you".format(name))     #You can preced the ":" with postional or keyword arguments
#print("Hello, my name is {:<10}. Nice to meet you".format(name))    #Left Align
#print("Hello, my name is {:>10}. Nice to meet you".format(name))    #Right Align
#print("Hello, my name is {:^10}. Nice to meet you".format(name))    #Center Align

number1 = 3.14159

print("The number pi is {:.2f}".format(number1))     #printing to how many digits shown

number2 = 1000
print("The number is {:,}".format(number2))
print("The number is {:b}".format(number2))
print("The number is {:o}".format(number2))
print("The number is {:X}".format(number2))
print("The number is {:E}".format(number2))