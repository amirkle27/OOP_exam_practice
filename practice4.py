from itertools import product


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product name: {self.name}\nProduct price: {self.price}\nProduct category: {self.category}"

class Store:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)
        print(f"{product.name} added to store:")
        print(f"{product}")
        print()

    def add_multiple_products(self, products):
        for product in products:
            self.add_product(product)
            print(f"{product.name} added to store:")
            print(f"{product}")
            print()

    def show_products(self):
        print("All products in store:\n")
        for product in self.products:
            print(product)
            print()

        #print("\n".join(f"- {product}\n" for product in self.products))

    def find_product(self,product_name):
        found_product = next((product for product in self.products if product.name.lower() == product_name.lower()),None)
        if found_product:
            print("Product found!")
            print(found_product)

store = Store()

product1 = Product("Wireless Bluetooth Headphones", 59.99, "Electronics")
store.add_product(product1)

more_products = [
    Product("Organic Cotton T-Shirt",19.99, "Clothing"),
    Product("Stainless Steel Water Bottle",24.99, "Home & Kitchen"),
    Product("Gaming Mouse",39.99, "Electronics"),
    Product("Leather Wallet",34.9, "Accessories")
]

store.add_multiple_products(more_products)

store.show_products()

# store.find_product("Gaming Mouse")
