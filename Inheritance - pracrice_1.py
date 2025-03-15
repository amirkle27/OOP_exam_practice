from abc import ABC, abstractmethod
from typing import override
from tkinter import PanedWindow


class Vehicle(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    @abstractmethod
    def describe(self):
        pass

    def make_sound(self):
        print("Vroom!")

class Car(Vehicle):
    def __init__(self, brand, year, fuel):
        super().__init__(brand, year)
        self.fuel = fuel

    @override
    def describe(self):
        return f"{self.brand}, {self.year}, {self.fuel}"

    def fuel_type(self):
        return f"{self.brand} uses {self.fuel}"

    def make_sound(self):
        super().make_sound()
        print ("Beep Beep!")

class Truck(Vehicle):
    def __init__(self, brand, year, load):
        super().__init__(brand, year)
        self.load = load

    @override
    def describe(self):
        return f"{self.brand}, {self.year}, {self.load}kg"

    def max_load(self):
        return f"{self.brand} has a max load of {self.load}kg"

    def make_sound(self):
        super().make_sound()
        print ("Honk Honk!")


car1 = Car("Toyota Camry",2024, "Gasoline" )
car2 = Car("Tesla Model 3", 2023, "Electric")
car3 = Car("Honda Accord Hybrid", 2024, "Hybrid")


truck1 = Truck("Ford F-150", 2024, 1503)
truck2 = Truck("Chevrolet Silverado 2500HD", 2023, 1769)
truck3 = Truck("Ram 3500", 2024, 1485)

print(car1.describe())
print(car2.describe())
print(car3.describe())

print(truck1.describe())
print(truck2.describe())
print(truck3.describe())

car1.make_sound()
truck1.make_sound()
print(car1.fuel_type())
print(truck1.max_load())

car1.make_sound()
truck1.make_sound()