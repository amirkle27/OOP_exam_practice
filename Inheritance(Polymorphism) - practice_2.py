from abc import ABC, abstractmethod
from typing import override

class Vehicle(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def describe(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, year, gasoline, colour):
        super().__init__(brand, year)
        self.gasoline = gasoline
        self.colour = colour

    @override
    def make_sound(self):
        print(f"{self.brand} goes Vroom Vroom!")

    @override
    def describe(self):
        print(f"{self.brand} was manufactured in {self.year}. Uses {self.gasoline}. Beautiful {self.colour}")

class Truck(Vehicle):
    def __init__(self, brand, year, max_load, height):
        super().__init__(brand, year)
        self.max_load = max_load
        self.height = height

    @override
    def make_sound(self):
        print(f"{self.brand} goes Bang Chuck Bam!")

    @override
    def describe(self):
        print(f"{self.brand} was manufactured in {self.year}. It has a max load of {self.max_load} and is {self.height}m in height")


car1 = Car("Toyota Camry",2024, "Gasoline", "Red" )
car2 = Car("Tesla Model 3", 2023, "Electric", "Shiny Blue")
car3 = Car("Honda Accord Hybrid", 2024, "Hybrid", "Bottle Green")


truck1 = Truck("Ford F-150", 2024, 1503, 4.5)
truck2 = Truck("Chevrolet Silverado 2500HD", 2023, 1769, 5)
truck3 = Truck("Ram 3500", 2024, 1485, 5.2)

vehicles = [car1,car2,car3,truck1,truck2,truck3]

for vehicle in vehicles:
    vehicle.describe()
    print()
    vehicle.make_sound()
    print("-"*40)
