from abc import ABC, abstractmethod
from typing import override

class Pet(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Pet):
    @override
    def make_sound(self):
        return f"🐶 {self.name} goes Woof-Woof!"


class Cat(Pet):
    @override
    def make_sound(self):
        return f"🐱 {self.name} goes Meow-Meow!"


class Bird(Pet):
    @override
    def make_sound(self):
        return f"🐦 {self.name} goes Cheep-Cheep!"

class PetFactory:
    @classmethod
    def choose_pet(cls, pet_type, pet_name):
        pets = {
            "dog":Dog,
            "cat":Cat,
            "bird":Bird
        }
        pet_type = pet_type.lower()

        if pet_type not in pets:
            print("❌ No such pet exists!")
            return None
        return pets[pet_type](pet_name.capitalize())

pet_type = input("Please choose a pet (Dog, Cat, Bird)")
pet_name = input("Please choose a name for your pet")

pet = PetFactory.choose_pet(pet_type,pet_name)

if pet:
    print(pet.make_sound())

