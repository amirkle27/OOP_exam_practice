from abc import ABC, abstractmethod

# 🛒 מחלקת בסיס - כל אובייקט בסל קניות יהיה Item (מוצר בודד או סל אחר)
class Item(ABC):
    @abstractmethod
    def get_price(self):
        pass

# 🍎 מחלקת מוצר (מוצר בודד)
class Product(Item):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self):
        return f"{self.name} - {self.price}$"

# 🛒 מחלקת סל קניות (שיכול לכלול מוצרים וגם סלים אחרים)
class ShoppingCart(Item):
    def __init__(self):
        self.items = []  # יכול לכלול גם מוצרים וגם סלים

    def add_item(self, item):
        if isinstance(item, Item):  # רק אובייקטים מסוג Item מותרים (מוצרים או סלים)
            self.items.append(item)
        else:
            print("\n❌ Invalid item! You must add a Product or another ShoppingCart.")

    def get_price(self):
        return sum(item.get_price() for item in self.items)  # חישוב מחיר כולל

    def __str__(self):
        item_list = "\n".join(f" - {item}" for item in self.items) or "Cart is empty"
        return f"\n🛒 Shopping Cart:\n{item_list}\nTotal Cost: {self.get_price()}$"

# ✅ יוצרים מוצרים
milk = Product("Milk", 10)
bread = Product("Bread", 5)
cheese = Product("Cheese", 20)

# ✅ יוצרים סל קניות ומוסיפים מוצרים
cart1 = ShoppingCart()
cart1.add_item(milk)
cart1.add_item(bread)

# ✅ יוצרים סל נוסף ומכניסים אליו מוצרים וגם סל קודם!
cart2 = ShoppingCart()
cart2.add_item(cart1)  # סל בתוך סל ✅
cart2.add_item(cheese)

# ✅ מציגים את תוכן הסל
print(cart2)  # יציג גם את המוצרים וגם את הסל שבתוך הסל
