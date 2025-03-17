from itertools import product


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self):
        return f"{self.name} costs {self.price}$"

class ShoppingCart():
    def __init__(self):
        self.products = []

    def __str__(self):
        product_list = "\n".join(f" -{product}" for product in self.products) or "Cart is Empty"
        return f"\n🛒 Shopping Cart:\n{product_list}"

    def add_product(self, product):
        if isinstance(product,Product):
            self.products.append(product)
            products_list = "\n".join(f" -{product}" for product in self.products)
            print(f"\n✅ Added {product.name} to the shopping cart.\nOur Shopping Cart now contains:\n{products_list}")
        else:
            print("\n❌ Invalid product! You must add a Product object.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            products_list = "\n".join(f" -{product}" for product in self.products) or "Nothing"
            print(f"\n❌We removed {product} from the shopping cart\nOur shopping Cart now contains:\n{products_list}")
        else:
            print(f"We don't have {product} in the cart")


    def get_total_cost(self):
        return sum(product.get_price() for product in self.products)

        #total_cost = 0
        #for product in self.products:
        #    total_cost += product.get_price()
        #return total_cost



apples = Product("Apples", 19.9)
milk = Product("Milk", 15)
rice = Product("Rice", 12)

cart = ShoppingCart()

cart.add_product(milk)
cart.add_product(apples)
cart.add_product(rice)

print()

print(cart)

print(milk.get_price())

print(cart.get_total_cost())