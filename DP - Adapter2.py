class OldFormat:
    def get_car_details(self):
        return {"brand":"Toyota", "year": 2022}

class NewFormat:
    def get_car_details(self,brand,year):
        print(f"brand: [{brand}], year: [{year}]")

class CarAdapter:
    def __init__(self,old_system):
        self.old_system = old_system

    def get_adapted_data(self):
        data = self.old_system.get_car_details()
        return data["brand"], data["year"]

old_system = OldFormat()
adapter = CarAdapter(old_system)
new_system = NewFormat()

brand, year = adapter.get_adapted_data()
new_system.get_car_details(brand,year)