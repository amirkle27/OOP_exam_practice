class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"Woof! I am {self.name} and I am a {self.breed}")

dog1 = Dog("Rexy", "Labrador")
dog2 = Dog("Lily", "Chihuahua")
dog3 = Dog("Meshukam", "Golden Retriever")

dog1.bark()
dog2.bark()
dog3.bark()