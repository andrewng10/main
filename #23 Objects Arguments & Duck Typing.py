#class Car:

    #color = None
# Motorcycle:

    #color = None

#def change_color(vehicle,color):

    #vehicle.color = color

#car_1 = Car()
#car_2 = Car()
#car_3 = Car()

#bike_1 = Motorcycle()

#change_color(car_1, "red")
#change_color(car_2, "white")
#change_color(car_3, "blue")
#change_color(bike_1,"black")

#print(car_1.color)
#print(car_2.color)
#print(car_3.color)
#print(bike_1.color)

#-----------------------------------------------------------------------------------------------------------------------

# Duck Typing = concept where the class of an object is less important than the methods/attributes class type is not
#checked if minimum methods/attributes are present

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)