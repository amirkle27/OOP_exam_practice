class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_cars(self):
        for car in self.cars:
            print(f" Model: {car.brand}, Year: {car.year}")

car1 = Car("Toyota Corolla", 2024)
car2 = Car("Ford Mustang", 2023)
car3 = Car("BMW X5", 2024)
car4 = Car("Honda Civic", 2023)
car5 = Car("Mercedes-Benz C-Class", 2024)

garage = Garage()

garage.add_car(car1)
garage.add_car(car2)
garage.add_car(car3)
garage.add_car(car4)
garage.add_car(car5)

garage.show_cars()

