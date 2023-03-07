#method overriding: when the child class provies the program with specific insturctions under the parents class

#class Animal:

    #def eat(self):
        #print("This animal is eating")

#class Rabbit(Animal):

    #def eat(self):
        #print("This rabbit is eating a carrot")


#rabbit = Rabbit()
#rabbit.eat()

#----------------------------------------------------------------------------------------------------------------------

#method chaining:   calling multiple methos squientially each call performs an action on the same obkect and returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()

car.turn_on()   #single command
car.drive()

car.turn_on().drive()   #chain command (same output) [Requires the "return self" function under each command]

#For long chains, you can seperate them into different lines using a continuation "\"

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()