# super() = function used to give access to the methods of a parent class.
# Returns a temporary object of a parent class when used


#class Rectangle:

    #def __init__(self, length, width):
        #self.length = length
        #self.width = width

#class Square(Rectangle):

    #def __init__(self, length, width):
        #super().__init__(length,width)

    #def area(self):
        #return self.length*self.width


#class Cube(Rectangle):

    #def __init__(self, length, width, height):
        #super().__init__(length,width)
        #self.height = height

    #def volume(self):
        #return self.length*self.width*self.height

#square = Square(3, 3)
#cube = Cube(3, 3, 3)

#print(square.area())
#print(cube.volume())

#-----------------------------------------------------------------------------------------------------------------------

#Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but does not have an implmentation.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    def stop(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()