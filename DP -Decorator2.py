class Pizza:
    def cost(self):
        return 20

class PizzaDecorator:
    def __init__(self,pizza):
        self.pizza = pizza

    def cost(self):
        return self.pizza.cost()

class PizzaExtraCheese(PizzaDecorator):
    def cost(self):
        return super().cost() + 3

class PizzaOlives(PizzaDecorator):
    def cost(self):
        return super().cost() + 2

class PizzaMushrooms(PizzaDecorator):
    def cost(self):
        return super().cost() + 2

class PizzaOnion(PizzaDecorator):
    def cost(self):
        return super().cost() + 2

pizza = Pizza()
extra_cheese = PizzaExtraCheese(pizza)
olives = PizzaOlives(pizza)
mushrooms = PizzaMushrooms(pizza)
onion = PizzaOnion(pizza)

print(f"Regular Pizza: {pizza.cost()}₪")
print(f"Pizza with Extra Cheese: {extra_cheese.cost()}₪")
print(f"Two Pizzas with Extra Cheese: {extra_cheese.cost()*2}₪ ")

double_extra_cheese = PizzaExtraCheese(extra_cheese)
print(f"Pizza with Double Extra Cheese: {double_extra_cheese.cost()}₪ ")

pizza_all = PizzaExtraCheese(PizzaOnion(PizzaMushrooms(PizzaOlives(pizza))))

print(f"Our special ALL-IN pizza-pie: {pizza_all.cost()}₪")

print("+++++++++++++++++++++++++++++++")

pizza = Pizza()
olives = PizzaOlives(pizza)
onion = PizzaOnion(olives)
mushrooms = PizzaMushrooms(onion)
extra_cheese = PizzaExtraCheese(mushrooms)

print(f"Pizza with all: {extra_cheese.cost()}")