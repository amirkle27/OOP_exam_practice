from collections.abc import Iterator, Iterable

class ShoppingIterator(Iterator):
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list
        #self.shopping_list = [item for item in shopping_list if item["bought"] == False]
        self.index = 0

    def __next__(self):
        while self.index < len(self.shopping_list):
            item = self.shopping_list[self.index]
            self.index += 1
            if not item["bought"]:
                return item
        raise StopIteration




class ItemsCollection(Iterable):
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    def __iter__(self):
        return ShoppingIterator(self.shopping_list)

shopping_list = [
    {"item": "Milk", "bought": False},
    {"item": "Eggs", "bought": True},
    {"item": "Bread", "bought": False},
    {"item": "Chocolate", "bought": True},
    {"item": "Cheese", "bought": False}
]

filtered_items = ItemsCollection(shopping_list)

print("🛒 Items left to buy:")

for item in filtered_items:
    print(f"✅ {item['item']}")

