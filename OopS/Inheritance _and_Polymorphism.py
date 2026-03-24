class Vehicle:
    def start_engine(self):
        return "Starting generic vehicle engine...\n"

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started with a key or button.\n"

class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started with a kick or self-start.\n"

v = Vehicle()
c = Car()
b = Bike()

print(v.start_engine())   # generic
print(c.start_engine())   # overridden
print(b.start_engine())   # overridden


#2
class Vehicle():
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def get_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color
    
    def display_car_info(self):
        self.get_info()
        print(f"Color: {self.color}")

obj = car ("Maruti Suzuki","Swift", "Navy Blue")
obj.display_car_info()
print("\n")

#3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


p = Person("Alice", 30)
print(p)   # calls __str__()
print("\n")

#4
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area().")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

rect = Rectangle(4, 5)
circle = Circle(3)

print("Rectangle area:", rect.area())
print("Circle area:", circle.area())



        