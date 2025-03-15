from abc import ABC, abstractmethod
from typing import override

class Vehicle(ABC):
    def __init__(self, name, type):
        self.type = type
        self.name = name

    @abstractmethod
    def describe(self):
        pass

class Truck(Vehicle):
    @override
    def describe(self):
        return f"This is a {self.type} Truck"

class Motorcycle(Vehicle):
    @override
    def describe(self):
        return f"This is a {self.type} Motorcycle"

class Car(Vehicle):
    @override
    def describe(self):
        return f"This is a {self.type} Car"

class VehicleFactory:
    @classmethod
    def choose_vehicle(cls, vehicle_name, vehicle_type):
        vehicles = {
            "car":Car,
            "motorcycle": Motorcycle,
            "truck": Truck
        }

        vehicle_name = vehicle_name.lower()
        if vehicle_name not in vehicles:
            return None

        return vehicles[vehicle_name](vehicle_name.capitalize(), vehicle_type)


vehicle_name = input("Please Choose a vehicle name: (Car, Motorcycle, Truck): ")
vehicle_type = input("Enter the type of your vehicle: ")

vehicle = VehicleFactory.choose_vehicle(vehicle_name, vehicle_type)

if vehicle:
    print(vehicle.describe())
else:
    print("❌ No such vehicle exists!")


